"""
Knowledge Retriever (Local Laboratory Blueprint)
Manages local unstructured research files and documentation grounding.
"""

from pathlib import Path

class KnowledgeRetriever:
    def __init__(self, base_path="data/knowledge"):
        self.base_path = Path(base_path)

    def list_documents(self) -> list:
        """
        Lists all available local reference files.
        """
        if not self.base_path.exists():
            return []
        return [p.name for p in self.base_path.iterdir() if p.is_file()]

    def read_document(self, filename: str) -> str:
        """
        Reads content from a specific institutional research document.
        Returns empty string if the file does not exist to prevent false grounding.
        """
        path = self.base_path / filename
        if path.exists() and path.suffix.lower() in [".txt", ".md"]:
            return path.read_text(encoding="utf-8")
        if path.exists():
            return f"[Simulated Content for Binary/PDF Document: {filename}]"
        return ""