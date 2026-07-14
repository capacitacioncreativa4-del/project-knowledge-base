from pkb.knowledge.object import KnowledgeObject
from pkb.validators.validation_result import ValidationResult

class ValidationEngine:
    @staticmethod
    def validate_metadata(obj: KnowledgeObject) -> ValidationResult:
        """
        Audita un objeto de conocimiento formal contra las reglas institucionales.
        Devuelve un objeto ValidationResult con los hallazgos.
        """
        # Inicializamos el resultado asociado a la ruta del archivo fuente
        resultado = ValidationResult(document=str(obj.source.name))
        
        # 1. Validar presencia de campos obligatorios en el objeto de dominio
        if not obj.identifier:
            resultado.errors.append("Falta el campo obligatorio o está vacío: 'id'")
        if not obj.title:
            resultado.errors.append("Falta el campo obligatorio o está vacío: 'title'")
        if not obj.object_type:
            resultado.errors.append("Falta el campo obligatorio o está vacío: 'type'")
        if not obj.status:
            resultado.errors.append("Falta el campo obligatorio o está vacío: 'status'")
            
        # 2. Validaciones de tipos de datos de dominio
        if obj.identifier and not isinstance(obj.identifier, str):
            resultado.errors.append("El campo 'id' debe ser una cadena de texto.")
            
        if obj.tags and not isinstance(obj.tags, list):
            resultado.errors.append("El campo 'tags' debe ser una lista de etiquetas.")
            
        return resultado