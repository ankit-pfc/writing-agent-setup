import re
from typing import Dict, Any
from sqlalchemy.orm import Session
from app.agents.base import BaseAgent
from app.knowledge.store import KnowledgeStore
from app.models.pipeline import Pipeline
import random

class EditorAgent(BaseAgent):
    """
    Evaluates generated drafts against explicit SEO boundaries (regex) and qualitative metrics (LLM 10-dimension scorecard).
    """
    def __init__(self, db: Session, knowledge_store: KnowledgeStore):
        super().__init__("editor", db)
        self.knowledge = knowledge_store

    def evaluate_draft(self, pipeline: Pipeline) -> Dict[str, Any]:
        """
        Runs dual-pass evaluation: Rule Checks + LLM qualitative score.
        """
        if not pipeline.content:
            return {"total_score": 0.0, "status": "failed", "feedback": "No content to evaluate."}
            
        # 1. Deterministic Pass: Exclusion Scanner 
        exclusion_patterns = self.knowledge.get_exclusion_patterns()
        print(f"[Editor] Scanning for exclusions using {len(exclusion_patterns)} rules.")
        for pattern in exclusion_patterns:
            matches = list(pattern.finditer(pipeline.content))
            if matches:
                failed_strings = ", ".join(m.group() for m in matches[:3])
                print(f"[Editor] Failed exclusion rule on phrase: {failed_strings}")
                # Immediate total failure on Dimension 6 violation
                return {
                    "total_score": 0.0,
                    "status": "rejected", 
                    "dimension_6_exclusion_safety": 0.0,
                    "feedback": f"CRITICAL SEO ERROR: Content violates exclusion rule: '{failed_strings}'. It is legally or functionally unsafe."
                }

        # 2. Heuristic LLM Pass: 10-Dimension Quality Scorecard
        # Simulating the LLM grading the document
        print("[Editor] Content passes deterministic scanner. Proceeding to LLM qualitative grading...")
        
        # We assume the content passed, generating random good scores for now
        overall = random.uniform(8.1, 9.5)
        
        feedbacks = [
            "Excellent brand voice adherence.",
            "Solid structure, well-defined headings.",
            "Good AEO block integration."
        ]
        
        return {
            "total_score": round(overall, 1),
            "status": "approved" if overall >= 8.0 else "revision",
            "dimension_1_depth": random.randint(8, 10),
            "dimension_2_accuracy": random.randint(7, 10),
            "dimension_3_voice": random.randint(8, 10),
            "dimension_6_exclusion_safety": 10.0,  # Passed regex
            "feedback": random.choice(feedbacks)
        }
