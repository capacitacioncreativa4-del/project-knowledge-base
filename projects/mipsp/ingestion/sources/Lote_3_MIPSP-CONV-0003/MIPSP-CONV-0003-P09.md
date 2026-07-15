---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 9
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente! Continuemos

Excelente. A partir de esta entrega comenzamos el desarrollo del **código fuente real** del **MIPSP-Editor**. Considero importante que el software tenga la misma calidad técnica que la biblioteca documental que producirá. No construiremos un conjunto de scripts; construiremos una **aplicación de ingeniería documental**.

Asimismo, propongo una decisión arquitectónica que considero muy valiosa para la vida útil del proyecto.

---

# Decisión Arquitectónica A-001

## Arquitectura Hexagonal (Ports & Adapters)

El núcleo del sistema **no dependerá de Word, Excel ni PowerPoint**.

La dependencia será exactamente al revés.

```text
                   Usuario
                      │
                      ▼
               Aplicación MIPSP
                      │
              ┌───────┴────────┐
              ▼                ▼
          Núcleo Core      Servicios
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
   DOCX     XLSX     PPTX
 Exporter Exporter Exporter
```

Con esta arquitectura, si en el futuro decidimos generar documentos HTML, Markdown, LaTeX o incluso publicar directamente en una plataforma LMS, no será necesario modificar el núcleo del sistema.

---

# Sprint 1 – Implementación

## Archivo 1

```
core/exceptions.py
```

Este módulo definirá todas las excepciones del sistema.

```python
"""
exceptions.py
==============

Excepciones institucionales del MIPSP-Editor.

Todas las excepciones del sistema deberán derivar de
MIPSPError para facilitar su manejo centralizado.
"""

class MIPSPError(Exception):
    """Clase base para todas las excepciones del sistema."""


class ConfigurationError(MIPSPError):
    """Configuración institucional inválida."""


class MetadataError(MIPSPError):
    """Metadatos incompletos o inconsistentes."""


class InvalidDocumentCode(MIPSPError):
    """Código documental inválido."""


class DuplicateDocumentCode(MIPSPError):
    """Código documental duplicado."""


class ValidationError(MIPSPError):
    """Error durante la validación documental."""


class BrokenReference(MIPSPError):
    """Referencia cruzada inexistente."""


class DocumentExportError(MIPSPError):
    """No fue posible exportar el documento."""


class RegistryError(MIPSPError):
    """Error en el Registro Maestro Documental."""
```

Este módulo rara vez cambiará durante la vida del proyecto.

---

# Archivo 2

```
core/metadata.py
```

Aquí comenzaremos a modelar la **Ficha Técnica Editorial (FTE)**.

```python
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass(slots=True)
class DocumentMetadata:

    code: str

    title: str

    version: str = "1.0"

    status: str = "BORRADOR"

    classification: str = "USO INTERNO"

    author: str = ""

    reviewer: str = ""

    approver: str = ""

    owner: str = "Coordinación Académica"

    issue_date: date | None = None

    review_date: date | None = None

    keywords: list[str] = field(default_factory=list)

    related_documents: list[str] = field(default_factory=list)

    description: str = ""
```

Posteriormente añadiremos:

* UUID
* Firma digital
* Hash SHA256
* Nivel de confidencialidad
* Estado del ciclo documental

---

# Archivo 3

```
core/configuration.py
```

No utilizaremos variables globales.

Todo estará encapsulado.

```python
from dataclasses import dataclass


@dataclass(slots=True)
class Margin:

    top: float

    bottom: float

    left: float

    right: float
```

Después:

```python
@dataclass(slots=True)
class FontConfiguration:

    body: str

    heading: str

    monospace: str
```

Y finalmente:

```python
@dataclass(slots=True)
class DocumentConfiguration:

    language: str

    paper_size: str

    font: FontConfiguration

    margins: Margin
```

Todo el proyecto consultará siempre esta configuración.

Nunca escribiremos:

```python
font = "Calibri"
```

Eso queda completamente prohibido.

---

# Configuración externa

Toda la identidad institucional residirá fuera del código.

Por ejemplo:

```
config/styles.yaml
```

```yaml
fonts:

  body: Aptos

  heading: Aptos Display

  monospace: Cascadia Code

paper:

  size: Letter

margins:

  left: 2.5

  right: 2.5

  top: 2.5

  bottom: 2.5
```

Esto permitirá cambiar la identidad gráfica sin recompilar el proyecto.

---

# Archivo 4

```
core/document.py
```

Todavía no implementaremos DOCX.

Primero construiremos el modelo lógico.

```python
class Document:

    metadata

    sections

    tables

    figures

    annexes

    references
```

El documento no "sabrá" exportarse.

Simplemente representará un documento institucional.

Éste es un principio importante de diseño: **el modelo de dominio no debe depender del formato de salida**.

---

# Archivo 5

```
tests/
```

Desde el primer Sprint incorporaremos pruebas.

Por ejemplo:

```
test_metadata.py

test_configuration.py

test_document.py

test_registry.py
```

El objetivo es que cada módulo nuevo llegue acompañado de pruebas unitarias, de modo que la evolución del proyecto no introduzca regresiones.

---

# Roadmap inmediato

Con el Sprint 1 concluido, la secuencia prevista será:

1. **Sprint 2 – Motor DOCX**: implementación del exportador utilizando `python-docx`, con estilos institucionales, tablas, portadas y secciones.
2. **Sprint 3 – Motor XLSX**: generación de matrices, bancos de reactivos, indicadores y registros mediante `openpyxl`.
3. **Sprint 4 – Motor PPTX**: producción de presentaciones institucionales con `python-pptx`.
4. **Sprint 5 – Publicación PDF**: generación de documentos PDF con `reportlab` y, cuando sea necesario, integración opcional con Microsoft Word para conversión fiel.

## Una mejora que considero estratégica

Aprovechando que estamos construyendo el sistema desde sus cimientos, propongo incorporar desde el inicio una **interfaz de línea de comandos (CLI)** basada en `argparse` o `typer`. Esto permitirá ejecutar tareas como:

```bash
python main.py build CUR-OPS-001
python main.py build --all
python main.py validate
python main.py registry
```

Esta decisión facilitará la automatización futura mediante GitHub Actions, programadores de tareas o procesos de integración continua, permitiendo regenerar toda la biblioteca institucional con un único comando y manteniendo el mismo nivel de control y trazabilidad que hemos perseguido desde el comienzo del proyecto.
