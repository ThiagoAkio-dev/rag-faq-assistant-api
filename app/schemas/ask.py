from typing import Any
from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str
    top_k: int = Field(default=3, ge=1, le=10)


class ContextItem(BaseModel):
    doc_id: str
    title: str
    chunk_text: str
    score: float
    metadata: dict[str, Any] = Field(default_factory=dict)


class AskResponse(BaseModel):
    question: str
    answer: str
    contexts: list[ContextItem]