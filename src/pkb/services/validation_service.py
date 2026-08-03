from pkb.config import PKB_ROOT
from pkb.reporting import ConsoleReporter, ValidationReport
from pkb.repository.loader import KnowledgeLoader
from pkb.validation.engine import ValidationEngine
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

        # Ejecutar todas las reglas
        results = engine.validate(registry)

        # Construir el reporte
        report = ValidationReport(results)

        # Mostrar el reporte
        ConsoleReporter.render(report)
