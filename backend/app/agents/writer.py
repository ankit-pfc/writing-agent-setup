from sqlalchemy.orm import Session
from app.agents.base import BaseAgent
from app.knowledge.store import KnowledgeStore
from app.models.pipeline import Pipeline
from app.services.llm_client import get_llm_client
from typing import Dict, Any, Optional


class WriterAgent(BaseAgent):
    """
    Sole content producer. Assembles system prompt based on user request, 
    injects precise deterministic SEO boundaries, and calls LLM.
    """
    def __init__(self, db: Session, knowledge_store: KnowledgeStore):
        super().__init__("writer", db)
        self.knowledge = knowledge_store
        self.llm = get_llm_client()

    def generate_draft(
        self, 
        pipeline: Pipeline,
        mode: Optional[str] = None,
        additional_context: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Executes the content creation phase using dynamic SOUL prompts.
        
        Args:
            pipeline: The content pipeline with topic and page_type
            mode: Optional content mode (practice_log, discourse_entry, etc.)
            additional_context: Optional extra context for generation
            
        Returns:
            Generated content draft
        """
        # Fetch SEO content rules based on the requested page type
        rules = self.knowledge.get_content_rules(pipeline.page_type)
        if not rules:
            raise ValueError(f"No SEO rules found for page type: {pipeline.page_type}")
        
        # Determine the skill/mode to use
        skill_name = mode or pipeline.page_type
        
        # Get specific writing skill template for this page type
        system_prompt = self.get_system_prompt(skill_name)
        if not system_prompt:
            system_prompt = self._build_fallback_prompt(pipeline, rules)

        print(f"[Writer] Assembled system prompt of length {len(system_prompt)}")
        print(f"[Writer] Injecting rules: {rules}")

        # Build user message with topic and constraints
        user_message = self._build_user_message(pipeline, rules, additional_context)
        
        # Call LLM
        draft = self.llm.generate(
            system_prompt=system_prompt,
            user_message=user_message,
            max_tokens=self._get_max_tokens(pipeline.page_type),
            temperature=0.7
        )
        
        return draft
    
    def _build_fallback_prompt(self, pipeline: Pipeline, rules: Dict[str, Any]) -> str:
        """Build a fallback system prompt if no skill template is found."""
        return f"""You are a skilled content writer creating {pipeline.page_type} content.

## Content Requirements
- Minimum words: {rules.get('min_words', 500)}
- Maximum words: {rules.get('max_words', 2000)}
- Required sections: {', '.join(rules.get('required_sections', []))}

## Writing Guidelines
- Write with clarity and precision
- Avoid clichés and overused phrases
- Be specific rather than vague
- Use active voice

Write the requested content following these guidelines."""

    def _build_user_message(
        self, 
        pipeline: Pipeline, 
        rules: Dict[str, Any],
        additional_context: Optional[Dict[str, Any]] = None
    ) -> str:
        """Build the user message with topic and constraints."""
        parts = [f"Topic: {pipeline.topic}"]
        
        if rules.get('max_characters'):
            parts.append(f"Maximum characters: {rules['max_characters']}")
        
        if rules.get('min_tweets') and rules.get('max_tweets'):
            parts.append(f"Thread length: {rules['min_tweets']}-{rules['max_tweets']} tweets")
        
        if rules.get('required_sections'):
            parts.append(f"Include these sections: {', '.join(rules['required_sections'])}")
        
        if additional_context:
            for key, value in additional_context.items():
                parts.append(f"{key}: {value}")
        
        parts.append("\nGenerate the content now.")
        
        return "\n".join(parts)
    
    def _get_max_tokens(self, page_type: str) -> int:
        """Get appropriate max tokens for content type."""
        token_limits = {
            'x_standalone': 150,
            'x_thread': 2000,
            'x_reply': 150,
            'blog_post': 4000,
            'practice_log': 500,
            'discourse_entry': 500,
            'mythological_narrative': 3000,
            'bridge_teaching': 1500,
            'single_line': 100
        }
        return token_limits.get(page_type, 2000)
