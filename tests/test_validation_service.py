
from pkb.services.validation_service import ValidationService
from pkb.validation.relationships import RelationshipValidator


def test_validation_service_import():
    """Verifica que el servicio de validación pueda importarse correctamente."""
    assert ValidationService is not None


def test_relationship_validator_import():
    """Verifica que el validador relacional esté disponible."""
    assert RelationshipValidator is not None


def test_validation_service_module_is_loadable():
    """Verifica que el módulo del servicio sea importable sin errores."""
    from pkb.services import validation_service

    assert validation_service is not None


def test_validation_service_dependencies_are_available():
    """Verifica las dependencias principales utilizadas por el servicio."""
    from pkb.reporting import ConsoleReporter, ValidationReport
    from pkb.repository.loader import KnowledgeLoader
    from pkb.validation.engine import ValidationEngine

    assert ConsoleReporter is not None
    assert ValidationReport is not None
    assert KnowledgeLoader is not None
    assert ValidationEngine is not None


def test_validation_service_runs_with_typed_relationship_diagnostics(
    monkeypatch,
    capsys,
):
    class FakeRelationshipReport:
        valid_relationships = 1
        unresolved_relationships = [("REQ-001", "derived_from", "ADR-999")]
        duplicate_relationships = [("REQ-002", "related", "ADR-001")]

        @property
        def unresolved_count(self):
            return len(self.unresolved_relationships)

        @property
        def duplicate_count(self):
            return len(self.duplicate_relationships)

        @property
        def is_valid(self):
            return False

    class FakeRegistry:
        def count(self):
            return 1

    class FakeKnowledgeLoader:
        @staticmethod
        def load_repository(_):
            return FakeRegistry()

    class FakeValidationEngine:
        def add_rule(self, _):
            pass

        def validate(self, _):
            return []

    class FakeRelationshipValidator:
        def __init__(self, _):
            pass

        def validate(self):
            return FakeRelationshipReport()

    class FakeValidationReport:
        def __init__(self, _):
            pass

    class FakeConsoleReporter:
        @staticmethod
        def render(_):
            pass

    monkeypatch.setattr(
        "pkb.services.validation_service.KnowledgeLoader",
        FakeKnowledgeLoader,
    )
    monkeypatch.setattr(
        "pkb.services.validation_service.ValidationEngine",
        FakeValidationEngine,
    )
    monkeypatch.setattr(
        "pkb.services.validation_service.RelationshipValidator",
        FakeRelationshipValidator,
    )
    monkeypatch.setattr(
        "pkb.services.validation_service.ValidationReport",
        FakeValidationReport,
    )
    monkeypatch.setattr(
        "pkb.services.validation_service.ConsoleReporter",
        FakeConsoleReporter,
    )

    ValidationService.run()

    output = capsys.readouterr().out

    assert "REQ-001 - derived_from -> ADR-999" in output
    assert "REQ-002 - related -> ADR-001" in output
    assert "Relaciones no resueltas:  1" in output
    assert "Relaciones duplicadas:    1" in output
    assert "[RELATIONSHIPS] ERROR" in output
