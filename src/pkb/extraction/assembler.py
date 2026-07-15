import os
import yaml

class KnowledgePackageAssembler:
    def __init__(self, output_base_dir):
        self.output_base_dir = output_base_dir

    def create_package_manifest(self, kp_id, kp_name, source_convs, entities):
        kp_dir = os.path.join(self.output_base_dir, kp_id)
        os.makedirs(kp_dir, exist_ok=True)

        manifest_data = {
            "entity": "KnowledgePackage",
            "id": kp_id,
            "name": kp_name,
            "source_conversations": source_convs,
            "extracted_entities": entities,
            "metadata": {
                "status": "DRAFT",
                "compiler": "PKB Semantic Extraction Engine"
            }
        }

        manifest_path = os.path.join(kp_dir, "manifest.yaml")
        with open(manifest_path, 'w', encoding='utf-8') as f:
            yaml.dump(manifest_data, f, allow_unicode=True, sort_keys=False)
        print(f"[SUCCESS] Manifiesto del Paquete {kp_id} ensamblado en: {manifest_path}")