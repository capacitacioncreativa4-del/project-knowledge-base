---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 44
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Vamos muy bien. Prosigamos con el proyecto

Excelente. Creo que éste es el momento adecuado para dar un paso que cambiará la naturaleza del proyecto.

Hasta ahora hemos diseñado el PKB como un repositorio inteligente. Mi propuesta es que evolucione hacia una **plataforma de ingeniería del conocimiento**.

La diferencia es importante:

* Un repositorio **almacena** conocimiento.
* Una plataforma **comprende, valida, relaciona y explota** el conocimiento.

Esa será la visión de la versión **1.0**.

---

# Sprint 1 – EPIC S1-002

## Repository Intelligence Layer (RIL)

Introduciremos una nueva capa de arquitectura que actuará como el núcleo operativo del PKB.

```text
                    PKB CLI
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    Validation     Inventory      Doctor
         │             │             │
         └─────────────┼─────────────┘
                       ▼
        Repository Intelligence Layer
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
 Repository       Metadata         Knowledge
   Scanner          Engine            Index
      ▼                ▼                ▼
 Filesystem      YAML Parser      Object Graph
```

Esta capa evitará que cada comando implemente nuevamente la misma lógica.

---

# Nueva organización del código

Propongo evolucionar `src/pkb` hacia la siguiente estructura:

```text
src/
└── pkb/
    ├── cli/
    ├── core/
    ├── repository/
    │   ├── scanner.py
    │   ├── locator.py
    │   ├── inventory.py
    │   └── loader.py
    │
    ├── metadata/
    │   ├── parser.py
    │   ├── validator.py
    │   ├── models.py
    │   └── cache.py
    │
    ├── knowledge/
    │   ├── object.py
    │   ├── registry.py
    │   ├── relationships.py
    │   └── graph_builder.py
    │
    ├── validators/
    ├── reporting/
    ├── services/
    └── utils/
```

---

# Nuevo modelo central

Hasta ahora nuestros validadores trabajan con diccionarios.

Propongo introducir un modelo de dominio.

## `src/pkb/knowledge/object.py`

```python
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class KnowledgeObject:
    """Representa un objeto de conocimiento del PKB."""

    identifier: str
    title: str
    object_type: str
    domain: str
    version: str
    status: str
    owner: str
    source: Path

    tags: list[str] = field(default_factory=list)

    relationships: list[str] = field(default_factory=list)
```

A partir de este momento el sistema dejará de intercambiar diccionarios y comenzará a trabajar con objetos del dominio.

---

# Servicio de Inventario

Uno de los primeros servicios de la nueva capa será el inventario.

```
pkb inventory
```

Deberá producir algo como:

```text
Repository Inventory

Documents .......... 482

Knowledge Objects .. 361

Standards .......... 24

Templates .......... 17

ADR ................ 8

Projects ........... 6

Broken Metadata .... 2

Broken Links ....... 0
```

Este comando será muy útil para medir el crecimiento del PKB.

---

# Servicio "Doctor"

Quiero introducir una herramienta inspirada en `git fsck`, `flutter doctor` y `brew doctor`.

```
pkb doctor
```

Su objetivo será revisar el estado general del repositorio.

Ejemplo:

```text
PKB Doctor

✔ Metadata

✔ Identifiers

✔ Links

✔ Templates

✔ Repository Structure

✔ Duplicate IDs

✔ YAML Syntax

✔ Version Consistency

✔ Graph Integrity

Overall Status

HEALTHY
```

Con el tiempo este comando se convertirá en el diagnóstico integral del PKB.

---

# Nuevo concepto: Repository Health Score

Además de detectar errores, propongo medir la salud del repositorio.

Ejemplo:

| Indicador              | Peso |
| ---------------------- | ---: |
| Metadatos válidos      | 20 % |
| Identificadores únicos | 15 % |
| Relaciones correctas   | 15 % |
| Enlaces válidos        | 10 % |
| Plantillas conformes   | 15 % |
| Cobertura de pruebas   | 10 % |
| Documentación          | 10 % |
| Integridad del grafo   |  5 % |

Resultado:

```
Repository Health

94.8 %

Grade A
```

Esto permitirá observar objetivamente la evolución del PKB a lo largo del tiempo.

---

# ADR-0011 — Modelo de Dominio Explícito

Propongo registrar una decisión arquitectónica adicional:

> **Toda la lógica del PKB deberá operar sobre un modelo de dominio explícito (`KnowledgeObject`, `Relationship`, `ValidationResult`, etc.) y no sobre estructuras de datos genéricas.**

Esta decisión tiene varias ventajas:

* El código será más legible y mantenible.
* Facilitará el tipado estático y el uso de herramientas como `mypy`.
* Reducirá errores asociados a claves de diccionarios.
* Permitirá extender el modelo con nuevas propiedades sin modificar toda la base de código.
* Facilitará la serialización a formatos como JSON, GraphML o RDF para el Knowledge Graph.

---

# Hoja de ruta inmediata

Creo que el siguiente conjunto de hitos debe ser:

### Sprint 1.1 — Plataforma ejecutable

* CLI funcional.
* `pkb validate`.
* `pkb inventory`.
* `pkb doctor`.

### Sprint 1.2 — Motor documental

* Carga de documentos.
* Parser YAML robusto.
* Registro de objetos de conocimiento.
* Inventario automático.

### Sprint 1.3 — Motor semántico

* Construcción del grafo de conocimiento.
* Validación de relaciones.
* Análisis de impacto.
* Navegación semántica.

### Sprint 1.4 — Automatización

* GitHub Actions.
* Validación continua.
* Generación automática de informes.
* Publicación de métricas.

## Recomendación estratégica

A partir de este punto, conviene que el desarrollo del PKB adopte un ciclo similar al de un proyecto de software profesional:

1. **Diseño** (ADR + estándar).
2. **Implementación** (código).
3. **Pruebas** (unitarias e integración).
4. **Automatización** (CI/CD).
5. **Documentación** (actualizada automáticamente).

Con este enfoque, el repositorio que has creado en GitHub no será únicamente el lugar donde almacenes proyectos como MIPSP, SIM-PYME o el Kit Editorial Maestro. Se convertirá en una plataforma capaz de gestionar, validar y relacionar todo ese conocimiento de forma consistente y automatizada. Esa es la dirección arquitectónica que considero más sólida para el objetivo que nos hemos planteado.
