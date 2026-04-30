from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

QDRANT_PATH = str(BASE_DIR / "qdrant_data")
COLLECTION_NAME = "faq_documents"

SQLITE_PATH = str(BASE_DIR / "logs.db")

EMBEDDING_DIMENSION = 384
TOP_K_DEFAULT = 3