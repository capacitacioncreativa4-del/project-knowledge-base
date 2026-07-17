from collections.abc import Iterator
from pkb.knowledge.object import KnowledgeObject

class KnowledgeRegistry:
    """Registro institucional centralizado en memoria de objetos de conocimiento (SSoT)."""
    
    def __init__(self) -> None:
        self._objects: dict[str, KnowledgeObject] = {}
        
    def add(self, obj: KnowledgeObject) -> None:
        """Añade un objeto al registro. Levanta un error si el ID ya existe."""
        if not obj.identifier:
            return  # Ignoramos objetos sin ID válido para el registro formal
            
        if obj.identifier in self._objects:
            raise ValueError(
                f"Identificador duplicado detectado en el repositorio: {obj.identifier}"
            )
        self._objects[obj.identifier] = obj
        
    def get(self, identifier: str) -> KnowledgeObject | None:
        """Recupera un objeto por su identificador único."""
        return self._objects.get(identifier)
        
    def all(self) -> Iterator[KnowledgeObject]:
        """Devuelve un iterador sobre todos los objetos registrados."""
        return iter(self._objects.values())
        
    def count(self) -> int:
        """Devuelve la cantidad total de objetos registrados."""
        return len(self._objects)