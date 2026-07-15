---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 7
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente idea, la apruebo. Continúa con el proyecto.

Excelente. Apruebo también ese cambio de enfoque porque, desde el punto de vista de ingeniería de software, es la evolución natural del proyecto.

A partir de este momento el proyecto tendrá **dos productos institucionales** que evolucionarán en paralelo:

1. **MIPSP (Biblioteca Editorial)**: los documentos técnicos, manuales, cursos y formatos.
2. **MIPSP-Editor (Motor Editorial)**: el software que genera esa biblioteca de forma reproducible.

Esto convierte al proyecto en un sistema mantenible y auditable. En lugar de editar cientos de archivos manualmente, el contenido se modelará como datos y el motor editorial producirá los documentos normalizados.

## Nueva arquitectura del proyecto

Propongo organizar el repositorio del motor editorial así:

```text
mipsp-editor/
│
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── main.py
├── config/
├── core/
├── builders/
├── exporters/
├── templates/
├── assets/
├── data/
├── tests/
├── output/
└── docs/
```

### `core/`

Será el núcleo reutilizable.

```
core/
    document.py
    metadata.py
    styles.py
    numbering.py
    registry.py
    validation.py
    configuration.py
```

Todo el sistema dependerá de este módulo.

---

### `builders/`

Cada tipo documental tendrá un constructor específico.

```
builders/

course_builder.py

manual_builder.py

ets_builder.py

procedure_builder.py

form_builder.py

presentation_builder.py

workbook_builder.py
```

Cada constructor conocerá únicamente la estructura lógica del documento.

---

### `exporters/`

Aquí se encapsularán las bibliotecas externas.

```
exporters/

docx_exporter.py

xlsx_exporter.py

pptx_exporter.py

pdf_exporter.py
```

De esta forma, si en el futuro cambiamos de biblioteca, el resto del código permanecerá intacto.

---

## Modelo orientado a objetos

No construiremos documentos mediante funciones aisladas.

Utilizaremos clases.

Ejemplo:

```python
class Document:
    pass

class Course(Document):
    pass

class Manual(Document):
    pass

class Procedure(Document):
    pass

class Form(Document):
    pass

class Workbook(Document):
    pass
```

Todos heredarán comportamiento común:

* metadatos;
* historial de versiones;
* encabezados;
* codificación;
* referencias;
* exportación.

---

## Configuración declarativa

Evitaremos "codificar" valores en el programa.

Toda la identidad institucional residirá en archivos de configuración (`YAML` o `JSON`), por ejemplo:

```yaml
organization:
  name: MIPSP
  version: 1.0

document:
  language: es-MX
  paper: Letter
  font:
    body: Aptos
    heading: Aptos Display
```

Cambiar la tipografía o el formato de papel implicará modificar la configuración, no el código.

---

## Primera línea de desarrollo

El motor editorial se desarrollará en este orden:

### Sprint 1 — Núcleo

* `configuration.py`
* `metadata.py`
* `styles.py`
* `numbering.py`
* `document.py`

### Sprint 2 — Exportación Word

* `docx_exporter.py`
* `word_styles.py`
* `sections.py`
* `tables.py`

### Sprint 3 — Exportación Excel

* matrices;
* bancos de reactivos;
* trazabilidad;
* indicadores.

### Sprint 4 — PowerPoint

* plantilla institucional;
* diapositivas maestras;
* módulos de contenido.

### Sprint 5 — PDF

* generación mediante ReportLab;
* portada;
* índice;
* anexos.

---

# Control de calidad del software

Aplicaremos al código el mismo rigor que a la documentación.

Cada módulo incluirá:

* documentación técnica;
* tipado (`type hints`);
* pruebas unitarias;
* validaciones;
* registro de errores;
* convenciones de estilo (PEP 8);
* separación clara entre lógica de negocio y exportación.

---

# La siguiente fase

La siguiente entrega ya no será un documento del curso, sino el inicio del **código fuente del MIPSP-Editor**. Comenzaremos con el **Sprint 1**, desarrollando el núcleo (`core`) que servirá de base para todos los generadores posteriores.

Este será el primer paso para que el MIPSP disponga no solo de una biblioteca documental, sino también de una plataforma de producción editorial capaz de regenerar, versionar y mantener toda la colección de forma consistente durante su ciclo de vida.
