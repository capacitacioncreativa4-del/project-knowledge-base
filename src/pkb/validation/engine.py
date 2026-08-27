from pkb.validation.result import ValidationResult
from pkb.validation.rules import ValidationRule


class ValidationEngine:
    """Orquesta la ejecución de todas las reglas de validación."""

    def __init__(self) -> None:
        self._rules: list[ValidationRule] = []

    def add_rule(self, rule: ValidationRule) -> None:
        """Registra una regla en el pipeline de validación."""
        self._rules.append(rule)

    def validate(self, registry) -> list[ValidationResult]:
        """Ejecuta todas las reglas sobre el KnowledgeRegistry."""
        results: list[ValidationResult] = []

        for rule in self._rules:
            results.extend(rule.validate(registry))

        return results
