from pathlib import Path

from app.core.openai_client import client
from app.services.document_loader import load_markdown_documents, split_documents
from app.services.embedding_service import embed_chunks

documents = load_markdown_documents(Path("data/raw"))
chunks = split_documents(documents)

embedded_chunks = None


def get_embedded_chunks():
    global embedded_chunks

    if embedded_chunks is None:
        embedded_chunks = embed_chunks(chunks, client=client)

    return embedded_chunks