# Asistente Capritxets RAG
Asistente de atención al cliente para Capritxets desarrollado con FastAPI y una arquitectura RAG (Retrieval-Augmented Generation).

El sistema utiliza una base de conocimiento propia del negocio, divide la documentación en fragmentos, genera embeddings, recupera el contexto más relevante para cada consulta y utiliza un modelo de lenguaje para generar la respuesta final.

## Estado actual

El proyecto cuenta actualmente con un backend RAG funcional que incluye:

- API desarrollada con FastAPI.
- Endpoint `GET /health` para comprobar el estado del servicio.
- Endpoint `POST /rag` para realizar consultas al asistente.
- Validación de entrada con Pydantic.
- Carga automática de documentos Markdown.
- División de documentos en fragmentos.
- Generación de embeddings.
- Caché de embeddings para evitar procesamiento innecesario.
- Recuperación semántica del contexto más relevante.
- Generación de respuestas utilizando un modelo de lenguaje.
- Separación de responsabilidades mediante servicios independientes.
- Manejo de errores de servicios externos mediante `ExternalServiceError`.
- Respuesta HTTP `503` segura cuando un proveedor externo no está disponible.
- Protección frente a filtración de detalles internos del proveedor.
- Pruebas unitarias y de integración con pytest.
- 43 pruebas automatizadas pasando correctamente.
- Control de calidad del código con Ruff.
- Documentación interactiva automática mediante Swagger en `/docs`.

## Tecnologías

- Python 3.14.3
- FastAPI
- Uvicorn
- Pydantic / Pydantic Settings
- OpenAI API
- Embeddings
- Arquitectura RAG
- Pytest
- Pytest-cov
- Ruff
- HTTPX
- unittest.mock

## Estructura actual
```text
app/
├── core/
│   ├── exceptions.py
│   └── openai_client.py
├── schemas/
│   └── rag.py
├── services/
│   ├── document_loader.py
│   ├── embedding_service.py
│   ├── generation_service.py
│   ├── knowledge_base_service.py
│   ├── rag_service.py
│   └── retrieval_service.py
└── main.py

data/
└── raw/
    └── documentos de la base de conocimiento

tests/
├── test_document_loader.py
├── test_embedding_service.py
├── test_generation_service.py
├── test_knowledge_base_service.py
├── test_main.py
├── test_rag_service.py
└── test_retrieval_service.py

CHECKPOINT.md
README.md
```
requirements.txt

## Ejecución local

Con el entorno virtual activado, iniciar la API con:

`python -m uvicorn app.main:app --reload`

La API estará disponible en:

- Salud: `http://127.0.0.1:8000/health`
- RAG: `http://127.0.0.1:8000/rag`
- Documentación interactiva: `http://127.0.0.1:8000/docs`

## Ejemplo de uso de `/rag`

Solicitud:

` ```json
{
  "query": "¿Tenéis tartas?"
} `


Respuesta esperada:

` ```json
{
  "answer": "Sí, tenemos tartas personalizadas."
} ```

El endpoint utiliza la consulta del usuario para:

1. Generar el embedding de la pregunta.
2. Recuperar los fragmentos más relevantes de la base de conocimiento.
3. Construir el contexto.
4. Enviar pregunta y contexto al modelo de lenguaje.
5. Devolver una respuesta fundamentada en la información recuperada.


## Pruebas

Ejecutar todas las pruebas automatizadas con:

`python -m pytest -q`

Estado actual:

- 43 pruebas automatizadas pasando correctamente.
- Cobertura actual del código: `100%` .
- Tests unitarios sobre servicios.
- Tests de integración del endpoint `/rag`.
- Validación de errores `422`.
- Validación de errores externos `503`.
- Comprobación de que no se filtran detalles internos del proveedor.

Para medir la cobertura:

`python -m pytest --cov=app --cov-report=term-missing`

## Calidad del código

Comprobar el código con Ruff:

`python -m ruff check app tests`

## Próximos pasos

- Ampliar los ejemplos de uso del endpoint `/rag` con ejemplos ejecutables.
- Documentar visualmente la arquitectura y las decisiones técnicas.
- Incorporar evaluación del sistema RAG.
- Añadir métricas de calidad de retrieval y generación.
- Revisar seguridad y configuración para producción.
- Preparar el frontend o interfaz visual del asistente.
- Preparar despliegue y entrega continua (CD).
- Preparar una demostración profesional para portfolio y entrevistas técnicas.
