from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Writing Agent API"
    DATABASE_URL: str = "sqlite:///./writing_agent.db"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
