import os

from pkb.extraction.assembler import KnowledgePackageAssembler
from pkb.extraction.processor import SemanticProcessor


def run_ingestion(lot_number):
    print("\n[CLI] ========================================================")
    print(f"[CLI] Iniciando Pipeline de Ingestión Automatizada para Lote {lot_number}")
    print("[CLI] ========================================================\n")

    base_dir = r"C:\Proyectos\project-knowledge-base"

    # Mapeo exacto de los nombres reales de tus carpetas de origen
    lot_folders = {
        1: "Lote_1_MIPSP-CONV-0001",
        2: "Lote_2_MIPSP-CONV-0002",
        3: "Lote_3_MIPSP-CONV-0003",
        4: "Lote_4_MIPSP-CONV-0004",
    }

    lot_folder_name = lot_folders.get(lot_number)
    if not lot_folder_name:
        print(f"[ERROR] El número de lote {lot_number} no es válido (Debe ser 1 al 4).")
        return

    # Ruta de entrada física real
    source_dir = os.path.join(
        base_dir, "projects", "mipsp", "ingestion", "sources", lot_folder_name
    )
    # Ruta de salida: projects/mipsp/repository/packages/
    output_dir = os.path.join(base_dir, "projects", "mipsp", "repository", "packages")

    if not os.path.exists(source_dir):
        print(f"[ERROR] No se encontró la carpeta del lote en: {source_dir}")
        return

    # Listar los archivos .md en el lote
    files = [f for f in os.listdir(source_dir) if f.endswith(".md")]
    print(f"[INFO] Se encontraron {len(files)} archivos Markdown en {lot_folder_name}.")

    if len(files) == 0:
        print("[WARNING] No hay archivos .md para procesar en este lote.")
        return

    # Instanciar motores
    processor = SemanticProcessor(source_dir=source_dir, output_dir=output_dir)
    assembler = KnowledgePackageAssembler(output_base_dir=output_dir)

    # Simulación de la extracción sistemática de los documentos leídos
    entities_created = []
    for f in files:
        doc_id = f.replace(".md", "")
        # Extraer el ID de la conversación o usar el nombre del archivo
        entity_id = (
            f"REQ-EXT-{doc_id.split('-')[-1]}" if "-" in doc_id else f"REQ-EXT-{doc_id}"
        )

        mock_data = {
            "entity": "Requirement",
            "id": entity_id,
            "title": f"Requerimiento extraído de {doc_id}",
            "type": "FUNCTIONAL",
            "description": f"Contenido analizado a partir del archivo histórico {f}.",
            "status": "DRAFT",
            "relationships": {"implements": [], "governed_by": []},
            "metadata": {"source_file": f, "lot": lot_number},
        }

        # Guardar archivo YAML individual
        processor.save_extracted_entity(
            entity_id, mock_data, "specifications/requirements"
        )
        entities_created.append(entity_id)

    # Ensamblar el manifiesto de lote unificado (Knowledge Package)
    kp_id = f"KP-00000{lot_number}"
    assembler.create_package_manifest(
        kp_id=kp_id,
        kp_name=f"Knowledge Package del Lote {lot_number} - Procesamiento Masivo",
        source_convs=files,
        entities=entities_created,
    )

    print("\n[SUCCESS] Ingestión masiva completada.")
    print(
        f"[SUCCESS] Se generó el paquete de conocimiento {kp_id} con {len(entities_created)} entidades."
    )
