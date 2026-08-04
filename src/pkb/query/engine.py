from collections.abc import Callable

from pkb.knowledge.object import KnowledgeObject
from pkb.knowledge.registry import KnowledgeRegistry


class QueryEngine:
    """
    Motor de consultas sobre el KnowledgeRegistry.
    """

    def __init__(self, registry: KnowledgeRegistry):
        self._registry = registry

    def all(self) -> list[KnowledgeObject]:
        """Devuelve todos los objetos."""
        return list(self._registry.all())

    def by_id(self, identifier: str) -> KnowledgeObject | None:
        """Busca un objeto por identificador."""
        return self._registry.get(identifier)

    def related(self, identifier: str) -> list[KnowledgeObject]:
        """Devuelve los objetos relacionados directamente con un objeto."""
        obj = self._registry.get(identifier)

        if obj is None:
            return []

        return [
            related
            for related_id in obj.relationships
            if (related := self._registry.get(related_id)) is not None
        ]

    def referenced_by(self, identifier: str) -> list[KnowledgeObject]:
        """Devuelve los objetos que referencian directamente al objeto indicado."""
        return [obj for obj in self._registry.all() if identifier in obj.relationships]

    def by_domain(self, domain: str) -> list[KnowledgeObject]:
        """Devuelve todos los objetos de un dominio."""
        domain = domain.upper().strip()

        return [
            obj
            for obj in self._registry.all()
            if (obj.domain or "").upper().strip() == domain
        ]

    def by_type(self, object_type: str) -> list[KnowledgeObject]:
        """Devuelve todos los objetos de un tipo."""
        object_type = object_type.upper().strip()

        return [
            obj
            for obj in self._registry.all()
            if (obj.object_type or "").upper().strip() == object_type
        ]

    def by_status(self, status: str) -> list[KnowledgeObject]:
        """Devuelve todos los objetos con un determinado estado."""
        status = status.upper().strip()

        return [
            obj
            for obj in self._registry.all()
            if (obj.status or "").upper().strip() == status
        ]

    def by_owner(self, owner: str) -> list[KnowledgeObject]:
        """Devuelve todos los objetos pertenecientes a un propietario."""
        owner = owner.upper().strip()

        return [
            obj
            for obj in self._registry.all()
            if (obj.owner or "").upper().strip() == owner
        ]

    def where(
        self,
        predicate: Callable[[KnowledgeObject], bool],
    ) -> list[KnowledgeObject]:
        """
        Ejecuta una consulta arbitraria mediante un predicado.
        """
        return [obj for obj in self._registry.all() if predicate(obj)]
