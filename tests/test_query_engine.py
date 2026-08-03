from pathlib import Path

from pkb.knowledge.object import KnowledgeObject
from pkb.knowledge.registry import KnowledgeRegistry
from pkb.query import QueryEngine


def build_registry():
    registry = KnowledgeRegistry()

    registry.add(
        KnowledgeObject(
            identifier="REQ-001",
            title="Requisito",
            object_type="REQUIREMENT",
            domain="CORE",
            version="1.0",
            status="APPROVED",
            owner="PKB",
            source=Path("a.md"),
        )
    )

    registry.add(
        KnowledgeObject(
            identifier="ADR-001",
            title="Arquitectura",
            object_type="ADR",
            domain="ARCHITECTURE",
            version="1.0",
            status="DRAFT",
            owner="PKB",
            source=Path("b.md"),
        )
    )

    return registry


def test_query_by_domain():
    engine = QueryEngine(build_registry())

    resultados = engine.by_domain("CORE")

    assert len(resultados) == 1
    assert resultados[0].identifier == "REQ-001"


def test_query_by_type():
    engine = QueryEngine(build_registry())

    resultados = engine.by_type("ADR")

    assert len(resultados) == 1
    assert resultados[0].identifier == "ADR-001"


def test_query_by_status():
    engine = QueryEngine(build_registry())

    resultados = engine.by_status("DRAFT")

    assert len(resultados) == 1


def test_query_where():
    engine = QueryEngine(build_registry())

    resultados = engine.where(lambda o: o.owner == "PKB")

    assert len(resultados) == 2
