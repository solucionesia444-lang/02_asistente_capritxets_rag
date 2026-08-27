def generate_answer(query, context, client):
    response = client.responses.create(
        input= f"Pregunta: {query }\nContexto: {' '.join(context)}"
    )
    return response.output_text