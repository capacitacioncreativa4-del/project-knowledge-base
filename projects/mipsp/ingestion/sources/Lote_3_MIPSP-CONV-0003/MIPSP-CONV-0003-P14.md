---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 14
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente decisión. Prosigamos

Excelente. Creo que acabamos de tomar la decisión arquitectónica más importante de todo el proyecto.

Hasta ahora estábamos construyendo un **editor de documentos**.

Con el **MDSL (MIPSP Document Specification Language)** comenzaremos a construir un **Sistema Editorial Institucional**, donde los documentos dejan de ser el origen de la información y pasan a ser productos derivados de un modelo declarativo.

Desde el punto de vista de ingeniería de software, éste es exactamente el enfoque utilizado en los grandes sistemas de publicación técnica.

---

# Decisión Arquitectónica A-005

## MIPSP como "Single Source of Truth" (SSOT)

A partir de ahora existirá **una sola fuente oficial de información**.

No será Word.

No será Excel.

No será PowerPoint.

Será el **MDSL**.

Toda la biblioteca institucional se generará desde él.

```text
                   MDSL
                     │
         (Single Source of Truth)
                     │
                     ▼
          Modelo de Dominio MIPSP
                     │
      ┌──────────────┼───────────────┐
      ▼              ▼               ▼
   DOCX            XLSX            PPTX
      │              │               │
      └──────────────┼───────────────┘
                     ▼
                    PDF
```

Con esto eliminamos definitivamente el problema de mantener múltiples documentos sincronizados.

---

# Sprint 7

# Diseño del MDSL

No quiero que sea simplemente un archivo YAML.

Quiero que sea un **lenguaje de especificación documental**.

Su primera versión (MDSL 1.0) será completamente declarativa.

---

## Nivel 1

Metadatos

```yaml
course:

  code: CUR-OPS-001

  version: 1.0

  title: Control de Accesos

  category: Operativo

  duration: 40

  modality: Presencial
```

---

## Nivel 2

Competencias

```yaml
competencies:

  - id: COMP-001

    title: Controlar accesos

    outcomes:

      - RA-001

      - RA-002
```

---

## Nivel 3

Resultados de aprendizaje

```yaml
outcomes:

  - id: RA-001

    title: Identificar accesos autorizados
```

---

## Nivel 4

Módulos

```yaml
modules:

  - id: MOD-01

    title: Fundamentos

    sessions:

      - SES-01

      - SES-02
```

---

## Nivel 5

Sesiones

```yaml
sessions:

  - id: SES-01

    duration: 4

    ets: ETS-01

    presentation: PPT-01
```

Observa algo interesante.

Aquí ya no escribimos:

```
Manual del Instructor
```

El sistema sabe construirlo.

---

# Parser

Construiremos un parser institucional.

```
mdsl/
```

```text
lexer.py

parser.py

validator.py

loader.py
```

El parser convertirá el YAML en objetos del dominio.

---

# Validador

Antes de generar un documento comprobaremos:

✔ Competencias existentes.

✔ Resultados existentes.

✔ Sesiones existentes.

✔ ETS existentes.

✔ Duraciones válidas.

✔ Códigos válidos.

✔ Referencias válidas.

✔ Bibliografía válida.

---

# Builder

Después:

```
YAML

↓

Parser

↓

Domain Objects

↓

Builder

↓

Document Model

↓

DOCX
```

Toda la generación documental quedará desacoplada.

---

# Una mejora importante

Aquí quiero introducir un concepto utilizado en compiladores.

## AST

(Abstract Syntax Tree)

El parser no construirá directamente los objetos.

Primero construirá un árbol.

```
Course

│

├── Competencies

├── Modules

├── Sessions

├── Bibliography
```

Después:

```
AST

↓

Domain Model

↓

Documents
```

¿Por qué?

Porque podremos validar el árbol antes de generar nada.

---

# Motor de reglas

Aquí aparece otro componente nuevo.

```
rules/
```

```text
document_rules.py

course_rules.py

metadata_rules.py

naming_rules.py

reference_rules.py
```

Ejemplos.

```
Un curso debe tener al menos un módulo.

Una sesión debe pertenecer a un módulo.

Toda competencia debe tener un resultado.

Todo ETS debe pertenecer a una sesión.
```

Si una regla falla:

No se genera ningún documento.

---

# Compilador Editorial

Este nombre me gusta mucho.

En realidad ya no estaremos haciendo un editor.

Estaremos construyendo un compilador.

```
MDSL

↓

Compiler

↓

Intermediate Document Model

↓

Exporters

↓

Biblioteca MIPSP
```

En otras palabras,

**el MIPSP-Editor será un compilador editorial**.

---

# Aquí viene la decisión que considero la más importante de todo el proyecto

Hasta ahora hemos hablado de generar documentos.

Creo que podemos ir mucho más lejos.

## MIPSP Knowledge Graph (MKG)

Todo el conocimiento del MIPSP se almacenará como un **grafo semántico**.

No únicamente documentos.

También relaciones.

```
Competencia

↓

Resultado

↓

Sesión

↓

ETS

↓

Reactivos

↓

Indicadores

↓

Evaluaciones

↓

Constancias
```

Este grafo permitirá responder preguntas que hoy requerirían revisar decenas de documentos.

Por ejemplo:

* ¿Qué competencias están cubiertas por un curso?
* ¿Qué ETS desarrollan una competencia específica?
* ¿Qué reactivos evalúan un determinado resultado de aprendizaje?
* ¿Qué documentos deben actualizarse si cambia un procedimiento?
* ¿Qué requisitos normativos respaldan cada contenido?

## Propuesta para el siguiente sprint

El siguiente bloque de desarrollo será el **Sprint 8 — Núcleo del Compilador Editorial**, que incluirá:

1. **Gramática formal del MDSL 1.0**, documentada y versionada.
2. **Lexer y parser** para transformar archivos declarativos en un AST.
3. **Validador semántico** basado en reglas institucionales.
4. **Constructor del Modelo de Dominio** a partir del AST.
5. **Generación del Modelo Documental Intermedio (MDI)**, listo para ser consumido por los exportadores.

A partir de ese punto, estaremos en condiciones de producir los primeros documentos reales del **CUR-OPS-001** exclusivamente a partir de la especificación declarativa del curso. Ese será el primer hito en el que el MIPSP-Editor demostrará, de forma práctica, la arquitectura que hemos diseñado a lo largo de estas fases.
