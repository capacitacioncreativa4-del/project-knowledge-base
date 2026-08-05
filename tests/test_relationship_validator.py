from pkb.knowledge.object import KnowledgeObject
from pkb.knowledge.registry import KnowledgeRegistry
from pkb.validation import RelationshipValidator
from pathlib import Path


def build_registry() -> KnowledgeRegistry:
    registry = KnowledgeRegistry()

    registry.add(
        KnowledgeObject(
            identifier="REQ-001",
            title="Requirement",
            object_type="REQUIREMENT",
            domain="CORE",
            version="1.0",
            status="APPROVED",
            owner="PKB",
            source=Path("test.md"),
        )
    )

    registry.add(
        KnowledgeObject(
            identifier="ADR-001",
            title="Architecture Decision",
            object_type="ADR",
            domain="ARCHITECTURE",
            version="1.0",
            status="APPROVED",
            owner="PKB",
            source=Path("test.md"),
        )
    )

    return registry


def test_relationship_validator_accepts_existing_reference():
    registry = build_registry()

    registry.get("REQ-001").relationships = ["ADR-001"]

    report = RelationshipValidator(registry).validate()

    assert report.is_valid
    assert report.valid_relationships == 1
    assert report.unresolved_count == 0
    assert report.duplicate_count == 0


def test_relationship_validator_detects_unresolved_reference():
    registry = build_registry()

    registry.get("REQ-001").relationships = ["ADR-999"]

    report = RelationshipValidator(registry).validate()

    assert not report.is_valid
    assert report.valid_relationships == 0
    assert report.unresolved_relationships == [("REQ-001", "ADR-999")]
    assert report.unresolved_count == 1


def test_relationship_validator_detects_duplicate_reference():
    registry = build_registry()

    registry.get("REQ-001").relationships = [
        "ADR-001",
        "ADR-001",
    ]

    report = RelationshipValidator(registry).validate()

    assert not report.is_valid
    assert report.valid_relationships == 1
    assert report.duplicate_relationships == [("REQ-001", "ADR-001")]
    assert report.duplicate_count == 1


def test_relationship_validator_detects_multiple_problems():
    registry = build_registry()

    registry.get("REQ-001").relationships = [
        "ADR-001",
        "ADR-001",
        "ADR-999",
        "REQ-999",
    ]

    report = RelationshipValidator(registry).validate()

    assert not report.is_valid
    assert report.valid_relationships == 1
    assert report.duplicate_relationships == [("REQ-001", "ADR-001")]
    assert report.unresolved_relationships == [
        ("REQ-001", "ADR-999"),
        ("REQ-001", "REQ-999"),
    ]


def test_relationship_validator_accepts_registry_without_relationships():
    registry = build_registry()

    report = RelationshipValidator(registry).validate()

    assert report.is_valid
    assert report.valid_relationships == 0
    assert report.unresolved_count == 0
    assert report.duplicate_count == 0
