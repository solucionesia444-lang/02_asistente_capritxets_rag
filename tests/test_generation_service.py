from unittest.mock import Mock

from app.services.generation_service import generate_answer


def test_generate_answer_returns_model_response():
  client = Mock()
  client.responses.create.return_value.output_text = "Tenemos tartas de chuches."

  result = generate_answer(
      "¿Tenéis tartas?",
      ["Tenemos tartas de chuches personalizadas."],
      client=client,
  )

  assert result == "Tenemos tartas de chuches."

def test_generate_answer_sends_query_and_context_to_model():
    client = Mock()
    client.responses.create.return_value.output_text = "Respuesta"

    generate_answer(
        "¿Tenéis tartas?",
        ["Tenemos tartas personalizadas."],
        client=client,
    )

    call_kwargs = client.responses.create.call_args.kwargs
    assert "¿Tenéis tartas?" in call_kwargs["input"]
    assert "Tenemos tartas personalizadas." in call_kwargs["input"]