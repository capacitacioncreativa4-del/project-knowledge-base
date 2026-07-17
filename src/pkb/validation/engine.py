import os
import yaml
from typing import Dict, Any, Tuple, List

class ValidationEngine:
    def __init__(self, schemas_dir: str):
        self.schemas_dir = schemas_dir

    def load_schema(self, entity_type: str) -> Dict[str, Any]:
        """Carga el archivo de esquema YAML correspondiente a la entidad."""
        # Se normaliza el nombre del archivo para coincidir con la nomenclatura física
        filename = f"{entity_type.lower()}.schema.yaml"
        schema_path = os.path.join(self.schemas_dir, "entities", filename)
        
        if not os.path.exists(schema_path):
            raise FileNotFoundError(f"Esquema no encontrado para la entidad '{entity_type}' en {schema_path}")
            
        with open(schema_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def validate_object(self, object_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Valida que un objeto de conocimiento cumpla con su esquema oficial."""
        errors = []
        entity_type = object_data.get("entity") or object_data.get("type")
        
        if not entity_type:
            return False, ["El objeto no define un tipo de entidad ('entity')."]
            
        try:
            schema = self.load_schema(entity_type)
        except Exception as e:
            return False, [str(e)]
            
        # Validar campos obligatorios (required)
        required_fields = schema.get("required", [])
        for field in required_fields:
            if field not in object_data:
                errors.append(f"Campo requerido ausente: '{field}'")
                
        return len(errors) == 0, errors