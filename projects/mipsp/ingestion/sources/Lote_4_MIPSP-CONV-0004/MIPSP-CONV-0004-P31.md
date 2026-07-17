---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 31
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Prosigamos

Excelente. Con el cierre del **Incremento 2**, considero que el PKB ya tiene una identidad institucional. Ahora entramos en una etapa distinta: **definir el modelo conceptual del sistema**.

Desde este momento, dejaremos de pensar en "documentos" y comenzaremos a pensar en **objetos de conocimiento**, porque esa será la base que permitirá automatizar el PKB, construir índices, validar relaciones y, en el futuro, integrar agentes de IA de forma consistente.

---

# Sprint 0 – Incremento 3

## EPIC S0-003 — PKB Kernel

### Documento 1 de 6

**Ruta**

```text
docs/kernel/METADATA-MODEL.md
```

---

````markdown
---
id: PKB-KERNEL-METADATA-001
title: Metadata Model
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
type: Kernel
parent: PKB-KERNEL-MANIFEST-001
---

# Modelo de Metadatos del Project Knowledge Base

## Propósito

Definir el conjunto mínimo y obligatorio de metadatos que deberán acompañar a todos los activos del Project Knowledge Base (PKB), con independencia de su tipo.

El objetivo es garantizar:

- Identificación única.
- Trazabilidad.
- Versionado.
- Descubrimiento.
- Automatización.
- Interoperabilidad.

---

# Principios

Los metadatos deberán ser:

- Obligatorios.
- Legibles por personas.
- Procesables por herramientas.
- Compatibles con Markdown y YAML.
- Estables a largo plazo.

---

# Encabezado YAML institucional

Todo documento comenzará con un bloque YAML.

Ejemplo:

```yaml
---
id: PKB-GOV-VISION-001
title: Vision
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: Governance
domain: PKB
parent: PKB-KERNEL-MANIFEST-001
tags:
  - governance
  - strategy
  - vision
---
```

---

# Metadatos obligatorios

| Campo | Obligatorio | Descripción |
|---------|:----------:|-------------|
| id | Sí | Identificador único y permanente. |
| title | Sí | Nombre oficial del activo. |
| version | Sí | Versión semántica. |
| status | Sí | Estado del activo. |
| owner | Sí | Responsable del activo. |
| created | Sí | Fecha de creación. |
| updated | Sí | Última actualización. |
| type | Sí | Tipo de objeto documental. |
| domain | Sí | Dominio de conocimiento. |
| parent | Sí* | Objeto del cual depende (cuando aplique). |
| tags | Sí | Etiquetas normalizadas. |

---

# Metadatos recomendados

Según el tipo de objeto podrán incorporarse:

- author
- reviewers
- approvers
- contributors
- project
- epic
- sprint
- priority
- classification
- confidentiality
- language
- references
- dependencies
- replaces
- supersedes
- related
- aliases

---

# Estados oficiales

Todo activo deberá encontrarse en uno de los siguientes estados:

| Estado | Descripción |
|----------|-------------|
| Draft | En elaboración. |
| Review | En revisión. |
| Approved | Aprobado. |
| Published | Publicado oficialmente. |
| Deprecated | Obsoleto pero vigente históricamente. |
| Archived | Retirado del uso activo. |

---

# Versionado

Se adopta Semantic Versioning.

Ejemplos:

- 1.0.0
- 1.1.0
- 1.2.0
- 2.0.0

Reglas:

- MAJOR → Cambios incompatibles.
- MINOR → Nuevas capacidades.
- PATCH → Correcciones.

---

# Convenciones

## Fechas

ISO 8601

Ejemplo:

2026-07-09

---

## Idioma

Los documentos institucionales del PKB se redactarán preferentemente en español.

Cuando un documento esté en otro idioma deberá indicarse mediante:

language: en

---

## Tags

Las etiquetas deberán:

- utilizar minúsculas;
- evitar espacios;
- utilizar guiones cuando sea necesario.

Ejemplo:

```yaml
tags:
  - governance
  - architecture
  - metadata
```

---

# Validaciones mínimas

Un documento será considerado válido cuando:

- contenga todos los metadatos obligatorios;
- el identificador sea único;
- la versión sea válida;
- el estado pertenezca al catálogo oficial;
- las fechas tengan formato ISO 8601;
- los enlaces internos existan.

---

# Relaciones

## Documento superior

- PKB-MANIFEST.md

## Documentos relacionados

- KNOWLEDGE-OBJECT-MODEL.md
- IDENTIFIER-STANDARD.md
- TRACEABILITY-MODEL.md

## Documentos derivados

- VALIDATION-RULES.md
- DOCUMENT-TEMPLATE.md
- YAML-STANDARD.md

---

# Historial de cambios

| Versión | Fecha | Descripción |
|----------|------------|----------------|
| 1.0.0 | 2026-07-09 | Primera versión institucional del modelo de metadatos. |
````

---

# Justificación arquitectónica

Este documento convierte los metadatos en un **contrato institucional**.

A partir de ahora, ningún activo ingresará al PKB sin cumplir este modelo. Esto permitirá que, en fases posteriores, podamos:

* generar índices automáticamente;
* validar consistencia mediante scripts;
* crear grafos de conocimiento;
* realizar búsquedas estructuradas;
* alimentar asistentes de IA con contexto fiable.

---

# Commit recomendado

```bash
docs(kernel): define institutional metadata model
```

---

# Checklist de aceptación

* [ ] Guardado en `docs/kernel/METADATA-MODEL.md`.
* [ ] Encabezado YAML conforme al estándar.
* [ ] Catálogo de estados definido.
* [ ] Metadatos obligatorios y recomendados documentados.
* [ ] Relaciones e historial incluidos.

---

# Decisión de arquitectura: un ajuste que fortalecerá el PKB

Quisiera introducir una mejora antes de seguir con el **Knowledge Object Model**.

En la mayoría de los repositorios documentales, el campo `type` contiene valores libres (`Governance`, `Kernel`, `ADR`, etc.). Eso funciona al principio, pero con cientos de documentos termina generando inconsistencias.

Propongo formalizar un **vocabulario controlado** para los metadatos. Por ejemplo:

| Campo            | Catálogo oficial                                              |
| ---------------- | ------------------------------------------------------------- |
| `status`         | Draft, Review, Approved, Published, Deprecated, Archived      |
| `type`           | ADR, GOV, KNO, STD, TMP, REG, RES, EPIC, REQ, MANIFEST, GUIDE |
| `domain`         | PKB, MIPSP, SIM-PYME, Condominios, Manualidades, Shared       |
| `classification` | Public, Internal, Confidential                                |

Con esta decisión, los metadatos dejarán de ser texto libre y se convertirán en datos normalizados. Esa normalización facilitará enormemente la automatización, la validación y el análisis del repositorio cuando incorporemos **Codex** y los flujos de **GitHub Actions**. En mi opinión, esta será una de las decisiones que más contribuirá a la calidad y escalabilidad del PKB a largo plazo.
