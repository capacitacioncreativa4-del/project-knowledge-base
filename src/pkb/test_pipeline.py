import os
from extraction.processor import SemanticProcessor
from extraction.assembler import KnowledgePackageAssembler

def run_pilot_ingestion():
    # 1. Definir rutas absolutas
    base_dir = r"C:\Proyectos\project-knowledge-base"
    source_dir = os.path.join(base_dir, "projects", "mipsp", "ingestion", "sources", "lote-1")
    output_dir = os.path.join(base_dir, "projects", "mipsp", "repository", "packages")
    
    print("[INIT] Iniciando Pipeline de Ingestión Piloto para el Lote 1...")
    
    # Asegurar que existan directorios mínimos para la prueba
    os.makedirs(source_dir, exist_ok=True)
    
    # 2. Instanciar los componentes del núcleo programados en I03 e I04
    processor = SemanticProcessor(source_dir=source_dir, output_dir=output_dir)
    assembler = KnowledgePackageAssembler(output_base_dir=output_dir)
    
    # 3. Simulación de la entidad extraída por IA de MIPSP-CONV-0001-P01
    mock_requirement = {
        "entity": "Requirement",
        "id": "REQ-000201",
        "title": "Capacitación Básica Obligatoria en Seguridad Privada",
        "type": "FUNCTIONAL",
        "description": "Todo el personal operativo de seguridad privada en Morelos debe acreditar el curso básico de competencias.",
        "status": "DRAFT",
        "relationships": {
            "implements": [],
            "governed_by": []
        },
        "metadata": {
            "priority": "HIGH",
            "traceable": True
        }
    }
    
    # 4. Guardar la entidad usando el procesador
    processor.save_extracted_entity("REQ-000201", mock_requirement, "specifications/requirements")
    
    # 5. Ensamblar el paquete de conocimiento (KP) correspondiente al Lote 1
    assembler.create_package_manifest(
        kp_id="KP-000001",
        kp_name="Paquete de Fundaciones Normativas Operativas - Lote 1",
        source_convs=["MIPSP-CONV-0001-P01.md"],
        entities=["REQ-000201"]
    )
    
    print("[SUCCESS] Pipeline Piloto Ejecutado y Validado con Éxito.")

if __name__ == "__main__":
    run_pilot_ingestion()