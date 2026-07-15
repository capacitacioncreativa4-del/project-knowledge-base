---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 13
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece perfecto. Prosigamos

Excelente. Considero que el proyecto ya ha alcanzado el grado de madurez suficiente para abandonar definitivamente el enfoque de "scripts" y comenzar a desarrollar un **producto de software**. A partir de este punto voy a trabajar como si fuéramos un equipo de arquitectura de software construyendo un sistema que permanecerá vigente durante muchos años.

También quiero proponer una decisión importante que aumentará considerablemente la calidad del proyecto.

---

# Decisión Arquitectónica A-004

## MIPSP-Editor será una aplicación basada en Plugins

Es decir, el núcleo nunca conocerá cómo generar un DOCX, un XLSX o un PDF.

Conocerá únicamente que existe un **exportador**.

```text
                  CORE
                    │
        ┌───────────┼────────────┐
        ▼           ▼            ▼
 DOCX Plugin   XLSX Plugin   PPTX Plugin
        │           │            │
        └───────────┼────────────┘
                    ▼
              PDF Plugin
```

En el futuro podremos agregar:

* HTML
* Markdown
* LaTeX
* EPUB
* SCORM
* Moodle XML
* JSON
* XML
* Base de datos
* API REST

sin modificar el núcleo.

Eso es precisamente lo que buscamos.

---

# Sprint 6

# El Dominio Editorial

Hasta ahora diseñamos clases.

Ahora construiremos el verdadero modelo del MIPSP.

## Primera capa

```text
domain/

course.py

module.py

session.py

competency.py

learning_objective.py

evaluation.py

evidence.py

procedure.py

form.py

bibliography.py

document.py
```

Esta carpeta representará el conocimiento institucional.

No contendrá una sola línea relacionada con Word.

---

# Course

La clase principal será:

```python
Course
```

Contendrá:

```text
Código

Nombre

Versión

Competencias

Módulos

Bibliografía

Documentos

Presentaciones

Instrumentos

Indicadores

Evidencias
```

No almacenará párrafos.

Almacenará conocimiento.

---

# Module

```python
Module
```

Contendrá:

```text
Número

Nombre

Duración

Sesiones

Competencias

Resultados

Materiales
```

---

# Session

```python
Session
```

Será la unidad mínima de producción.

Contendrá:

```text
Objetivos

Duración

Instructor

Actividades

Recursos

Evaluaciones

ETS

Presentación

Ejercicios
```

Observa algo interesante.

Una sesión conoce automáticamente cuál es su ETS.

Eso significa que podremos generar el ETS sin volver a escribir información.

---

# Competency

Aquí está probablemente el corazón académico.

```python
Competency
```

```text
Código

Nombre

Descripción

Resultados

Indicadores

Evidencias

Instrumentos
```

---

# Resultado de aprendizaje

```python
LearningOutcome
```

Será independiente.

Después podremos construir automáticamente matrices como:

```text
Competencia

↓

Resultado

↓

Sesión

↓

ETS

↓

Reactivo

↓

Indicador
```

Todo ello sin escribir una sola tabla manualmente.

---

# Relaciones

Todo el dominio se convertirá en un grafo.

```text
Curso
│
├── Módulos
│      │
│      ├── Sesiones
│      │      │
│      │      ├── ETS
│      │      ├── PPT
│      │      ├── Evaluaciones
│      │      └── Formatos
│      │
│      └── Competencias
│
└── Bibliografía
```

---

# Builder automático

Hasta ahora hacíamos esto.

```python
doc.add_heading(...)

doc.add_table(...)
```

Ya no.

Ahora haremos:

```python
CourseBuilder(course)

↓

Document

↓

DOCX
```

Eso significa que una modificación del dominio regenerará automáticamente toda la documentación.

---

# Ventaja enorme

Supongamos que cambia:

```
Competencia 8
```

Automáticamente podremos regenerar:

* Manual del Instructor
* Manual del Participante
* ETS
* Presentación
* Banco de Reactivos
* Matriz de Competencias
* Matriz de Evidencias

sin editar seis documentos.

---

# Siguiente decisión

Aquí quiero proponer algo que, sinceramente, considero que llevará el proyecto a un nivel comparable con plataformas editoriales de alto nivel.

## Lenguaje Declarativo del MIPSP (MDSL)

En lugar de escribir el contenido directamente en Python, definiremos los cursos mediante un lenguaje declarativo propio, basado inicialmente en YAML.

Por ejemplo:

```yaml
course:
  code: CUR-OPS-001
  title: Control de Accesos
  version: 1.0

modules:
  - code: MOD-01
    title: Fundamentos del Control de Accesos
```

El MIPSP-Editor leerá estos archivos y construirá automáticamente el modelo de dominio.

Las ventajas son significativas:

* el contenido queda separado del código;
* expertos en capacitación podrán editar cursos sin modificar Python;
* los cambios serán más fáciles de revisar mediante control de versiones;
* el mismo contenido podrá publicarse en múltiples formatos.

---

# Próximo Sprint (Sprint 7)

Con esta decisión, el siguiente bloque de trabajo será especialmente importante. Construiremos:

1. **Parser del MDSL** para interpretar los archivos declarativos.
2. **Validador semántico**, que comprobará que los cursos están completos y consistentes.
3. **Constructor del modelo de dominio**, que transformará el contenido declarativo en objetos del sistema.
4. **Primer generador funcional**, capaz de producir el primer documento del **CUR-OPS-001** a partir del modelo de dominio, sin lógica específica del curso incrustada en el código.

Con este paso, el MIPSP dejará de depender de documentos escritos manualmente y pasará a ser una **plataforma editorial dirigida por datos**, donde el conocimiento institucional será el activo principal y los documentos serán productos generados automáticamente. En mi valoración, ésta es la arquitectura que mejor garantiza la sostenibilidad, mantenibilidad y escalabilidad del proyecto a largo plazo.
