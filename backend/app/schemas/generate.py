from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class GenerateRequest(BaseModel):
    topic: str
    page_type: str
    max_revisions: Optional[int] = 3


class GenerateResponse(BaseModel):
    pipeline_id: str
    status: str
    message: str


class ContentBriefResponse(BaseModel):
    topic: str
    page_type: str
    target_audience: Optional[str] = None
    content_requirements: Optional[Dict[str, Any]] = None
    seo_requirements: Optional[Dict[str, Any]] = None


class QualityScoreResponse(BaseModel):
    total_score: Optional[float] = None
    status: Optional[str] = None
    feedback: Optional[str] = None
    dimension_1_depth: Optional[int] = None
    dimension_2_accuracy: Optional[int] = None
    dimension_3_voice: Optional[int] = None
    dimension_6_exclusion_safety: Optional[int] = None


class SEOScoreResponse(BaseModel):
    score: Optional[int] = None
    grade: Optional[str] = None
    breakdown: Optional[Dict[str, int]] = None


class PipelineStatusResponse(BaseModel):
    id: str
    topic: str
    page_type: str
    status: str
    revision_count: Optional[int] = 0
    max_revisions: Optional[int] = 3
    content: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None
    seo_output: Optional[Dict[str, Any]] = None
    content_brief: Optional[Dict[str, Any]] = None
    research_bundle: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class FeedbackRequest(BaseModel):
    pipeline_id: str
    stage: str
    feedback_type: str  # edit, approval, rejection, comment
    original_content: Optional[str] = None
    edited_content: Optional[str] = None
    comment: Optional[str] = None


class FeedbackResponse(BaseModel):
    id: int
    pipeline_id: str
    stage: str
    feedback_type: str
    comment: Optional[str] = None
    created_at: Optional[str] = None


class PipelineListResponse(BaseModel):
    id: str
    topic: str
    page_type: str
    status: str
    revision_count: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
