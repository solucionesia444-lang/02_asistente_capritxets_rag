from fastapi import FastAPI

from app.core.openai_client import client
from app.schemas.rag import RagRequest
from app.services.knowledge_base_service import get_embedded_chunks
from app.services.rag_service import answer_query

app = FastAPI(
    title="Asistente Capritxets RAG",
    version="0.1.0",
)

@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/rag")
def rag_endpoint(payload: RagRequest) -> dict[str, str]:
    answer = answer_query(
        payload.query,
        get_embedded_chunks(),
       client,
    )
    return {"answer": answer}