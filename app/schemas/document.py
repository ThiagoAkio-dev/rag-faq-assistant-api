from typing import Any
from pydantic import BaseModel, Field


class DocumentInput(BaseModel):
    doc_id: str = Field(..., description="Unique document id")
    title: str
    text: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class DocumentBatchInput(BaseModel):
    documents: list[DocumentInput]


class DocumentResponse(BaseModel):
    message: str
    inserted_chunks: int
    document_ids: list[str]