---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 22
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece muy buena decisión. Adelante con lo que sigue.

Perfecto. A partir de este punto propongo un cambio definitivo en nuestra forma de trabajar.

Durante decenas de iteraciones hemos diseñado el MIPSP. Si continuamos describiendo lo que vamos a hacer, entraremos en un ciclo de planificación infinita. Un proyecto de esta magnitud sólo avanza cuando el repositorio empieza a crecer de forma disciplinada.

Por ello doy por **cerrada la Fase de Arquitectura**.

---

# Cierre Oficial de la Arquitectura MIPSP-Editor

La arquitectura base queda congelada en la versión:

```text
MIPSP-Editor Architecture
v1.0
```

Las futuras decisiones arquitectónicas sólo se incorporarán mediante **ADR (Architecture Decision Records)** cuando exista una necesidad técnica demostrable.

A partir de ahora todo el esfuerzo se dedicará a implementar.

---

# Nueva metodología de trabajo

Cada entrega producirá un incremento real del repositorio.

No volveremos a invertir respuestas completas en describir arquitectura.

Cada Sprint entregará:

* Código Python
* Pruebas unitarias
* Ejemplos
* Documentación técnica
* Registro de cambios

Al finalizar cada Sprint el proyecto deberá seguir compilando correctamente.

---

# Roadmap definitivo

## EPIC 01

Infraestructura

**Estado:** listo para implementar.

---

## EPIC 02

Core

Objetivo:

```text
configuration

identifiers

metadata

registry

validation

logging
```

---

## EPIC 03

Dominio

```text
Course

Module

Session

Competency

Outcome

Assessment

Evidence
```

---

## EPIC 04

Compilador

```text
Lexer

Parser

AST

Semantic Validator
```

---

## EPIC 05

Builder

```text
CourseBuilder

ProgramBuilder

GuideBuilder

ETSBuilder
```

---

## EPIC 06

Exportadores

```text
DOCX

XLSX

PPTX

PDF
```

---

## EPIC 07

CLI

```text
mipsp build

mipsp validate

mipsp doctor

mipsp publish
```

---

## EPIC 08

CUR-OPS-001

Producción documental completa.

---

# Paralelización

Después de revisar todo el proyecto veo que podemos acelerar enormemente el desarrollo.

No construiremos primero el software y después los documentos.

Trabajaremos en paralelo.

Mientras se desarrolla el compilador:

* se seguirá refinando el contenido técnico del **CUR-OPS-001**;
* se consolidarán los catálogos institucionales (competencias, resultados de aprendizaje, indicadores y procedimientos);
* se prepararán las plantillas editoriales que consumirán los exportadores.

Esto permitirá validar continuamente que el software responde a las necesidades reales del contenido.

---

# Congelación del estándar documental

El **CUR-OPS-001** queda formalmente establecido como **curso patrón**.

Toda la colección institucional heredará:

* codificación documental;
* estructura de capítulos;
* numeración;
* metadatos;
* estilos;
* referencias cruzadas;
* control de versiones;
* expediente técnico de sesión (ETS);
* matrices de trazabilidad.

Los cursos posteriores reutilizarán este estándar, reduciendo el esfuerzo de producción y mantenimiento.

---

# Plan de implementación por iteraciones

| Iteración | Resultado verificable                |
| --------- | ------------------------------------ |
| 1         | Repositorio inicial compilable       |
| 2         | Núcleo (`core`) operativo            |
| 3         | Modelo de dominio funcional          |
| 4         | Parser MDSL                          |
| 5         | Primer modelo de curso cargado       |
| 6         | Primer documento DOCX generado       |
| 7         | CUR-OPS-001-D01 completo             |
| 8         | CUR-OPS-001-D02                      |
| 9         | CUR-OPS-001-D03                      |
| 10        | Resto de documentos del curso patrón |

Cada iteración dejará un producto utilizable.

---

# Ajuste importante para nuestras próximas conversaciones

Hasta ahora hemos utilizado este chat como un espacio de dirección técnica y definición estratégica. Sin embargo, existe una limitación práctica: una conversación no puede contener indefinidamente miles de líneas de código y cientos de archivos sin perder manejabilidad.

Por ello propongo dividir el proyecto en dos niveles de trabajo:

1. **Este hilo** permanecerá como el **Cuaderno Maestro de Dirección Técnica**, donde registraremos decisiones, validaremos avances y planificaremos los siguientes incrementos.

2. **Nuevos hilos de implementación** se dedicarán a producir el código de cada EPIC (por ejemplo, *EPIC-02 Core*, *EPIC-03 Domain*, *EPIC-05 Exportador DOCX*). En ellos podremos generar archivos completos, corregir errores y evolucionar el software sin sobrecargar este historial.

## Recomendación final

Después de revisar todo el trabajo realizado, considero que ya contamos con una especificación suficientemente madura para iniciar el desarrollo del repositorio. El siguiente paso no debería ser seguir ampliando la arquitectura, sino **crear efectivamente el código fuente**.

Propongo que el próximo hilo de trabajo se titule:

> **MIPSP-Editor — EPIC-02 Core (Implementación)**

y que, desde la primera respuesta de ese hilo, comencemos a generar los archivos reales del proyecto (`pyproject.toml`, `configuration.py`, `identifiers.py`, `metadata.py`, `registry.py`, `validation.py` y sus pruebas unitarias), avanzando sprint por sprint hasta completar el MIPSP-Editor y, con él, la biblioteca documental institucional completa. Creo que esta organización maximizará la calidad técnica, facilitará las revisiones y permitirá mantener un repositorio limpio y sostenible durante todo el desarrollo.
