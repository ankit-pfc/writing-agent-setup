from sqlalchemy.orm import Session
from app.services.memory_service import MemoryService
import os

class BaseAgent:
    """
    Base class for all agents. Handles loading SOUL.md configurations 
    and applying database-backed memory overrides.
    """
    def __init__(self, name: str, db: Session):
        self.name = name
        self.db = db
        self.memory_service = MemoryService(db)
        self.base_soul = self._load_soul()
        self.learned_preferences = self._load_preferences()

    def _load_soul(self) -> str:
        """Loads foundational, read-only configuration."""
        return self.memory_service.load_base_soul(self.name)

    def _load_preferences(self) -> dict:
        """Loads mutable runtime database overrides."""
        return self.memory_service.get_learned_preferences(self.name)

    def _get_skill(self, skill_name: str) -> str:
        """
        Loads a specific markdown skill template.
        E.g., `writer/blog_post.md`
        """
        filepath = f"../skills/{self.name}/{skill_name}.md"
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    def get_system_prompt(self, skill_name: str = "base") -> str:
        """
        Synthesizes the final prompt from SOUL + Mem + Skill.
        """
        skill_text = self._get_skill(skill_name)
        
        # In a real situation, this format would be cleaner and potentially XML wrapped 
        # for strict isolation.
        prompt = f"{self.base_soul}\n\n"
        if self.learned_preferences:
            prompt += "## Learned Runtime Preferences:\n"
            for k, v in self.learned_preferences.items():
                prompt += f"- {k}: {v}\n"
        prompt += f"\n\n## Current Task Instructions:\n{skill_text}"
        
        return prompt
