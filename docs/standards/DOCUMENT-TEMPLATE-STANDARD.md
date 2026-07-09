---
id: PKB-STD-0003
title: Document Template Standard
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: STD
domain: PKB
tags:
  - standard
  - templates
  - documentation
---

# Estándar Institucional de Plantillas

## Propósito
Establecer la estructura mínima y obligatoria que deberán seguir todas las plantillas oficiales del Project Knowledge Base (PKB) para asegurar su homogeneidad y automatización.

---

# Objetivos del Sistema de Plantillas

Toda plantilla desarrollada dentro del ecosistema PKB deberá cumplir con los siguientes objetivos operacionales:
- **Consistencia Editorial**: Mantener una línea gráfica y textual unificada a lo largo de todos los proyectos.
- **Facilidad de Automatización**: Permitir que herramientas automatizadas e inteligencias artificiales parseen la información de forma predecible.
- **Minimización del Esfuerzo**: Reducir la fricción cognitiva al momento de crear un nuevo documento.
- **Preservación de Trazabilidad**: Garantizar que los enlaces y metadatos de control nativos no se rompan.

---

# Estructura Obligatoria del Objeto Plantilla

Todo documento que aspire a ser catalogado como plantilla oficial contendrá de manera mandatoria la siguiente anatomía de 7 bloques:

1. **Encabezado YAML**: Bloque de control semántico indexable.
2. **Título**: Encabezado principal de nivel 1 (`# Title`).
3. **Propósito**: Declaración corta del fin del documento.
4. **Alcance**: Delimitación del contexto de aplicación.
5. **Contenido Principal**: Cuerpo técnico del activo[cite: 3].
6. **Relaciones**: Sección explícita de enlaces cruzados superiores, horizontales y derivados[cite: 3].
7. **Historial de Cambios**: Tabla formal de auditoría de versiones[cite: 3].

### Bloque YAML Base Estándar
```yaml
---
id:
title:
version:
status:
owner:
created:
updated:
type:
domain:
tags:
---