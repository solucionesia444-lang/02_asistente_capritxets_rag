def cosine_similarity(
    vector_a: list[float], 
    vector_b: list[float],
)  -> float:
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimensions")
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = sum(a ** 2 for a in vector_a) ** 0.5
    magnitude_b = sum(b ** 2 for b in vector_b) ** 0.5
    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("One or both vectors are zero vectors, cannot compute cosine similarity.")
    
    return dot_product / (magnitude_a * magnitude_b)

def retrieve_top_k(
        query_embedding: list[float],
        chunks: list[dict],
        k: int,
) -> list[dict]:
    if k < 0:
        raise ValueError("k must be non-negative")
    scored_chunks = []
    for chunk in chunks:
        score = cosine_similarity(query_embedding, chunk["embedding"])
        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)
    return [chunk for _, chunk in scored_chunks[:k]]