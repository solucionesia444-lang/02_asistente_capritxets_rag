

EMBEDDING_MODEL = "text-embedding-3-small" 
def get_embedding(text: str, client) -> list[float]:
    if not text.strip():
        raise ValueError("Text cannot be empty.")

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )
    return response.data[0].embedding

def get_embeddings(chunks: list[str], client) -> list[list[float]]:
    return [get_embedding(chunk, client=client) for chunk in chunks]

def embed_chunks(
    chunks: list[dict[str, str | int]],
    client,
) -> list[dict[str, str | int | list[float]]]:
    embedded_chunks = []
    for chunk in chunks:
        embedding = get_embedding(chunk["content"], client=client)
        embedded_chunk = {
            **chunk,
            "embedding": embedding,
        }
        embedded_chunks.append(embedded_chunk)
    return embedded_chunks