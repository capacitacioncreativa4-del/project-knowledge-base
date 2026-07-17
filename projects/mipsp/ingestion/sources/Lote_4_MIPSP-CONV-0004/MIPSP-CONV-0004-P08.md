---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 8
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Genial. Comencemos con la primera épica

De acuerdo. A partir de este momento cambiaremos la dinámica de trabajo. Dejaremos de hablar sobre el PKB y comenzaremos a **producir sus activos**.

Hay una decisión de ingeniería documental que considero importante tomar antes de escribir el primer archivo.

## DEC-0001 — El PKB será un producto

No construiremos una simple carpeta con documentos.

Construiremos un **producto documental**.

Eso implica que el PKB tendrá:

* arquitectura;
* versiones;
* roadmap;
* backlog;
* releases;
* métricas;
* control de calidad;
* gobierno documental.

En otras palabras, administraremos el conocimiento con el mismo rigor con el que se administra un proyecto de software.

Creo que esa decisión marcará una diferencia importante a medida que el repositorio crezca.

---

# EPIC-PKB-001

## Fundación del Repositorio

**Objetivo**

Construir la infraestructura documental permanente sobre la que se apoyarán todos los proyectos futuros.

---

## Alcance

Esta épica producirá los siguientes activos:

| ID      | Documento              | Estado esperado |
| ------- | ---------------------- | --------------- |
| PKB-001 | README Maestro         | Approved        |
| PKB-002 | INDEX Maestro          | Approved        |
| PKB-003 | Arquitectura del PKB   | Approved        |
| PKB-004 | Gobierno Documental    | Approved        |
| PKB-005 | Convenciones           | Approved        |
| PKB-006 | Plantillas             | Approved        |
| PKB-007 | Inventario Maestro     | Approved        |
| PKB-008 | Registro de Decisiones | Approved        |
| PKB-009 | Registro de Riesgos    | Approved        |
| PKB-010 | Registro de Ideas      | Approved        |
| PKB-011 | Roadmap                | Approved        |
| PKB-012 | ChangeLog              | Approved        |

---

# Una mejora arquitectónica

Después de revisar todo lo que hemos diseñado, propongo una mejora que suele aparecer en repositorios maduros, pero que es más fácil incorporar desde el principio.

Separar claramente el **conocimiento estable** del **conocimiento operativo**.

Quedaría así:

```text
PKB
│
├── 00_Governance
├── 01_Projects
├── 02_Shared_Knowledge
├── 03_Operations
├── 04_Templates
├── 05_Research
├── 06_History
└── 99_System
```

¿Por qué?

Porque un repositorio crece en dos direcciones distintas:

* documentos permanentes;
* trabajo diario.

Si ambos se mezclan, el mantenimiento se vuelve más difícil.

---

# ¿Qué contendrá cada carpeta?

## 00_Governance

Toda la gobernanza.

Nunca dependerá de un proyecto.

Ejemplo:

```text
Vision

Mission

Principles

Policies

Standards

Taxonomy

Naming

ADR

Glossary
```

---

## 01_Projects

Aquí vivirán:

```text
MIPSP

KitEditorial

Condominios

SIM-PYME

Manualidades

...
```

Cada uno completamente independiente.

---

## 02_Shared_Knowledge

Biblioteca común.

Ejemplos:

* patrones
* normas
* componentes
* metodologías
* diagramas
* bibliografía
* checklists
* buenas prácticas

---

## 03_Operations

Esta carpeta administrará el trabajo.

Aquí estarán:

* backlog
* roadmap
* sprint
* migraciones
* métricas
* calidad
* inventario

Es decir, la operación del PKB.

---

## 04_Templates

Plantillas maestras.

No versiones particulares.

Ejemplos:

* Requisito
* EPIC
* ADR
* Caso de Uso
* Manual
* API
* Arquitectura
* Investigación

---

## 05_Research

Investigaciones.

Normatividad.

Comparativos.

Benchmarking.

Estudios técnicos.

---

## 06_History

Histórico.

Versiones anteriores.

Chats resumidos.

Ideas descartadas.

---

## 99_System

Información técnica del propio PKB.

Por ejemplo:

* configuración
* scripts
* automatizaciones
* integración con Git
* integración con Codex

---

# Arquitectura documental

Creo que ya estamos listos para definir el modelo de documento que utilizará absolutamente todo el repositorio.

Todos los documentos heredarán la misma estructura:

1. Encabezado (identificación y metadatos).
2. Propósito.
3. Alcance.
4. Contexto.
5. Contenido principal.
6. Relaciones con otros activos.
7. Historial de cambios.
8. Estado y versión.

Con esa homogeneidad podremos automatizar validaciones, búsquedas y generación de índices.

---

# Mi propuesta para el siguiente ciclo

Hasta ahora hemos definido la arquitectura. El siguiente paso ya no es seguir diseñando, sino **materializar** el repositorio.

Propongo que el siguiente conjunto de entregables sea el primero que genere físicamente y que sirva como base para todos los demás:

1. `README.md` (documento rector del PKB).
2. `INDEX.md` (índice maestro navegable).
3. `TAXONOMY.md` (taxonomía oficial).
4. `NAMING-STANDARD.md` (convenciones de nombres).
5. `DOCUMENT-STANDARD.md` (estructura obligatoria de todos los documentos).
6. `DECISION-REGISTER.xlsx` (registro maestro de decisiones).
7. `KNOWLEDGE-INVENTORY.xlsx` (inventario maestro de activos).
8. `ROADMAP.md` (plan de evolución del PKB).

## Una recomendación adicional

Dado el volumen de documentación que ya estamos planificando, recomiendo que el PKB no se limite a Markdown. Propongo un enfoque híbrido:

* **Markdown (`.md`)** para documentación técnica, requisitos, arquitectura, ADR y manuales.
* **Excel (`.xlsx`)** para inventarios, matrices de trazabilidad, registros de decisiones, riesgos, backlog y métricas.
* **Diagramas** (por ejemplo, Mermaid o Draw.io) para la arquitectura y los flujos.
* **Git** como sistema de control de versiones.

Ese conjunto proporciona una base muy sólida: Markdown facilita la revisión y el versionado, Excel es excelente para gestionar registros y matrices, y Git mantiene el historial completo. Además, es un formato con el que tanto ChatGPT como Codex pueden trabajar de manera eficaz.

A partir de la siguiente iteración, mi objetivo será que cada respuesta produzca un pequeño conjunto de activos completos, listos para incorporarse directamente al repositorio, de modo que el PKB crezca de forma incremental y permanezca siempre en un estado utilizable.
