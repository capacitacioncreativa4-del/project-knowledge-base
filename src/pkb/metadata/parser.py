import re
import yaml
from pathlib import Path
from typing import Tuple
from pkb.core.exceptions import MetadataError
from pkb.knowledge.object import KnowledgeObject

class MetadataParser:
    @staticmethod
    def parse_file(file_path: str) -> Tuple[KnowledgeObject, str]:
        """
        Lee un archivo Markdown, separa el Front Matter (YAML) del contenido,
        y mapea las propiedades a un modelo de dominio explícito KnowledgeObject.
        Devuelve una tupla (KnowledgeObject, contenido_plano).
        """
        try:
            ruta = Path(file_path).resolve()
            if not ruta.exists():
                raise MetadataError(f"El archivo no existe: {file_path}")
                
            contenido_completo = ruta.read_text(encoding="utf-8")
            
            # Expresión regular para capturar el bloque entre los primeros dos '---'
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", contenido_completo, re.DOTALL)
            
            # Si no contiene Front Matter, inicializamos con campos vacíos de seguridad
            if not match:
                obj_vacio = KnowledgeObject(
                    identifier="", title="", object_type="", domain="",
                    version="", status="", owner="", source=ruta
                )
                return obj_vacio, contenido_completo
                
            bloque_yaml = match.group(1)
            contenido_plano = match.group(2)
            
            # Parsear el bloque extraído usando PyYAML
            metadatos = yaml.safe_load(bloque_yaml) or {}
            
            if not isinstance(metadatos, dict):
                raise MetadataError(f"El formato del Front Matter en {file_path} no es un objeto YAML válido.")
                
            # Construcción del Modelo de Dominio Explícito con extracción segura (.get)
            knowledge_object = KnowledgeObject(
                identifier=str(metadatos.get("id", "") or ""),
                title=str(metadatos.get("title", "") or ""),
                object_type=str(metadatos.get("type", "") or ""),
                domain=str(metadatos.get("domain", "") or ""),
                version=str(metadatos.get("version", "") or ""),
                status=str(metadatos.get("status", "") or ""),
                owner=str(metadatos.get("owner", "") or ""),
                source=ruta,
                tags=list(metadatos.get("tags", []) or []),
                relationships=list(metadatos.get("relationships", []) or [])
            )
            
            return knowledge_object, contenido_plano
            
        except yaml.YAMLError as ye:
            raise MetadataError(f"Error de sintaxis YAML en {file_path}: {str(ye)}")
        except Exception as e:
            if not isinstance(e, MetadataError):
                raise MetadataError(f"Fallo inesperado al parsear metadatos en {file_path}: {str(e)}")
            raise e