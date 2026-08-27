from pathlib import Path

from pkb.knowledge.object import KnowledgeObject
from pkb.knowledge.registry import KnowledgeRegistry
from pkb.validation.engine import ValidationEngine
from pkb.validation.rules import MetadataValidationRule


def build_registry() -> KnowledgeRegistry:
    registry = KnowledgeRegistry()

    registry.add(
        KnowledgeObject(
            identifier="PKB-001",
            title="Manual",
            object_type="DOC",
            domain="CORE",
            version="1.0.0",
            status="Approved",
            owner="Admin",
            source=Path("test.md"),
        )
    )

    return registry


def test_validation_engine_executes_registered_rule():
    engine = ValidationEngine()
    engine.add_rule(MetadataValidationRule())

    results = engine.validate(build_registry())

    assert len(results) == 1
    assert results[0].success is True
    assert results[0].rule == "MetadataValidationRule"


def test_metadata_validation_rule_accepts_valid_metadata():
    rule = MetadataValidationRule()

    results = rule.validate(build_registry())

    assert len(results) == 1
    assert results[0].success is True
    assert results[0].errors == []


def test_metadata_validation_rule_detects_missing_required_fields():
    registry = KnowledgeRegistry()

    registry.add(
        KnowledgeObject(
            identifier="PKB-001",
            title="",
            object_type="",
            domain="",
            version="",
            status="",
            owner="",
            source=Path("test.md"),
        )
    )

    rule = MetadataValidationRule()

    results = rule.validate(registry)

    assert len(results) == 1
    assert results[0].success is False
    assert len(results[0].errors) == 3


def test_validation_engine_executes_multiple_registered_rules_in_order():
    from pkb.validation.result import ValidationResult

    class FirstRule:
        def validate(self, registry):
            return [
                ValidationResult(
                    success=True,
                    rule="FirstRule",
                )
            ]

    class SecondRule:
        def validate(self, registry):
            return [
                ValidationResult(
                    success=False,
                    rule="SecondRule",
                    errors=["Error de prueba"],
                )
            ]

    engine = ValidationEngine()
    engine.add_rule(FirstRule())
    engine.add_rule(SecondRule())

    results = engine.validate(build_registry())

    assert len(results) == 2
    assert results[0].rule == "FirstRule"
    assert results[0].success is True
    assert results[1].rule == "SecondRule"
    assert results[1].success is False
    assert results[1].errors == ["Error de prueba"]
