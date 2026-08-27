from pathlib import Path

from pkb.knowledge.object import KnowledgeObject
from pkb.knowledge.registry import KnowledgeRegistry
from pkb.validation import RelationshipValidator


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


def test_relationship_validator_accepts_existing_typed_reference():
    registry = build_registry()

    registry.get("REQ-001").add_relationship(
        relation_type="related",
        target_id="ADR-001",
    )

    report = RelationshipValidator(registry).validate()

    assert report.is_valid
    assert report.valid_relationships == 1
    assert report.unresolved_count == 0
    assert report.duplicate_count == 0


def test_relationship_validator_detects_unresolved_typed_reference():
    registry = build_registry()

    registry.get("REQ-001").add_relationship(
        relation_type="related",
        target_id="ADR-999",
    )

    report = RelationshipValidator(registry).validate()

    assert not report.is_valid
    assert report.valid_relationships == 0
    assert report.unresolved_relationships == [("REQ-001", "related", "ADR-999")]
    assert report.unresolved_count == 1
    assert report.duplicate_count == 0


def test_relationship_validator_detects_duplicate_typed_reference():
    registry = build_registry()

    registry.get("REQ-001").add_relationship(
        relation_type="related",
        target_id="ADR-001",
    )
    registry.get("REQ-001").add_relationship(
        relation_type="related",
        target_id="ADR-001",
    )

    report = RelationshipValidator(registry).validate()

    assert not report.is_valid
    assert report.valid_relationships == 1
    assert report.duplicate_relationships == [("REQ-001", "related", "ADR-001")]
    assert report.duplicate_count == 1


def test_relationship_validator_allows_different_types_to_same_target():
    registry = build_registry()

    registry.get("REQ-001").add_relationship(
        relation_type="related",
        target_id="ADR-001",
    )
    registry.get("REQ-001").add_relationship(
        relation_type="derived_from",
        target_id="ADR-001",
    )

    report = RelationshipValidator(registry).validate()

    assert report.is_valid
    assert report.valid_relationships == 2
    assert report.unresolved_count == 0
    assert report.duplicate_count == 0


def test_relationship_validator_detects_multiple_problems():
    registry = build_registry()

    registry.get("REQ-001").add_relationship(
        relation_type="related",
        target_id="ADR-001",
    )
    registry.get("REQ-001").add_relationship(
        relation_type="related",
        target_id="ADR-001",
    )
    registry.get("REQ-001").add_relationship(
        relation_type="derived_from",
        target_id="ADR-001",
    )
    registry.get("REQ-001").add_relationship(
        relation_type="related",
        target_id="ADR-999",
    )
    registry.get("REQ-001").add_relationship(
        relation_type="depends_on",
        target_id="REQ-999",
    )

    report = RelationshipValidator(registry).validate()

    assert not report.is_valid
    assert report.valid_relationships == 2
    assert report.duplicate_relationships == [("REQ-001", "related", "ADR-001")]
    assert report.unresolved_relationships == [
        ("REQ-001", "related", "ADR-999"),
        ("REQ-001", "depends_on", "REQ-999"),
    ]
    assert report.duplicate_count == 1
    assert report.unresolved_count == 2


def test_relationship_validator_accepts_registry_without_relationships():
    registry = build_registry()

    report = RelationshipValidator(registry).validate()

    assert report.is_valid
    assert report.valid_relationships == 0
    assert report.unresolved_count == 0
    assert report.duplicate_count == 0


def test_relationship_validator_ignores_legacy_relationship_view():
    registry = build_registry()

    obj = registry.get("REQ-001")
    obj._relationship_ids.append("ADR-001")

    report = RelationshipValidator(registry).validate()

    assert report.is_valid
    assert report.valid_relationships == 0
    assert report.unresolved_count == 0
    assert report.duplicate_count == 0


def test_relationship_validator_uses_typed_relationships_as_source_of_truth():
    registry = build_registry()

    registry.get("REQ-001").add_relationship(
        relation_type="derived_from",
        target_id="ADR-001",
    )

    report = RelationshipValidator(registry).validate()

    assert report.is_valid
    assert report.valid_relationships == 1
    assert report.unresolved_count == 0
    assert report.duplicate_count == 0


def test_relationship_validator_preserves_relation_type_in_diagnostics():
    registry = build_registry()

    registry.get("REQ-001").add_relationship(
        relation_type="derived_from",
        target_id="ADR-999",
    )

    report = RelationshipValidator(registry).validate()

    assert not report.is_valid
    assert report.unresolved_relationships == [("REQ-001", "derived_from", "ADR-999")]
    assert report.unresolved_count == 1


def test_relationship_validator_preserves_relation_type_in_duplicate_diagnostics():
    registry = build_registry()

    registry.get("REQ-001").add_relationship(
        relation_type="derived_from",
        target_id="ADR-001",
    )
    registry.get("REQ-001").add_relationship(
        relation_type="derived_from",
        target_id="ADR-001",
    )

    report = RelationshipValidator(registry).validate()

    assert not report.is_valid
    assert report.duplicate_relationships == [("REQ-001", "derived_from", "ADR-001")]
    assert report.duplicate_count == 1
