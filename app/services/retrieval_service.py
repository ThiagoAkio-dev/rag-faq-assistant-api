from app.core.config import COLLECTION_NAME
from app.db.qdrant_client import client
from app.utils.embeddings import embedding_model


def retrieve_contexts(question: str, top_k: int = 3) -> list[dict]:
    query_vector = embedding_model.embed(question)

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k,
    )

    contexts = []
    for result in results:
        payload = result.payload or {}
        contexts.append(
            {
                "doc_id": payload.get("doc_id", ""),
                "title": payload.get("title", ""),
                "chunk_text": payload.get("chunk_text", ""),
                "score": float(result.score),
                "metadata": payload.get("metadata", {}),
            }
        )

    return contexts