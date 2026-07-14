from pathlib import Path
from pkb.knowledge.object import KnowledgeObject

class KnowledgeObjectBuilder:
    """Responsable de la construcción y tipado estricto de objetos de conocimiento."""

    @staticmethod
    def build(metadata: dict, source_path: Path) -> KnowledgeObject:
        """Construye una instancia válida de KnowledgeObject a partir de un diccionario de metadatos."""
        # Extraemos y normalizamos las cadenas críticas a mayúsculas limpias
        raw_type = metadata.get("type", "UNK")
        raw_domain = metadata.get("domain", "UNK")
        
        object_type = str(raw_type).upper().strip()
        domain = str(raw_domain).upper().strip()

        return KnowledgeObject(
            identifier=metadata.get("id"),
            title=metadata.get("title", "Untitled"),
            object_type=object_type,
            domain=domain,
            version=metadata.get("version", "0.1.0"),
            status=metadata.get("status", "Draft"),
            owner=metadata.get("owner", "Unknown"),
            source=source_path,
            tags=metadata.get("tags", [])
        )