from pathlib import Path

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
