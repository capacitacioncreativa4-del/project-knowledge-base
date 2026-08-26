from abc import ABC, abstractmethod
from collections import Counter

from pkb.catalogs.domains import VALID_DOMAINS
from pkb.validation.result import ValidationResult


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


class MetadataValidationRule(ValidationRule):
    """Valida los metadatos obligatorios de los objetos de conocimiento."""

    def validate(self, registry) -> list[ValidationResult]:
        resultados: list[ValidationResult] = []
        errores: list[str] = []

        for obj in registry.all():
            valores = {
                "id": getattr(obj, "identifier", None),
                "title": getattr(obj, "title", None),
                "type": getattr(obj, "object_type", None),
                "domain": getattr(obj, "domain", None),
            }

            for campo in ("id", "title", "type", "domain"):
                if not valores.get(campo):
                    errores.append(
                        f"Falta el campo obligatorio: '{campo}' "
                        f"en '{getattr(obj, 'identifier', '<sin-id>')}'"
                    )

        resultados.append(
            ValidationResult(
                success=(len(errores) == 0),
                rule=self.name,
                field_name="metadata",
                errors=errores,
            )
        )

        return resultados
