import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SRC_PATH = str(RAIZ / "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from pkb.knowledge.object import KnowledgeObject
from pkb.validators.rules import ValidationEngine

def test_metadata_valida():
    """Verifica que un objeto con todos sus campos no genere errores."""
    obj = KnowledgeObject(
        identifier="PKB-001", title="Manual", object_type="DOC",
        domain="CORE", version="1.0.0", status="Approved",
        owner="Admin", source=Path("test.md")
    )
    resultado = ValidationEngine.validate_metadata(obj)
    assert resultado.success is True
    assert len(resultado.errors) == 0

def test_metadata_invalida_campos_faltantes():
    """Verifica que detecte la ausencia de atributos obligatorios."""
    obj = KnowledgeObject(
        identifier="PKB-001", title="", object_type="",
        domain="", version="", status="", owner="", source=Path("test.md")
    )
    resultado = ValidationEngine.validate_metadata(obj)
    assert resultado.success is False
    assert len(resultado.errors) == 3  # Faltan: title, type, status