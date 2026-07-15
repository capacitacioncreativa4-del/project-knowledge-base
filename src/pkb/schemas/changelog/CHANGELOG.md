# Changelog — Project Knowledge Base (PKB)

Todos los cambios notables en este proyecto serán documentados en este archivo bajo los lineamientos de [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.3.4] — 2026-07-15
### Added
- **EPIC-01 CAP-03 (Baseline S - Schema Repository):** Estructuración dual de los contratos sintácticos del sistema[cite: 2].
- **Requirement Entity Package:** Creación coordinada de la especificación conceptual (`Specification.md`) y el contrato Json-Schema (`Schema.yaml`)[cite: 2].
- **Requirement Complete Assets:** Integración de `Example.yaml`, `Lifecycle.md` y `Validation.md` para cerrar la estructura pentagonal de la entidad[cite: 2].

## [0.3.4] — 2026-07-15
### Added
- [cite_start]**EPIC-01 CAP-03 (Baseline S - Schema Repository):** Estructuración dual de los contratos sintácticos del sistema .
- [cite_start]**Requirement Entity Package:** Creación coordinada de la especificación conceptual (`Specification.md`) y el contrato Json-Schema (`Schema.yaml`) para la entidad de requerimientos .

## [0.3.2] — 2026-07-15
### Added
- [cite_start]**EPIC-01 CAP-01/CAP-02 (Baseline A - Architecture):** Culminación y congelación formal del modelo de arquitectura técnica bajo el estándar C4 [cite: 361-364].
- [cite_start]**C4 Level 3 Components:** Lanzamiento de `ARCH-003-Component.md` definiendo interacciones de procesamiento interno.
- [cite_start]**C4 Level 4 Code Organization:** Creación de `ARCH-004-Code-Organization.md` con el mapeo estructural del repositorio físico.

## [0.3.1] — 2026-07-15
### Added
- [cite_start]**EPIC-01 CAP-01 (Governance Baseline):** Despliegue del marco normativo institucional del PKB .
- [cite_start]**Platform Specification:** Creación de `PKB-SPEC-001-Platform-Specification.md` para delimitar las 8 capacidades del sistema[cite: 438].
- [cite_start]**Object Lifecycle:** Implementación de `PKB-LIFECYCLE-001-Object-Lifecycle.md` y su contrato automatizado `object_lifecycle.yaml` [cite: 335-365, 439].
- [cite_start]**Functional Catalog:** Estructuración de `PKB-CAPABILITY-CATALOG.md` para el rastreo de procesos de conocimiento [cite: 384-400, 440].
- [cite_start]**Governance Policy:** Lanzamiento de `PKB-GOVERNANCE-POLICY.md` regulando la inmutabilidad estructural y roles de aprobación .

## [0.3.0] — 2026-07-15
### Added
- **Constitución del PKB (I01):** Publicación del documento base `PKB-CONSTITUTION-001.md` y `DEFINITION-OF-DONE.md`.
- **Arquitectura de Capas (I02):** Implementación de `ARCH-001-System-Context.md` y decisión de arquitectura en `ADR-000001-Adopt-Dual-Representation.md`.
- **CLI Core (I03):** Creación del motor de comandos unificado en Python (`src/pkb/cli/main.py`).
- **Ingesta Masiva (I04):** Integración de comandos CLI con el motor de extracción para procesar los Lotes 1 al 4 de manera masiva.

## [0.2.0] — 2026-07-14
### Added
- **Pipeline Governance (I01):** Despliegue de `PKB-SPEC-003` y esquema para `System`.
- **Prompt Framework (I02):** Creación de `PKB-SPEC-004` y contrato de validación para `Artifact`.
- **Core Processing (I03):** Lógica del procesador en Python (`processor.py`) y esquema para `SystemModule`.
- **Assembler Engine (I04):** Módulo de ensamblaje en Python (`assembler.py`) y esquema de `KnowledgePackage`.
- **Pilot Test (I05):** Script de ejecución piloto del pipeline (`test_pipeline.py`).
- **Release Documentation (I06):** Notas de versión oficiales de la entrega `0.2.0`.

## [0.1.0] — 2026-07-14
### Added
- **Core Foundation (I01):** Lanzamiento de `PKB-SPEC-001` (Especificación Normativa) y `PKB-ENGINEERING-HANDBOOK.md`.
- **Entity Schemas (I02):** Catálogo de 11 esquemas YAML de entidades completado.
- **Relation Schemas (I03):** Contratos de aristas (`relation-types.yaml`) y axiomas ontológicos en `METAMODEL-ONTOLOGY.md`.
- **Registry & Lifecycle (I04):** Máquina de estados lógicos oficializada en `LIFECYCLE-POLICY.yaml`.
- **Templates (I05):** Plantillas YAML listas para instanciación.
- **Validation (I06):** Motor de validación sintáctica en Python (`engine.py`).
- **MIPSP Pilot (I07):** Tres objetos reales integrados con el nuevo modelo.
- **Release Documentation (I08):** Notas de versión oficiales de la entrega `0.1.0`.