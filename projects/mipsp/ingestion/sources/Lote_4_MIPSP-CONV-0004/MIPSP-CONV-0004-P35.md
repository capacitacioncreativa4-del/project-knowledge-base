---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 35
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente! Prosigamos con la estandarización de plantillas

Excelente. Creo que éste es el momento adecuado para introducir una decisión que, en mi experiencia, marcará una diferencia enorme en el crecimiento del PKB.

## DEC-0009 — Separación entre Modelo y Plantillas

Quiero evitar un error muy común en muchos repositorios documentales: mezclar las **reglas** con las **plantillas**.

En el PKB vamos a separarlas completamente.

```text
Kernel
│
├── Define QUÉ es un documento
│
Standards
│
├── Define CÓMO debe construirse
│
Templates
│
└── Implementan ese estándar
```

Esta separación permitirá cambiar una plantilla sin modificar el estándar, o evolucionar el estándar sin tener que rehacer inmediatamente todas las plantillas.

Considero que esta decisión nos dará mucha flexibilidad a largo plazo.

---

# Comienza la EPIC S0-004

## Estandarización de Plantillas

En mi opinión, ésta será una de las épicas más reutilizadas de todo el PKB.

No estará ligada a un proyecto específico.

Servirá para:

* MIPSP
* Kit Editorial Maestro
* Condominios
* SIM-PYME
* Manualidades
* futuros proyectos

---

# Objetivo

Crear un **Sistema Institucional de Plantillas (Institutional Template System)**.

No construiremos documentos.

Construiremos una **fábrica de documentos**.

---

# Arquitectura propuesta

```text
shared/
└── templates/
    │
    ├── governance/
    ├── architecture/
    ├── kernel/
    ├── standards/
    ├── projects/
    ├── requirements/
    ├── research/
    ├── reports/
    ├── registers/
    ├── meetings/
    ├── diagrams/
    └── assets/
```

Esta estructura es suficientemente amplia para cubrir prácticamente cualquier proyecto que incorporemos al PKB.

---

# Catálogo Institucional de Plantillas v1.0

Propongo comenzar con un conjunto reducido pero muy sólido.

| Código  | Plantilla               | Estado   |
| ------- | ----------------------- | -------- |
| TMP-001 | Documento Institucional | Sprint 0 |
| TMP-002 | ADR                     | Sprint 0 |
| TMP-003 | Estándar                | Sprint 0 |
| TMP-004 | Requisito               | Sprint 1 |
| TMP-005 | Investigación           | Sprint 1 |
| TMP-006 | Proyecto                | Sprint 1 |
| TMP-007 | Acta de reunión         | Sprint 2 |
| TMP-008 | Registro de riesgos     | Sprint 2 |
| TMP-009 | Informe técnico         | Sprint 2 |
| TMP-010 | Caso de uso             | Sprint 2 |

---

# Primer documento de la EPIC

## Ruta

```text
docs/standards/DOCUMENT-TEMPLATE-STANDARD.md
```

---

````markdown
---
id: PKB-STD-0003
title: Document Template Standard
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: STD
domain: PKB
tags:
  - standard
  - templates
  - documentation
---

# Estándar Institucional de Plantillas

## Propósito

Establecer la estructura mínima obligatoria que deberán seguir todas las plantillas oficiales del Project Knowledge Base.

---

# Objetivos

Toda plantilla deberá:

- mantener consistencia editorial;
- facilitar la automatización;
- minimizar el esfuerzo de creación;
- preservar la trazabilidad.

---

# Estructura Obligatoria

Toda plantilla oficial contendrá, como mínimo:

1. Encabezado YAML
2. Título
3. Propósito
4. Alcance
5. Contenido principal
6. Relaciones
7. Historial de cambios

---

# Encabezado YAML

```yaml
---
id:
title:
version:
status:
owner:
created:
updated:
type:
domain:
tags:
---
```

---

# Convenciones

## Encabezados

Utilizar exclusivamente encabezados Markdown.

---

## Tablas

Preferentemente Markdown.

---

## Diagramas

Mermaid cuando sea posible.

---

## Identificadores

Conforme a IDENTIFIER-SCHEME.md.

---

## Relaciones

Todo documento deberá indicar:

### Documento superior

### Relacionados

### Derivados

---

# Calidad mínima

Antes de publicarse una plantilla deberá verificarse:

- sintaxis Markdown;
- YAML válido;
- relaciones completas;
- identificadores válidos;
- enlaces internos.

---

# Versionado

Las plantillas evolucionarán mediante Semantic Versioning.

---

# Relaciones

Documento superior:

- PKB-MANIFEST.md

Relacionados:

- METADATA-MODEL.md
- IDENTIFIER-SCHEME.md
- TRACEABILITY-MODEL.md

---

# Historial

| Versión | Fecha | Descripción |
|----------|------------|----------------|
|1.0.0|2026-07-09|Primera versión institucional.|
````

---

# Commit recomendado

```bash
docs(standards): establish institutional document template standard
```

---

# Checklist

* [ ] Documento incorporado.
* [ ] Referenciado desde el Manifest.
* [ ] Compatible con el Metadata Model.
* [ ] Compatible con Identifier Scheme.
* [ ] Compatible con Traceability Model.

---

# Una evolución que considero estratégica

Quiero proponerte una mejora que no estaba en el plan original y que, en mi opinión, elevará el PKB a un nivel profesional.

## Introducir "Template Packages"

En lugar de gestionar plantillas como archivos individuales, las agruparemos en **paquetes coherentes**.

Por ejemplo:

```text
shared/
└── templates/
    ├── package-governance/
    │   ├── README.md
    │   ├── GOVERNANCE-TEMPLATE.md
    │   ├── ADR-TEMPLATE.md
    │   ├── POLICY-TEMPLATE.md
    │   └── CHECKLIST.md
    │
    ├── package-project/
    │   ├── README.md
    │   ├── PROJECT-CHARTER.md
    │   ├── EPIC.md
    │   ├── REQUIREMENT.md
    │   └── ROADMAP.md
    │
    └── package-research/
        ├── README.md
        ├── RESEARCH.md
        ├── SOURCE-LOG.md
        ├── BIBLIOGRAPHY.md
        └── REVIEW.md
```

Cada paquete incluirá:

* las plantillas;
* una guía de uso;
* ejemplos;
* un checklist de calidad;
* dependencias con otros estándares.

## Mi recomendación

Creo que esta decisión será una de las más rentables del proyecto. En lugar de mantener decenas de plantillas aisladas, administraremos **bibliotecas reutilizables**. Cuando migremos proyectos como **MIPSP**, **SIM-PYME** o el **Kit Editorial Maestro**, bastará con seleccionar el paquete adecuado y el proyecto nacerá ya alineado con los estándares del PKB, reduciendo significativamente el esfuerzo de documentación y asegurando consistencia desde el primer día.
