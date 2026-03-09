from sqlalchemy import Column, String, DateTime, JSON, Integer, Text, ForeignKey, Enum
from datetime import datetime
import uuid
import enum
from app.db.database import Base


class PipelineStatus(str, enum.Enum):
    """Pipeline status values for explicit state tracking."""
    PENDING = "pending"
    BRIEF = "brief"
    RESEARCH = "research"
    WRITING = "writing"
    EDITING = "editing"
    REVISION = "revision"
    SEO_OPTIMIZATION = "seo_optimization"
    PUBLISHED = "published"
    FAILED = "failed"


class Pipeline(Base):
    __tablename__ = "pipelines"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    status = Column(String, default="pending")  # pending, brief, research, writing, editing, revision, seo_optimization, published, failed
    topic = Column(String, nullable=False)
    page_type = Column(String, nullable=False)
    
    # Content brief from Orchestrator
    content_brief = Column(JSON, nullable=True)
    
    # Research bundle from Researcher
    research_bundle = Column(JSON, nullable=True)
    
    # Stores the final or current draft
    content = Column(String, nullable=True)
    
    # Structured JSON for quality scores, research data, etc.
    metadata_json = Column(JSON, default={})
    
    # Revision tracking
    revision_count = Column(Integer, default=0)
    max_revisions = Column(Integer, default=3)
    
    # SEO output from SEO Specialist
    seo_output = Column(JSON, nullable=True)
    
    # Published URL after Publisher agent
    published_url = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class FeedbackEntry(Base):
    """Stores human feedback linked to a pipeline and stage."""
    __tablename__ = "feedback_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(String, ForeignKey("pipelines.id"), index=True, nullable=False)
    stage = Column(String, nullable=False)  # writing, editing, seo_optimization, etc.
    feedback_type = Column(String, nullable=False)  # edit, approval, rejection, comment
    original_content = Column(Text, nullable=True)  # Content before edit
    edited_content = Column(Text, nullable=True)  # Content after edit (if applicable)
    comment = Column(Text, nullable=True)  # Freeform feedback comment
    metadata_json = Column(JSON, default={})  # Additional context (diff, user, etc.)
    created_at = Column(DateTime, default=datetime.utcnow)


class AgentMemory(Base):
    __tablename__ = "agent_memories"
    
    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String, index=True, nullable=False) # e.g., 'writer', 'editor'
    key = Column(String, nullable=False) # e.g., 'preferred_voice', 'avoid_words'
    value = Column(JSON, nullable=False) # Stores the learned preference or override
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ContentDraft(Base):
    """Stores all draft versions for a pipeline (for revision history)."""
    __tablename__ = "content_drafts"
    
    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(String, ForeignKey("pipelines.id"), index=True, nullable=False)
    version = Column(Integer, nullable=False)  # 1, 2, 3...
    content = Column(Text, nullable=False)
    editor_feedback = Column(JSON, nullable=True)  # Feedback that led to this revision
    created_at = Column(DateTime, default=datetime.utcnow)
