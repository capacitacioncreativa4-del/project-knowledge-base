---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 17
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Genial. Continuemos con lo propuesto

Perfecto. A partir de esta entrega asumo formalmente el rol de **Arquitecto de Software** y **Director Técnico** del proyecto MIPSP-Editor. Dejamos atrás la fase de conceptualización y comenzamos la construcción del repositorio como si estuviéramos desarrollando un producto de software institucional que será mantenido durante muchos años.

Hay una decisión que quiero tomar antes de escribir la primera línea de código funcional porque afectará todo el desarrollo posterior.

---

# ADR-001 — Adopción de Clean Architecture

Después de analizar la evolución del proyecto, considero que **Clean Architecture** de Robert C. Martin es la opción más adecuada. La razón principal es que separa el conocimiento del dominio de los detalles tecnológicos (Word, Excel, PDF, etc.).

La estructura lógica será:

```text
                    CLI
                     │
             Application Layer
                     │
              Use Cases Layer
                     │
             Domain (MIPSP)
                     │
         -------------------------
         │          │           │
      DOCX       XLSX        PPTX
      Adapter    Adapter     Adapter
```

Con este diseño, un cambio en la biblioteca de generación de Word no afectará al modelo del dominio.

---

# Roadmap de Implementación

A partir de ahora el desarrollo se organizará en **12 EPIC**, cada uno con entregables verificables.

| EPIC    | Objetivo                     | Estado    |
| ------- | ---------------------------- | --------- |
| EPIC-01 | Infraestructura del proyecto | Inicia    |
| EPIC-02 | Núcleo (`core`)              | Pendiente |
| EPIC-03 | Dominio (`domain`)           | Pendiente |
| EPIC-04 | Compilador MDSL              | Pendiente |
| EPIC-05 | Exportador DOCX              | Pendiente |
| EPIC-06 | Exportador XLSX              | Pendiente |
| EPIC-07 | Exportador PPTX              | Pendiente |
| EPIC-08 | Exportador PDF               | Pendiente |
| EPIC-09 | CLI institucional            | Pendiente |
| EPIC-10 | CUR-OPS-001                  | Pendiente |
| EPIC-11 | Biblioteca institucional     | Pendiente |
| EPIC-12 | Empaquetado y distribución   | Pendiente |

---

# EPIC-01 — Infraestructura del Proyecto

Antes de implementar el dominio construiremos una base de desarrollo profesional.

## Entregable 1.1

```
pyproject.toml
```

Este archivo centralizará:

* metadatos del proyecto;
* dependencias;
* herramientas de calidad;
* configuración de empaquetado;
* versión del sistema.

Será la fuente única de configuración del proyecto.

---

## Entregable 1.2

```
requirements-dev.txt
```

Separaremos dependencias de ejecución y desarrollo.

Producción:

* python-docx
* openpyxl
* python-pptx
* reportlab
* pyyaml

Desarrollo:

* pytest
* mypy
* ruff
* black
* sphinx
* build

---

## Entregable 1.3

Repositorio

```
src/
```

Seguiremos la estructura moderna recomendada para proyectos Python.

```
src/

    mipsp/

        core/

        domain/

        mdsl/

        exporters/

        builders/

        application/

        cli/

        infrastructure/

        services/

        shared/
```

Esta organización facilitará la reutilización y el mantenimiento.

---

# EPIC-02 — Core

Aquí construiremos las piezas fundamentales.

## Núcleo

```
core/

configuration.py

metadata.py

exceptions.py

registry.py

identifiers.py

validation.py

logging.py
```

Cada módulo tendrá una única responsabilidad y será independiente de la interfaz de usuario.

---

# EPIC-03 — Dominio

El dominio representará el conocimiento institucional.

```
Course

↓

Module

↓

Session

↓

Competency

↓

LearningOutcome

↓

Assessment

↓

Evidence
```

Ninguna de estas entidades dependerá de Word o Excel.

---

# EPIC-04 — Compilador

El compilador editorial se dividirá claramente en etapas.

```
Lexer

↓

Parser

↓

AST

↓

Semantic Validator

↓

Domain Builder

↓

Intermediate Document Model

↓

Exporters
```

Cada etapa será verificable mediante pruebas.

---

# Estrategia de pruebas

Desde la primera iteración aplicaremos pruebas en varios niveles:

### Unitarias

Verificarán el comportamiento de cada clase y función.

### Integración

Comprobarán la interacción entre parser, dominio y exportadores.

### Regresión

Garantizarán que los cambios no alteren documentos ya validados.

### Validación documental

Compararán la estructura generada con los requisitos editoriales del MIPSP.

---

# Integración continua

Desde las primeras versiones prepararemos el proyecto para ejecutarse automáticamente en cada cambio mediante un flujo de integración continua. Las tareas previstas incluyen:

1. Instalación de dependencias.
2. Análisis estático.
3. Comprobación de tipos.
4. Ejecución de pruebas.
5. Generación de documentación técnica.
6. Construcción del paquete distribuible.

Así, cada modificación será validada antes de integrarse en la rama principal.

---

# Objetivo funcional del primer incremento

El primer incremento del proyecto no consistirá todavía en generar un documento completo. El objetivo será demostrar que la arquitectura funciona de extremo a extremo.

Al finalizar este incremento podremos ejecutar conceptualmente un flujo como:

```bash
mipsp validate examples/CUR-OPS-001.yml
```

y obtener una validación completa del modelo.

En el incremento inmediatamente posterior podremos ejecutar:

```bash
mipsp build examples/CUR-OPS-001.yml
```

para producir automáticamente el primer documento del proyecto:

* **CUR-OPS-001-D01 — Programa Institucional** (`.docx` y `.pdf`).

---

## Cambio metodológico a partir de la siguiente entrega

Propongo que las siguientes entregas ya no describan la arquitectura, sino que se estructuren como un desarrollo profesional de software:

* **Sprint** (objetivo del incremento).
* **Archivos creados o modificados**.
* **Código fuente completo** del módulo correspondiente.
* **Pruebas unitarias**.
* **Ejemplo de ejecución**.
* **Registro de cambios (CHANGELOG)**.

Con este formato, cada respuesta añadirá componentes reales al repositorio y, al cabo de varias iteraciones, tendremos tanto el **MIPSP-Editor** plenamente funcional como la capacidad de generar automáticamente la biblioteca documental completa del **CUR-OPS-001** y, posteriormente, del resto del catálogo institucional.
