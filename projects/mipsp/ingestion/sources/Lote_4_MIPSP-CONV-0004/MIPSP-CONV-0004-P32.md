---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 32
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Continuemos con el proyecto

Excelente. Hemos llegado al punto donde, desde mi perspectiva como arquitecto del PKB, comienza la verdadera ingeniería del conocimiento.

Quiero hacer una observación antes de continuar.

Hasta ahora hemos definido **cómo se gobierna** el PKB. A partir de este momento definiremos **qué entidades existen dentro del PKB**.

Esta diferencia es enorme.

Un documento ya no será simplemente un archivo Markdown.

Será un **Objeto de Conocimiento**.

Eso significa que, en el futuro, podremos construir:

* índices automáticos;
* grafos de conocimiento;
* consultas por tipo de objeto;
* navegación semántica;
* agentes de IA especializados.

En otras palabras, estaremos construyendo una pequeña base de conocimiento sobre Git.

---

# Sprint 0 – Incremento 3

## Documento 2 de 6

Ruta

```text
docs/kernel/KNOWLEDGE-OBJECT-MODEL.md
```

---

````markdown
---
id: PKB-KERNEL-KOM-001
title: Knowledge Object Model
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: KERNEL
domain: PKB
parent: PKB-KERNEL-MANIFEST-001
tags:
  - kernel
  - knowledge
  - model
---

# Modelo de Objetos de Conocimiento

## Propósito

Definir el modelo conceptual mediante el cual el Project Knowledge Base representa todo el conocimiento institucional.

En el PKB el conocimiento se organiza mediante Objetos de Conocimiento (Knowledge Objects), cada uno con identidad, metadatos, relaciones y ciclo de vida propios.

---

# Definición

Un Objeto de Conocimiento es la unidad mínima de información gobernada por el PKB.

Todo objeto posee:

- identidad permanente;
- metadatos;
- contenido;
- relaciones;
- historial;
- estado;
- responsable.

---

# Modelo Conceptual

```text
Knowledge Object
│
├── Identity
├── Metadata
├── Content
├── Relationships
├── Lifecycle
├── Version
├── Owner
└── History
```

---

# Catálogo Institucional de Objetos

## ADR

Architecture Decision Record

Documenta decisiones arquitectónicas.

Ejemplos:

- ADR-0001
- ADR-0002

---

## GOV

Gobierno

Define políticas institucionales.

Ejemplos:

- Vision
- Mission
- Manifest

---

## STD

Standard

Normas técnicas.

Ejemplos:

- Metadata Model
- Naming Standard

---

## TMP

Template

Plantillas oficiales.

---

## KNO

Knowledge Object

Conocimiento reutilizable independiente de proyectos.

Ejemplos:

- Mecánica de Fluidos
- Python
- Marketing Digital

---

## EPIC

Agrupación funcional de trabajo.

---

## REQ

Requisito.

---

## DES

Diseño.

---

## PROC

Procedimiento.

---

## REG

Registro institucional.

---

## RSK

Riesgo.

---

## MET

Métrica.

---

## RES

Investigación.

---

## REF

Referencia documental.

---

# Relaciones Permitidas

Los objetos podrán relacionarse mediante:

- Parent
- Child
- Depends On
- Related To
- Implements
- References
- Supersedes
- Replaces
- Derived From

---

# Propiedades Obligatorias

Todo objeto deberá poseer:

- ID
- Tipo
- Versión
- Estado
- Propietario
- Dominio
- Fecha de creación
- Fecha de actualización

---

# Ciclo de Vida

```text
Draft
    ↓
Review
    ↓
Approved
    ↓
Published
    ↓
Deprecated
    ↓
Archived
```

---

# Principios

## Un objeto = una responsabilidad

Cada objeto representa un único concepto claramente definido.

---

## Identidad permanente

El identificador nunca cambia.

---

## Versionado independiente

Cada objeto evoluciona de forma autónoma.

---

## Relaciones explícitas

Toda dependencia deberá documentarse.

---

## Reutilización

Los objetos deberán diseñarse para ser utilizados por múltiples proyectos.

---

# Ejemplo

```text
REQ-001
│
├── depende de ADR-0001
├── implementado por DES-004
├── relacionado con STD-002
└── utilizado por Proyecto MIPSP
```

---

# Relaciones

## Documento superior

- PKB-KERNEL-MANIFEST.md

## Documentos relacionados

- METADATA-MODEL.md
- IDENTIFIER-STANDARD.md
- TRACEABILITY-MODEL.md

## Documentos derivados

- OBJECT-CATALOG.md
- RELATIONSHIP-STANDARD.md

---

# Historial de Cambios

| Versión | Fecha | Descripción |
|----------|------------|-----------------------------|
|1.0.0|2026-07-09|Primera versión institucional.|
````

---

# Justificación arquitectónica

Este documento representa un cambio de paradigma.

Hasta ahora el repositorio era, conceptualmente, un conjunto de carpetas y archivos. Con el **Knowledge Object Model**, pasa a ser un sistema compuesto por entidades con identidad propia, relaciones explícitas y un ciclo de vida definido.

Esta abstracción nos permitirá construir herramientas que operen sobre el conocimiento en lugar de hacerlo sobre los archivos físicos.

---

# Commit recomendado

```bash
docs(kernel): define institutional knowledge object model
```

---

# Checklist de aceptación

* [ ] Archivo ubicado en `docs/kernel/KNOWLEDGE-OBJECT-MODEL.md`.
* [ ] Catálogo inicial de objetos definido.
* [ ] Relaciones permitidas documentadas.
* [ ] Ciclo de vida consistente con `METADATA-MODEL.md`.
* [ ] Metadatos YAML conformes al estándar.

---

# Una mejora arquitectónica para el siguiente documento

Quiero proponerte una evolución respecto al plan original.

Inicialmente habíamos previsto redactar el **IDENTIFIER-STANDARD**. Sin embargo, tras consolidar el modelo de objetos, considero más conveniente separar el problema en dos niveles:

1. **IDENTIFIER-SCHEME.md**: define la sintaxis y las reglas de construcción de los identificadores (prefijos, secuencias, dominios, unicidad, persistencia).
2. **IDENTIFIER-REGISTRY.md**: establece cómo se administran y reservan esos identificadores dentro del PKB.

Esta separación sigue un principio de ingeniería de software: **separar la especificación del mecanismo de gestión**. Con ello evitaremos que el estándar de identificadores dependa de la forma en que se administran los registros y dejaremos abierta la posibilidad de automatizar el registro más adelante mediante GitHub Actions o Codex, sin modificar el estándar base.

Creo que esta pequeña decisión hará que el Kernel sea más limpio, más extensible y mucho más fácil de mantener conforme el PKB crezca.
