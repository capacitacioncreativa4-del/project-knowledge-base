from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from pkb.knowledge.relationship import Relationship


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
    _typed_relationships: List[Relationship] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    def __post_init__(self) -> None:
        """Construye la representación tipada a partir de las relaciones heredadas."""
        self._typed_relationships = [
            Relationship(
                relation_type="related",
                target_id=target_id,
            )
            for target_id in self.relationships
        ]

    @property
    def typed_relationships(self) -> List[Relationship]:
        """Devuelve las relaciones en su representación tipada."""
        return list(self._typed_relationships)

    def add_relationship(
        self,
        relation_type: str,
        target_id: str,
    ) -> None:
        """Agrega una relación tipada manteniendo la representación compatible."""
        relationship = Relationship(
            relation_type=relation_type,
            target_id=target_id,
        )

        self._typed_relationships.append(relationship)

        if target_id not in self.relationships:
            self.relationships.append(target_id)
