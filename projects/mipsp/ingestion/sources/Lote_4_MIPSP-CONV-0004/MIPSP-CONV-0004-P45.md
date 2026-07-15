---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 45
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Vamos muy bien. Continuemos con el proyecto

Excelente. Creo que estamos en el momento adecuado para cambiar definitivamente la naturaleza del proyecto.

Hasta ahora hemos construido la **infraestructura del PKB**. A partir de este Sprint comenzaremos a construir el **motor del PKB**.

Hay una diferencia importante entre ambos conceptos:

* La infraestructura organiza el conocimiento.
* El motor interpreta el conocimiento.

Ese será el mayor salto tecnológico del proyecto.

---

# EPIC S1-003 — Knowledge Engine

## Objetivo

Construir el **Knowledge Engine**, el componente responsable de transformar documentos Markdown en objetos de conocimiento que puedan ser consultados, relacionados y analizados.

La arquitectura propuesta es:

```text
                 Markdown
                     │
                     ▼
             Repository Scanner
                     │
                     ▼
              Metadata Parser
                     │
                     ▼
           Knowledge Object Builder
                     │
                     ▼
            Knowledge Registry
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    Validation Engine      Knowledge Graph
          ▼                     ▼
       Reporting          AI / Codex
```

Este componente será el núcleo de todo el PKB.

---

# Incremento 1 — Knowledge Registry

El primer servicio será el registro institucional de objetos de conocimiento.

## Estructura

```text
src/pkb/knowledge/
│
├── object.py
├── relationship.py
├── registry.py
├── loader.py
├── builder.py
├── catalog.py
└── exceptions.py
```

---

# Archivo 1

## `relationship.py`

```python
from dataclasses import dataclass


@dataclass(slots=True)
class Relationship:
    """Representa una relación entre dos objetos de conocimiento."""

    source: str
    target: str
    relation_type: str
```

---

# Archivo 2

## `registry.py`

```python
from collections.abc import Iterator

from pkb.knowledge.object import KnowledgeObject


class KnowledgeRegistry:
    """Registro central de objetos de conocimiento."""

    def __init__(self) -> None:
        self._objects: dict[str, KnowledgeObject] = {}

    def add(self, obj: KnowledgeObject) -> None:
        if obj.identifier in self._objects:
            raise ValueError(
                f"Identificador duplicado: {obj.identifier}"
            )

        self._objects[obj.identifier] = obj

    def get(self, identifier: str) -> KnowledgeObject | None:
        return self._objects.get(identifier)

    def all(self) -> Iterator[KnowledgeObject]:
        return iter(self._objects.values())

    def count(self) -> int:
        return len(self._objects)
```

---

# Archivo 3

## `catalog.py`

```python
from collections import Counter

from pkb.knowledge.registry import KnowledgeRegistry


class KnowledgeCatalog:
    """Genera estadísticas del repositorio."""

    def __init__(self, registry: KnowledgeRegistry):
        self.registry = registry

    def by_type(self):

        counter = Counter()

        for obj in self.registry.all():
            counter[obj.object_type] += 1

        return counter

    def by_domain(self):

        counter = Counter()

        for obj in self.registry.all():
            counter[obj.domain] += 1

        return counter
```

---

# Archivo 4

## `builder.py`

```python
from pathlib import Path

from pkb.knowledge.object import KnowledgeObject


class KnowledgeObjectBuilder:

    @staticmethod
    def build(metadata: dict, source: Path):

        return KnowledgeObject(
            identifier=metadata["id"],
            title=metadata["title"],
            object_type=metadata["type"],
            domain=metadata["domain"],
            version=metadata["version"],
            status=metadata["status"],
            owner=metadata["owner"],
            source=source,
            tags=metadata.get("tags", []),
        )
```

---

# Nuevo comando

## `pkb inventory`

El objetivo es generar automáticamente un inventario del repositorio.

Salida esperada:

```text
Repository Inventory

Total Objects ............. 184

Governance ................. 12

Standards ................. 27

Templates ................. 19

Projects ................... 6

Research .................. 35

Requirements .............. 41

Designs ................... 22

Risks ...................... 8

Procedures ................ 14
```

Más adelante este comando podrá exportar el inventario a:

* JSON
* CSV
* Excel
* Markdown

---

# Archivo generado

```
reports/
└── repository-inventory.md
```

Ejemplo:

```markdown
# Repository Inventory

## Summary

| Type | Count |
|------|------:|
| GOV | 12 |
| STD | 27 |
| TMP | 19 |
| REQ | 41 |

---

Generated automatically by PKB.
```

---

# Pruebas

Incorporaremos pruebas sobre el registro.

```python
from pkb.knowledge.registry import KnowledgeRegistry
from pkb.knowledge.object import KnowledgeObject
from pathlib import Path


def test_registry_add():

    registry = KnowledgeRegistry()

    registry.add(
        KnowledgeObject(
            identifier="PKB-STD-0001",
            title="Metadata",
            object_type="STD",
            domain="PKB",
            version="1.0.0",
            status="Approved",
            owner="Architecture",
            source=Path("metadata.md"),
        )
    )

    assert registry.count() == 1
```

---

# ADR-0012 — El registro como fuente única de verdad

Quiero formalizar una decisión arquitectónica que considero esencial para el crecimiento del PKB.

> **El `KnowledgeRegistry` será la fuente única de verdad (*Single Source of Truth*) para todos los objetos de conocimiento cargados en memoria.**

Esto implica que:

* Los validadores no recorrerán directamente el sistema de archivos.
* Los informes se generarán a partir del registro.
* El grafo de conocimiento se construirá desde el registro.
* Los futuros agentes de IA (incluido Codex) consultarán el registro y no los archivos individuales.

Esta decisión desacopla el almacenamiento físico (Git y Markdown) del modelo lógico del conocimiento.

---

# Hito de la versión 0.2.0

Con los incrementos propuestos para esta épica podremos considerar completada la primera versión funcional del motor del PKB. Los criterios de aceptación para ese hito serían:

* ✅ Descubrir automáticamente todos los documentos Markdown.
* ✅ Extraer y validar sus metadatos.
* ✅ Construir objetos `KnowledgeObject`.
* ✅ Registrar los objetos en memoria mediante `KnowledgeRegistry`.
* ✅ Generar un inventario automático del repositorio.
* ✅ Exponer los comandos `pkb validate`, `pkb inventory` y `pkb doctor`.

## Recomendación para la siguiente fase

A partir de la versión **0.2.0**, creo que conviene empezar a incorporar tus proyectos reales de forma gradual. En lugar de desarrollar el PKB de manera aislada, utilizaremos **MIPSP** como primer proyecto piloto. Esto nos permitirá validar la arquitectura con un caso de uso auténtico, detectar ajustes necesarios en los estándares y comprobar que el flujo completo —desde los documentos hasta el inventario y las validaciones— funciona sobre un proyecto de tamaño significativo. Ese paso reducirá el riesgo antes de migrar el resto de tus iniciativas, como SIM-PYME, el Kit Editorial Maestro o el proyecto de Condominios.
