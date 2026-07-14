from collections import Counter
from pkb.knowledge.registry import KnowledgeRegistry

class KnowledgeCatalog:
    """Provee capacidades analíticas y de indexación estadística sobre el registro SSoT."""

    def __init__(self, registry: KnowledgeRegistry):
        self._registry = registry

    def by_type(self) -> Counter:
        """Devuelve un contador con la frecuencia acumulada por tipo de objeto normalizado."""
        # Contamos directamente usando la propiedad unificada del objeto de dominio
        return Counter(obj.object_type for obj in self._registry.all())

    def by_domain(self) -> Counter:
        """Devuelve un contador con la frecuencia acumulada por dominio normalizado."""
        return Counter(obj.domain for obj in self._registry.all())