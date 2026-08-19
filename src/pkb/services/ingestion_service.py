from pkb.config import PKB_ROOT
from pkb.extraction.assembler import KnowledgePackageAssembler
from pkb.extraction.processor import SemanticProcessor


class IngestionService:
    """Servicio responsable de la ingestión de conocimiento."""

    @staticmethod
    def run(lot_number: int) -> None:
        print("\n[CLI] ========================================================")
        print(
            f"[CLI] Iniciando Pipeline de Ingestión Automatizada para Lote {lot_number}"
        )
        print("[CLI] ========================================================\n")

        base_dir = PKB_ROOT

        lot_folders = {
            1: "Lote_1_MIPSP-CONV-0001",
            2: "Lote_2_MIPSP-CONV-0002",
            3: "Lote_3_MIPSP-CONV-0003",
            4: "Lote_4_MIPSP-CONV-0004",
        }

        lot_folder_name = lot_folders.get(lot_number)

        if not lot_folder_name:
            print(f"[ERROR] El número de lote {lot_number} no es válido.")
            return

        source_dir = (
            base_dir / "projects" / "mipsp" / "ingestion" / "sources" / lot_folder_name
        )

        output_dir = base_dir / "projects" / "mipsp" / "repository" / "packages"

        if not source_dir.exists():
            print(f"[ERROR] No existe: {source_dir}")
            return

        files = [f.name for f in source_dir.glob("*.md")]

        print(f"[INFO] Se encontraron {len(files)} archivos.")

        if not files:
            print("[WARNING] No existen archivos para procesar.")
            return

        processor = SemanticProcessor(
            source_dir=source_dir,
            output_dir=output_dir,
        )

        assembler = KnowledgePackageAssembler(
            output_base_dir=output_dir,
        )

        entities_created = []

        for f in files:
            doc_id = f.replace(".md", "")

            entity_id = (
                f"REQ-EXT-{doc_id.split('-')[-1]}"
                if "-" in doc_id
                else f"REQ-EXT-{doc_id}"
            )

            data = {
                "entity": "Requirement",
                "id": entity_id,
                "title": f"Requerimiento extraído de {doc_id}",
                "type": "FUNCTIONAL",
                "description": f"Contenido analizado desde {f}",
                "status": "DRAFT",
                "relationships": {
                    "implements": [],
                    "governed_by": [],
                },
                "metadata": {
                    "source_file": f,
                    "lot": lot_number,
                },
            }

            processor.save_extracted_entity(
                entity_id,
                data,
                "specifications/requirements",
            )

            entities_created.append(entity_id)

        kp_id = f"KP-00000{lot_number}"

        assembler.create_package_manifest(
            kp_id=kp_id,
            kp_name=f"Knowledge Package {lot_number}",
            source_convs=files,
            entities=entities_created,
        )

        print("\n[SUCCESS] Ingestión completada.")
