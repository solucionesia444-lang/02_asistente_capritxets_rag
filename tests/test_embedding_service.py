from unittest.mock import Mock

import pytest

from app.services.embedding_service import (
    EMBEDDING_MODEL,
    get_embedding,
    get_embeddings,
)


def test_get_embedding_rejects_empty_text():
    with pytest.raises(ValueError, match="Text cannot be empty."):
        get_embedding("", client=None)

def test_get_embedding_rejects_whitespace_only_text():
    with pytest.raises(ValueError, match="Text cannot be empty."):
        get_embedding("  ", client=None)

def test_get_embedding_returns_embedding_from_client():
    client_mock = Mock()
    expected_embedding = [0.1, 0.2, 0.3]
    test_text= "Hola"
    embedding_item = Mock()
    embedding_item.embedding = expected_embedding
    response_mock = Mock()
    response_mock.data = [embedding_item]
    client_mock.embeddings.create.return_value = response_mock
    result = get_embedding(test_text, client=client_mock)
    assert result == expected_embedding
    assert client_mock.embeddings.create.call_args.kwargs == {
    "model": EMBEDDING_MODEL,
    "input": test_text,
}

def test_get_embeddings_returns_embedding_for_each_chunk():
  client_mock = Mock()
  chunks = ["chunk uno", "chunk dos"]
  embedding_one = [0.1, 0.2]
  embedding_two = [0.3, 0.4]
  embedding_item_one = Mock()
  embedding_item_one.embedding = embedding_one
  embedding_item_two = Mock()
  embedding_item_two.embedding = embedding_two
  response_one = Mock()
  response_one.data = [embedding_item_one]
  response_two = Mock()
  response_two.data = [embedding_item_two]
  client_mock.embeddings.create.side_effect = [response_one, response_two]
  result = get_embeddings(chunks, client=client_mock)
  assert result == [embedding_one, embedding_two]
  assert client_mock.embeddings.create.call_count == 2