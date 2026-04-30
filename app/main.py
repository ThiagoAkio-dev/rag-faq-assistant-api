from fastapi import FastAPI

from app.api.routes_ask import router as ask_router
from app.api.routes_documents import router as documents_router
from app.api.routes_health import router as health_router
from app.db.qdrant_client import ensure_collection
from app.db.sqlite_logs import init_db

app = FastAPI(title="RAG FAQ Assistant API", version="1.0.0")


@app.on_event("startup")
def startup_event() -> None:
    ensure_collection()
    init_db()


app.include_router(health_router)
app.include_router(documents_router)
app.include_router(ask_router)