from fastapi import APIRouter

from app.db.sqlite_logs import fetch_logs
from app.schemas.ask import AskRequest, AskResponse, ContextItem
from app.services.qa_service import answer_question

router = APIRouter(tags=["qa"])


@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest) -> AskResponse:
    result = answer_question(
        question=payload.question,
        top_k=payload.top_k,
    )

    contexts = [ContextItem(**context) for context in result["contexts"]]

    return AskResponse(
        question=result["question"],
        answer=result["answer"],
        contexts=contexts,
    )


@router.get("/logs")
def get_logs():
    return fetch_logs()