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

    def filter(
        self,
        *,
        domain: str | None = None,
        object_type: str | None = None,
        status: str | None = None,
        owner: str | None = None,
    ) -> list[KnowledgeObject]:
        """
        Devuelve objetos que cumplen todos los filtros proporcionados.

        Los valores de texto se comparan sin distinguir mayúsculas/minúsculas
        y eliminando espacios exteriores.
        """

        normalized_domain = domain.upper().strip() if domain is not None else None
        normalized_type = (
            object_type.upper().strip() if object_type is not None else None
        )
        normalized_status = status.upper().strip() if status is not None else None
        normalized_owner = owner.upper().strip() if owner is not None else None

        def matches(obj: KnowledgeObject) -> bool:
            if (
                normalized_domain is not None
                and (obj.domain or "").upper().strip() != normalized_domain
            ):
                return False

            if (
                normalized_type is not None
                and (obj.object_type or "").upper().strip() != normalized_type
            ):
                return False

            if (
                normalized_status is not None
                and (obj.status or "").upper().strip() != normalized_status
            ):
                return False

            if (
                normalized_owner is not None
                and (obj.owner or "").upper().strip() != normalized_owner
            ):
                return False

            return True

        return self.where(matches)

    def by_domain(self, domain: str) -> list[KnowledgeObject]:
        """Devuelve todos los objetos de un dominio."""
        return self.filter(domain=domain)

    def by_type(self, object_type: str) -> list[KnowledgeObject]:
        """Devuelve todos los objetos de un tipo."""
        return self.filter(object_type=object_type)

    def by_status(self, status: str) -> list[KnowledgeObject]:
        """Devuelve todos los objetos con un determinado estado."""
        return self.filter(status=status)

    def by_owner(self, owner: str) -> list[KnowledgeObject]:
        """Devuelve todos los objetos pertenecientes a un propietario."""
        return self.filter(owner=owner)

    def where(
        self,
        predicate: Callable[[KnowledgeObject], bool],
    ) -> list[KnowledgeObject]:
        """
        Ejecuta una consulta arbitraria mediante un predicado.
        """
        return [obj for obj in self._registry.all() if predicate(obj)]
