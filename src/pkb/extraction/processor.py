import os
import yaml

class SemanticProcessor:
    def __init__(self, source_dir, output_dir):
        self.source_dir = source_dir
        self.output_dir = output_dir

    def load_source_file(self, file_name):
        path = os.path.join(self.source_dir, file_name)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def save_extracted_entity(self, entity_id, data, category):
        target_dir = os.path.join(self.output_dir, category)
        os.makedirs(target_dir, exist_ok=True)
        
        target_path = os.path.join(target_dir, f"{entity_id}.yaml")
        with open(target_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
        print(f"[SUCCESS] Artefacto guardado: {target_path}")