from pathlib import Path


def load_markdown_documents(directory: Path) -> list[dict[str, str]]:
  """Carga documentos Markdown desde una carpeta."""

  documents: list[dict[str, str]] = []
  if not directory.is_dir():
    raise NotADirectoryError(f"No existe la carpeta: {directory}")

  for file_path in sorted(directory.glob("*.md")):
    content = file_path.read_text(encoding="utf-8")
    documents.append({"path": str(file_path), "content": content})
  return documents