"""
Orchestrator Agent - Strategic planning + pipeline configuration.

Receives content requests, creates content briefs, and configures the pipeline
for optimal content generation based on topic, page type, and knowledge store.
"""
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from app.agents.base import BaseAgent
from app.knowledge.store import KnowledgeStore
from app.models.pipeline import Pipeline


class OrchestratorAgent(BaseAgent):
    """
    The Orchestrator is the strategic brain of the content pipeline.
    It analyzes requests, creates content briefs, and configures agents.
    """
    
    def __init__(self, db: Session, knowledge_store: KnowledgeStore):
        super().__init__("orchestrator", db)
        self.knowledge = knowledge_store

    def create_content_brief(self, pipeline: Pipeline) -> Dict[str, Any]:
        """
        Creates a structured content brief for the pipeline.
        
        This brief guides all downstream agents (Researcher, Writer, Editor, SEO).
        """
        # Get content rules for this page type
        rules = self.knowledge.get_content_rules(pipeline.page_type) or {}
        
        # Get internal linking opportunities for the topic
        link_targets = self.knowledge.get_internal_link_targets(pipeline.topic)
        
        # Build the content brief
        brief = {
            "topic": pipeline.topic,
            "page_type": pipeline.page_type,
            "target_audience": self._infer_audience(pipeline.page_type),
            "content_requirements": {
                "min_words": rules.get("min_words", 800),
                "required_sections": rules.get("required_sections", []),
                "tone": rules.get("tone", "informative"),
            },
            "seo_requirements": {
                "primary_keyword": pipeline.topic,
                "internal_link_targets": link_targets,
                "meta_title_max_chars": 60,
                "meta_desc_max_chars": 160,
            },
            "quality_thresholds": {
                "min_overall_score": 8.0,
                "exclusion_safety_required": True,
                "max_revision_loops": 3,
            },
            "pipeline_config": {
                "skip_research": False,
                "skip_seo": False,
                "auto_publish_threshold": 9.0,
            }
        }
        
        return brief

    def _infer_audience(self, page_type: str) -> str:
        """Infers target audience based on page type."""
        audience_map = {
            "blog_post": "general readers seeking information",
            "glossary_term": "readers new to the topic",
            "comparison": "readers evaluating options",
            "how_to": "readers seeking practical guidance",
            "product_page": "potential customers",
            "article": "engaged readers seeking depth",
        }
        return audience_map.get(page_type, "general readers")

    def configure_pipeline(self, pipeline: Pipeline) -> Dict[str, Any]:
        """
        Configures the pipeline based on the content brief.
        Returns configuration for downstream agents.
        """
        brief = self.create_content_brief(pipeline)
        
        # Store brief in pipeline
        pipeline.content_brief = brief
        pipeline.status = "brief"
        self.db.commit()
        
        return brief

    def advance_stage(self, pipeline: Pipeline, next_stage: str) -> None:
        """
        Advances the pipeline to the next stage.
        Called by agents when they complete their work.
        """
        pipeline.status = next_stage
        self.db.commit()

    def should_continue_revision(self, pipeline: Pipeline) -> bool:
        """
        Determines if the pipeline should continue with another revision loop.
        """
        return pipeline.revision_count < pipeline.max_revisions

    def get_pipeline_status_summary(self, pipeline: Pipeline) -> Dict[str, Any]:
        """
        Returns a summary of the pipeline status for monitoring.
        """
        return {
            "id": pipeline.id,
            "topic": pipeline.topic,
            "page_type": pipeline.page_type,
            "status": pipeline.status,
            "revision_count": pipeline.revision_count,
            "max_revisions": pipeline.max_revisions,
            "has_content": pipeline.content is not None,
            "has_brief": pipeline.content_brief is not None,
            "has_research": pipeline.research_bundle is not None,
            "has_seo": pipeline.seo_output is not None,
            "created_at": pipeline.created_at.isoformat() if pipeline.created_at else None,
            "updated_at": pipeline.updated_at.isoformat() if pipeline.updated_at else None,
        }