from dataclasses import dataclass, field

from pkb.knowledge.registry import KnowledgeRegistry


@dataclass
class RelationshipValidationReport:
    """Resultado de la validación de integridad relacional."""

    valid_relationships: int = 0
    unresolved_relationships: list[tuple[str, str, str]] = field(default_factory=list)
    duplicate_relationships: list[tuple[str, str, str]] = field(default_factory=list)

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
        Valida todas las relaciones tipadas declaradas en el Knowledge Registry.

        La identidad semántica de una relación está determinada por:

            (relation_type, target_id)

        Por tanto, dos relaciones con distinto ``relation_type`` que apunten
        al mismo objeto no se consideran duplicadas.

        Los diagnósticos conservan la identidad completa de la relación:

            (source_id, relation_type, target_id)
        """
        report = RelationshipValidationReport()

        for obj in self._registry.all():
            seen: set[tuple[str, str]] = set()

            for relationship in obj.typed_relationships:
                relation_key = (
                    relationship.relation_type,
                    relationship.target_id,
                )

                diagnostic_key = (
                    obj.identifier,
                    relationship.relation_type,
                    relationship.target_id,
                )

                if relation_key in seen:
                    report.duplicate_relationships.append(diagnostic_key)
                    continue

                seen.add(relation_key)

                if self._registry.get(relationship.target_id) is None:
                    report.unresolved_relationships.append(diagnostic_key)
                    continue

                report.valid_relationships += 1

        return report
