from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Relationship:
    """Representa una relación semántica entre dos objetos PKB."""

    relation_type: str
    target_id: str
