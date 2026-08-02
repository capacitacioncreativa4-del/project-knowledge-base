from typing import Any


class ValidationResult:
    """Representa el resultado de una validación."""

    def __init__(
        self,
        file_path: str = "",
        success: bool = False,
        errors: list[str] | None = None,
    ):
        self.file_path = file_path
        self.success = success
        self.is_valid = success  # Compatibilidad con código existente
        self.errors = errors or []

    def to_dict(self) -> dict[str, Any]:
        return {
            "file": self.file_path,
            "status": "PASS" if self.success else "FAIL",
            "errors": self.errors,
        }
