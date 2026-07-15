---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 37
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Continuemos con el proyecto

Excelente. Considero que hemos alcanzado un punto en el que conviene empezar a construir la **infraestructura del repositorio**, no únicamente su documentación.

Hasta ahora hemos definido **qué debe existir**. El siguiente paso es hacer que el propio repositorio **verifique automáticamente** que esos estándares se cumplen.

En un proyecto maduro, la calidad no depende de que alguien recuerde las reglas, sino de que el sistema las valide.

## EPIC S0-005 — Quality Assurance Framework

**Objetivo:** convertir el PKB en un repositorio con control automático de calidad documental.

---

# Incremento 1 — Framework de Validación

## Estructura

```text
tools/
├── README.md
├── validators/
│   ├── __init__.py
│   ├── validate_metadata.py
│   ├── validate_identifiers.py
│   ├── validate_links.py
│   ├── validate_templates.py
│   └── validate_repository.py
│
├── reports/
│   └── .gitkeep
│
└── config/
    ├── metadata_schema.yaml
    ├── identifier_rules.yaml
    └── validation.yaml
```

Esta estructura separa claramente:

* **validadores**
* **configuración**
* **reportes**

---

# Archivo 1

## Ruta

```text
tools/README.md
```

```markdown
# PKB Quality Assurance Framework

## Propósito

Este módulo contiene las herramientas encargadas de validar automáticamente la calidad del Project Knowledge Base.

Los validadores comprueban el cumplimiento de los estándares institucionales antes de aceptar cambios en el repositorio.

---

## Objetivos

- Validar metadatos.
- Verificar identificadores.
- Detectar enlaces rotos.
- Validar plantillas.
- Generar reportes automáticos.
- Facilitar la integración con GitHub Actions.

---

## Componentes

| Herramienta | Función |
|-------------|---------|
| validate_metadata.py | Verifica YAML institucional |
| validate_identifiers.py | Comprueba unicidad y formato |
| validate_links.py | Revisa referencias internas |
| validate_templates.py | Valida estructura documental |
| validate_repository.py | Ejecuta todas las validaciones |

---

## Flujo

Repositorio
↓
Validadores
↓
Reporte
↓
GitHub Actions
↓
Pull Request
```

---

# Archivo 2

## Ruta

```text
tools/config/metadata_schema.yaml
```

```yaml
required:
  - id
  - title
  - version
  - status
  - owner
  - created
  - updated
  - type
  - domain
  - tags

status:
  - Draft
  - Review
  - Approved
  - Published
  - Deprecated
  - Archived

version_pattern: "^[0-9]+\\.[0-9]+\\.[0-9]+$"

date_format: ISO-8601
```

---

# Archivo 3

## Ruta

```text
tools/config/identifier_rules.yaml
```

```yaml
pattern: "^[A-Z]+-[A-Z]+-[0-9]{4}$"

reserved_domains:

  - PKB
  - MIPSP
  - SIMPYME
  - CONDO
  - SHARED

reserved_types:

  - ADR
  - GOV
  - STD
  - TMP
  - REQ
  - EPIC
  - DES
  - PROC
  - REG
  - RSK
  - MET
  - RES
```

---

# Archivo 4

## Ruta

```text
tools/config/validation.yaml
```

```yaml
validation:

  metadata: true

  identifiers: true

  markdown: true

  links: true

  relationships: true

  templates: true

reports:

  output: tools/reports/

fail_on_error: true
```

---

# Archivo 5

## Ruta

```text
tools/validators/__init__.py
```

```python
"""
PKB Validation Framework
"""
```

---

# Commit recomendado

```bash
feat(quality): create validation framework structure
```

---

# Checklist

* [ ] Carpeta `tools` creada.
* [ ] Configuración versionada.
* [ ] Esquemas YAML definidos.
* [ ] Estructura preparada para automatización.
* [ ] Compatible con GitHub Actions.

---

# Decisión arquitectónica: separar motor y reglas

Antes de escribir una sola línea de lógica de validación, propongo una decisión que tendrá un gran impacto en la mantenibilidad del proyecto.

En lugar de codificar reglas como:

```python
if metadata["status"] not in [
    "Draft",
    "Approved",
    ...
]:
```

los validadores **nunca contendrán reglas de negocio**.

Las reglas vivirán exclusivamente en los archivos YAML de `tools/config/`.

El código Python actuará únicamente como un **motor de validación** que interpreta esas reglas.

La arquitectura quedaría así:

```text
Configuración (YAML)
        │
        ▼
Motor de Validación (Python)
        │
        ▼
Reporte
        │
        ▼
GitHub Actions
```

Las ventajas son importantes:

* Cambiar un estándar no requerirá modificar código Python.
* Podrán añadirse nuevos tipos de objetos simplemente actualizando archivos de configuración.
* Será posible versionar las reglas independientemente del motor.
* Más adelante, un agente como Codex podrá generar o modificar reglas automáticamente sin alterar la lógica del sistema.

## Próximo incremento

El siguiente incremento será el primero con **código funcional** del PKB:

* `validate_metadata.py`
* Lectura de documentos Markdown.
* Extracción del encabezado YAML.
* Validación contra `metadata_schema.yaml`.
* Generación de un reporte de errores en formato Markdown.

Con ese componente dejaremos de diseñar la plataforma y comenzaremos a desarrollar su primera capacidad operativa real: la validación automática de la calidad documental. A partir de ese momento, el repositorio empezará a comportarse como un sistema de ingeniería del conocimiento, no solo como una colección de archivos.
