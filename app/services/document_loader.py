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

def split_documents(
    documents: list[dict[str, str]],
) -> list[dict[str, str | int]]:
    """Fragmenta documentos conservando su procedencia."""
    chunks: list[dict[str, str | int]] = []
    for document in documents:
       sections = document["content"].split("\n\n")
       for chunk_index, section in enumerate(sections):
           content = section.strip()  
           if not content:
               continue
           chunks.append(
        {
                "path": document["path"],
                "chunk_index": chunk_index,
                "content": content,
        }
            )
    return chunks