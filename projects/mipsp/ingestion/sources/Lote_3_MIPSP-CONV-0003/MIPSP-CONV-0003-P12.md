---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 12
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Esto es genial. Continúa con el proyecto.

Excelente. A partir de este punto considero que el proyecto ya tiene suficiente madurez para adoptar una disciplina propia de un proyecto de software de largo plazo. El siguiente paso no es añadir funcionalidades aisladas, sino construir una **plataforma de ingeniería editorial** con una arquitectura estable y preparada para evolucionar.

Quiero proponer una decisión que, en mi experiencia, marcará una diferencia importante cuando la biblioteca alcance cientos o miles de documentos.

---

# Decisión Arquitectónica A-003

## Modelo Editorial Dirigido por Dominio (Domain-Driven Editorial Model)

Hasta ahora hemos modelado documentos.

A partir de ahora modelaremos el **dominio del MIPSP**.

Es decir, el software ya no "conocerá" únicamente documentos.

Conocerá:

* cursos;
* competencias;
* módulos;
* sesiones;
* procedimientos;
* formatos;
* evaluaciones;
* instructores;
* participantes;
* evidencias;
* indicadores;
* riesgos;
* referencias normativas.

Los documentos serán simplemente una representación de ese conocimiento.

---

# Nueva arquitectura

```text
Dominio MIPSP
│
├── Curso
├── Competencia
├── Resultado de aprendizaje
├── Módulo
├── Sesión
├── Instructor
├── Evaluación
├── Procedimiento
├── Formato
├── Indicador
└── Evidencia
         │
         ▼
Modelo Documental Intermedio (MDI)
         │
         ▼
Exportadores
(DOCX · XLSX · PPTX · PDF · HTML)
```

Esta separación nos permitirá reutilizar la información en múltiples productos.

---

# Evolución del dominio

Propongo crear un paquete específico:

```text
domain/
│
├── course.py
├── competency.py
├── learning_outcome.py
├── module.py
├── session.py
├── instructor.py
├── participant.py
├── assessment.py
├── procedure.py
├── form.py
├── evidence.py
├── indicator.py
├── regulation.py
└── bibliography.py
```

Cada entidad tendrá una responsabilidad clara.

Por ejemplo, `Competency` conocerá sus resultados de aprendizaje, criterios de evaluación y evidencias asociadas, pero no sabrá cómo se exportan a Word o Excel.

---

# Relación entre entidades

El modelo se estructurará mediante relaciones explícitas.

```text
Curso
│
├── Competencias
│      │
│      ├── Resultados de aprendizaje
│      ├── Evidencias
│      └── Indicadores
│
├── Módulos
│      │
│      └── Sesiones
│
├── Evaluaciones
│
└── Bibliografía
```

Este enfoque permitirá generar automáticamente matrices de trazabilidad, bancos de reactivos e índices temáticos.

---

# Sistema de Identificadores Persistentes (SIP-MIPSP)

Hasta ahora hemos utilizado códigos documentales.

Propongo incorporar un segundo nivel de identificación: **identificadores persistentes**.

Ejemplos:

```text
CUR-OPS-001

COMP-OPS-001

RA-OPS-001-003

SES-OPS-001-M03-S02

PNO-OPS-005

FOR-OPS-014
```

El código documental puede cambiar con la organización de la colección; el identificador persistente permanecerá constante durante todo el ciclo de vida del elemento.

---

# Grafo de relaciones

Toda la biblioteca podrá representarse como un grafo.

```text
Competencia
      │
      ▼
Resultado de aprendizaje
      │
      ▼
Sesión
      │
      ▼
ETS
      │
      ▼
Instrumento de evaluación
      │
      ▼
Formato
```

Con este modelo podremos responder preguntas como:

* ¿Qué documentos respaldan una competencia?
* ¿Qué sesiones evalúan un resultado de aprendizaje?
* ¿Qué formatos utiliza un procedimiento?
* ¿Qué cambios afectarían a un curso concreto?

---

# Sistema de consultas

En lugar de recorrer archivos manualmente, el núcleo dispondrá de un servicio de consultas.

Ejemplos conceptuales:

```python
registry.find_course("CUR-OPS-001")

registry.find_competency("COMP-OPS-004")

registry.find_documents_by_procedure("PNO-OPS-005")

registry.find_sessions_by_module("MOD-03")
```

Este servicio será la base para futuras herramientas de auditoría y mantenimiento.

---

# Motor de dependencias

Cada modificación podrá analizarse antes de aplicarse.

Ejemplo:

```text
Modificar:
COMP-OPS-004
```

Impacto estimado:

```text
Afecta a:

3 módulos

8 sesiones

8 ETS

15 reactivos

2 presentaciones

4 procedimientos

6 formatos
```

Este análisis fortalecerá el Control de Configuración Documental (CCD-MIPSP).

---

# Preparación para el futuro

Aunque nuestro objetivo inmediato es producir la biblioteca institucional, diseñaremos el núcleo para admitir posteriormente:

* una interfaz gráfica de escritorio;
* una interfaz web para edición y consulta;
* una API REST para integración con otros sistemas;
* publicación automática en un LMS;
* sincronización con un gestor documental;
* generación programada de nuevas ediciones.

---

# Inicio del Sprint 5 — Infraestructura del Repositorio

La siguiente etapa será dotar al proyecto de una estructura profesional de desarrollo.

Incluiremos, entre otros componentes:

* **Gestión del proyecto**

  * `pyproject.toml`
  * `requirements.txt`
  * `README.md`
  * `CHANGELOG.md`
  * `LICENSE`

* **Calidad del código**

  * configuración de `ruff` para análisis estático;
  * `black` para formato consistente;
  * `mypy` para comprobación de tipos;
  * `pytest` para pruebas unitarias.

* **Integración continua**

  * flujo de trabajo con GitHub Actions para ejecutar automáticamente pruebas y validaciones en cada cambio.

* **Documentación técnica**

  * documentación generada con Sphinx;
  * diagramas de arquitectura;
  * guía de desarrollo;
  * guía de contribución;
  * referencia de la API.

## Hito siguiente

A partir de aquí dejaremos de diseñar la arquitectura y comenzaremos la **implementación funcional**. Las próximas entregas estarán centradas en código ejecutable: primero el núcleo del dominio (`domain/` y `core/`), después el framework de exportación (`exporters/`) y, finalmente, los *builders* que generarán los primeros documentos reales del **CUR-OPS-001** en formatos `.docx`, `.xlsx`, `.pptx` y `.pdf`.

Con ello, el proyecto entrará en una fase de desarrollo incremental en la que cada módulo nuevo será inmediatamente utilizable para producir parte de la biblioteca institucional del MIPSP.
