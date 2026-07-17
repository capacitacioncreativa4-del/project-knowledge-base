---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 42
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante. Continuemos

Excelente. A partir de este punto propongo elevar el nivel de ingeniería del proyecto. En lugar de seguir desarrollando por archivos, comenzaremos a construir el PKB siguiendo una arquitectura por capas, inspirada en principios de *Clean Architecture* y *Domain-Driven Design*. Esto hará que el proyecto sea escalable cuando incorporemos el MIPSP, SIM-PYME, el Kit Editorial Maestro y los demás proyectos.

## Sprint 1 – Incremento 2

### Objetivo

Transformar el comando `pkb validate` en un flujo de trabajo real mediante la separación de responsabilidades.

---

# Arquitectura objetivo

```text
src/
└── pkb/
    ├── cli/
    │   ├── __init__.py
    │   ├── main.py
    │   └── commands/
    │       ├── validate.py
    │       ├── doctor.py
    │       └── inventory.py
    │
    ├── core/
    │   ├── config.py
    │   ├── exceptions.py
    │   └── logging.py
    │
    ├── repository/
    │   ├── scanner.py
    │   └── filesystem.py
    │
    ├── metadata/
    │   ├── parser.py
    │   ├── schema.py
    │   └── models.py
    │
    ├── validators/
    │   ├── metadata_validator.py
    │   ├── identifier_validator.py
    │   └── validation_result.py
    │
    ├── reporting/
    │   ├── markdown_report.py
    │   └── console_report.py
    │
    └── graph/
```

Esta estructura evita dependencias circulares y facilita el crecimiento del proyecto.

---

# Primer flujo funcional

El comando:

```bash
pkb validate
```

ejecutará internamente la siguiente cadena:

```text
CLI
 │
 ▼
Repository Scanner
 │
 ▼
Markdown Parser
 │
 ▼
YAML Metadata Parser
 │
 ▼
Metadata Validator
 │
 ▼
Validation Result
 │
 ▼
Markdown Report
 │
 ▼
Console Report
```

Cada componente tendrá una única responsabilidad.

---

# Archivo 1

## `src/pkb/repository/scanner.py`

```python
from pathlib import Path
from typing import Iterator

EXCLUDED = {
    ".git",
    ".github",
    ".venv",
    "__pycache__",
    ".pytest_cache",
}


class RepositoryScanner:
    """Localiza documentos Markdown dentro del repositorio."""

    def __init__(self, root: Path):
        self.root = root

    def markdown_files(self) -> Iterator[Path]:
        for path in self.root.rglob("*.md"):
            if any(part in EXCLUDED for part in path.parts):
                continue
            yield path
```

---

# Archivo 2

## `src/pkb/metadata/parser.py`

```python
import yaml


class MetadataParser:

    @staticmethod
    def extract(text: str):

        if not text.startswith("---"):
            return None

        parts = text.split("---", 2)

        if len(parts) < 3:
            return None

        return yaml.safe_load(parts[1])
```

---

# Archivo 3

## `src/pkb/validators/validation_result.py`

```python
from dataclasses import dataclass, field


@dataclass
class ValidationResult:

    document: str

    errors: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    @property
    def success(self):

        return len(self.errors) == 0
```

---

# Archivo 4

## `src/pkb/reporting/console_report.py`

```python
from rich.console import Console

console = Console()


def summary(results):

    total = len(results)

    failures = sum(not r.success for r in results)

    console.rule("PKB Validation")

    console.print(f"Documentos : {total}")

    console.print(f"Errores    : {failures}")

    console.rule()
```

---

# Archivo 5

## `src/pkb/cli/commands/validate.py`

```python
from pathlib import Path

from pkb.repository.scanner import RepositoryScanner
from pkb.reporting.console_report import summary


def execute():

    scanner = RepositoryScanner(Path.cwd())

    files = list(scanner.markdown_files())

    summary([])
    
    print(f"{len(files)} documentos encontrados.")
```

Este archivo sustituirá progresivamente la lógica experimental que escribimos en el Sprint 0.

---

# Refactorización prevista

Una vez integrado este incremento, el antiguo script:

```text
tools/validators/validate_metadata.py
```

no desaparecerá inmediatamente.

Su contenido se migrará gradualmente hacia:

```text
src/pkb/
```

hasta que:

```bash
pkb validate
```

sea el único punto de entrada oficial.

Esta transición reduce el riesgo y mantiene compatibilidad durante el desarrollo.

---

# Pruebas automatizadas

Añadiremos las primeras pruebas unitarias para los componentes desacoplados.

## `tests/test_repository_scanner.py`

```python
from pathlib import Path

from pkb.repository.scanner import RepositoryScanner


def test_scanner_returns_iterator():

    scanner = RepositoryScanner(Path("."))

    assert scanner.markdown_files() is not None
```

## `tests/test_metadata_parser.py`

```python
from pkb.metadata.parser import MetadataParser


def test_extract_none():

    assert MetadataParser.extract("# Documento") is None
```

Estas pruebas son sencillas, pero establecen la disciplina de incorporar pruebas desde el inicio.

---

# ADR-0010 — Adoptar una arquitectura basada en servicios

Propongo registrar una nueva decisión arquitectónica:

> **Toda funcionalidad del PKB deberá implementarse como un servicio desacoplado, invocado desde la CLI y probado de forma independiente.**

Esto implica varias reglas:

1. La CLI no contendrá lógica de negocio.
2. Los validadores no accederán directamente al sistema de archivos.
3. Los generadores de informes no conocerán los detalles de validación.
4. Los componentes se comunicarán mediante modelos de datos bien definidos (`ValidationResult`, `Metadata`, `KnowledgeObject`, etc.).

Con esta decisión, el PKB podrá evolucionar hacia una aplicación mantenible y extensible.

## Hito alcanzado

Con este incremento habremos establecido la base para que el desarrollo futuro sea incremental y seguro. A partir del siguiente ciclo podremos implementar capacidades completas —como el validador de identificadores, el inventario del repositorio y el generador del grafo de conocimiento— reutilizando esta infraestructura, sin necesidad de rediseñar la arquitectura en cada nueva funcionalidad. Esto marcará el paso definitivo de un repositorio documental a una plataforma de software orientada a la gestión del conocimiento.
