---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 38
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Continuemos el proyecto

Excelente. A partir de este incremento comenzamos una transición importante: **del diseño de la arquitectura a la implementación del PKB**.

Hasta ahora hemos construido la especificación. A partir de este momento comenzaremos a desarrollar la **primera herramienta oficial del repositorio**.

Mi objetivo es que todo el código que produzcamos pueda ejecutarse directamente desde tu repositorio GitHub sin necesidad de reescribirlo.

---

# Sprint 0 – EPIC S0-005

## Incremento 2 — Primer Validador Funcional

## Objetivo

Desarrollar el primer componente operativo del PKB:

> **Validador institucional de metadatos YAML**

Este programa recorrerá automáticamente el repositorio, localizará documentos Markdown, extraerá su encabezado YAML y verificará que cumpla el estándar institucional.

---

# Arquitectura

```text
Repositorio PKB
        │
        ▼
Buscar archivos *.md
        │
        ▼
Extraer bloque YAML
        │
        ▼
Leer metadata_schema.yaml
        │
        ▼
Validar
        │
        ▼
Generar reporte Markdown
        │
        ▼
Código de salida
```

---

# Archivo

Ruta

```text
tools/validators/validate_metadata.py
```

---

```python
"""
PKB Metadata Validator
Version: 1.0.0

Valida los encabezados YAML de todos los documentos Markdown del repositorio.
"""

from pathlib import Path
import yaml
import re

ROOT = Path(__file__).resolve().parents[2]

SCHEMA = ROOT / "tools" / "config" / "metadata_schema.yaml"

REQUIRED = []
STATUS = []
VERSION_PATTERN = ""

with open(SCHEMA, encoding="utf-8") as f:
    config = yaml.safe_load(f)

REQUIRED = config["required"]
STATUS = config["status"]
VERSION_PATTERN = re.compile(config["version_pattern"])


def extract_yaml(text: str):
    """
    Extrae el bloque YAML inicial.
    """

    if not text.startswith("---"):
        return None

    parts = text.split("---", 2)

    if len(parts) < 3:
        return None

    return yaml.safe_load(parts[1])


def validate(document: Path):

    errors = []

    content = document.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    metadata = extract_yaml(content)

    if metadata is None:
        return ["No se encontró encabezado YAML."]

    for field in REQUIRED:

        if field not in metadata:
            errors.append(f"Campo obligatorio ausente: {field}")

    if "status" in metadata:

        if metadata["status"] not in STATUS:
            errors.append(
                f"Estado inválido: {metadata['status']}"
            )

    if "version" in metadata:

        if not VERSION_PATTERN.match(str(metadata["version"])):
            errors.append(
                f"Versión inválida: {metadata['version']}"
            )

    return errors


def markdown_documents():

    excluded = {
        ".git",
        ".github",
        ".venv",
        "__pycache__"
    }

    for path in ROOT.rglob("*.md"):

        if any(part in excluded for part in path.parts):
            continue

        yield path


def main():

    report = []

    total = 0
    failures = 0

    for doc in markdown_documents():

        total += 1

        errors = validate(doc)

        if errors:

            failures += 1

            report.append(f"# {doc.relative_to(ROOT)}")

            for e in errors:
                report.append(f"- {e}")

            report.append("")

    report_file = ROOT / "tools" / "reports" / "metadata-report.md"

    report_file.write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    print("=" * 60)
    print("PKB Metadata Validation")
    print("=" * 60)
    print(f"Documentos revisados : {total}")
    print(f"Con errores          : {failures}")
    print(f"Reporte              : {report_file}")
    print("=" * 60)

    return failures


if __name__ == "__main__":

    raise SystemExit(main())
```

---

# Archivo

Ruta

```text
tools/reports/metadata-report.md
```

Este archivo será generado automáticamente.

Ejemplo:

```
# docs/governance/VISION.md

- Campo obligatorio ausente: updated

# docs/kernel/METADATA-MODEL.md

- Estado inválido: approved

# shared/templates/package-governance/README.md

- Versión inválida: v1
```

---

# Archivo

Ruta

```text
requirements.txt
```

```text
PyYAML>=6.0
```

---

# Ejecución

Desde la raíz del repositorio:

```bash
python tools/validators/validate_metadata.py
```

---

# Commit recomendado

```bash
feat(validation): implement metadata validator
```

---

# Criterios de aceptación

* [ ] Recorre todo el repositorio.
* [ ] Ignora carpetas excluidas.
* [ ] Extrae correctamente el YAML.
* [ ] Detecta campos obligatorios ausentes.
* [ ] Valida el estado documental.
* [ ] Valida la versión semántica.
* [ ] Genera un informe en Markdown.
* [ ] Devuelve un código de salida distinto de cero cuando existen errores (ideal para CI).

---

# Revisión de arquitectura: hacia un PKB "self-healing"

Quiero proponerte una evolución que considero uno de los mayores diferenciadores del proyecto.

Hasta ahora los validadores solo detectan errores. Mi propuesta es introducir una segunda fase: **asistentes de corrección**.

La arquitectura evolucionaría así:

```text
Repositorio
     │
     ▼
Validadores
     │
     ▼
Diagnóstico
     │
     ├──────────────┐
     ▼              ▼
Reporte        Correctores
                    │
                    ▼
Pull Request sugerido
                    │
                    ▼
Revisión humana
```

Esto implica separar claramente dos responsabilidades:

* **Validadores**: nunca modifican documentos; únicamente detectan incumplimientos y generan diagnósticos reproducibles.
* **Correctores (Fixers)**: proponen cambios automáticos, como añadir un campo `updated` faltante, normalizar un identificador, corregir un valor de `status` o insertar secciones obligatorias. Estos cambios siempre se presentarían para revisión antes de integrarse.

Más adelante podremos implementar estos correctores con Python y complementarlos con agentes como Codex para generar propuestas de refactorización documental más sofisticadas. De esta forma, el PKB no solo detectará desviaciones respecto a los estándares, sino que ayudará activamente a mantener la calidad del conocimiento almacenado. Ese será un paso importante hacia un repositorio con capacidades de mantenimiento asistido.
