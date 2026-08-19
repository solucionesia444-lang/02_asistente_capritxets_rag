import pytest

from app.services.retrieval_service import cosine_similarity, retrieve_top_k


def test_cosine_similarity_identical_vectors():
    vector_a = [1.0, 0.0]
    vector_b = [1.0, 0.0]
    result = cosine_similarity(vector_a, vector_b)
    assert result == 1.0

def test_cosine_similarity_orthogonal_vectors():
    vector_a = [1.0, 0.0]
    vector_b = [0.0, 1.0]
    result = cosine_similarity(vector_a, vector_b)
    assert result == 0.

def test_cosine_similarity_rejects_zero_vector():
    vector_a = [0.0, 0.0]
    vector_b = [1.0, 0.0]
    with pytest.raises(ValueError):
        cosine_similarity(vector_a, vector_b)

def test_retrieve_top_k_returns_most_similar_chunk():
    query_embedding = [1.0, 0.0]
    chunks = [
        {"content": "Chunk 1", "embedding": [1.0, 0.0]},
        {"content": "Chunk 2", "embedding": [0.0, 1.0]},
        {"content": "Chunk 3", "embedding": [0.5, 0.5]},
    ]
    result = retrieve_top_k(query_embedding, chunks, k=1)
    assert result[0]["content"] == "Chunk 1"

def test_retrieve_top_k_returns_results_in_similarity_order():
    query_embedding = [1.0, 0.0]
    chunks = [
        {"content": "Chunk 1", "embedding": [1.0, 0.0]},
        {"content": "Chunk 2", "embedding": [0.5, 0.5]},    
        {"content": "Chunk 3", "embedding": [0.0, 1.0]},
    ]
    result = retrieve_top_k(query_embedding, chunks, k=2)
    assert result[0]["content"] == "Chunk 1"
    assert result[1]["content"] == "Chunk 2"

def test_retrieve_top_k_returns_exactly_k_results():
    query_embedding = [1.0, 0.0]
    chunks = [
        {"content": "Chunk 1", "embedding": [1.0, 0.0]},
        {"content": "Chunk 2", "embedding": [0.5, 0.5]},
        {"content": "Chunk 3", "embedding": [0.0, 1.0]},
    ]
    result = retrieve_top_k(query_embedding, chunks, k=2)
    assert len(result) == 2

def test_retrieve_top_k_with_zero_k():
    query_embedding = [1.0, 0.0]
    chunks = [
        {"content": "Chunk 1", "embedding": [1.0, 0.0]},
        {"content": "Chunk 2", "embedding": [0.5, 0.5]},
    ]
    result = retrieve_top_k(query_embedding, chunks, k=0)
    assert result == []