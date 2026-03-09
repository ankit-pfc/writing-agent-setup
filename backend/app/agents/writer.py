from sqlalchemy.orm import Session
from app.agents.base import BaseAgent
from app.knowledge.store import KnowledgeStore
from app.models.pipeline import Pipeline
import time

class WriterAgent(BaseAgent):
    """
    Sole content producer. Assembles system prompt based on user request, 
    injects precise deterministic SEO boundaries, and calls LLM.
    """
    def __init__(self, db: Session, knowledge_store: KnowledgeStore):
        super().__init__("writer", db)
        self.knowledge = knowledge_store

    def generate_draft(self, pipeline: Pipeline) -> str:
        """
        Executes the content creation phase using dynamic SOUL prompts.
        """
        # Fetch SEO content rules based on the requested page type
        rules = self.knowledge.get_content_rules(pipeline.page_type)
        if not rules:
            raise ValueError(f"No SEO rules found for page type: {pipeline.page_type}")
            
        # Get specific writing skill template for this page type
        system_prompt = self.get_system_prompt(pipeline.page_type)
        if not system_prompt:
            system_prompt = f"Base rules fallback: Please write about {pipeline.topic}. Minimum {rules.get('min_words')} words."

        print(f"[Writer] Assembled system prompt of length {len(system_prompt)}")
        print(f"[Writer] Injecting rules: {rules}")

        # Simulate LLM Network Call
        time.sleep(1)
        
        draft = (
            f"# {pipeline.topic}\n\n"
            f"This is an automated placeholder generated for a `{pipeline.page_type}` request.\n\n"
            f"## Section 1\n"
            f"Knowledge store requested minimum length of {rules.get('min_words', 0)} words, "
            f"and required these sections: {', '.join(rules.get('required_sections', []))}.\n\n"
            f"In the final version, the LLM client (like an Anthropic wrapper) will replace this."
        )
        return draft
