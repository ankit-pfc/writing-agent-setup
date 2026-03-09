"""
API Routes for Content Generation Pipeline.

Provides endpoints for:
- Starting new pipelines
- Polling pipeline status
- Listing all pipelines
- Submitting feedback
- Advancing pipeline stages (human-in-the-loop)
"""
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.generate import (
    GenerateRequest, GenerateResponse, PipelineStatusResponse,
    FeedbackRequest, FeedbackResponse, PipelineListResponse
)
from app.models.pipeline import Pipeline, FeedbackEntry
from app.services.pipeline_service import run_pipeline_sync, advance_pipeline_stage

router = APIRouter()


@router.get("/pipelines", response_model=List[PipelineListResponse])
def get_all_pipelines(db: Session = Depends(get_db)):
    """
    Get all content generation pipelines for the kanban board.
    Returns a summary of each pipeline without full content.
    """
    pipelines = db.query(Pipeline).order_by(Pipeline.created_at.desc()).all()
    return [
        PipelineListResponse(
            id=p.id,
            topic=p.topic,
            page_type=p.page_type,
            status=p.status,
            revision_count=p.revision_count or 0,
            created_at=p.created_at.isoformat() if p.created_at else None,
            updated_at=p.updated_at.isoformat() if p.updated_at else None,
        ) for p in pipelines
    ]


@router.post("/generate", response_model=GenerateResponse)
def start_generation(
    request: GenerateRequest, 
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Initiates the content generation pipeline.
    Returns the pipeline ID immediately while the agents run in the background.
    """
    pipeline = Pipeline(
        topic=request.topic,
        page_type=request.page_type,
        max_revisions=request.max_revisions or 3
    )
    db.add(pipeline)
    db.commit()
    db.refresh(pipeline)
    
    # Run the full pipeline in the background
    background_tasks.add_task(run_pipeline_sync, pipeline.id, db)
    
    return GenerateResponse(
        pipeline_id=pipeline.id,
        status=pipeline.status,
        message="Pipeline started in background. Poll /api/status/{pipeline_id} for updates."
    )


@router.get("/status/{pipeline_id}", response_model=PipelineStatusResponse)
def get_status(pipeline_id: str, db: Session = Depends(get_db)):
    """
    Polling endpoint for the frontend to check the current state of a generation request.
    Returns full pipeline details including content and scores.
    """
    pipeline = db.query(Pipeline).filter(Pipeline.id == pipeline_id).first()
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    
    return PipelineStatusResponse(
        id=pipeline.id,
        topic=pipeline.topic,
        page_type=pipeline.page_type,
        status=pipeline.status,
        revision_count=pipeline.revision_count or 0,
        max_revisions=pipeline.max_revisions or 3,
        content=pipeline.content,
        metadata_json=pipeline.metadata_json,
        seo_output=pipeline.seo_output,
        content_brief=pipeline.content_brief,
        research_bundle=pipeline.research_bundle,
        created_at=pipeline.created_at.isoformat() if pipeline.created_at else None,
        updated_at=pipeline.updated_at.isoformat() if pipeline.updated_at else None,
    )


@router.post("/feedback", response_model=FeedbackResponse)
def submit_feedback(
    request: FeedbackRequest,
    db: Session = Depends(get_db)
):
    """
    Submit human feedback for a pipeline at a specific stage.
    Feedback is stored for pattern analysis and agent calibration.
    """
    # Verify pipeline exists
    pipeline = db.query(Pipeline).filter(Pipeline.id == request.pipeline_id).first()
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    
    feedback = FeedbackEntry(
        pipeline_id=request.pipeline_id,
        stage=request.stage,
        feedback_type=request.feedback_type,
        original_content=request.original_content,
        edited_content=request.edited_content,
        comment=request.comment,
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    
    return FeedbackResponse(
        id=feedback.id,
        pipeline_id=feedback.pipeline_id,
        stage=feedback.stage,
        feedback_type=feedback.feedback_type,
        comment=feedback.comment,
        created_at=feedback.created_at.isoformat() if feedback.created_at else None,
    )


@router.get("/feedback/{pipeline_id}", response_model=List[FeedbackResponse])
def get_pipeline_feedback(pipeline_id: str, db: Session = Depends(get_db)):
    """
    Get all feedback entries for a specific pipeline.
    """
    feedbacks = db.query(FeedbackEntry).filter(
        FeedbackEntry.pipeline_id == pipeline_id
    ).order_by(FeedbackEntry.created_at.desc()).all()
    
    return [
        FeedbackResponse(
            id=f.id,
            pipeline_id=f.pipeline_id,
            stage=f.stage,
            feedback_type=f.feedback_type,
            comment=f.comment,
            created_at=f.created_at.isoformat() if f.created_at else None,
        ) for f in feedbacks
    ]


@router.post("/advance/{pipeline_id}")
def advance_stage(
    pipeline_id: str, 
    next_stage: str,
    db: Session = Depends(get_db)
):
    """
    Manually advance a pipeline to the next stage.
    Used for human-in-the-loop gates in Mode 1 (Full Control).
    """
    success = advance_pipeline_stage(pipeline_id, next_stage, db)
    if not success:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    
    return {"status": "success", "pipeline_id": pipeline_id, "new_stage": next_stage}


@router.delete("/pipelines/{pipeline_id}")
def delete_pipeline(pipeline_id: str, db: Session = Depends(get_db)):
    """
    Delete a pipeline and all associated data.
    """
    pipeline = db.query(Pipeline).filter(Pipeline.id == pipeline_id).first()
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    
    # Delete associated feedback entries
    db.query(FeedbackEntry).filter(FeedbackEntry.pipeline_id == pipeline_id).delete()
    
    # Delete the pipeline
    db.delete(pipeline)
    db.commit()
    
    return {"status": "deleted", "pipeline_id": pipeline_id}