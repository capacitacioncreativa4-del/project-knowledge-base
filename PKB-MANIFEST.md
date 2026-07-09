---
id: PKB-MANIFEST-0001
type: governance
status: draft
version: 0.1.0-alpha
owner: ChatGPT (Architecture) / Miguel (Implementation)
last_update: 2026-07-08
references: [README.md]
---

# PKB-MANIFEST
> Manifiesto de activos e inventario de control de la Base de Conocimientos del Proyecto (PKB).

---

## 1. Control Documental
Este documento registra y valida la existencia, el estado actual y los metadatos de todos los componentes oficiales que conforman el ecosistema del PKB.

| ID Activo | Nombre Archivo | Componente / Ruta | Estado | Versión | Responsable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DOC-0001** | `README.md` | Raíz | `approved` | v0.1.0-alpha | Architecture / Implementation |
| **DOC-0002** | `PKB-MANIFEST.md` | Raíz | `in-review` | v0.1.0-alpha | Architecture / Implementation |
| **DOC-0003** | `VISION.md` | Raíz | `backlog` | v0.0.0 | Architecture |
| **DOC-0004** | `MISSION.md` | Raíz | `backlog` | v0.0.0 | Architecture |
| **DOC-0005** | `CORE-PRINCIPLES.md` | Raíz | `backlog` | v0.0.0 | Architecture |
| **ADR-0001** | `ADR-0001.md` | `registers/decisions/` | `backlog` | v0.0.0 | Architecture |

---

## 2. Mapa de Trazabilidad Cruzada
* El archivo [README.md](README.md) actúa como la puerta de enlace institucional y hace referencia explícita a este Manifiesto.
* Este Manifiesto mapeará de forma incremental las decisiones arquitectónicas (`registers/decisions/`) y las políticas de contribución a medida que sean desplegadas en los próximos incrementos.

---

## 3. Criterios de Validación (Políticas de Calidad)
Para que un nuevo activo sea indexado con éxito en este Manifiesto, debe certificar de manera obligatoria:
- [x] Poseer un encabezado de metadatos estructurado en formato YAML.
- [x] Contar con un identificador único global (`id`).
- [x] Definir explícitamente un propietario del activo (`owner`).
- [x] Declarar la versión vigente utilizando Semantic Versioning.