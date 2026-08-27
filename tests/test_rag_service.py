from unittest.mock import patch

from app.services.rag_service import retrieve_context


def test_retrieve_context_uses_embedding_and_retrieval():
    query = "¿Qué productos ofrecéis?"
    chunks = [{"content": "Tartas de chuches", "embedding": [0.1, 0.2]}]
    client = object()
    query_embedding = [0.1, 0.2]
    with patch("app.services.rag_service.get_embedding") as mock_get_embedding:
        mock_get_embedding.return_value = query_embedding
        with patch("app.services.rag_service.retrieve_top_k") as mock_retrieve_top_k:
            mock_retrieve_top_k.return_value = chunks
            result = retrieve_context(query, chunks, client)
            assert result == chunks
            mock_get_embedding.assert_called_once_with(query, client=client)
            mock_retrieve_top_k.assert_called_once_with(query_embedding, chunks, k=3)

def test_retrieve_context_uses_custom_k():
  query = "¿Qué productos ofrecéis?"
  chunks = [{"content": "Tartas de chuches", "embedding": [0.1, 0.2]}]
  client = object()
  query_embedding = [0.1, 0.2]

  with patch("app.services.rag_service.get_embedding") as mock_get_embedding:
      mock_get_embedding.return_value = query_embedding

      with patch("app.services.rag_service.retrieve_top_k") as mock_retrieve_top_k:
          mock_retrieve_top_k.return_value = chunks

          retrieve_context(query, chunks, client, k=2)

          mock_retrieve_top_k.assert_called_once_with(
              query_embedding, chunks, k=2
          )

            