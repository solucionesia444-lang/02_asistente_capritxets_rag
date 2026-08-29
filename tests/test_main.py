from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_rag_endpoint_returns_answer():
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