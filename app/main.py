from fastapi import FastAPI, HTTPException

from app.core.exceptions import ExternalServiceError
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
    try:
       answer = answer_query(
          payload.query,
          get_embedded_chunks(),
          client,
        )
    except ExternalServiceError as exc:
        raise HTTPException(
        status_code=503,
        detail="External service temporarily unavailable",
    ) from exc

    return {"answer": answer}