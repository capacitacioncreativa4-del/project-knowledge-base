from dataclasses import dataclass, field
from pathlib import Path

from pkb.knowledge.relationship import Relationship


@dataclass(slots=True, init=False)
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
    tags: list[str] = field(default_factory=list)
    _relationship_ids: list[str] = field(
        default_factory=list,
        init=False,
        repr=False,
    )
    _typed_relationships: list[Relationship] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    def __init__(
        self,
        identifier: str,
        title: str,
        object_type: str,
        domain: str,
        version: str,
        status: str,
        owner: str,
        source: Path,
        tags: list[str] | None = None,
        relationships: list[str] | None = None,
    ) -> None:
        self.identifier = identifier
        self.title = title
        self.object_type = object_type
        self.domain = domain
        self.version = version
        self.status = status
        self.owner = owner
        self.source = source
        self.tags = list(tags or [])

        self._relationship_ids = list(relationships or [])

        self._typed_relationships = [
            Relationship(
                relation_type="related",
                target_id=target_id,
            )
            for target_id in self._relationship_ids
        ]

    @property
    def relationships(self) -> list[str]:
        """
        Compatibilidad con la API histórica.

        Devuelve los identificadores de destino conservando
        exactamente la multiplicidad declarada.
        """
        return list(self._relationship_ids)

    @relationships.setter
    def relationships(self, values: list[str]) -> None:
        """Convierte relaciones históricas a relaciones tipadas."""
        self._relationship_ids = list(values)

        self._typed_relationships = [
            Relationship(
                relation_type="related",
                target_id=value,
            )
            for value in self._relationship_ids
        ]

    @property
    def typed_relationships(self) -> list[Relationship]:
        """Devuelve una copia de las relaciones tipadas."""
        return list(self._typed_relationships)

    def add_relationship(
        self,
        relation_type: str,
        target_id: str,
    ) -> None:
        """Agrega una relación tipada manteniendo la representación compatible."""
        self._typed_relationships.append(
            Relationship(
                relation_type=relation_type,
                target_id=target_id,
            )
        )

        if target_id not in self._relationship_ids:
            self._relationship_ids.append(target_id)
