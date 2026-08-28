from app.services.embedding_service import get_embedding
from app.services.generation_service import generate_answer
from app.services.retrieval_service import retrieve_top_k


def retrieve_context(
        query: str,
        chunks: list[dict],
        client,
        k: int = 3,
) -> list[dict]:
    query_embedding=get_embedding(query, client=client)
    return retrieve_top_k(query_embedding, chunks, k=k)

def answer_query(query, chunks, client):
    context = retrieve_context(query, chunks, client)
    context_texts = [item["content"] for item in context]
    return generate_answer(query, context_texts, client=client)