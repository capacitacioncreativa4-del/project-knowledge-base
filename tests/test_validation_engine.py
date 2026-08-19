from pathlib import Path

from pkb.knowledge.object import KnowledgeObject
from pkb.validation.rules import ValidationEngine


def test_metadata_valida():
    """Verifica que un objeto con todos sus campos no genere errores."""
    obj = KnowledgeObject(
        identifier="PKB-001",
        title="Manual",
        object_type="DOC",
        domain="CORE",
        version="1.0.0",
        status="Approved",
        owner="Admin",
        source=Path("test.md"),
    )
    resultado = ValidationEngine.validate_metadata(obj)
    assert resultado.success is True
    assert len(resultado.errors) == 0


def test_metadata_invalida_campos_faltantes():
    """Verifica que detecte la ausencia de atributos obligatorios."""
    obj = KnowledgeObject(
        identifier="PKB-001",
        title="",
        object_type="",
        domain="",
        version="",
        status="",
        owner="",
        source=Path("test.md"),
    )
    resultado = ValidationEngine.validate_metadata(obj)
    assert resultado.success is False
    assert len(resultado.errors) == 3  # Faltan: title, type, status
