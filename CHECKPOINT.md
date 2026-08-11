# CHECKPOINT — Asistente Capritxets RAG

## Información general

- Proyecto: `02_asistente_capritxets_rag`
- Fecha del checkpoint: 10 de agosto de 2026
- Entorno: Windows, Visual Studio Code y PowerShell
- Ruta local: `C:\Users\servi\portafolio-ia-generativa\02_asistente_capritxets_rag`

## Objetivo del proyecto

Construir un asistente RAG profesional para Capritxets que pueda consultar documentos del negocio, recuperar información relevante y generar respuestas fundamentadas.

El desarrollo se realizará progresivamente, comenzando con un backend funcional sin inteligencia artificial.

## Estado actual

### Bloque A1 — Definición del proyecto

Completado:

- Validación de la idea.
- Requisitos.
- Alcance.
- Definición de terminado.

### Bloque A2 — Preparación del proyecto

Completado:

- Carpeta del proyecto creada.
- Proyecto abierto en Visual Studio Code.
- Estructura inicial de carpetas creada.
- Entorno virtual `.venv` creado y activado.
- Intérprete del entorno virtual seleccionado.
- Python comprobado: `3.14.3`.
- `pip` actualizado: `26.2.1`.

### Bloque A3 — Dependencias base

Completado:

- FastAPI `0.141.1`.
- Uvicorn `0.52.1`.
- Pydantic Settings instalado.
- Pytest `9.1.1`.
- Pytest-cov `7.1.0`.
- Ruff `0.16.2`.
- Archivo `requirements.txt` generado y verificado.

## Incidencias solucionadas

1. PowerShell no pudo crear inicialmente algunas carpetas porque sus carpetas superiores todavía no existían.
2. `pytest` y `pytest-cov` se escribieron unidos como `pytestpytest-cov`.
3. Se utilizó por error `pip install freeze` en lugar de `pip freeze`.

Todas las incidencias fueron identificadas, comprendidas y corregidas sin dañar el proyecto.

## Estado actual
El Bloque A5 — Backend mínimo sin IA está completado. Los resultados, comprobaciones e incidencias están registrados al final de este documento.

## Cómo retomar el proyecto

Abrir PowerShell en la carpeta del proyecto y activar el entorno:

```powershell
cd C:\Users\servi\portafolio-ia-generativa\02_asistente_capritxets_rag
.\.venv\Scripts\Activate.ps1


## Bloque A5 — Backend mínimo sin IA completado

Se creó la aplicación mínima de FastAPI en `app/main.py` con:

- Nombre: Asistente Capritxets RAG.
- Versión: 0.1.0.
- Endpoint `GET /health`.
- Respuesta esperada: `{"status": "ok"}`.

Comprobaciones realizadas:

- Ruff aprobó `app/main.py` y `tests/test_main.py`.
- Uvicorn inició correctamente.
- `/health` respondió correctamente desde el navegador.
- `/docs` mostró la documentación automática de la API.
- Uvicorn se detuvo correctamente con `Ctrl + C`.
- Se creó la primera prueba automática en `tests/test_main.py`.
- Pytest descubrió y aprobó la prueba: `1 passed`.
- La cobertura actual de `app/main.py` es del 100 %.
- Se instaló `httpx==0.28.1` para utilizar `TestClient`.
- `requirements.txt` se actualizó en UTF-8 y se verificó que contiene `httpx`.

### Incidencias del Bloque A5

- La primera ejecución de Pytest se detuvo porque faltaba `httpx`. No fue un error de escritura y se solucionó instalando la dependencia.
- Pytest muestra una advertencia de compatibilidad, pero la prueba se ejecuta y se aprueba correctamente.
- La primera redirección de `pip freeze` produjo un problema de lectura por codificación. Se solucionó guardando `requirements.txt` explícitamente en UTF-8.