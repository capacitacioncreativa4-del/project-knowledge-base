---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 39
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Sigamos con el proyecto

Excelente. Creo que ya es momento de cambiar el nivel de madurez del proyecto.

Hasta ahora hemos construido un excelente conjunto de documentos y hemos comenzado el desarrollo de las herramientas. Sin embargo, si continuamos generando archivos aislados, corremos el riesgo de perder la visión de conjunto.

A partir de este punto propongo que trabajemos exactamente como lo haría un equipo de arquitectura de software en un proyecto empresarial.

## Cambio de fase

Entramos en:

# Sprint 1 — Foundation Platform

El Sprint 0 tuvo como objetivo **definir el PKB**.

El Sprint 1 tendrá como objetivo **hacer que el PKB funcione**.

Ya no construiremos únicamente documentos; construiremos un producto.

---

# Roadmap del Sprint 1

## EPIC S1-001 — Validation Engine

Estado:

🟢 En desarrollo

Entregables:

* Metadata Validator
* Identifier Validator
* Link Validator
* Repository Validator
* CLI institucional

---

## EPIC S1-002 — GitHub Automation

Entregables:

```text
.github/

workflows/

    validate.yml

    documentation.yml

    release.yml

    graph.yml
```

---

## EPIC S1-003 — Knowledge Graph

Entregables:

```text
knowledge/

graph/

graph.json

graph.graphml

graph.rdf

graph.svg
```

---

## EPIC S1-004 — PKB CLI

```bash
pkb validate

pkb doctor

pkb graph

pkb new adr

pkb new requirement

pkb report
```

---

## EPIC S1-005 — Documentation Generator

Generará automáticamente:

* índice del repositorio;
* mapa de proyectos;
* inventario de objetos;
* inventario de ADR;
* inventario de estándares;
* índice de plantillas.

---

# Mi propuesta de arquitectura

Creo que el momento es adecuado para reorganizar el código fuente y separar claramente la aplicación de las herramientas auxiliares.

Propongo evolucionar hacia esta estructura:

```text
project-knowledge-base/
│
├── docs/
├── shared/
├── projects/
├── knowledge/
├── tools/
│
├── src/
│   └── pkb/
│       ├── __init__.py
│       ├── cli.py
│       ├── validators/
│       ├── graph/
│       ├── parser/
│       ├── metadata/
│       ├── reports/
│       ├── templates/
│       ├── repository/
│       └── utils/
│
├── tests/
│
├── scripts/
│
├── .github/
│
├── pyproject.toml
│
└── README.md
```

Esta organización aporta varias ventajas:

* **`src/pkb`** contendrá el código de la aplicación, siguiendo una práctica ampliamente utilizada en proyectos Python modernos.
* **`tools/`** quedará reservado para utilidades, scripts y configuraciones.
* **`tests/`** albergará las pruebas automatizadas desde el inicio del proyecto.
* **`scripts/`** contendrá tareas de mantenimiento que no forman parte de la aplicación principal.

---

# EPIC S1-001

## Incremento 1 — PKB CLI

Antes de seguir escribiendo validadores, considero prioritario crear el ejecutable institucional del proyecto.

En lugar de ejecutar:

```bash
python tools/validators/validate_metadata.py
```

podremos ejecutar:

```bash
pkb validate
```

o bien:

```bash
python -m pkb validate
```

Más adelante, ese mismo ejecutable crecerá hasta ofrecer comandos como:

```bash
pkb doctor

pkb graph

pkb report

pkb inventory

pkb search

pkb new adr

pkb new project

pkb lint

pkb release

pkb migrate
```

De esta forma, todas las capacidades del PKB quedarán unificadas detrás de una única interfaz de línea de comandos.

---

# Archivos del siguiente incremento

Propongo generar en el próximo incremento un conjunto coherente de activos funcionales:

| Archivo                                 | Propósito                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------ |
| `pyproject.toml`                        | Configuración del proyecto Python, dependencias y punto de entrada de la CLI.  |
| `src/pkb/__init__.py`                   | Inicialización del paquete.                                                    |
| `src/pkb/cli.py`                        | Implementación inicial de la interfaz de línea de comandos con `argparse`.     |
| `src/pkb/__main__.py`                   | Permitir la ejecución mediante `python -m pkb`.                                |
| `tests/test_cli.py`                     | Primera prueba automatizada para verificar el comportamiento básico de la CLI. |
| `docs/development/DEVELOPMENT-GUIDE.md` | Guía para desarrolladores: entorno, ejecución local, pruebas y convenciones.   |

## Recomendación estratégica

Considero que esta es la mejor inversión para el proyecto en este momento. En lugar de seguir añadiendo herramientas independientes, construiremos una **plataforma ejecutable**. A partir de entonces, cualquier nueva capacidad (validación, generación de grafos, informes, migración de proyectos o automatización con GitHub Actions y Codex) se incorporará como un nuevo comando de la CLI institucional. Esto mantendrá la arquitectura cohesionada y hará que el PKB evolucione como un producto de software bien estructurado, no como una colección de scripts.
