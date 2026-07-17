---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 46
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Simplemente, genial. Adelante con la siguiente fase del proyecto

Excelente. Considero que éste es el momento más importante desde que iniciamos el proyecto.

Voy a proponerte una decisión de arquitectura que cambia completamente el alcance del PKB.

---

# DEC-0013 — El PKB deja de ser un repositorio y se convierte en una plataforma

Hasta ahora hemos hablado del PKB como un repositorio Git muy bien organizado.

Creo que debemos dejar atrás esa idea.

A partir de ahora el PKB será una **plataforma**, compuesta por cuatro productos que evolucionan de manera coordinada.

```text
                   Project Knowledge Base
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
 PKB Platform         PKB Knowledge       PKB Projects
     (software)          (contenido)       (proyectos)
      │
      ▼
 PKB Automation
```

Esto nos permitirá mantener una separación muy clara entre:

* el software que administra el conocimiento;
* el conocimiento institucional;
* los proyectos que viven dentro del PKB;
* la automatización.

Esta separación facilitará el mantenimiento y la evolución de la plataforma.

---

# FASE 2 — PKB Platform

## Objetivo

Construir el software que administrará el conocimiento.

Ya no desarrollaremos únicamente utilidades.

Desarrollaremos una aplicación.

---

# Arquitectura v1.0

```text
src/pkb/

core/
│
├── config.py
├── exceptions.py
├── logging.py
├── settings.py
└── constants.py

repository/
│
├── scanner.py
├── loader.py
├── inventory.py
├── cache.py
└── locator.py

knowledge/
│
├── object.py
├── relationship.py
├── registry.py
├── builder.py
├── graph.py
└── catalog.py

metadata/
│
├── parser.py
├── validator.py
├── schema.py
└── serializer.py

validation/
│
├── engine.py
├── result.py
├── rules.py
└── pipeline.py

reporting/
│
├── markdown.py
├── html.py
├── json.py
├── csv.py
└── excel.py

cli/
│
├── main.py
├── commands/
│
└── services/

plugins/

tests/
```

Esta organización permite que el proyecto siga creciendo sin perder coherencia.

---

# EPIC S2-001

## Validation Pipeline

Hasta ahora los validadores son independientes.

Propongo integrarlos mediante un **Pipeline**.

```text
Markdown

↓

Repository Scanner

↓

Metadata Parser

↓

Knowledge Builder

↓

Knowledge Registry

↓

Validation Pipeline

├── Metadata Rule

├── Identifier Rule

├── Relationship Rule

├── Template Rule

├── Link Rule

├── Semantic Rule

↓

Report Builder

↓

CLI
```

Cada regla será un componente intercambiable.

---

# Clase base

## validation/rules.py

```python
from abc import ABC
from abc import abstractmethod

from pkb.validation.result import ValidationResult


class ValidationRule(ABC):

    name: str

    @abstractmethod
    def validate(self, registry) -> list[ValidationResult]:
        pass
```

Todas las reglas heredarán de esta clase.

---

# Validation Engine

```python
class ValidationEngine:

    def __init__(self):

        self.rules = []

    def add_rule(self, rule):

        self.rules.append(rule)

    def validate(self, registry):

        results = []

        for rule in self.rules:

            results.extend(
                rule.validate(registry)
            )

        return results
```

Esto convierte el sistema en una arquitectura abierta.

Agregar un nuevo validador será tan sencillo como registrar una nueva regla.

---

# Primeras reglas

Propongo desarrollar las siguientes:

```text
MetadataValidationRule

IdentifierValidationRule

DuplicateIdentifierRule

RelationshipValidationRule

BrokenReferenceRule

TemplateValidationRule

LifecycleValidationRule
```

En el futuro podremos añadir otras sin modificar el motor.

---

# Nuevo concepto

## Repository Index

El PKB generará automáticamente un índice completo del repositorio.

Ejemplo:

```text
Repository

Projects

MIPSP

SIMPYME

Editorial

Knowledge Objects

ADR

Standards

Templates

Requirements

Risks

Research

Reports
```

Este índice será la base para la navegación y la generación de documentación.

---

# Segundo concepto

## Knowledge Manifest

Cada proyecto incorporado al PKB tendrá un manifiesto estandarizado.

Ejemplo:

```yaml
project:
  id: MIPSP

name: MIPSP Editor

owner: Miguel Angel

version: 1.0

knowledge_objects:

  requirements: 182

  designs: 61

  adr: 19

  standards: 11

dependencies:

  - PKB Kernel

  - Shared Templates

status: Active
```

Con ello podremos conocer el estado de cualquier proyecto de un vistazo.

---

# Tercer concepto

## Dependency Map

Cada proyecto declarará explícitamente de qué otros activos depende.

```text
MIPSP

↓

Kernel

↓

Standards

↓

Templates

↓

Shared Knowledge

↓

Research
```

Esto permitirá realizar análisis de impacto antes de introducir cambios.

---

# ADR-0013 — Arquitectura basada en capacidades (*Capability-Based Architecture*)

Quiero formalizar una decisión que, en mi opinión, garantizará la evolución del PKB durante años.

> **El desarrollo del PKB se organizará por capacidades funcionales y no por proyectos concretos.**

Las capacidades incluirán, entre otras:

* Gestión del repositorio.
* Gestión de metadatos.
* Validación.
* Inventario.
* Grafo de conocimiento.
* Generación de informes.
* Automatización.
* Integración con IA.

Los proyectos como **MIPSP**, **SIM-PYME**, **Kit Editorial Maestro** o **Condominios** utilizarán estas capacidades, pero no introducirán lógica específica dentro del núcleo de la plataforma.

## Propuesta para la siguiente gran fase: Proyecto piloto MIPSP

Creo que ya hemos alcanzado un nivel de madurez suficiente para dejar de desarrollar el PKB en abstracto. Mi recomendación es que el siguiente gran hito sea la **migración controlada del proyecto MIPSP** al PKB.

Propongo hacerlo como un proyecto piloto con estas etapas:

1. **Inventario del conocimiento existente** (chats, documentos, código y decisiones).
2. **Conversión a Objetos de Conocimiento** siguiendo los estándares del PKB.
3. **Carga en el `KnowledgeRegistry`** y validación automática.
4. **Generación del primer grafo de conocimiento** del proyecto.
5. **Integración con Codex** para asistir en el análisis y evolución del código y la documentación.

Esta fase tendrá una ventaja importante: en lugar de seguir validando la plataforma con ejemplos sintéticos, la probaremos sobre un proyecto real, complejo y de gran volumen. Los ajustes que surjan de esa experiencia fortalecerán el PKB antes de incorporar el resto de tus proyectos. En mi opinión, ése será el paso que consolidará definitivamente la plataforma.
