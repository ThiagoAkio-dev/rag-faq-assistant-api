import json

from app.db.sqlite_logs import insert_log
from app.services.retrieval_service import retrieve_contexts


def build_answer_from_context(question: str, contexts: list[dict]) -> str:
    if not contexts:
        return "Não encontrei informação suficiente nos documentos para responder."

    best_context = contexts[0]["chunk_text"]

    return (
        "Com base nos documentos carregados, esta é a informação mais relevante encontrada:\n\n"
        f"{best_context}"
    )


def answer_question(question: str, top_k: int) -> dict:
    contexts = retrieve_contexts(question=question, top_k=top_k)
    answer = build_answer_from_context(question=question, contexts=contexts)

    insert_log(
        question=question,
        answer=answer,
        contexts=json.dumps(contexts, ensure_ascii=False),
    )

    return {
        "question": question,
        "answer": answer,
        "contexts": contexts,
    }