from unittest.mock import patch

import pytest

import app.services.knowledge_base_service as knowledge_base_module
from app.services.knowledge_base_service import get_embedded_chunks


def test_get_embedded_chunks_keeps_cache_empty_if_embedding_fails():
    with (
        patch(
            "app.services.knowledge_base_service.embedded_chunks",
            None,
        ),
        patch(
            "app.services.knowledge_base_service.embed_chunks",
            side_effect=RuntimeError("Embedding failed"),
        ),
    ):
        with pytest.raises(RuntimeError, match="Embedding failed"):
            get_embedded_chunks()

        assert knowledge_base_module.embedded_chunks is None


def test_get_embedded_chunks_uses_cache():
    cached_chunks = [{"content": "Tartas", "embedding": [0.1, 0.2]}]

    with (
        patch(
            "app.services.knowledge_base_service.embedded_chunks",
            None,
        ),
        patch(
            "app.services.knowledge_base_service.embed_chunks",
        ) as mock_embed_chunks,
    ):
        mock_embed_chunks.return_value = cached_chunks

        first_result = get_embedded_chunks()
        second_result = get_embedded_chunks()

        assert first_result == cached_chunks
        assert second_result == cached_chunks
        assert mock_embed_chunks.call_count == 1