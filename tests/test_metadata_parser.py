import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SRC_PATH = str(RAIZ / "src")

if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from pkb.knowledge.object import KnowledgeObject
from pkb.knowledge.relationship import Relationship
from pkb.metadata.parser import MetadataParser


def test_parser_sin_front_matter(tmp_path):
    """Verifica que un archivo sin metadatos devuelva un objeto vacío pero tipado."""
    f = tmp_path / "nota.md"
    f.write_text(
        "Este es un texto plano sin guiones.",
        encoding="utf-8",
    )

    obj, contenido = MetadataParser.parse_file(str(f))

    assert isinstance(obj, KnowledgeObject)
    assert obj.identifier == ""
    assert "texto plano" in contenido
    assert obj.relationships == []
    assert obj.typed_relationships == []


def test_parser_con_front_matter_valido(tmp_path):
    """Verifica la extracción básica del Front Matter."""
    f = tmp_path / "documento.md"

    contenido_archivo = (
        "---\nid: DOC-001\ntitle: Prueba\ntype: GUIDELINES\n---\nCuerpo del documento"
    )

    f.write_text(
        contenido_archivo,
        encoding="utf-8",
    )

    obj, contenido = MetadataParser.parse_file(str(f))

    assert isinstance(obj, KnowledgeObject)
    assert obj.identifier == "DOC-001"
    assert obj.title == "Prueba"
    assert obj.object_type == "GUIDELINES"
    assert "Cuerpo del documento" in contenido

    assert obj.relationships == []
    assert obj.typed_relationships == []


def test_parser_con_front_matter_con_relaciones_tipadas(tmp_path):
    """Verifica la extracción de relaciones tipadas desde Front Matter."""
    f = tmp_path / "documento.md"

    contenido_archivo = """---
id: REQ-001
title: Requisito de prueba
type: REQUIREMENT
relationships:
  derived_from:
    - ADR-001
  implemented_by:
    - DOC-001
---
Cuerpo del documento
"""

    f.write_text(
        contenido_archivo,
        encoding="utf-8",
    )

    obj, contenido = MetadataParser.parse_file(str(f))

    assert isinstance(obj, KnowledgeObject)
    assert obj.identifier == "REQ-001"
    assert obj.title == "Requisito de prueba"
    assert obj.object_type == "REQUIREMENT"
    assert "Cuerpo del documento" in contenido

    assert obj.relationships == [
        "ADR-001",
        "DOC-001",
    ]

    assert obj.typed_relationships == [
        Relationship(
            relation_type="derived_from",
            target_id="ADR-001",
        ),
        Relationship(
            relation_type="implemented_by",
            target_id="DOC-001",
        ),
    ]
