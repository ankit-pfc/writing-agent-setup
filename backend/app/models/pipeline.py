from sqlalchemy import Column, String, DateTime, JSON, Integer
from datetime import datetime
import uuid
from app.db.database import Base

class Pipeline(Base):
    __tablename__ = "pipelines"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    status = Column(String, default="pending")  # pending, writing, editing, completed, failed
    topic = Column(String, nullable=False)
    page_type = Column(String, nullable=False)
    
    # Stores the final or current draft
    content = Column(String, nullable=True)
    
    # Structured JSON for quality scores, research data, etc.
    metadata_json = Column(JSON, default={})
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AgentMemory(Base):
    __tablename__ = "agent_memories"
    
    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String, index=True, nullable=False) # e.g., 'writer', 'editor'
    key = Column(String, nullable=False) # e.g., 'preferred_voice', 'avoid_words'
    value = Column(JSON, nullable=False) # Stores the learned preference or override
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
