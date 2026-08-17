from unittest.mock import Mock

import pytest

from app.services.embedding_service import EMBEDDING_MODEL, get_embedding


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