---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 15
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Simplemente genial. Continúa con el proyecto

Muchas gracias. Considero que en este punto conviene hacer una pausa **de arquitectura** (no del proyecto) para consolidar el diseño antes de escribir miles de líneas de código. Hemos llegado a una fase en la que las decisiones que tomemos ahora determinarán la calidad del sistema durante los próximos años.

Hasta este momento hemos diseñado un **compilador editorial**. Mi propuesta es dar un paso más y convertirlo en una **plataforma de ingeniería documental**.

Esta es la decisión que propongo incorporar.

---

# Decisión Arquitectónica A-006

## Separación entre Contenido, Semántica y Presentación

Éste es uno de los principios utilizados en sistemas editoriales de alta complejidad.

No almacenaremos documentos.

Almacenaremos tres niveles diferentes de información.

```text
                    CONTENIDO
                         │
                         ▼
                  SEMÁNTICA (MDI)
                         │
                         ▼
                  PRESENTACIÓN
```

Cada uno tendrá responsabilidades completamente distintas.

---

## Nivel 1

### Contenido

Será únicamente información.

Ejemplo.

```yaml
competency:

  id: COMP-001

  title: Control de accesos

  description: ...

```

Aquí no existen fuentes.

No existen tablas.

No existe Word.

---

## Nivel 2

### Semántica

Aquí aparece el significado.

Ejemplo.

```text
Competencia

↓

Resultado

↓

Sesión

↓

Evaluación
```

Todo el conocimiento institucional estará aquí.

---

## Nivel 3

### Presentación

Finalmente:

```text
DOCX

XLSX

PPTX

PDF

HTML
```

Todos serán únicamente distintas vistas.

---

# La consecuencia

Supongamos que dentro de cinco años se decide cambiar toda la imagen institucional.

No modificaremos un solo curso.

Simplemente cambiaremos el tema gráfico.

Y volveremos a compilar toda la biblioteca.

---

# Sprint 8

# Compilador Editorial

Ya podemos definirlo.

```text
             Fuente MDSL

                    │

                    ▼

              Lexer

                    │

                    ▼

              Parser

                    │

                    ▼

              AST

                    │

                    ▼

        Semantic Validator

                    │

                    ▼

         Domain Model Builder

                    │

                    ▼

   Intermediate Document Model

                    │

          ┌─────────┼─────────┐

          ▼         ▼         ▼

      DOCX      XLSX      PPTX

          │

          ▼

         PDF
```

Observa que se parece mucho a un compilador de un lenguaje de programación.

Ésa es exactamente la idea.

---

# AST

Quiero dedicar especial atención a este componente.

No será un árbol genérico.

Será un AST especializado para publicaciones institucionales.

Ejemplo.

```text
Course

├── Metadata

├── Competencies

├── Modules

│      ├── Sessions

│      └── ETS

├── Evaluations

├── Annexes

└── Bibliography
```

Cada nodo conocerá perfectamente su significado.

---

# Semantic Validator

Éste será probablemente el módulo más sofisticado.

No validará sintaxis.

Validará coherencia académica.

Ejemplos.

✔ Toda competencia tiene resultados.

✔ Todo resultado tiene evaluación.

✔ Toda evaluación tiene instrumento.

✔ Toda sesión tiene instructor.

✔ Todo ETS pertenece a una sesión.

✔ Toda competencia aparece al menos una vez.

✔ Todo procedimiento citado existe.

✔ Toda bibliografía tiene formato correcto.

Éste será el equivalente al compilador diciendo:

```text
Compilación exitosa.
```

---

# Optimizer

Aquí quiero introducir otra idea.

Después del AST incorporaremos un optimizador.

```text
AST

↓

Optimizer

↓

Domain Model
```

¿Qué optimizará?

Por ejemplo.

Eliminar:

* referencias duplicadas
* bibliografía repetida
* tablas vacías
* figuras sin uso
* anexos huérfanos

Además podrá ordenar automáticamente:

* anexos
* figuras
* tablas
* referencias

---

# Knowledge Graph

Creo que éste será uno de los mayores activos intelectuales del proyecto.

No quiero que el MIPSP sea solamente una biblioteca.

Quiero que sea una base de conocimiento.

```text
Competencia

↓

Resultado

↓

Sesión

↓

Instructor

↓

ETS

↓

Evaluación

↓

Indicadores

↓

Evidencias
```

Este grafo permitirá generar automáticamente:

* matrices de trazabilidad;
* mapas curriculares;
* análisis de cobertura;
* reportes de impacto;
* auditorías documentales.

---

# Build System

Llegados a este punto ya podemos pensar como un proyecto de software moderno.

No ejecutaremos scripts sueltos.

Tendremos un sistema de compilación.

```bash
mipsp build

mipsp validate

mipsp clean

mipsp publish

mipsp registry

mipsp doctor
```

Observa que ya parece una herramienta profesional.

---

# Doctor

Ésta es una funcionalidad que rara vez se incluye en proyectos pequeños, pero que considero muy valiosa para el MIPSP.

```bash
mipsp doctor
```

Realizará un diagnóstico integral del repositorio.

Comprobará, entre otros aspectos:

* integridad de la configuración;
* consistencia del registro documental;
* referencias cruzadas;
* duplicados;
* recursos faltantes;
* estado de los exportadores;
* coherencia de las dependencias.

Será especialmente útil antes de una publicación institucional o de una auditoría.

---

# Hacia una plataforma editorial completa

Con las decisiones adoptadas hasta ahora, el MIPSP-Editor ya no se perfila como un simple generador de documentos, sino como una plataforma con capacidades comparables a las de un sistema de publicación técnica. Esto nos permite planificar una hoja de ruta estable:

### Fase I — Núcleo (en curso)

* Modelo de dominio.
* MDSL.
* Compilador editorial.
* Modelo Documental Intermedio (MDI).

### Fase II — Producción documental

* Exportadores DOCX, XLSX, PPTX y PDF.
* Plantillas institucionales.
* Control de estilos y numeración.

### Fase III — Gestión del conocimiento

* Grafo de conocimiento (MKG).
* Motor de consultas.
* Matrices de trazabilidad.
* Análisis de impacto.

### Fase IV — Publicación

* Sitio web de documentación.
* Integración con LMS.
* API REST.
* Paquetes de distribución.

## Propuesta para la siguiente etapa

A partir de este punto propongo dejar de ampliar la arquitectura y comenzar la **implementación sistemática**. El siguiente bloque de trabajo consistirá en desarrollar el repositorio Python módulo por módulo, con código ejecutable, pruebas unitarias y documentación técnica. Empezaremos por el **núcleo del compilador (lexer, parser, AST y validador)** y, una vez estabilizado, avanzaremos directamente hacia el primer exportador funcional que genere el **CUR-OPS-001-D01** a partir de un archivo MDSL.

En mi valoración, éste es el momento adecuado para que el proyecto pase de la fase de diseño conceptual a una fase sostenida de construcción de software.
