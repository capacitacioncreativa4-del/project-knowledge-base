from abc import ABC, abstractmethod
from collections import Counter
from pkb.validation.result import ValidationResult
from pkb.catalogs.domains import VALID_DOMAINS


class ValidationRule(ABC):
    """Clase base para todas las reglas de validación."""

    def __init__(self) -> None:
        self.name = self.__class__.__name__

    @abstractmethod
    def validate(self, registry) -> list[ValidationResult]:
        """Ejecuta la regla sobre el registro."""
        raise NotImplementedError


class DuplicateIdentifierRule(ValidationRule):
    """Detecta identificadores duplicados."""

    def validate(self, registry) -> list[ValidationResult]:
        resultados: list[ValidationResult] = []

        identifiers = [
            obj.identifier for obj in registry.all() if getattr(obj, "identifier", None)
        ]

        conteos = Counter(identifiers)
        duplicados = [
            identifier for identifier, cantidad in conteos.items() if cantidad > 1
        ]

        if duplicados:
            errores = [
                f"Identificador duplicado encontrado: '{identifier}'"
                for identifier in duplicados
            ]

            resultados.append(
                ValidationResult(
                    success=False,
                    rule=self.name,
                    field_name="identifier",
                    value=", ".join(duplicados),
                    errors=errores,
                )
            )
        else:
            resultados.append(
                ValidationResult(
                    success=True,
                    rule=self.name,
                )
            )

        return resultados


class BrokenReferenceRule(ValidationRule):
    """Detecta referencias hacia objetos inexistentes."""

    def validate(self, registry) -> list[ValidationResult]:
        resultados: list[ValidationResult] = []
        errores: list[str] = []

        ids_validos = {
            obj.identifier for obj in registry.all() if getattr(obj, "identifier", None)
        }

        for obj in registry.all():
            relaciones = getattr(obj, "relationships", None)

            if not relaciones:
                continue

            for ref_id in relaciones:
                if ref_id not in ids_validos:
                    errores.append(
                        f"Referencia rota en '{obj.identifier}': '{ref_id}' no existe."
                    )

        if errores:
            resultados.append(
                ValidationResult(
                    success=False,
                    rule=self.name,
                    field_name="relationships",
                    errors=errores,
                )
            )
        else:
            resultados.append(
                ValidationResult(
                    success=True,
                    rule=self.name,
                )
            )

        return resultados


class DomainRule(ValidationRule):
    """Valida que el dominio pertenezca al catálogo institucional."""

    def validate(self, registry) -> list[ValidationResult]:
        resultados = []
        errores = []

        for obj in registry.all():
            dominio = (obj.domain or "").upper().strip()

            if dominio not in VALID_DOMAINS:
                errores.append(
                    f"Dominio inválido en '{obj.identifier}': '{obj.domain}'"
                )

        resultados.append(
            ValidationResult(
                success=(len(errores) == 0),
                rule=self.name,
                field_name="domain",
                errors=errores,
            )
        )

        return resultados


class ValidationEngine:
    """Compatibilidad con la API existente."""

    @staticmethod
    def validate_metadata(metadata) -> ValidationResult:
        errors = []

        if metadata is None:
            return ValidationResult(
                success=False,
                rule="MetadataValidation",
                errors=["El archivo no contiene metadatos válidos."],
            )

        if hasattr(metadata, "identifier"):
            valores = {
                "id": metadata.identifier,
                "title": metadata.title,
                "type": metadata.object_type,
                "domain": metadata.domain,
                "status": metadata.status,
            }
        else:
            valores = metadata

        for campo in ("id", "title", "type", "domain"):
            if not valores.get(campo):
                errors.append(f"Falta el campo obligatorio: '{campo}'")

        return ValidationResult(
            success=(len(errors) == 0),
            rule="MetadataValidation",
            errors=errors,
        )
