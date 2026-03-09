import os
import json
from sqlalchemy.orm import Session
from app.models.pipeline import AgentMemory

class MemoryService:
    def __init__(self, db: Session):
        self.db = db

    def load_base_soul(self, agent_name: str) -> str:
        """
        Loads the foundational, read-only prompt configuration from disk.
        """
        filepath = f"../workspace/agents/{agent_name}/SOUL.md"
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        return f"# {agent_name} Agent - Default\nNo SOUL.md found."

    def get_learned_preferences(self, agent_name: str) -> dict:
        """
        Loads overrides, preferences, and feedback from the database instead of the file system.
        Addresses Architecture Review issue 2 regarding stateless container deployment.
        """
        memories = self.db.query(AgentMemory).filter(AgentMemory.agent_name == agent_name).all()
        preferences = {}
        for row in memories:
            preferences[row.key] = row.value
        return preferences

    def save_learned_preference(self, agent_name: str, key: str, value: dict):
        """
        Saves a new preference override to the SQLite database.
        """
        memory = self.db.query(AgentMemory).filter(
            AgentMemory.agent_name == agent_name, AgentMemory.key == key
        ).first()

        if memory:
            memory.value = value
        else:
            memory = AgentMemory(agent_name=agent_name, key=key, value=value)
            self.db.add(memory)
        
        self.db.commit()
