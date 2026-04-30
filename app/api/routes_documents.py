from fastapi import APIRouter

from app.schemas.document import DocumentBatchInput, DocumentResponse
from app.services.ingestion_service import ingest_documents

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("", response_model=DocumentResponse)
def upload_documents(payload: DocumentBatchInput) -> DocumentResponse:
    inserted_chunks, document_ids = ingest_documents(payload.documents)

    return DocumentResponse(
        message="Documents indexed successfully",
        inserted_chunks=inserted_chunks,
        document_ids=document_ids,
    )