from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.generate import GenerateRequest, GenerateResponse, PipelineStatusResponse
from app.models.pipeline import Pipeline
from app.services.pipeline_service import run_pipeline_sync

router = APIRouter()

from typing import List

@router.get("/pipelines", response_model=List[PipelineStatusResponse])
def get_all_pipelines(db: Session = Depends(get_db)):
    """
    Get all content generation pipelines for the kanban board.
    """
    pipelines = db.query(Pipeline).order_by(Pipeline.created_at.desc()).all()
    # Need to convert models to schemas with default values for missing data
    return [
        PipelineStatusResponse(
            id=p.id,
            topic=p.topic,
            page_type=p.page_type,
            status=p.status,
            content=p.content,
            metadata_json=p.metadata_json
        ) for p in pipelines
    ]

@router.post("/generate", response_model=GenerateResponse)
def start_generation(
    request: GenerateRequest, 
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Initates the content generation pipeline.
    Returns the pipeline ID immediately while the agents run in the background.
    """
    pipeline = Pipeline(
        topic=request.topic,
        page_type=request.page_type
    )
    db.add(pipeline)
    db.commit()
    db.refresh(pipeline)
    
    # Run the orchestration synchronously in the background task
    background_tasks.add_task(run_pipeline_sync, pipeline.id, db)
    
    return GenerateResponse(
        pipeline_id=pipeline.id,
        status=pipeline.status,
        message="Pipeline started in background."
    )

@router.get("/status/{pipeline_id}", response_model=PipelineStatusResponse)
def get_status(pipeline_id: str, db: Session = Depends(get_db)):
    """
    Polling endpoint for the frontend to check the current state of a generation request.
    """
    pipeline = db.query(Pipeline).filter(Pipeline.id == pipeline_id).first()
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")
        
    return PipelineStatusResponse(
        id=pipeline.id,
        topic=pipeline.topic,
        page_type=pipeline.page_type,
        status=pipeline.status,
        content=pipeline.content,
        metadata_json=pipeline.metadata_json
    )
