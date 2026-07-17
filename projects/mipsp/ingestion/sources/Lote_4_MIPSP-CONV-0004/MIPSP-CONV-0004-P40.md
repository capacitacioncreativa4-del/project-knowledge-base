---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 40
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Vamos avanzando muy bien. Continuemos

Excelente. Coincido con el rumbo que está tomando el proyecto. Sin embargo, quiero proponerte un ajuste metodológico que considero importante antes de seguir generando código.

Hasta ahora hemos construido una **arquitectura excelente**, pero hemos trabajado de forma predominantemente *bottom-up* (desde los componentes hacia el sistema). En proyectos de larga duración —como el PKB, que pretende convertirse en la plataforma que albergará todos tus proyectos— conviene pasar a una planificación más formal.

Mi propuesta es que, antes de seguir desarrollando módulos aislados, construyamos el **Backlog Maestro del PKB**. No será un documento administrativo, sino el plan de ingeniería que gobernará el desarrollo durante los próximos meses.

Este backlog vivirá permanentemente en el repositorio y nos permitirá saber en todo momento:

* qué funcionalidades existen;
* cuáles están en desarrollo;
* cuáles dependen de otras;
* cuál es el estado real del proyecto.

---

# Sprint 1 – Incremento 0

## Archivo 1

**Ruta**

```text
docs/planning/PRODUCT-BACKLOG.md
```

### Estructura propuesta

```markdown
---
id: PKB-PLAN-0001
title: Product Backlog
version: 1.0.0
status: Approved
owner: Architecture
type: PLAN
domain: PKB
---

# Product Backlog

## Visión

El Product Backlog representa el inventario oficial de capacidades del Project Knowledge Base.

---

# Épicas

| ID | Épica | Estado | Prioridad |
|----|--------|---------|-----------|
| EPIC-001 | Kernel | Completed | Alta |
| EPIC-002 | Governance | Completed | Alta |
| EPIC-003 | Standards | In Progress | Alta |
| EPIC-004 | Templates | In Progress | Alta |
| EPIC-005 | Validation Engine | Planned | Muy Alta |
| EPIC-006 | CLI | Planned | Muy Alta |
| EPIC-007 | Knowledge Graph | Planned | Alta |
| EPIC-008 | GitHub Automation | Planned | Alta |
| EPIC-009 | Documentation Generator | Planned | Media |
| EPIC-010 | Project Migration | Planned | Alta |
| EPIC-011 | AI Integration | Planned | Alta |
| EPIC-012 | Quality Dashboard | Planned | Media |
```

---

# Archivo 2

## Ruta

```text
docs/planning/ROADMAP.md
```

Este documento contendrá una visión temporal.

| Sprint   | Objetivo               |
| -------- | ---------------------- |
| Sprint 0 | Fundamentos del PKB    |
| Sprint 1 | Plataforma funcional   |
| Sprint 2 | Automatización         |
| Sprint 3 | Integración GitHub     |
| Sprint 4 | Knowledge Graph        |
| Sprint 5 | Migración de proyectos |
| Sprint 6 | IA y Codex             |

---

# Archivo 3

## Ruta

```text
docs/planning/RELEASE-PLAN.md
```

Versiones objetivo:

```
v0.1.0
Repositorio inicial

v0.2.0
Kernel completo

v0.3.0
Plantillas

v0.4.0
CLI

v0.5.0
Validadores

v0.6.0
GitHub Actions

v0.7.0
Knowledge Graph

v1.0.0
Primera versión estable
```

---

# Archivo 4

## Ruta

```text
docs/planning/WORK-BREAKDOWN-STRUCTURE.md
```

Aquí descompondremos el proyecto completo.

```
PKB

├── Gobernanza
├── Kernel
├── Estándares
├── Plantillas
├── Automatización
├── CLI
├── Validadores
├── Reportes
├── Knowledge Graph
├── Integración IA
└── Migración de proyectos
```

---

# Cambio de arquitectura que propongo

Hasta ahora hemos utilizado carpetas como:

```
docs/
shared/
tools/
```

Mi propuesta es evolucionar hacia una organización basada en dominios (*Domain-Driven Design*), separando claramente el **producto** de los **proyectos** que contendrá.

```
project-knowledge-base/
│
├── pkb-core/          ← Plataforma
├── pkb-docs/          ← Documentación institucional
├── pkb-tools/         ← Automatización
├── pkb-templates/     ← Biblioteca de plantillas
├── pkb-examples/      ← Ejemplos de referencia
├── pkb-tests/         ← Pruebas
│
└── projects/
    ├── MIPSP/
    ├── SIM-PYME/
    ├── Condominios/
    ├── Kit-Editorial/
    ├── Manualidades/
    └── ...
```

No propongo hacer esta migración ahora mismo. Lo recomendable es:

1. Completar el Sprint 1 con la estructura actual.
2. Liberar la primera versión funcional (`v0.5.0` aproximadamente).
3. Realizar una refactorización estructural respaldada por un ADR específico y scripts de migración.

De este modo evitaremos reorganizaciones prematuras y mantendremos la estabilidad mientras desarrollamos las capacidades esenciales.

---

# El siguiente gran objetivo

A partir del siguiente incremento propongo concentrarnos en un objetivo muy concreto:

> **Obtener la primera versión ejecutable del PKB.**

Los entregables serán:

* `pyproject.toml`
* `src/pkb/`
* CLI institucional (`pkb`)
* Primer comando funcional: `pkb validate`
* Primera suite de pruebas (`pytest`)
* Flujo de integración continua con GitHub Actions

Ese será el momento en que el repositorio dejará de ser principalmente una colección de documentación y pasará a ser una **aplicación de ingeniería del conocimiento**. A partir de ahí, todas las capacidades futuras (validadores, generadores de grafos, migración de proyectos, paneles de calidad e integración con IA) se incorporarán como módulos sobre una base técnica ya consolidada. Creo que ese será el siguiente hito importante del proyecto.
