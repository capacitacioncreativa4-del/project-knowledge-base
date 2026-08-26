from pkb.knowledge.registry import KnowledgeRegistry
from pkb.metadata.parser import MetadataParser
from pkb.repository.diagnostics import LoadDiagnostics
from pkb.repository.scanner import RepositoryScanner
from pkb.validation import RelationshipValidator


class KnowledgeLoader:
    """Orquestador encargado de escanear, parsear y cargar el repositorio completo."""

    @staticmethod
    def load_repository(ruta_raiz: str = ".") -> KnowledgeRegistry:
        """
        Carga el repositorio y devuelve únicamente el KnowledgeRegistry.

        Mantiene la API histórica del Loader para evitar regresiones.
        """
        registry, _ = KnowledgeLoader.load_repository_with_diagnostics(ruta_raiz)
        return registry

    @staticmethod
    def load_repository_with_diagnostics(
        ruta_raiz: str = ".",
    ) -> tuple[KnowledgeRegistry, LoadDiagnostics]:
        """
        Carga el repositorio y devuelve el Registry junto con sus diagnósticos.

        La validación de integridad relacional se delega a
        RelationshipValidator una vez construido el Registry completo.
        """
        registry = KnowledgeRegistry()
        diagnostics = LoadDiagnostics()

        archivos = RepositoryScanner.markdown_files(ruta_raiz)
        diagnostics.scanned_files = len(archivos)

        for archivo in archivos:
            try:
                knowledge_object, _ = MetadataParser.parse_file(str(archivo))
                diagnostics.parsed_files += 1

                if not knowledge_object.identifier:
                    diagnostics.objects_without_identifier += 1
                    continue

                if knowledge_object.object_type:
                    knowledge_object.object_type = (
                        str(knowledge_object.object_type).upper().strip()
                    )

                if knowledge_object.domain:
                    knowledge_object.domain = (
                        str(knowledge_object.domain).upper().strip()
                    )

                typed_relationships = knowledge_object.typed_relationships

                if typed_relationships:
                    diagnostics.objects_with_relationships += 1
                    diagnostics.declared_relationships += len(typed_relationships)

                registry.add(knowledge_object)
                diagnostics.registered_objects += 1

            except Exception:
                diagnostics.rejected_files += 1
                continue

        relationship_report = RelationshipValidator(registry).validate()

        diagnostics.unresolved_relationships = list(
            relationship_report.unresolved_relationships
        )

        diagnostics.duplicate_relationships = list(
            relationship_report.duplicate_relationships
        )

        diagnostics.valid_relationships = relationship_report.valid_relationships

        return registry, diagnostics
