def hit_at_k(
    retrieved_chunks: list[dict],
    expected_text: str,
) -> bool:
    expected = expected_text.lower()

    return any(
        expected in chunk["content"].lower()
        for chunk in retrieved_chunks
    )

def hit_rate(results: list[bool]) -> float:
  if not results:
      return 0.0

  return sum(results) / len(results)
