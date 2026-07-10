import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SRC_PATH = str(RAIZ / "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from pkb.knowledge.object import KnowledgeObject

def test_knowledge_object_instantiation():
    """Verifica que el modelo de dominio guarde correctamente sus atributos."""
    ruta_dummy = Path("docs/dummy.md")
    obj = KnowledgeObject(
        identifier="PKB-PLAN-0001",
        title="Product Backlog",
        object_type="PLAN",
        domain="PKB",
        version="1.0.0",
        status="Approved",
        owner="Architecture",
        source=ruta_dummy,
        tags=["planning", "core"]
    )
    
    assert obj.identifier == "PKB-PLAN-0001"
    assert obj.object_type == "PLAN"
    assert "planning" in obj.tags
    assert len(obj.relationships) == 0