from unittest.mock import patch

import pytest

from app.services.rag_service import answer_query, retrieve_context


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

def test_retrieve_context_with_empty_chunks():
    query = "¿Qué productos ofrecéis?"
    chunks = []
    client = object()
    query_embedding = [0.1, 0.2]

    with patch("app.services.rag_service.get_embedding") as mock_get_embedding:
        mock_get_embedding.return_value = query_embedding

        with patch("app.services.rag_service.retrieve_top_k") as mock_retrieve_top_k:
            mock_retrieve_top_k.return_value = []

            result = retrieve_context(query, chunks, client)

            assert result == []
            mock_retrieve_top_k.assert_called_once_with(
                query_embedding, chunks, k=3
            )

def test_retrieve_context_does_not_retrieve_when_embedding_fails():
  query = "¿Qué productos ofrecéis?"
  chunks = [{"content": "Tartas de chuches", "embedding": [0.1, 0.2]}]
  client = object()
  with patch("app.services.rag_service.get_embedding") as mock_get_embedding:
    mock_get_embedding.side_effect = RuntimeError("embedding failed")
    with patch("app.services.rag_service.retrieve_top_k") as mock_retrieve_top_k:
      with pytest.raises(RuntimeError, match="embedding failed"):
          retrieve_context(query, chunks, client)
      mock_retrieve_top_k.assert_not_called()

def test_retrieve_context_propagates_retrieval_failure():
   query = "¿Qué productos ofrecéis?"
   chunks = [{"content": "Tartas de chuches", "embedding": [0.1, 0.2]}]
   client = object()
   query_embedding = [0.1, 0.2]
   with patch("app.services.rag_service.get_embedding") as mock_get_embedding:
       mock_get_embedding.return_value = query_embedding

       with patch("app.services.rag_service.retrieve_top_k") as mock_retrieve_top_k:
            mock_retrieve_top_k.side_effect = RuntimeError("retrieval failed")

            with pytest.raises(RuntimeError, match="retrieval failed"):
                retrieve_context(query, chunks, client)

            mock_retrieve_top_k.assert_called_once_with(
                query_embedding, chunks, k=3
            )

def test_answer_query_retrieves_context_and_generates_answer():
  query = "¿Tenéis tartas?"
  chunks = [{"content": "Tenemos tartas personalizadas."}]
  client = object()
  context = [{"content": "Tenemos tartas personalizadas."}]

  with patch("app.services.rag_service.retrieve_context") as mock_retrieve_context:
      mock_retrieve_context.return_value = context

      with patch("app.services.rag_service.generate_answer") as mock_generate_answer:
          mock_generate_answer.return_value = "Sí, tenemos tartas personalizadas."

          result = answer_query(query, chunks, client)

          assert result == "Sí, tenemos tartas personalizadas."
          mock_retrieve_context.assert_called_once_with(query, chunks, client)