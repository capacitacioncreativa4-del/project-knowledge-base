---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 8
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece perfecto. Continúa con lo que sigue

Excelente. A partir de esta entrega comenzamos el desarrollo del **MIPSP-Editor**, el segundo gran producto del proyecto. Si el MIPSP es el patrimonio documental, el MIPSP-Editor será la herramienta que permitirá producirlo, mantenerlo y evolucionarlo de forma controlada.

Propongo que el desarrollo del software siga un ciclo similar al de un proyecto profesional de ingeniería: arquitectura → núcleo → pruebas → generadores → integración.

---

# MIPSP-Editor v1.0

## Sprint 1 — Núcleo del Sistema (Core)

### Objetivo

Construir un núcleo completamente independiente de Word, Excel o PowerPoint. El núcleo conocerá únicamente el **modelo documental**, mientras que los módulos de exportación se encargarán de convertirlo en archivos físicos.

La dependencia entre componentes será:

```text
                main.py
                   │
                   ▼
             Application
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
   Configuration Metadata  Registry
        │          │          │
        └──────────┼──────────┘
                   ▼
              Document Model
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
 DOCX Exporter XLSX Exporter PPTX Exporter
```

---

# Estructura inicial

```text
mipsp-editor/
│
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
│
├── core/
│   ├── __init__.py
│   ├── configuration.py
│   ├── metadata.py
│   ├── document.py
│   ├── numbering.py
│   ├── registry.py
│   ├── validation.py
│   └── exceptions.py
│
├── config/
│   ├── config.yaml
│   ├── styles.yaml
│   └── metadata.yaml
│
└── tests/
```

---

# Módulo 1 — configuration.py

Este módulo centralizará toda la configuración institucional.

En lugar de escribir:

```python
font = "Calibri"
```

el código consultará siempre la configuración.

Ejemplo:

```python
cfg.document.font.body
```

Esto permitirá cambiar la identidad editorial sin modificar el programa.

La clase principal será:

```python
from dataclasses import dataclass

@dataclass(slots=True)
class DocumentConfig:
    language: str
    paper_size: str
    body_font: str
    heading_font: str
    margins: dict
```

Y existirá una clase superior:

```python
@dataclass(slots=True)
class Configuration:
    organization: str
    version: str
    document: DocumentConfig
```

---

# Módulo 2 — metadata.py

Aquí se modelará la Ficha Técnica Editorial (FTE).

```python
DocumentMetadata
```

Campos principales:

```text
Código

Título

Versión

Estado

Clasificación

Autor

Revisor

Aprobador

Fecha de emisión

Fecha de revisión

Palabras clave

Documentos relacionados
```

No será un diccionario libre, sino una clase fuertemente tipada.

---

# Módulo 3 — numbering.py

Este módulo generará automáticamente códigos documentales.

Ejemplo:

```text
CUR-OPS-001-D01
```

o

```text
ETS-CUR001-MOD03-SES02
```

La interfaz será sencilla:

```python
NumberingService.next_document()

NumberingService.next_figure()

NumberingService.next_table()

NumberingService.next_annex()
```

Toda la numeración quedará concentrada en un único componente.

---

# Módulo 4 — document.py

Éste será probablemente el archivo más importante de todo el proyecto.

Contendrá la clase base:

```python
class Document:
```

Atributos:

```text
metadata

sections

tables

figures

annexes

references
```

Métodos:

```python
add_section()

add_table()

add_figure()

add_annex()

validate()

export()
```

Todos los documentos heredarán de esta clase.

---

# Módulo 5 — registry.py

Este módulo mantendrá el Registro Maestro Documental.

Permitirá responder preguntas como:

* ¿Qué documentos existen?
* ¿Cuál es la versión vigente?
* ¿Quién aprobó el documento?
* ¿Qué documentos dependen de otro?
* ¿Qué cursos utilizan un mismo procedimiento?

Internamente administrará un catálogo único.

---

# Módulo 6 — validation.py

Antes de exportar cualquier archivo se ejecutarán validaciones automáticas.

Ejemplos:

✔ Código válido.

✔ Versión válida.

✔ Autor definido.

✔ Clasificación definida.

✔ Sin referencias rotas.

✔ Sin tablas vacías.

✔ Sin anexos duplicados.

✔ Sin códigos repetidos.

Esto reducirá errores de producción.

---

# Módulo 7 — exceptions.py

En lugar de errores genéricos utilizaremos excepciones específicas.

Por ejemplo:

```python
InvalidDocumentCode

MissingMetadata

DuplicatedDocument

BrokenReference

ConfigurationError
```

Esto facilitará el diagnóstico y el mantenimiento.

---

# Estándares de desarrollo

Desde el primer módulo aplicaremos criterios propios de un proyecto profesional:

* **Python 3.12+** como versión objetivo.
* Tipado estático con `typing`.
* `dataclasses` con `slots=True` para eficiencia y claridad.
* Documentación mediante *docstrings* compatibles con Sphinx.
* Pruebas unitarias desde el inicio.
* Separación estricta entre el modelo de datos y los exportadores.
* Dependencias mínimas y bien definidas.

## Próximo hito

La siguiente entrega iniciará la implementación efectiva del **Sprint 1** con el código fuente de los módulos `configuration.py`, `metadata.py` y `exceptions.py`. Estos componentes constituirán la base sobre la que se apoyará todo el ecosistema del **MIPSP-Editor**. A partir de ese momento, cada entrega incorporará código ejecutable, documentado y listo para integrarse en un repositorio Git, avanzando de forma incremental hasta disponer de un generador editorial completo para la biblioteca institucional del MIPSP.
