---
id: PKB-KERNEL-LIFECYCLE-001
title: Document Lifecycle
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
  - lifecycle
  - workflow
---

# Modelo de Ciclo de Vida Documental

## Propósito
Definir los estados oficiales, las transiciones permitidas y las reglas de aprobación que rigen el ciclo de vida de los Objetos de Conocimiento en el PKB. Este proceso asegura un flujo controlado de ingeniería de la información, desde su concepción inicial hasta su eventual desincorporación o archivo histórico.

---

# Estados del Ciclo de Vida del Objeto de Conocimiento

Todo activo integrado al ecosistema debe reflejar fielmente su madurez técnica mapeando en el metadato `status` de su bloque YAML uno de los siguientes estados controlados, progresando de manera lineal:

```text
Draft (Borrador)
    ↓
Review (En Revisión)
    ↓
Approved (Aprobado)
    ↓
Published (Publicado)
    ↓
Deprecated (Obsoleto)
    ↓
Archived (Archivado)