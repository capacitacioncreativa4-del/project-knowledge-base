from pkb.config import PKB_ROOT
from pkb.reporting import ConsoleReporter, ValidationReport
from pkb.repository.loader import KnowledgeLoader
from pkb.validation.engine import ValidationEngine
from pkb.validation.relationships import RelationshipValidator
from pkb.validation.rules import (
    BrokenReferenceRule,
    DomainRule,
    DuplicateIdentifierRule,
)


class ValidationService:
    """Servicio de validación del repositorio."""

    @staticmethod
    def run() -> None:
        print("\n[CLI] Iniciando proceso de validación del repositorio...")

        registry = KnowledgeLoader.load_repository(str(PKB_ROOT))

        print(f"[INFO] Objetos cargados: {registry.count()}")

        engine = ValidationEngine()
        engine.add_rule(DuplicateIdentifierRule())
        engine.add_rule(BrokenReferenceRule())
        engine.add_rule(DomainRule())

        # Ejecutar las reglas de validación existentes.
        results = engine.validate(registry)

        # Validar la integridad estructural de las relaciones.
        relationship_report = RelationshipValidator(registry).validate()

        # Construir el reporte existente.
        report = ValidationReport(results)

        # Mostrar el reporte existente sin alterar su contrato.
        ConsoleReporter.render(report)

        # Mostrar el resultado específico de integridad relacional.
        print("\n[RELATIONSHIPS] Integridad relacional")
        print("------------------------------------")
        print(f"Relaciones válidas:       {relationship_report.valid_relationships}")
        print(f"Relaciones no resueltas:  {relationship_report.unresolved_count}")
        print(f"Relaciones duplicadas:    {relationship_report.duplicate_count}")

        if relationship_report.unresolved_relationships:
            print("\n[RELATIONSHIPS] Referencias no resueltas:")

            for (
                source_id,
                relation_type,
                target_id,
            ) in relationship_report.unresolved_relationships:
                print(f"  - {source_id} - {relation_type} -> {target_id}")

        if relationship_report.duplicate_relationships:
            print("\n[RELATIONSHIPS] Referencias duplicadas:")

            for (
                source_id,
                relation_type,
                target_id,
            ) in relationship_report.duplicate_relationships:
                print(f"  - {source_id} - {relation_type} -> {target_id}")

        if relationship_report.is_valid:
            print("\n[RELATIONSHIPS] OK: integridad relacional válida.")
        else:
            print("\n[RELATIONSHIPS] ERROR: se detectaron problemas relacionales.")
