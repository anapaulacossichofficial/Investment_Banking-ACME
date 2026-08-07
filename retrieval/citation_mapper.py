"""
Citation Mapper (Local Laboratory Blueprint)
Standardizes source attribution tags for Zero Trust output generation.
"""

class CitationMapper:
    @staticmethod
    def format_crm(reference_id: str) -> str:
        """Formats CRM record identifiers into strict source tags."""
        return f"[Source: CRM {reference_id}]"

    @staticmethod
    def format_document(filename: str) -> str:
        """Formats research file names into strict document citation tags."""
        return f"[Document: {filename}]"