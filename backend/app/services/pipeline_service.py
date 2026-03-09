"""
Pipeline Service - Orchestrates the full content generation pipeline.

Manages the flow from Orchestrator → Researcher → Writer ↔ Editor → SEO Specialist.
Implements revision loops and stage advancement.
"""
import time
from sqlalchemy.orm import Session
from app.models.pipeline import Pipeline, ContentDraft
from app.agents.orchestrator import OrchestratorAgent
from app.agents.researcher import ResearcherAgent
from app.agents.writer import WriterAgent
from app.agents.editor import EditorAgent
from app.agents.seo_specialist import SEOSpecialistAgent
from app.knowledge.store import KnowledgeStore

# Singleton knowledge store instance
knowledge_store = KnowledgeStore(data_dir="../knowledge/parsed")


def run_pipeline_sync(pipeline_id: str, db: Session):
    """
    Executes the full content generation pipeline with revision loops.
    
    Stages:
    1. Brief (Orchestrator creates content brief)
    2. Research (Researcher gathers knowledge)
    3. Writing (Writer produces draft)
    4. Editing (Editor evaluates quality)
    5. Revision (Writer revises if needed, max 3 loops)
    6. SEO Optimization (SEO Specialist optimizes)
    7. Published (Final output ready)
    """
    pipeline = db.query(Pipeline).filter(Pipeline.id == pipeline_id).first()
    if not pipeline:
        print(f"[Pipeline] Pipeline {pipeline_id} not found")
        return

    try:
        # Initialize agents
        orchestrator = OrchestratorAgent(db, knowledge_store)
        researcher = ResearcherAgent(db, knowledge_store)
        writer = WriterAgent(db, knowledge_store)
        editor = EditorAgent(db, knowledge_store)
        seo_specialist = SEOSpecialistAgent(db, knowledge_store)

        # Stage 1: Create Content Brief
        print(f"[Pipeline {pipeline_id}] Stage 1: Creating content brief...")
        pipeline.status = "brief"
        db.commit()
        
        brief = orchestrator.configure_pipeline(pipeline)
        print(f"[Pipeline {pipeline_id}] Brief created for {pipeline.page_type}")

        # Stage 2: Conduct Research
        print(f"[Pipeline {pipeline_id}] Stage 2: Conducting research...")
        pipeline.status = "research"
        db.commit()
        
        research_bundle = researcher.conduct_research(pipeline)
        pipeline.research_bundle = research_bundle
        db.commit()
        print(f"[Pipeline {pipeline_id}] Research complete")

        # Stage 3-5: Writing + Editing + Revision Loop
        max_revisions = pipeline.max_revisions
        revision_count = 0
        approved = False

        while not approved and revision_count <= max_revisions:
            # Writing Stage
            print(f"[Pipeline {pipeline_id}] Stage 3: Writing (attempt {revision_count + 1})...")
            pipeline.status = "writing"
            db.commit()
            
            draft = writer.generate_draft(pipeline)
            pipeline.content = draft
            db.commit()
            
            # Save draft version
            _save_draft_version(db, pipeline, revision_count + 1)
            print(f"[Pipeline {pipeline_id}] Draft {revision_count + 1} saved")

            # Editing Stage
            print(f"[Pipeline {pipeline_id}] Stage 4: Editing...")
            pipeline.status = "editing"
            db.commit()
            
            evaluation = editor.evaluate_draft(pipeline)
            pipeline.metadata_json = evaluation
            db.commit()
            
            # Check if approved or needs revision
            total_score = evaluation.get("total_score", 0)
            status = evaluation.get("status", "revision")
            
            if status == "approved" and total_score >= 8.0:
                approved = True
                print(f"[Pipeline {pipeline_id}] Content approved with score {total_score}")
            elif status == "rejected":
                # Exclusion violation - hard reject
                print(f"[Pipeline {pipeline_id}] Content rejected due to exclusion violation")
                pipeline.status = "failed"
                db.commit()
                return
            else:
                # Needs revision
                revision_count += 1
                pipeline.revision_count = revision_count
                pipeline.status = "revision"
                db.commit()
                
                if revision_count <= max_revisions:
                    print(f"[Pipeline {pipeline_id}] Score {total_score} - starting revision {revision_count}")
                    # Pass feedback to writer for next iteration
                    writer_feedback = evaluation.get("feedback", "Improve content quality")
                    pipeline.metadata_json["revision_feedback"] = writer_feedback
                    db.commit()
                else:
                    print(f"[Pipeline {pipeline_id}] Max revisions ({max_revisions}) reached")
                    # Accept best effort or fail based on score
                    if total_score >= 6.0:
                        approved = True
                        print(f"[Pipeline {pipeline_id}] Accepting with score {total_score}")
                    else:
                        pipeline.status = "failed"
                        db.commit()
                        return

        # Stage 6: SEO Optimization
        print(f"[Pipeline {pipeline_id}] Stage 6: SEO Optimization...")
        pipeline.status = "seo_optimization"
        db.commit()
        
        seo_output = seo_specialist.optimize_content(pipeline)
        pipeline.seo_output = seo_output
        db.commit()
        
        # Get SEO score
        seo_score = seo_specialist.get_seo_score(pipeline)
        pipeline.metadata_json["seo_score"] = seo_score
        db.commit()
        print(f"[Pipeline {pipeline_id}] SEO optimization complete - Grade: {seo_score.get('grade', 'N/A')}")

        # Stage 7: Published
        print(f"[Pipeline {pipeline_id}] Stage 7: Publishing...")
        pipeline.status = "published"
        db.commit()
        print(f"[Pipeline {pipeline_id}] Pipeline completed successfully!")

    except Exception as e:
        print(f"[Pipeline {pipeline_id}] Error: {str(e)}")
        db.rollback()
        pipeline.status = "failed"
        pipeline.metadata_json = {"error": str(e)}
        db.commit()


def _save_draft_version(db: Session, pipeline: Pipeline, version: int):
    """
    Saves a draft version to the content_drafts table for history.
    """
    draft = ContentDraft(
        pipeline_id=pipeline.id,
        version=version,
        content=pipeline.content or "",
        editor_feedback=pipeline.metadata_json
    )
    db.add(draft)
    db.commit()


def get_pipeline_status(pipeline_id: str, db: Session) -> dict:
    """
    Returns the current status of a pipeline for polling.
    """
    pipeline = db.query(Pipeline).filter(Pipeline.id == pipeline_id).first()
    if not pipeline:
        return {"error": "Pipeline not found"}
    
    return {
        "id": pipeline.id,
        "topic": pipeline.topic,
        "page_type": pipeline.page_type,
        "status": pipeline.status,
        "revision_count": pipeline.revision_count,
        "max_revisions": pipeline.max_revisions,
        "content": pipeline.content,
        "metadata_json": pipeline.metadata_json,
        "seo_output": pipeline.seo_output,
        "created_at": pipeline.created_at.isoformat() if pipeline.created_at else None,
        "updated_at": pipeline.updated_at.isoformat() if pipeline.updated_at else None,
    }


def advance_pipeline_stage(pipeline_id: str, next_stage: str, db: Session) -> bool:
    """
    Manually advances a pipeline to a specific stage.
    Used for human-in-the-loop gates.
    """
    pipeline = db.query(Pipeline).filter(Pipeline.id == pipeline_id).first()
    if not pipeline:
        return False
    
    pipeline.status = next_stage
    db.commit()
    return True