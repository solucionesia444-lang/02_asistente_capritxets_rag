from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app, get_embedded_chunks

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_rag_endpoint_returns_answer():
    with patch("app.main.get_embedded_chunks") as mock_get_embedded_chunks:
        mock_get_embedded_chunks.return_value = []

        with patch("app.main.answer_query") as mock_answer_query:
            mock_answer_query.return_value = "Sí, tenemos tartas personalizadas."

            response = client.post(
                "/rag",
                json={"query": "¿Tenéis tartas?"},
            )

            assert response.status_code == 200
            assert response.json() == {
                "answer": "Sí, tenemos tartas personalizadas."
            }    

def test_get_embedded_chunks_uses_cache():
    cached_chunks = [{"content": "Tartas", "embedding": [0.1, 0.2]}]

    with patch("app.main.embed_chunks") as mock_embed_chunks:
        mock_embed_chunks.return_value = cached_chunks

        first_result = get_embedded_chunks()
        second_result = get_embedded_chunks()

        assert first_result == cached_chunks
        assert second_result == cached_chunks
        assert mock_embed_chunks.call_count == 1