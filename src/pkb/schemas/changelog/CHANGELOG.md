# Changelog — Project Knowledge Base (PKB)

Todos los cambios notables en este proyecto serán documentados en este archivo bajo los lineamientos de [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.1.0-beta] — 2026-07-14
### Added
- **Core Architecture:** Diseño base de 7 capas del núcleo funcional (`schemas`, `ontology`, `graph`, `validation`, `ingestion`, `templates`, `registry`).
- **Contracts (YAML):** Esquemas iniciales de validación para `ADR`, `Requirement`, `Conversation`, `KnowledgePackage` y `EngineeringSession`.
- **Registry:** Registro maestro de entidades oficiales (`OBJECT-REGISTRY.yaml`), política de identificadores de 6 dígitos (`IDENTIFIER-POLICY.md`) y prefijos (`PREFIXES.md`).

### Changed
- **Strategy Shift:** Transición metodológica oficial de un flujo basado en chats a un modelo de ingeniería basado en *Releases Físicas Estables*.
- **Project Routing:** Los proyectos de conocimiento (ej. `projects/mipsp/`) ahora se configuran y orquestan desde el interior del núcleo del PKB.