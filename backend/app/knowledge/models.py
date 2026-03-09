from pydantic import BaseModel
from typing import List, Dict

class ContentRule(BaseModel):
    page_type: str
    min_words: int
    required_sections: List[str]

class KeywordCluster(BaseModel):
    cluster_name: str
    priority: str
    keywords: List[str]

class MetaTemplate(BaseModel):
    page_type: str
    title_formula: str
    description_formula: str

class AEOPattern(BaseModel):
    query_type: str
    pattern_name: str
    example: str
    description: str

class InternalLinkTarget(BaseModel):
    concept: str
    canonical_url: str
