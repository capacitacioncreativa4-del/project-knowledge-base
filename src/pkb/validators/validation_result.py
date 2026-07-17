from dataclasses import dataclass, field
from typing import List

@dataclass
class ValidationResult:
    """Modela de forma explícita el resultado de auditoría de un documento."""
    document: str
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def success(self) -> bool:
        """Retorna True si el objeto de conocimiento no posee errores críticos."""
        return len(self.errors) == 0