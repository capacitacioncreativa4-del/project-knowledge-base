from dataclasses import dataclass, field


@dataclass
class LoadDiagnostics:
    """Métricas y anomalías producidas durante la carga del repositorio."""

    scanned_files: int = 0
    parsed_files: int = 0
    registered_objects: int = 0
    rejected_files: int = 0
    objects_without_identifier: int = 0
    objects_with_relationships: int = 0
    declared_relationships: int = 0
    unresolved_relationships: list[str] = field(default_factory=list)
    typed_relationships: int = 0

    @property
    def unresolved_relationship_count(self) -> int:
        """Devuelve la cantidad de relaciones cuyo destino no fue encontrado."""
        return len(self.unresolved_relationships)
