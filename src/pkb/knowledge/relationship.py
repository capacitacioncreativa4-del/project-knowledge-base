from dataclasses import dataclass

@dataclass(slots=True)
class Relationship:
    """Representa una relación semántica dirigida entre dos objetos de conocimiento."""
    source: str
    target: str
    relation_type: str