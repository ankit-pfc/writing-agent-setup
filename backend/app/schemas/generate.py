from pydantic import BaseModel
from typing import Optional

class GenerateRequest(BaseModel):
    topic: str
    page_type: str

class GenerateResponse(BaseModel):
    pipeline_id: str
    status: str
    message: str

class PipelineStatusResponse(BaseModel):
    id: str
    topic: str
    page_type: str
    status: str
    content: Optional[str] = None
    metadata_json: Optional[dict] = None
