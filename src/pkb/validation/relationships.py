from dataclasses import dataclass, field

from pkb.knowledge.registry import KnowledgeRegistry


@dataclass
class RelationshipValidationReport:
    """Resultado de la validación de integridad relacional."""

    valid_relationships: int = 0
    unresolved_relationships: list[tuple[str, str]] = field(default_factory=list)
    duplicate_relationships: list[tuple[str, str]] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        """Indica si todas las relaciones declaradas son estructuralmente válidas."""
        return not self.unresolved_relationships and not self.duplicate_relationships

    @property
    def unresolved_count(self) -> int:
        """Cantidad de relaciones cuyo destino no existe."""
        return len(self.unresolved_relationships)

    @property
    def duplicate_count(self) -> int:
        """Cantidad de relaciones duplicadas detectadas."""
        return len(self.duplicate_relationships)


class RelationshipValidator:
    """Valida la integridad estructural de las relaciones del Registry."""

    def __init__(self, registry: KnowledgeRegistry) -> None:
        self._registry = registry

    def validate(self) -> RelationshipValidationReport:
        """
        Valida todas las relaciones declaradas en el Knowledge Registry.

        Cada relación se representa como:
            (identificador_origen, identificador_destino)
        """
        report = RelationshipValidationReport()

        for obj in self._registry.all():
            seen: set[str] = set()

            for related_id in obj.relationships:
                if related_id in seen:
                    report.duplicate_relationships.append((obj.identifier, related_id))
                    continue

                seen.add(related_id)

                if self._registry.get(related_id) is None:
                    report.unresolved_relationships.append((obj.identifier, related_id))
                    continue

                report.valid_relationships += 1

        return report
