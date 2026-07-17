from dataclasses import dataclass, field
from pathlib import Path
from typing import List

@dataclass(slots=True)
class KnowledgeObject:
    """Representa un objeto de conocimiento formal dentro del dominio de la plataforma PKB."""
    identifier: str
    title: str
    object_type: str
    domain: str
    version: str
    status: str
    owner: str
    source: Path
    tags: List[str] = field(default_factory=list)
    relationships: List[str] = field(default_factory=list)