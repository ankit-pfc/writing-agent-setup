from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Writing Agent API"
    DATABASE_URL: str = "sqlite:///./writing_agent.db"
    
    # LLM Configuration
    ANTHROPIC_API_KEY: Optional[str] = None
    LLM_MODEL: str = "claude-sonnet-4-20250514"
    LLM_MAX_TOKENS: int = 4096
    LLM_TEMPERATURE: float = 0.7
    
    # Knowledge paths
    KNOWLEDGE_DATA_DIR: str = "knowledge/parsed"
    WORKSPACE_DIR: str = "workspace/agents"
    SKILLS_DIR: str = "skills"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
