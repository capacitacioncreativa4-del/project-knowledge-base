from typing import List, Dict, Any

class ValidationResult:
    def __init__(self, file_path: str, is_valid: bool, errors: List[str]):
        self.file_path = file_path
        self.is_valid = is_valid
        self.errors = errors

    def to_dict(self) -> Dict[str, Any]:
        """Serializa el resultado de la validación para auditorías."""
        return {
            "file": self.file_path,
            "status": "PASS" if self.is_valid else "FAIL",
            "errors": self.errors
        }