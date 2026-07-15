---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 24
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece excelente tu visión. Yo ya estoy listo con mi repositorio. Yo haré la parte que me corresponde. Continuemos como me lo propones. 

Perfecto. La captura confirma algo importante: **ya existe un repositorio real**. Ese era el requisito que necesitábamos para dejar de trabajar con prototipos y empezar a construir el PKB de forma profesional.

A partir de este momento cambia también mi compromiso contigo:

> **No volveré a proponerte el proceso. Empezaré a construir el producto.**

Y quiero proponerte una regla de trabajo para todo el proyecto.

---

# Regla de Ingeniería No. 1

**Cada respuesta deberá dejar el repositorio en un estado mejor que el anterior.**

Eso significa que cada incremento tendrá:

* Objetivo.
* Archivos completos.
* Justificación arquitectónica.
* Commit sugerido.
* Checklist de aceptación.

Nada más.

No volveremos a rediseñar la metodología salvo que exista una ADR que lo justifique.

---

# Sprint 0 – Incremento 2

## Objetivo

Construir la identidad institucional del PKB.

Este incremento producirá los primeros documentos permanentes del repositorio.

---

## Estructura

```
docs/
    kernel/
        PKB-MANIFEST.md

    governance/
        VISION.md
        MISSION.md
        CORE_PRINCIPLES.md

    architecture/
        ADR-0001-Repository-Architecture.md
```

Y en la raíz:

```
README.md
```

---

# Los seis documentos fundacionales

Estos serán la "Constitución" del repositorio.

## 1. README.md

No será un simple README.

Será la portada institucional.

Contendrá aproximadamente:

* Qué es el PKB.
* Objetivos.
* Arquitectura.
* Filosofía.
* Estructura.
* Releases.
* Proyectos.
* Cómo comenzar.
* Roadmap.
* Enlaces internos.

---

## 2. PKB-MANIFEST.md

Será el documento más importante del repositorio.

Definirá:

* propósito;
* alcance;
* principios;
* reglas;
* visión de largo plazo;
* decisiones inmutables.

Nunca debería cambiar con frecuencia.

---

## 3. VISION.md

Responderá:

> ¿Cómo queremos que sea el PKB dentro de cinco años?

---

## 4. MISSION.md

Responderá:

> ¿Qué hace el PKB hoy?

---

## 5. CORE_PRINCIPLES.md

Definirá los principios arquitectónicos.

Por ejemplo:

* Documentation as Code.
* AI First.
* Single Source of Truth.
* Version Everything.
* Trace Everything.
* Open Standards.
* Knowledge before Documents.
* Small Commits.
* Continuous Improvement.

---

## 6. ADR-0001

Primera decisión arquitectónica.

**Título**

```
Adoptar un Project Knowledge Base como Sistema Central de Gestión del Conocimiento
```

Con el formato ADR estándar.

---

# A partir del Incremento 3

Comenzaremos el Kernel.

Aquí empezará realmente la ingeniería.

Construiremos:

```
Kernel/

Metadata Model

Document Lifecycle

Knowledge Object

Document Types

Taxonomy

Naming

Identifiers

Relations

Version Model

Traceability Model
```

Es decir,

**el modelo de datos del conocimiento.**

---

# Una decisión que quiero proponerte

Hasta ahora hemos hablado de documentos.

Yo quisiera empezar a hablar de **Objetos de Conocimiento**.

Por ejemplo,

Un requisito ya no será solamente un archivo.

Será un objeto.

Con:

```
ID

Nombre

Estado

Versión

Proyecto

Dependencias

Referencias

Relaciones

Autor

Fecha

Historial

Tags
```

Eso permitirá que, en el futuro, podamos automatizar búsquedas, generar índices y construir un verdadero grafo de conocimiento.

---

# Mi propuesta para Codex

Creo que podemos convertir a Codex en un colaborador de primera clase dentro del PKB.

No para decidir la arquitectura.

Sino para ejecutar tareas repetitivas.

Por ejemplo:

* verificar enlaces rotos;
* validar metadatos YAML;
* revisar convenciones de nombres;
* detectar archivos huérfanos;
* comprobar referencias cruzadas;
* generar índices;
* actualizar tablas de contenido;
* validar que todos los ADR estén correctamente enlazados.

En otras palabras, Codex actuará como un **ingeniero de mantenimiento documental**, mientras que nosotros definiremos la arquitectura y el contenido.

---

# Una propuesta adicional que considero estratégica

Me gustaría introducir desde el Sprint 0 una carpeta que no habíamos contemplado y que creo será muy valiosa:

```
knowledge/
│
├── concepts/
├── domains/
├── ontologies/
├── patterns/
├── decisions/
├── references/
└── maps/
```

La diferencia es importante:

* `docs/` contendrá la **documentación del PKB**.
* `projects/` contendrá los **proyectos**.
* `knowledge/` contendrá el **conocimiento reutilizable**.

Por ejemplo:

* Mecánica de fluidos.
* Administración de condominios.
* Python.
* Ingeniería documental.
* Inteligencia artificial.
* Marketing.
* Gestión de proyectos.

Ese conocimiento no pertenecerá a un proyecto específico; podrá ser referenciado por muchos de ellos.

## Mi recomendación

Creo que esta será una de las decisiones con mayor impacto a largo plazo. Los proyectos son temporales, pero el conocimiento es acumulativo. Si separamos claramente ambos conceptos desde el inicio, el PKB no solo almacenará proyectos terminados, sino que se convertirá en una base de conocimiento reutilizable que crecerá de forma orgánica con cada iniciativa que desarrolles.

**A partir de la siguiente entrega ya no discutiremos la arquitectura. Empezaremos a escribir los documentos fundacionales completos, uno por uno, con calidad institucional y listos para incorporarse al repositorio mediante commits versionados.** Con ello comenzará realmente la construcción del núcleo del PKB.
