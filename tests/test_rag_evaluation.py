from pathlib import Path

from app.services.document_loader import load_markdown_documents, split_documents
from app.services.rag_evaluation_service import hit_at_k


def test_faq_contains_relevant_tarta_chunk():
    documents = load_markdown_documents(Path("data/raw"))
    chunks = split_documents(documents)

    matching_chunks = [
        chunk
        for chunk in chunks
        if "tarta de chuches" in chunk["content"].lower()
    ]

    assert matching_chunks


def test_hit_at_k_returns_true_when_expected_content_is_retrieved():
    retrieved_chunks = [
        {"content": "Horario de atención"},
        {"content": "Las tartas de chuches deben solicitarse con anticipación"},
    ]

    result = hit_at_k(
        retrieved_chunks,
        expected_text="tartas de chuches",
    )

    assert result is True


def test_hit_at_k_returns_false_when_expected_content_is_not_retrieved():
    retrieved_chunks = [
        {"content": "Horario de atención"},
        {"content": "Información sobre ubicación"},
    ]

    result = hit_at_k(
        retrieved_chunks,
        expected_text="tartas de chuches",
    )

    assert result is False