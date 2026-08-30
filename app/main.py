from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.core.openai_client import client
from app.services.document_loader import load_markdown_documents, split_documents
from app.services.embedding_service import embed_chunks
from app.services.rag_service import answer_query


class RagRequest(BaseModel):
    query: str= Field(min_length=1, pattern=r".*\S.*")

documents = load_markdown_documents(Path("data/raw"))
chunks = split_documents(documents)

embedded_chunks = None


def get_embedded_chunks():
    global embedded_chunks

    if embedded_chunks is None:
        embedded_chunks = embed_chunks(chunks, client=client)

    return embedded_chunks

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