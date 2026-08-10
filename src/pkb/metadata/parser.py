import re
from pathlib import Path
from typing import Tuple

import yaml

from pkb.core.exceptions import MetadataError
from pkb.knowledge.object import KnowledgeObject


class MetadataParser:
    @staticmethod
    def parse_file(file_path: str) -> Tuple[KnowledgeObject, str]:
        """
        Lee un archivo Markdown, separa el Front Matter (YAML) del contenido
        y mapea las propiedades a un modelo de dominio explícito
        KnowledgeObject.

        Soporta dos representaciones de relaciones:

        1. Formato histórico:
            relationships:
              - ADR-001
              - DOC-001

        2. Formato tipado:
            relationships:
              derived_from:
                - ADR-001
              implemented_by:
                - DOC-001

        En ambos casos se conserva la representación histórica
        ``relationships`` y, cuando corresponde, la representación
        tipada ``typed_relationships``.
        """
        try:
            ruta = Path(file_path).resolve()

            if not ruta.exists():
                raise MetadataError(f"El archivo no existe: {file_path}")

            contenido_completo = ruta.read_text(encoding="utf-8")

            match = re.match(
                r"^---\s*\n(.*?)\n---\s*\n(.*)$",
                contenido_completo,
                re.DOTALL,
            )

            if not match:
                obj_vacio = KnowledgeObject(
                    identifier="",
                    title="",
                    object_type="",
                    domain="",
                    version="",
                    status="",
                    owner="",
                    source=ruta,
                )
                return obj_vacio, contenido_completo

            bloque_yaml = match.group(1)
            contenido_plano = match.group(2)

            metadatos = yaml.safe_load(bloque_yaml) or {}

            if not isinstance(metadatos, dict):
                raise MetadataError(
                    f"El formato del Front Matter en {file_path} "
                    "no es un objeto YAML válido."
                )

            relaciones = metadatos.get("relationships", []) or []

            knowledge_object = KnowledgeObject(
                identifier=str(metadatos.get("id", "") or ""),
                title=str(metadatos.get("title", "") or ""),
                object_type=str(metadatos.get("type", "") or ""),
                domain=str(metadatos.get("domain", "") or ""),
                version=str(metadatos.get("version", "") or ""),
                status=str(metadatos.get("status", "") or ""),
                owner=str(metadatos.get("owner", "") or ""),
                source=ruta,
            )

            if isinstance(relaciones, list):
                legacy_relationships = [
                    str(target_id) for target_id in relaciones if target_id is not None
                ]

                knowledge_object.relationships = legacy_relationships

            elif isinstance(relaciones, dict):
                for relation_type, target_ids in relaciones.items():
                    if target_ids is None:
                        continue

                    if isinstance(target_ids, str):
                        target_ids = [target_ids]

                    if not isinstance(target_ids, list):
                        raise MetadataError(
                            f"La relación '{relation_type}' en {file_path} "
                            "debe contener una lista de identificadores."
                        )

                    for target_id in target_ids:
                        if target_id is None:
                            continue

                        knowledge_object.add_relationship(
                            str(relation_type),
                            str(target_id),
                        )

            else:
                raise MetadataError(
                    f"El campo 'relationships' en {file_path} "
                    "debe ser una lista o un objeto YAML."
                )

            return knowledge_object, contenido_plano

        except yaml.YAMLError as ye:
            raise MetadataError(
                f"Error de sintaxis YAML en {file_path}: {str(ye)}"
            ) from ye

        except MetadataError:
            raise

        except Exception as e:
            raise MetadataError(
                f"Fallo inesperado al parsear metadatos en {file_path}: {str(e)}"
            ) from e
