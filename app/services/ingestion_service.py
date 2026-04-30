import uuid

from qdrant_client.models import PointStruct

from app.core.config import COLLECTION_NAME
from app.db.qdrant_client import client
from app.schemas.document import DocumentInput
from app.utils.chunking import chunk_text
from app.utils.embeddings import embedding_model


def ingest_documents(documents: list[DocumentInput]) -> tuple[int, list[str]]:
    points = []
    document_ids = []
    inserted_chunks = 0

    for document in documents:
        document_ids.append(document.doc_id)
        chunks = chunk_text(document.text)

        for chunk_index, chunk in enumerate(chunks):
            vector = embedding_model.embed(chunk)

            payload = {
                "doc_id": document.doc_id,
                "title": document.title,
                "chunk_text": chunk,
                "chunk_index": chunk_index,
                "metadata": document.metadata,
            }

            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload=payload,
            )
            points.append(point)
            inserted_chunks += 1

    if points:
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
        )

    return inserted_chunks, document_ids