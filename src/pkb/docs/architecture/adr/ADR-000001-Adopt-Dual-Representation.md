# ADR-000001: Adopt Dual Representation (Human and Machine Readable)

## Estado
PROPUESTO

## Contexto
El PKB necesita ser comprensible tanto para personas (auditores, instructores, directores) como para herramientas automatizadas (compiladores, validadores, motores de búsqueda semántica).

## Decisión
Adoptar de manera universal el principio de dualidad:
1. Toda entidad de conocimiento (ADR, Requirement, Standard) poseerá una versión en Markdown (`.md`) para el consumo humano.
2. Paralelamente, poseerá una representación JSON/YAML estructurada (`.yaml`) para el procesamiento de herramientas de software.

## Consecuencias
* **Positivas:** Facilita la automatización de análisis semántico, validación de esquemas y generación automática de índices.
* **Negativas:** Requiere un proceso de sincronización estricto que será gestionado por el motor de automatización.