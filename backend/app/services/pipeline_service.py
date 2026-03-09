import time
from sqlalchemy.orm import Session
from app.models.pipeline import Pipeline
from app.agents.writer import WriterAgent
from app.agents.editor import EditorAgent
from app.knowledge.store import KnowledgeStore

# We instantiate the static rule cache once
knowledge_store = KnowledgeStore(data_dir="../knowledge/parsed")

def run_pipeline_sync(pipeline_id: str, db: Session):
    """
    Executes the background orchestration.
    Loads SOUL configs, writes a draft, scans it against exclusion rules, and assigns a qualitative score.
    """
    pipeline = db.query(Pipeline).filter(Pipeline.id == pipeline_id).first()
    if not pipeline:
        return

    try:
        writer = WriterAgent(db, knowledge_store)
        editor = EditorAgent(db, knowledge_store)

        # 1. Writing Stage
        pipeline.status = "writing"
        db.commit()
        
        draft = writer.generate_draft(pipeline)
        pipeline.content = draft
        db.commit()
        
        # 2. Editing Stage 
        pipeline.status = "editing"
        db.commit()
        
        evaluation = editor.evaluate_draft(pipeline)
        pipeline.metadata_json = evaluation
        
        # 3. Finalization logic based on qualitative and deterministic gates
        pipeline.status = evaluation.get("status", "failed")
        db.commit()
        
    except Exception as e:
        db.rollback()
        pipeline.status = "failed"
        pipeline.metadata_json = {"error": str(e)}
        db.commit()
