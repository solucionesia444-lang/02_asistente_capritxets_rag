from unittest.mock import patch

from fastapi.testclient import TestClient

import app.main as main_module
from app.core.exceptions import ExternalServiceError
from app.main import app

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

def test_rag_endpoint_rejects_missing_query():
    response = client.post(
        "/rag",
        json={},
    )

    assert response.status_code == 422

def test_rag_endpoint_rejects_empty_query():
    with (
        patch("app.main.get_embedded_chunks", return_value=[]),
        patch("app.main.answer_query", return_value="Respuesta"),
    ):
        response = client.post(
            "/rag",
            json={"query": ""},
        )

    assert response.status_code == 422   

def test_rag_endpoint_rejects_whitespace_query():
    with (
        patch("app.main.get_embedded_chunks", return_value=[]),
        patch("app.main.answer_query", return_value="Respuesta"),
    ):
        response = client.post(
            "/rag",
            json={"query": "   "},
        )

    assert response.status_code == 422     

def test_rag_endpoint_passes_embedded_chunks_to_answer_query():
  embedded_chunks = [
      {"content": "Tartas personalizadas", "embedding": [0.1, 0.2]}
  ]

  with (
      patch("app.main.get_embedded_chunks", return_value=embedded_chunks),
      patch("app.main.answer_query", return_value="Respuesta") as mock_answer_query,
  ):
      client.post(
          "/rag",
          json={"query": "¿Tenéis tartas?"},
      )

      mock_answer_query.assert_called_once_with(
          "¿Tenéis tartas?",
          embedded_chunks,
          main_module.client,
      )

def test_rag_endpoint_returns_503_when_external_service_fails():
  with (
      patch("app.main.get_embedded_chunks", return_value=[]),
      patch(
          "app.main.answer_query",
          side_effect=ExternalServiceError("secret provider detail"),
      ),
  ):
      response = client.post(
          "/rag",
          json={"query": "¿Tenéis tartas?"},
      )

  assert response.status_code == 503
  assert response.json() == {
      "detail": "External service temporarily unavailable"
  }            