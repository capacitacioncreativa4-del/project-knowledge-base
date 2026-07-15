from abc import ABC, abstractmethod
from collections import Counter
from pkb.validation.result import ValidationResult

class ValidationRule(ABC):
    """Clase base abstracta para todas las reglas de validación modulares."""
    
    def __init__(self):
        self.name = self.__class__.__name__

    @abstractmethod
    def validate(self, registry) -> list[ValidationResult]:
        """Ejecuta la lógica de auditoría sobre el registro SSoT en memoria."""
        pass


class DuplicateIdentifierRule(ValidationRule):
    """Audita el SSoT para garantizar que no existan identificadores ('id') duplicados."""
    
    def validate(self, registry) -> list[ValidationResult]:
        resultados = []
        identifiers = [obj.identifier for obj in registry.all() if obj.identifier]
        conteos = Counter(identifiers)
        duplicados = [ident for ident, count in conteos.items() if count > 1]
        
        if duplicados:
            errores = [f"Identificador duplicado encontrado en el repositorio: '{id_duplicado}'" for id_duplicado in duplicados]
            resultados.append(ValidationResult(False, errores))
        else:
            resultados.append(ValidationResult(True, []))
            
        return resultados


class BrokenReferenceRule(ValidationRule):
    """Audita las relaciones cruzadas para detectar referencias rotas hacia IDs inexistentes."""
    
    def validate(self, registry) -> list[ValidationResult]:
        resultados = []
        errores = []
        
        # Mapeamos un set con todos los IDs válidos existentes en el SSoT para búsquedas eficientes
        id_validos = {obj.identifier for obj in registry.all() if obj.identifier}
        
        # Analizamos las referencias cruzadas de cada objeto
        for obj in registry.all():
            if hasattr(obj, "relationships") and obj.relationships:
                for ref_id in obj.relationships:
                    if ref_id not in id_validos:
                        errores.append(
                            f"Referencia rota en '{obj.identifier}': apunta al objeto inexistente '{ref_id}'"
                        )
                        
        if errores:
            resultados.append(ValidationResult(False, errores))
        else:
            resultados.append(ValidationResult(True, []))
            
        return resultados


class ValidationEngine:
    """Motor encargado de orquestar y ejecutar el pipeline de reglas modulares."""
    
    def __init__(self):
        self.rules = []
        
    def add_rule(self, rule: ValidationRule):
        """Agrega una nueva regla de validación al pipeline activo."""
        self.rules.append(rule)
        
    def validate(self, registry) -> list[ValidationResult]:
        """Somete el repositorio completo a todas las reglas del pipeline."""
        results = []
        for rule in self.rules:
            results.extend(rule.validate(registry))
        return results

    @staticmethod
    def validate_metadata(metadata: dict) -> ValidationResult:
        """Mantiene la compatibilidad temporal con el validador estructural de metadatos previo."""
        errors = []
        if not metadata:
            return ValidationResult(False, ["El archivo no contiene metadatos válidos o el front-matter está vacío."])
            
        campos_obligatorios = ["id", "title", "type", "domain"]
        for campo in campos_obligatorios:
            if not metadata.get(campo):
                errors.append(f"Falta el campo obligatorio: '{campo}'")
                
        return ValidationResult(len(errors) == 0, errors)