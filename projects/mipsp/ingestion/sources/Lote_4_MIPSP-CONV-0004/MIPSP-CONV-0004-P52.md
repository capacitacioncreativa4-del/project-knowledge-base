---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 52
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Quiero hacerte una petición: concretemos la ingestión del proyecto MIPSP. Quiero que el PKB deje de ser un proyecto de infraestructura y comience a generar valor práctico administrando uno de mis proyectos reales. Si puedes postergar nuevas funcionalidades o mejoras al proyecto, hazlo. Vamos de una vez con la ingestión del proyecto, a menos que haya algo estrictamente necesario que debamos hacer antes. Tú mismo has señalado la importancia de probar con un proyecto real antes de avanzar en otros aspectos. Entonces, analiza y ajusta lo que consideres conveniente a fin de concretar ya la ingestión del proyecto MIPSP. Vayamos a la prueba piloto tan anunciada.

Estoy de acuerdo con el cambio de enfoque. De hecho, creo que es la decisión correcta.

Después de revisar mentalmente todo el camino recorrido, llego a una conclusión: **si seguimos diseñando el PKB sin ponerlo bajo la presión de un proyecto real, empezaremos a optimizar una arquitectura que aún no ha sido validada en producción**.

Por ello propongo un cambio formal de estrategia.

---

# DEC-0020 — Congelación de la arquitectura base

A partir de este momento:

* Se congela la arquitectura del PKB.
* No se incorporarán nuevas capacidades al núcleo salvo correcciones indispensables.
* Todo el desarrollo se orientará a soportar la ingestión de MIPSP.
* Cualquier mejora detectada durante la ingestión se registrará como incidencia o ADR para implementarse después.

En otras palabras:

> **El piloto manda. La arquitectura se adapta al piloto, no al revés.**

Creo que ésta será una de las decisiones más importantes del proyecto.

---

# Comienza oficialmente el Programa Piloto

```
PROGRAM

PKB Pilot Program

Proyecto Piloto

MIPSP Editor
```

Este programa tendrá un único objetivo:

> Conseguir que MIPSP quede completamente administrado por el PKB.

Hasta no lograrlo, no abriremos nuevas líneas de desarrollo.

---

# Objetivos del piloto

No vamos a "copiar archivos".

Vamos a demostrar que el PKB es capaz de administrar un proyecto complejo.

El piloto estará terminado únicamente cuando podamos responder preguntas como:

* ¿Cuántos requisitos tiene MIPSP?
* ¿Qué ADR afectan un módulo determinado?
* ¿Qué documentos dependen de un estándar?
* ¿Qué componentes todavía no tienen pruebas?
* ¿Qué chats dieron origen a una decisión?
* ¿Qué requisitos aún no están implementados?
* ¿Qué cambios romperían el proyecto?

Si el PKB responde estas preguntas, el piloto habrá sido exitoso.

---

# El activo más importante

Hasta ahora pensábamos que el proyecto era el código.

En realidad no.

El activo más valioso son **las conversaciones**.

En ellas está:

* el razonamiento;
* las decisiones;
* los cambios de rumbo;
* los ADR implícitos;
* la evolución de la arquitectura.

Por ello la ingestión debe comenzar allí.

---

# Nueva estrategia

Hasta ahora imaginábamos:

```
Proyecto

↓

Markdown

↓

PKB
```

Creo que debemos cambiar.

La estrategia correcta será:

```
Chats

↓

Knowledge Extraction

↓

Knowledge Objects

↓

Project

↓

PKB
```

Es un cambio enorme.

---

# La verdadera fuente del proyecto

El proyecto MIPSP realmente existe en tres lugares.

```
GitHub

+

Conversaciones ChatGPT

+

Documentos
```

Los tres deben fusionarse.

---

# Nueva arquitectura del piloto

```
                 MIPSP

        ┌─────────┼─────────┐

        ▼         ▼         ▼

     Chats     GitHub     Files

        │         │         │

        └─────────┼─────────┘

                  ▼

         Ingestion Pipeline

                  ▼

       Knowledge Extraction

                  ▼

      Knowledge Registry

                  ▼

         Traceability Graph

                  ▼

             PKB
```

Éste será el primer flujo completo.

---

# EPIC PILOT-001

## Conversational Knowledge Extraction

Ésta será la primera épica del piloto.

Y creo que será la más importante de todo el proyecto.

---

## Objetivo

Transformar todas las conversaciones del proyecto MIPSP en conocimiento estructurado.

No vamos a guardar conversaciones.

Vamos a extraer conocimiento.

---

# ¿Qué extraeremos?

Cada conversación puede contener distintos tipos de objetos.

Por ejemplo.

```
Requirement

Architecture Decision

Idea

Risk

Problem

Solution

Question

Constraint

Assumption

Research

Standard

Template

Task

Roadmap

Milestone

Issue
```

Es decir, un mismo chat puede originar decenas de objetos de conocimiento.

---

# Nuevo objeto

```
Conversation

↓

Conversation Segment

↓

Knowledge Candidate

↓

Knowledge Object
```

La conversación deja de ser un documento monolítico.

Se convierte en una fuente de conocimiento.

---

# Pipeline del piloto

Propongo exactamente este flujo.

```
Conversación

↓

Segmentación

↓

Clasificación

↓

Extracción

↓

Normalización

↓

Revisión

↓

Knowledge Registry

↓

Relationships

↓

Project Manifest
```

Éste será el corazón del piloto.

---

# ¿Qué NO haremos?

No vamos a importar miles de líneas de conversación literalmente.

Eso produciría ruido.

Extraeremos únicamente el conocimiento.

---

# La gran decisión

Creo que aquí está la mayor oportunidad de todo el PKB.

Hasta ahora imaginábamos que los objetos nacían de Markdown.

Ahora veo algo mejor.

Los objetos nacen del razonamiento.

Markdown será únicamente un formato de persistencia.

---

# El plan operativo

A partir de este momento propongo organizar el trabajo en **ocho etapas**, con entregables verificables.

## ETAPA 1 — Inventario de conversaciones

Objetivo:

Construir el catálogo maestro de todas las conversaciones de MIPSP.

Entregables:

* Índice de conversaciones.
* Identificador único.
* Fecha.
* Tema.
* Estado de ingestión.
* Prioridad.

---

## ETAPA 2 — Extracción de conocimiento

Para cada conversación identificaremos:

* decisiones;
* requisitos;
* riesgos;
* tareas;
* arquitectura;
* estándares;
* dependencias.

---

## ETAPA 3 — Normalización

Convertiremos esos elementos en objetos normalizados del PKB.

---

## ETAPA 4 — Relacionamiento

Crearemos las relaciones entre objetos.

---

## ETAPA 5 — Construcción del grafo

Obtendremos el primer grafo de conocimiento de MIPSP.

---

## ETAPA 6 — Validación

Ejecutaremos el motor de validación sobre el proyecto.

---

## ETAPA 7 — Publicación

Generaremos el manifiesto, inventario e informes.

---

## ETAPA 8 — Retroalimentación

Todo problema detectado dará origen a:

* un Issue;
* un ADR;
* o una mejora planificada para el PKB.

De este modo, el piloto será el mecanismo que haga evolucionar la plataforma.

# Un ajuste importante a la estrategia

Hay un aspecto que sí modificaría respecto a lo que habíamos planteado anteriormente. En un principio pensábamos que la ingestión debía partir de los documentos existentes. Ahora creo que el orden correcto es diferente:

1. **Conversaciones** (porque contienen el contexto y las decisiones).
2. **Repositorio GitHub** (porque contiene la implementación).
3. **Documentación existente** (porque consolida el conocimiento).

Así preservaremos primero el contexto de las decisiones y después las vincularemos con el código y la documentación.

## La siguiente respuesta cambiará el tipo de trabajo

A partir de este punto propongo dejar de elaborar planes generales y comenzar la **ejecución operativa del piloto**.

La siguiente fase ya no será una propuesta arquitectónica. Será la construcción de los primeros activos reales del proyecto piloto MIPSP: el **Inventario Maestro de Conversaciones**, el **Manifiesto del Proyecto**, el **Catálogo Inicial de Objetos de Conocimiento** y la **Matriz de Trazabilidad** que servirán como base para la ingestión efectiva dentro del PKB.

En mi opinión, ese será el momento en que el PKB dejará de ser una infraestructura prometedora y comenzará a demostrar, con un proyecto real, que puede administrar conocimiento de manera útil y sostenible.
