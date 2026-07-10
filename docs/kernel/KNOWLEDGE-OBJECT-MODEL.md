---
id: PKB-KERNEL-OBJMODEL-001
title: Knowledge Object Model
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
type: Kernel
parent: PKB-KERNEL-MANIFEST-001
updated: '2026-07-09'
domain: Kernel
tags:
- pkb
- kernel
- kernel
---
# Modelo de Objetos de Conocimiento (Knowledge Object Model)

## Propósito
Definir de forma explícita el Catálogo de Objetos de Conocimiento del PKB, estableciendo su taxonomía, esquemas de contenido estructural y el propósito operativo de cada tipo de activo para posibilitar búsquedas relacionales y la automatización mediante agentes de IA.

---

# Catálogo de Objetos de Conocimiento (Vocabulario de Tipos)

Todos los activos del Project Knowledge Base deben mapearse e identificarse con exactitud utilizando alguno de los siguientes tipos normalizados[cite: 3]:

### 1. ADR (Architecture Decision Record)
- **Propósito**: Registrar de manera inmutable las decisiones técnicas y arquitectónicas del sistema, justificando el contexto, las alternativas evaluadas y sus consecuencias[cite: 3].
- **Ubicación típica**: `docs/architecture/` o `registers/decisions/`.

### 2. REQ (Requirement)
- **Propósito**: Especificar requisitos funcionales y no funcionales detallados de los sistemas o del propio repositorio[cite: 3].
- **Ubicación típica**: `docs/requirements/`.

### 3. EPIC (Epic)
- **Propósito**: Agrupar bloques funcionales y estratégicos de alto nivel organizados en el tiempo[cite: 3].
- **Ubicación típica**: Planificaciones e índices maestros del Kernel.

### 4. STD (Standard)
- **Propósito**: Normar estándares operativos, convenciones de codificación, guías estilísticas y pautas de formateo técnico[cite: 3].
- **Ubicación típica**: `docs/standards/`.

### 5. GOV (Governance)
- **Propósito**: Albergar los activos de control estratégico, visión, misión y las políticas institucionales del ecosistema[cite: 3].
- **Ubicación típica**: `docs/governance/`.

### 6. TMP (Template)
- **Propósito**: Servir como la biblioteca de plantillas oficiales reutilizables para garantizar la homogeneidad documental del sistema[cite: 3].
- **Ubicación típica**: `docs/templates/`.

### 7. RSK (Risk)
- **Propósito**: Identificar, analizar y documentar los riesgos arquitectónicos, técnicos u operativos junto con sus respectivas mitigaciones[cite: 3].
- **Ubicación típica**: `registers/risks/`.

### 8. MET (Metric)
- **Propósito**: Compilar métricas, indicadores clave de rendimiento (KPIs) y analíticas de calidad documental del repositorio[cite: 3].
- **Ubicación típica**: `registers/metrics/`.

### 9. RES (Research)
- **Propósito**: Contener documentos de investigación avanzada, análisis técnico de viabilidad, experimentos arquitectónicos y descubrimientos exploratorios[cite: 3].
- **Ubicación típica**: `docs/research/`.

### 10. KNO (Knowledge Object)
- **Propósito**: Servir como activos de conocimiento reutilizable general, explicaciones contextuales o bibliotecas comunes extrapolables a múltiples iniciativas[cite: 3].
- **Ubicación típica**: `docs/knowledge/`.

---

# Anatomía Estructural Obligatoria

Cada objeto de conocimiento, sin importar su tipo, se compone estrictamente de las siguientes capas o bloques físicos:
1. **Bloque de Control (Metadata YAML)**: Delimitado por `---`, con los metadatos obligatorios y el tipo mapeado del vocabulario controlado.
2. **Bloque de Propósito**: Un encabezado `## Propósito` que describe la intencionalidad clara y directa del documento.
3. **Bloque de Contenido Central**: Secciones de desarrollo de ingeniería libre o estructurada de acuerdo a su respectiva plantilla.
4. **Bloque de Relaciones**: Mapeo explícito con hipervínculos funcionales hacia sus documentos superiores, relacionados y derivados.
5. **Bloque de Control de Cambios**: Tabla formal que registra de manera auditable las versiones semánticas del activo.

---

# Relaciones

## Documento superior
- [PKB-MANIFEST.md](PKB-MANIFEST.md)

## Documentos relacionados
- [METADATA-MODEL.md](METADATA-MODEL.md)
- IDENTIFIER-STANDARD.md
- TRACEABILITY-MODEL.md

---

# Historial de cambios
| Versión | Fecha | Descripción |
|----------|------------|----------------|
| 1.0.0 | 2026-07-09 | Primera versión institucional del Modelo de Objetos de Conocimiento. |