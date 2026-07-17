---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 18
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece perfecto. Continuemos

Perfecto. A partir de esta entrega comenzamos la **implementación propiamente dicha**. Mantendremos la disciplina de un proyecto de ingeniería: cada sprint producirá componentes completos, reutilizables y probados. Dejaremos de ampliar la arquitectura salvo cuando sea estrictamente necesario.

## SPRINT 01 — Infraestructura del repositorio

**Objetivo:** disponer de un repositorio Python profesional, listo para comenzar el desarrollo del compilador editorial.

### Entregable 1.1 — Estructura definitiva del proyecto

Propongo adoptar desde el inicio esta estructura, que considero suficientemente robusta para soportar la evolución del MIPSP durante muchos años:

```text
mipsp-editor/
│
├── pyproject.toml
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── .editorconfig
├── requirements-dev.txt
│
├── src/
│   └── mipsp/
│       ├── __init__.py
│       ├── application/
│       ├── builders/
│       ├── cli/
│       ├── compiler/
│       ├── core/
│       ├── domain/
│       ├── exporters/
│       ├── infrastructure/
│       ├── mdsl/
│       ├── services/
│       ├── shared/
│       └── templates/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── regression/
│   └── fixtures/
│
├── docs/
│   ├── architecture/
│   ├── adr/
│   ├── api/
│   ├── user-guide/
│   └── developer-guide/
│
├── examples/
│
├── assets/
│   ├── logos/
│   ├── icons/
│   ├── fonts/
│   └── images/
│
├── output/
└── scripts/
```

Esta estructura diferencia claramente el código fuente, la documentación técnica, las pruebas y los recursos gráficos.

---

# Entregable 1.2 — Convenciones del proyecto

Desde el primer día seguiremos reglas uniformes.

## Convenciones de nombres

### Clases

```python
Course
DocumentMetadata
DocumentExporter
SessionBuilder
```

### Funciones

```python
build_course()
validate_document()
load_configuration()
export_docx()
```

### Constantes

```python
DEFAULT_LANGUAGE

MAX_TITLE_LENGTH

SUPPORTED_EXPORTERS
```

### Archivos

```text
course.py

document.py

metadata.py

validation.py
```

Nunca utilizaremos nombres ambiguos como:

```text
utils2.py

helpers_final.py

nuevo.py
```

---

# Entregable 1.3 — Política de tipado

Todo el proyecto utilizará **anotaciones de tipos**.

Ejemplo:

```python
def load_course(path: Path) -> Course:
```

No habrá funciones sin tipos salvo casos muy excepcionales.

Esto permitirá utilizar `mypy` desde las primeras versiones.

---

# Entregable 1.4 — Estándares de documentación

Cada módulo comenzará con una cabecera uniforme.

Ejemplo:

```python
"""
MIPSP-Editor

Module:
    metadata.py

Description:
    Defines the institutional document metadata model.

Author:
    MIPSP Development Team

License:
    MIT

Version:
    1.0
"""
```

Además, todas las clases públicas incluirán docstrings compatibles con herramientas de documentación automática.

---

# Entregable 1.5 — Política de pruebas

Cada módulo deberá incorporar, como mínimo:

* pruebas de creación;
* pruebas de validación;
* pruebas de errores;
* pruebas de serialización (cuando aplique);
* pruebas de integración con el resto del sistema.

La meta es mantener una cobertura elevada en el núcleo (`core`, `domain` y `compiler`).

---

# Backlog priorizado

Con la infraestructura definida, el trabajo se organizará en el siguiente orden:

| Sprint | Objetivo               | Resultado esperado                              |
| ------ | ---------------------- | ----------------------------------------------- |
| S-01   | Infraestructura        | Repositorio listo                               |
| S-02   | `core`                 | Configuración, metadatos, registro y validación |
| S-03   | `domain`               | Modelo completo del dominio MIPSP               |
| S-04   | `compiler`             | Lexer, parser, AST y validación semántica       |
| S-05   | `exporters.docx`       | Primer generador DOCX funcional                 |
| S-06   | `builders`             | Construcción automática de documentos           |
| S-07   | CUR-OPS-001-D01        | Primer documento institucional completo         |
| S-08   | CUR-OPS-001-D02        | Carta Descriptiva                               |
| S-09   | CUR-OPS-001-D03        | Guía del Instructor                             |
| S-10   | Resto del curso patrón | Documentación completa                          |

---

# Cambio importante en nuestra dinámica

Creo que el proyecto ha alcanzado un punto en el que es conveniente cambiar también la forma de nuestras conversaciones.

Hasta ahora hemos trabajado como un comité de diseño. A partir del siguiente sprint, cada entrega estará orientada a **producir software utilizable**. Es decir, en lugar de seguir describiendo cómo será el sistema, construiremos sus componentes uno a uno.

Cada entrega incluirá:

1. El conjunto de archivos del sprint.
2. El código fuente completo de esos archivos.
3. Las pruebas unitarias correspondientes.
4. Un ejemplo de ejecución.
5. El registro de cambios.

## Mi propuesta para la siguiente entrega

Propongo comenzar inmediatamente el **Sprint 02 — Núcleo (`core`)**, desarrollando los primeros módulos reales del repositorio:

* `configuration.py`
* `metadata.py`
* `exceptions.py`
* `identifiers.py`
* `registry.py`
* `validation.py`

Con esos componentes tendremos el primer bloque funcional del MIPSP-Editor y una base sólida sobre la cual construir el compilador editorial y, posteriormente, el generador del **CUR-OPS-001**. A partir de ese momento, el énfasis del proyecto estará en la implementación efectiva y no en la definición conceptual.
