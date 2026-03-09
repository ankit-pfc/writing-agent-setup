from fastapi import APIRouter
from app.knowledge.store import KnowledgeStore

router = APIRouter()
knowledge_store = KnowledgeStore(data_dir="../knowledge/parsed")

@router.get("/techniques")
def get_techniques():
    """Returns knowledge regarding writing techniques."""
    return {"techniques": ["Comparison", "Step-by-step"]}

@router.get("/rules/{page_type}")
def get_rules(page_type: str):
    """Returns specific minimum requirements per page type."""
    rules = knowledge_store.get_content_rules(page_type)
    if rules:
        return rules
    return {"error": "Page type not found"}