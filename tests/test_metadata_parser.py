import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SRC_PATH = str(RAIZ / "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from pkb.metadata.parser import MetadataParser
from pkb.knowledge.object import KnowledgeObject

def test_parser_sin_front_matter(tmp_path):
    """Verifica que un archivo sin metadatos devuelva un objeto vacío pero tipado."""
    f = tmp_path / "nota.md"
    f.write_text("Este es un texto plano sin guiones.", encoding="utf-8")
    
    obj, contenido = MetadataParser.parse_file(str(f))
    assert isinstance(obj, KnowledgeObject)
    assert obj.identifier == ""
    assert "texto plano" in contenido

def test_parser_con_front_matter_valido(tmp_path):
    """Verifica la correcta extracción mapeando hacia atributos de clase del objeto."""
    f = tmp_path / "documento.md"
    contenido_archivo = "---\nid: DOC-001\ntitle: Prueba\ntype: GUIDELINES\n---\nCuerpo del documento"
    f.write_text(contenido_archivo, encoding="utf-8")
    
    obj, contenido = MetadataParser.parse_file(str(f))
    assert isinstance(obj, KnowledgeObject)
    assert obj.identifier == "DOC-001"
    assert obj.title == "Prueba"
    assert obj.object_type == "GUIDELINES"
    assert "Cuerpo del documento" in contenido