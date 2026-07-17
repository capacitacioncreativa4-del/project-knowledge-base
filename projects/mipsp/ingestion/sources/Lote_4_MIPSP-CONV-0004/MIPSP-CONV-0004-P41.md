---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 41
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Avancemos con lo siguiente

Excelente. Considero que ya tenemos suficiente arquitectura definida. A partir de este momento quiero cambiar el enfoque del proyecto hacia un criterio que utilizan los equipos de plataformas de ingeniería más maduros:

> **Cada incremento debe producir software ejecutable y verificable.**

Eso significa que, a partir de ahora, cada Sprint terminará con una versión del PKB que podrás ejecutar en tu computadora.

---

# Sprint 1 — Incremento 1

## Objetivo

Construir la **primera versión ejecutable del PKB**.

Al finalizar este incremento podrás instalar el proyecto localmente y ejecutar:

```bash
pkb --help
```

y

```bash
pkb validate
```

aunque inicialmente solo realicen validaciones básicas.

---

# Entregable 1 — pyproject.toml

## Ruta

```text
pyproject.toml
```

Contenido propuesto:

```toml
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-knowledge-base"
version = "0.1.0"
description = "Project Knowledge Base Platform"
readme = "README.md"
requires-python = ">=3.11"

authors = [
    { name = "Miguel Angel" }
]

dependencies = [
    "PyYAML>=6.0",
    "rich>=13.0",
    "networkx>=3.4",
    "click>=8.1"
]

[project.scripts]
pkb = "pkb.cli:main"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

# Entregable 2

## Nueva estructura

```text
src/
└── pkb/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── version.py
    │
    ├── validators/
    ├── graph/
    ├── metadata/
    ├── templates/
    ├── reports/
    ├── repository/
    └── utils/
```

---

# Entregable 3

## src/pkb/version.py

```python
VERSION = "0.1.0"
```

---

# Entregable 4

## src/pkb/**init**.py

```python
from .version import VERSION

__version__ = VERSION
```

---

# Entregable 5

## src/pkb/**main**.py

```python
from .cli import main

if __name__ == "__main__":
    main()
```

---

# Entregable 6

## src/pkb/cli.py

```python
import argparse

from pkb.version import VERSION


def cmd_validate(args):
    print("PKB Validation Engine")
    print("Versión:", VERSION)
    print("Estado: operativo")


def cmd_version(args):
    print(VERSION)


def build_parser():

    parser = argparse.ArgumentParser(
        prog="pkb",
        description="Project Knowledge Base"
    )

    parser.add_argument(
        "--version",
        action="store_true"
    )

    sub = parser.add_subparsers(dest="command")

    validate = sub.add_parser(
        "validate",
        help="Ejecuta los validadores"
    )

    validate.set_defaults(func=cmd_validate)

    return parser


def main():

    parser = build_parser()

    args = parser.parse_args()

    if args.version:
        cmd_version(args)
        return

    if hasattr(args, "func"):
        args.func(args)
        return

    parser.print_help()
```

---

# Resultado esperado

Después de instalar el proyecto:

```bash
pip install -e .
```

podrás ejecutar:

```bash
pkb --help
```

Resultado:

```text
usage: pkb [-h] [--version] {validate}

Project Knowledge Base

commands:

validate
```

Y:

```bash
pkb validate
```

Resultado:

```text
PKB Validation Engine

Versión 0.1.0

Estado: operativo
```

---

# Entregable 7

## tests/test_cli.py

```python
from pkb.version import VERSION


def test_version():

    assert VERSION == "0.1.0"
```

---

# Entregable 8

## Primera integración continua

**Ruta**

```text
.github/workflows/ci.yml
```

```yaml
name: PKB CI

on:

  push:

  pull_request:

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - run: pip install -e .

      - run: pip install pytest

      - run: pytest
```

---

# Commit recomendado

```bash
feat(core): bootstrap executable PKB platform
```

---

# Criterios de aceptación

Al finalizar este incremento deberás poder ejecutar correctamente:

```bash
python -m pkb
```

```bash
pkb --help
```

```bash
pkb --version
```

```bash
pkb validate
```

```bash
pytest
```

y el flujo de GitHub Actions deberá ejecutarse sin errores.

---

# Propuesta para la siguiente etapa: Sprint 1 — Incremento 2

A partir de aquí propongo reorganizar el desarrollo en torno a un **núcleo de servicios**, en lugar de scripts independientes.

La arquitectura evolucionaría hacia componentes con responsabilidades bien definidas:

```text
src/pkb/
├── core/          # Configuración, logging y excepciones
├── repository/    # Descubrimiento y lectura del repositorio
├── metadata/      # Parseo y validación de YAML
├── validators/    # Reglas de validación
├── reporting/     # Generación de informes
├── cli/           # Comandos de la línea de comandos
└── graph/         # Construcción del grafo de conocimiento
```

Con esta organización, el comando:

```bash
pkb validate
```

dejará de ser un ejemplo y pasará a ejecutar realmente el flujo completo:

1. Descubrir documentos del repositorio.
2. Extraer metadatos.
3. Validar contra los estándares institucionales.
4. Generar un informe en `tools/reports/`.
5. Devolver un código de salida apropiado para GitHub Actions.

Ese será el primer ciclo funcional completo del PKB y marcará el inicio de la plataforma como una aplicación de software plenamente operativa.
