"""
Researcher Agent - Knowledge retrieval + source synthesis.

Gathers relevant information from the knowledge store and prepares
a research bundle for the Writer agent.
"""
from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session
from app.agents.base import BaseAgent
from app.knowledge.store import KnowledgeStore
from app.models.pipeline import Pipeline


class ResearcherAgent(BaseAgent):
    """
    The Researcher gathers structured knowledge for content creation.
    Uses deterministic retrieval from the knowledge store (not RAG).
    """
    
    def __init__(self, db: Session, knowledge_store: KnowledgeStore):
        super().__init__("researcher", db)
        self.knowledge = knowledge_store

    def conduct_research(self, pipeline: Pipeline) -> Dict[str, Any]:
        """
        Conducts research based on the content brief and topic.
        Returns a structured research bundle for the Writer.
        """
        brief = pipeline.content_brief or {}
        topic = pipeline.topic
        page_type = pipeline.page_type
        
        # Gather research components
        research_bundle = {
            "topic": topic,
            "page_type": page_type,
            "content_rules": self.knowledge.get_content_rules(page_type),
            "internal_links": self.knowledge.get_internal_link_targets(topic),
            "exclusion_patterns": self._get_exclusion_summary(),
            "seo_guidance": self._get_seo_guidance(topic, page_type),
            "source_references": self._get_source_references(topic),
        }
        
        return research_bundle

    def _get_exclusion_summary(self) -> Dict[str, Any]:
        """
        Returns a summary of exclusion rules for the Writer to follow.
        """
        patterns = self.knowledge.get_exclusion_patterns()
        return {
            "pattern_count": len(patterns),
            "warning": "Content must pass all exclusion checks. Avoid medical claims, copyrighted content, and prohibited phrases.",
            "critical": "Any exclusion violation results in automatic rejection.",
        }

    def _get_seo_guidance(self, topic: str, page_type: str) -> Dict[str, Any]:
        """
        Returns SEO-specific guidance for the topic and page type.
        """
        guidance = {
            "primary_keyword": topic,
            "keyword_placement": [
                "Include primary keyword in H1",
                "Include primary keyword in first 100 words",
                "Include primary keyword in at least one H2",
            ],
            "structure_requirements": {
                "blog_post": ["Introduction", "Main Content (3-5 sections)", "FAQ", "Conclusion"],
                "glossary_term": ["Definition", "Explanation", "Examples", "Related Terms", "FAQ"],
                "comparison": ["Introduction", "Overview of Each", "Key Differences", "Comparison Table", "FAQ"],
                "how_to": ["Introduction", "Prerequisites", "Step-by-Step Guide", "Tips", "FAQ"],
            }.get(page_type, ["Introduction", "Main Content", "Conclusion"]),
            "aeo_blocks": [
                "Include a clear definition block for featured snippets",
                "Use FAQ schema-compatible Q&A format",
                "Include step-by-step lists for how-to content",
            ],
        }
        return guidance

    def _get_source_references(self, topic: str) -> List[Dict[str, str]]:
        """
        Returns source references for the topic.
        In production, this would query the knowledge base for relevant sources.
        """
        # Placeholder - in production, this would search the knowledge store
        return [
            {
                "type": "internal_knowledge",
                "topic": topic,
                "note": "Source references would be populated from the knowledge base",
            }
        ]

    def prepare_writer_context(self, pipeline: Pipeline) -> str:
        """
        Prepares a formatted context string for the Writer agent.
        Combines brief, research, and rules into a single prompt component.
        """
        brief = pipeline.content_brief or {}
        research = pipeline.research_bundle or {}
        
        context = f"""
## Content Brief
Topic: {brief.get('topic', pipeline.topic)}
Page Type: {brief.get('page_type', pipeline.page_type)}
Target Audience: {brief.get('target_audience', 'general readers')}

## Content Requirements
- Minimum Words: {brief.get('content_requirements', {}).get('min_words', 800)}
- Required Sections: {', '.join(brief.get('content_requirements', {}).get('required_sections', []))}
- Tone: {brief.get('content_requirements', {}).get('tone', 'informative')}

## SEO Requirements
- Primary Keyword: {brief.get('seo_requirements', {}).get('primary_keyword', pipeline.topic)}
- Internal Link Targets: {len(brief.get('seo_requirements', {}).get('internal_link_targets', []))} available

## Research Summary
- Content Rules: Loaded
- Internal Links: {len(research.get('internal_links', []))} targets found
- Exclusion Patterns: {research.get('exclusion_patterns', {}).get('pattern_count', 0)} rules to follow
"""
        return context