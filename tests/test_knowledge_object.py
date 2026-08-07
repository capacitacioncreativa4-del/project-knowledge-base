import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SRC_PATH = str(RAIZ / "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from pkb.knowledge.object import KnowledgeObject
from pkb.knowledge.relationship import Relationship


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
        tags=["planning", "core"],
    )

    assert obj.identifier == "PKB-PLAN-0001"
    assert obj.object_type == "PLAN"
    assert "planning" in obj.tags
    assert len(obj.relationships) == 0


def test_knowledge_object_initializes_typed_relationships_from_legacy_values():
    obj = KnowledgeObject(
        identifier="REQ-001",
        title="Requirement",
        object_type="REQUIREMENT",
        domain="CORE",
        version="1.0",
        status="APPROVED",
        owner="PKB",
        source=None,
        relationships=["ADR-001", "STD-001"],
    )

    assert obj.relationships == ["ADR-001", "STD-001"]
    assert obj.typed_relationships == [
        Relationship(relation_type="related", target_id="ADR-001"),
        Relationship(relation_type="related", target_id="STD-001"),
    ]


def test_add_relationship_updates_both_representations():
    obj = KnowledgeObject(
        identifier="REQ-001",
        title="Requirement",
        object_type="REQUIREMENT",
        domain="CORE",
        version="1.0",
        status="APPROVED",
        owner="PKB",
        source=None,
    )

    obj.add_relationship("derived_from", "ADR-001")

    assert obj.relationships == ["ADR-001"]
    assert obj.typed_relationships == [
        Relationship(
            relation_type="derived_from",
            target_id="ADR-001",
        )
    ]


def test_add_relationship_preserves_typed_relationship_when_target_already_exists():
    obj = KnowledgeObject(
        identifier="REQ-001",
        title="Requirement",
        object_type="REQUIREMENT",
        domain="CORE",
        version="1.0",
        status="APPROVED",
        owner="PKB",
        source=None,
        relationships=["ADR-001"],
    )

    obj.add_relationship("derived_from", "ADR-001")

    assert obj.relationships == ["ADR-001"]
    assert obj.typed_relationships == [
        Relationship(
            relation_type="related",
            target_id="ADR-001",
        ),
        Relationship(
            relation_type="derived_from",
            target_id="ADR-001",
        ),
    ]


def test_typed_relationships_returns_copy():
    obj = KnowledgeObject(
        identifier="REQ-001",
        title="Requirement",
        object_type="REQUIREMENT",
        domain="CORE",
        version="1.0",
        status="APPROVED",
        owner="PKB",
        source=None,
        relationships=["ADR-001"],
    )

    relationships = obj.typed_relationships
    relationships.clear()

    assert obj.typed_relationships == [
        Relationship(
            relation_type="related",
            target_id="ADR-001",
        )
    ]
