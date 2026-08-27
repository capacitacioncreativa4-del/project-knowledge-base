from dataclasses import dataclass, field
from pathlib import Path

from pkb.knowledge.relationship import Relationship


@dataclass(slots=True, init=False)
class KnowledgeObject:
    """Representa un objeto de conocimiento formal dentro del dominio PKB."""

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

        self._relationship_ids = []
        self._typed_relationships = []

        for target_id in relationships or []:
            self._relationship_ids.append(target_id)
            self._typed_relationships.append(
                Relationship(
                    relation_type="related",
                    target_id=target_id,
                )
            )

    @property
    def relationships(self) -> list[str]:
        """
        Devuelve la representación histórica de relaciones.

        La representación legacy conserva exactamente la multiplicidad
        declarada cuando las relaciones son asignadas directamente.
        """
        return list(self._relationship_ids)

    @relationships.setter
    def relationships(self, values: list[str]) -> None:
        """
        Reemplaza las relaciones históricas y reconstruye las relaciones
        tipadas correspondientes utilizando el tipo ``related``.

        La multiplicidad declarada se conserva deliberadamente para que
        los validadores puedan detectar referencias duplicadas.
        """
        self._relationship_ids = []
        self._typed_relationships = []

        for target_id in values:
            self._relationship_ids.append(target_id)
            self._typed_relationships.append(
                Relationship(
                    relation_type="related",
                    target_id=target_id,
                )
            )

    @property
    def typed_relationships(self) -> list[Relationship]:
        """Devuelve una copia de las relaciones semánticas tipadas."""
        return list(self._typed_relationships)

    def add_relationship(
        self,
        relation_type: str,
        target_id: str,
    ) -> None:
        """
        Agrega una relación semántica tipada.

        Las relaciones tipadas conservan su multiplicidad semántica:
        dos relaciones con distinto ``relation_type`` pueden apuntar
        al mismo ``target_id``.

        La representación legacy mantiene únicamente un identificador
        por destino.
        """
        self._add_typed_relationship(
            relation_type=relation_type,
            target_id=target_id,
        )

    def _add_typed_relationship(
        self,
        relation_type: str,
        target_id: str,
    ) -> None:
        """Agrega una relación tipada y sincroniza la vista histórica."""
        relationship = Relationship(
            relation_type=relation_type,
            target_id=target_id,
        )

        self._typed_relationships.append(relationship)

        if target_id not in self._relationship_ids:
            self._relationship_ids.append(target_id)
