from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from app.core.config import COLLECTION_NAME, EMBEDDING_DIMENSION, QDRANT_PATH

client = QdrantClient(path=QDRANT_PATH)


def ensure_collection() -> None:
    collections = client.get_collections().collections
    existing_names = {collection.name for collection in collections}

    if COLLECTION_NAME not in existing_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=EMBEDDING_DIMENSION,
                distance=Distance.COSINE,
            ),
        )