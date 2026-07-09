---
id: PKB-CONTRIBUTING-0001
type: governance
status: draft
version: 0.1.0-alpha
owner: Tú (Implementation)
last_update: 2026-07-08
references: [README.md, PKB-MANIFEST.md]
---

# Guía de Contribución al PKB

## 1. Flujo de Trabajo (Git Flow)
Para mantener la integridad de la base de conocimientos, se prohíbe realizar commits directos a la rama `main`. Todo cambio debe seguir el siguiente flujo:
1. Crear una rama de tarea a partir de `develop` (ej. `feat/nueva-plantilla` o `docs/actualizacion`).
2. Realizar los commits respetando los estándares semánticos.
3. Abrir un Pull Request (PR) hacia `develop` para su revisión y aprobación.

## 2. Convención de Commits (Conventional Commits)
Los mensajes de commit deben usar estructuras claras para que las herramientas automatizadas puedan generar registros de cambios automáticamente. El formato obligatorio es:

`tipo(alcance): descripción breve en minúsculas`

* **docs**: Cambios exclusivos en la documentación (ej. `docs(readme): update roadmap`).
* **chore**: Tareas de mantenimiento o infraestructura (ej. `chore(repository): initialize structure`).
* **feat**: Adición de nuevas secciones, carpetas o herramientas del sistema.

## 3. Requisitos de un Documento AI-First
Todo archivo Markdown añadido al PKB debe cumplir con:
- Encabezado YAML con metadatos válidos (`id`, `type`, `version`, `status`, `owner`).
- Uso estricto de títulos jerárquicos (`#`, `##`, `###`) sin saltarse niveles.
- Referencias explícitas en la sección de trazabilidad hacia otros documentos relacionados.