from fastapi import FastAPI

from app.services.rag_service import answer_query

app = FastAPI(
    title="Asistente Capritxets RAG",
    version="0.1.0",
)

@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/rag")
def rag_endpoint(payload: dict[str, str]) -> dict[str, str]:
    answer = answer_query(
        payload["query"],
        [],
        None,
    )
    return {"answer": answer}