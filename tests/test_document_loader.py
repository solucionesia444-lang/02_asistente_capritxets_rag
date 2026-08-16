from pathlib import Path

import pytest

from app.services.document_loader import load_markdown_documents, split_documents


def test_load_markdown_documents_reads_files(tmp_path: Path) -> None:
  (tmp_path / "b.md").write_text("Documento B", encoding="utf-8")
  (tmp_path / "a.md").write_text("Documento A", encoding="utf-8")
  documents = load_markdown_documents(tmp_path)
  assert [document["content"] for document in documents] == ["Documento A", "Documento B"]

def test_load_markdown_documents_raises_for_missing_directory(
  tmp_path: Path,
) -> None:
  missing_directory = tmp_path / "missing"

  with pytest.raises(NotADirectoryError, match="No existe la carpeta"):
      load_markdown_documents(missing_directory)

def test_split_documents_preserves_source_and_order() -> None:
    documents = [
        {
            "path": "data/raw/faq.md",
            "content": "Primera sección.\n\nSegunda sección.",

        },
    ]
    chunks = split_documents(documents)
    assert chunks == [
        {
            "path": "data/raw/faq.md",
            "chunk_index": 0,
            "content": "Primera sección.",
        },
        {
            "path": "data/raw/faq.md",
            "chunk_index": 1,
            "content": "Segunda sección.",
        },
    ]

def test_split_documents_ignores_empty_sections() -> None:
    documents = [{"path": "data/raw/empty.md", "content":"\n\n"}]

    assert split_documents(documents) == []