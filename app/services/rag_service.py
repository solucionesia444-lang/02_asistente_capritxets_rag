from app.services.embedding_service import get_embedding
from app.services.retrieval_service import retrieve_top_k


def retrieve_context(
        query: str,
        chunks: list[dict],
        client,
        k: int = 3,
) -> list[dict]:
    query_embedding=get_embedding(query, client=client)
    return retrieve_top_k(query_embedding, chunks, k=k)