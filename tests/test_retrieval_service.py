import pytest

from app.services.retrieval_service import cosine_similarity


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