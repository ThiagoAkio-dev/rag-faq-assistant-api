import sqlite3
from app.core.config import SQLITE_PATH


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(SQLITE_PATH)


def init_db() -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS query_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            contexts TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_log(question: str, answer: str, contexts: str) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO query_logs (question, answer, contexts)
        VALUES (?, ?, ?)
        """,
        (question, answer, contexts),
    )

    conn.commit()
    conn.close()


def fetch_logs() -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question, answer, contexts, created_at
        FROM query_logs
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "question": row[1],
            "answer": row[2],
            "contexts": row[3],
            "created_at": row[4],
        }
        for row in rows
    ]