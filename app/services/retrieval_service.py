def cosine_similarity(
    vector_a: list[float], 
    vector_b: list[float],
)  -> float:
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = sum(a ** 2 for a in vector_a) ** 0.5
    magnitude_b = sum(b ** 2 for b in vector_b) ** 0.5
    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("One or both vectors are zero vectors, cannot compute cosine similarity.")
    
    return dot_product / (magnitude_a * magnitude_b)

