from pkb.validation.result import ValidationResult


class ValidationReport:
    """
    Contenedor del resultado completo de una ejecución de validación.
    """

    def __init__(self, results: list[ValidationResult]):
        self.results = results

    @property
    def total_rules(self) -> int:
        return len(self.results)

    @property
    def total_errors(self) -> int:
        return sum(len(r.errors) for r in self.results)

    @property
    def success(self) -> bool:
        return self.total_errors == 0
