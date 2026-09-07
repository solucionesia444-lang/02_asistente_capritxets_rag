from pathlib import Path

from app.services.document_loader import load_markdown_documents, split_documents
from app.services.rag_evaluation_service import hit_at_k, hit_rate


def test_faq_contains_relevant_tarta_chunk():
    documents = load_markdown_documents(Path("data/raw"))
    chunks = split_documents(documents)

    matching_chunks = [
        chunk
        for chunk in chunks
        if "tarta de chuches" in chunk["content"].lower()
    ]

    assert matching_chunks


def test_hit_at_k_returns_true_when_expected_content_is_retrieved():
    retrieved_chunks = [
        {"content": "Horario de atención"},
        {"content": "Las tartas de chuches deben solicitarse con anticipación"},
    ]

    result = hit_at_k(
        retrieved_chunks,
        expected_text="tartas de chuches",
    )

    assert result is True


def test_hit_at_k_returns_false_when_expected_content_is_not_retrieved():
    retrieved_chunks = [
        {"content": "Horario de atención"},
        {"content": "Información sobre ubicación"},
    ]

    result = hit_at_k(
        retrieved_chunks,
        expected_text="tartas de chuches",
    )

    assert result is False

    
def test_hit_rate_returns_fraction_of_successful_cases():
    from app.services.rag_evaluation_service import hit_rate

    results = [True, False, True, True]

    assert hit_rate(results) == 0.75

def test_business_evaluation_case_can_be_scored_with_hit_at_k():
  retrieved_chunks = [
      {"content": "Las tartas de chuches deben solicitarse con uno o dos días de anticipación."},
      {"content": "Capritxets abre de lunes a viernes de 09:30 a 19:00."},
  ]

  result = hit_at_k(
      retrieved_chunks,
      expected_text="uno o dos días de anticipación",
  )

  assert result is True

def test_hit_rate_over_multiple_business_cases():
  results = [
      hit_at_k(
          [
              {"content": "Las tartas de chuches deben solicitarse con uno o dos días de anticipación."},
          ],
          expected_text="uno o dos días de anticipación",
      ),
      hit_at_k(
          [
              {"content": "Capritxets abre de lunes a viernes de 09:30 a 19:00."},
          ],
          expected_text="09:30 a 19:00",
      ),
      hit_at_k(
          [
              {"content": "Información sobre ubicación"},
          ],
          expected_text="alérgenos",
      ),
  ]

  assert hit_rate(results) == 2 / 3