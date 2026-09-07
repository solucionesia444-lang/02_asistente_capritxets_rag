def hit_at_k(
    retrieved_chunks: list[dict],
    expected_text: str,
) -> bool:
    expected = expected_text.lower()

    return any(
        expected in chunk["content"].lower()
        for chunk in retrieved_chunks
    )

def test_hit_at_k_returns_false_when_expected_content_is_not_retrieved():
    from app.services.rag_evaluation_service import hit_at_k

    retrieved_chunks = [
        {"content": "Horario de atención"},
        {"content": "Información sobre ubicación"},
    ]

    result = hit_at_k(
        retrieved_chunks,
        expected_text="tartas de chuches",
    )

    assert result is False