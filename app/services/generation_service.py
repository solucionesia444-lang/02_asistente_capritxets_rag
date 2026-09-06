from app.core.exceptions import ExternalServiceError


def generate_answer(query, context, client):
    try:
       response = client.responses.create(
          model="gpt-5-mini",
           input=f"Pregunta: {query}\nContexto: {' '.join(context)}"
        )
    except Exception as exc:
     raise ExternalServiceError("Generation service failed") from exc

    return response.output_text