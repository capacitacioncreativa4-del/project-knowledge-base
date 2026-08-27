from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ValidationResult:
    """
    Representa el resultado de una regla de validación sobre
    un objeto del repositorio.
    """

    success: bool

    rule: str = ""

    identifier: str = ""

    file_path: str = ""

    field_name: str = ""

    value: str = ""

    errors: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        """Compatibilidad con versiones anteriores."""
        return self.success

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": "PASS" if self.success else "FAIL",
            "rule": self.rule,
            "identifier": self.identifier,
            "file": self.file_path,
            "field": self.field_name,
            "value": self.value,
            "errors": self.errors,
        }
