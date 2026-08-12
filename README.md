# Asistente Capritxets RAG

Asistente de atención al cliente para Capritxets, desarrollado con FastAPI y preparado para incorporar una arquitectura RAG.

## Estado actual

El proyecto cuenta con un backend mínimo sin IA que incluye:

- Aplicación FastAPI funcional.
- Endpoint `GET /health`.
- Documentación automática en `/docs`.
- Primera prueba automática con Pytest.
- Cobertura actual del 100 % en `app/main.py`.
- Control de calidad con Ruff.

## Tecnologías

- Python 3.14.3
- FastAPI
- Uvicorn
- Pydantic Settings
- Pytest
- Pytest-cov
- Ruff
- HTTPX

## Estructura actual

```text
app/
└── main.py

tests/
└── test_main.py

CHECKPOINT.md
README.md
requirements.txt
```

## Ejecución local

Con el entorno virtual activado, iniciar la API con:

`python -m uvicorn app.main:app --reload`

La API estará disponible en:

- Salud: `http://127.0.0.1:8000/health`
- Documentación: `http://127.0.0.1:8000/docs`

## Pruebas

Ejecutar las pruebas automáticas con:

`python -m pytest -v`

Para medir la cobertura:

`python -m pytest --cov=app --cov-report=term-missing`

## Calidad del código

Comprobar el código con Ruff:

`python -m ruff check app tests`

## Próximos pasos

- Incorporar la base de conocimiento de Capritxets.
- Dividir los documentos en fragmentos.
- Generar embeddings.
- Implementar la recuperación de información.
- Integrar el modelo de lenguaje.