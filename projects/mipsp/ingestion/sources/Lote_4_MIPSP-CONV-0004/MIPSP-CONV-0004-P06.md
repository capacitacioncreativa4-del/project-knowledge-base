---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 6
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente propuesta. Adelante con la siguiente fase

Perfecto. Esta fase es, en mi opinión, la que determina el éxito del proyecto. Una migración sin inventario termina generando duplicados, contradicciones y documentos difíciles de mantener. Un buen inventario convierte el PKB en una verdadera base de conocimiento.

A partir de aquí cambiaremos de enfoque: **dejaremos de pensar en conversaciones y empezaremos a pensar en activos de conocimiento**.

---

# FASE 3

# Inventario Maestro de Activos de Conocimiento (Knowledge Asset Inventory)

## Objetivo

Construir un catálogo completo de todo el conocimiento existente para responder, en cualquier momento, preguntas como:

* ¿Qué sabemos?
* ¿Dónde está documentado?
* ¿Cuál es la versión vigente?
* ¿Qué información falta?
* ¿Qué información está duplicada?
* ¿Qué documentos dependen de otros?
* ¿Qué conversaciones ya fueron consolidadas?

Este inventario será el "catálogo bibliográfico" del PKB.

---

# Entregable 3.1 – Modelo conceptual

Ya no administraremos conversaciones.

Administraremos **Activos de Conocimiento (Knowledge Assets)**.

Un activo puede ser:

* una conversación
* un documento
* un manual
* un requisito
* una investigación
* una decisión arquitectónica
* un diagrama
* un modelo de datos
* un archivo fuente
* una plantilla
* una norma
* una presentación
* un conjunto de imágenes

Todos ellos se registrarán con el mismo modelo.

---

# Entregable 3.2 – Identificador único

Cada activo tendrá un identificador persistente.

Por ejemplo:

```text
KA-000001
KA-000002
KA-000003
...
```

Donde **KA** significa **Knowledge Asset**.

El identificador nunca cambiará, aunque el archivo cambie de nombre o de ubicación.

---

# Entregable 3.3 – Ficha del Activo

Cada activo tendrá una ficha con metadatos normalizados.

| Campo                | Descripción                          |
| -------------------- | ------------------------------------ |
| KA-ID                | Identificador único                  |
| Nombre               | Nombre descriptivo                   |
| Proyecto             | Proyecto al que pertenece            |
| Categoría            | Documento, conversación, norma, etc. |
| Estado               | Draft, Review, Approved, Archived    |
| Responsable          | Autor o mantenedor                   |
| Fecha de creación    | Alta del activo                      |
| Última actualización | Última modificación                  |
| Versión              | Semántica (v1.2.0, etc.)             |
| Fuente               | Chat, archivo, repositorio           |
| Documentos derivados | Activos generados a partir de él     |
| Dependencias         | Otros activos relacionados           |
| Observaciones        | Información adicional                |

---

# Entregable 3.4 – Clasificación

Propondría una taxonomía transversal.

| Código | Categoría                  |
| ------ | -------------------------- |
| CHAT   | Conversaciones             |
| DOC    | Documentación              |
| REQ    | Requisitos                 |
| ADR    | Decisiones arquitectónicas |
| EPIC   | Épicas                     |
| CU     | Casos de uso               |
| API    | Interfaces                 |
| DB     | Modelo de datos            |
| UI     | Interfaces gráficas        |
| TEST   | Pruebas                    |
| PLAN   | Planeación                 |
| MAN    | Manuales                   |
| LEG    | Normativa                  |
| RES    | Investigación              |
| IMG    | Recursos gráficos          |
| TMP    | Plantillas                 |
| CODE   | Código fuente              |

Esto permitirá búsquedas homogéneas.

---

# Entregable 3.5 – Estados de migración

Cada conversación tendrá un estado específico.

| Estado          | Significado                    |
| --------------- | ------------------------------ |
| No inventariada | Aún no registrada              |
| Inventariada    | Registrada en el catálogo      |
| Analizada       | Se identificó su contenido     |
| Fragmentada     | Se dividió en activos          |
| Consolidada     | Todo el conocimiento migrado   |
| Verificada      | Revisión final completada      |
| Archivada       | Conservada solo como histórico |

Así podremos saber exactamente en qué punto se encuentra cada conversación.

---

# Entregable 3.6 – Matriz Maestra del Inventario

Esta será probablemente la tabla más importante de todo el PKB.

| KA-ID     | Proyecto     | Activo               | Tipo | Estado    | Fuente       | Consolidado |
| --------- | ------------ | -------------------- | ---- | --------- | ------------ | ----------- |
| KA-000001 | MIPSP        | Arquitectura Inicial | CHAT | Analizada | Conversación | Sí          |
| KA-000002 | MIPSP        | Arquitectura General | DOC  | Approved  | Markdown     | Sí          |
| KA-000003 | MIPSP        | EPIC-01              | DOC  | Approved  | Markdown     | Sí          |
| KA-000004 | Condominios  | Reglamento           | LEG  | Approved  | PDF          | Sí          |
| KA-000005 | Manualidades | Estrategia Comercial | DOC  | Review    | Conversación | No          |

Esta matriz será la "portada" del conocimiento.

---

# Entregable 3.7 – Índice por proyectos

Cada proyecto tendrá su propio inventario.

Por ejemplo:

```text
MIPSP

KA-000001

KA-000002

KA-000003

KA-000004

KA-000005

...
```

Mientras que el PKB tendrá un inventario global que permita localizar cualquier activo.

---

# Entregable 3.8 – Grafo de conocimiento

Además del inventario tabular, construiremos un modelo de relaciones.

```text
Proyecto
     │
     ▼
Arquitectura
     │
     ▼
EPIC
     │
     ▼
Caso de Uso
     │
 ┌───┼────┐
 ▼   ▼    ▼
API UI BaseDatos
     │
     ▼
Pruebas
     │
     ▼
Manual
```

Cada activo podrá tener múltiples relaciones, convirtiendo el PKB en un grafo navegable.

---

# Entregable 3.9 – Indicadores de calidad

Cada activo recibirá una puntuación basada en criterios objetivos.

| Indicador         | Escala |
| ----------------- | ------ |
| Completitud       | 0–100  |
| Actualidad        | 0–100  |
| Consistencia      | 0–100  |
| Trazabilidad      | 0–100  |
| Reutilización     | 0–100  |
| Calidad editorial | 0–100  |

Esto permitirá identificar rápidamente qué documentos requieren atención.

---

# Entregable 3.10 – Backlog de migración

Con el inventario podremos generar un plan de trabajo priorizado.

| Prioridad | Proyecto     | Activo       | Complejidad | Horas estimadas |
| --------- | ------------ | ------------ | ----------- | --------------- |
| Alta      | MIPSP        | Arquitectura | Alta        | 6               |
| Alta      | MIPSP        | EPIC-02      | Media       | 3               |
| Media     | Condominios  | Reglamento   | Baja        | 2               |
| Media     | Manualidades | Estrategia   | Baja        | 1               |

Este backlog facilitará la planificación de cada sesión de trabajo.

---

# Una mejora que considero especialmente valiosa

Hasta ahora hemos tratado el PKB como un repositorio documental. Yo añadiría un nivel más: un **Registro Maestro de Decisiones (Decision Register)**.

No todas las conversaciones producen requisitos o manuales; muchas contienen decisiones que afectan al diseño futuro. Por ello, propongo crear un catálogo independiente donde cada decisión tenga un identificador (por ejemplo, `DEC-0001`), una justificación, las alternativas evaluadas, la decisión adoptada, su impacto y los documentos afectados. Esto permitirá reconstruir el razonamiento detrás de la evolución de cada proyecto sin depender de releer conversaciones completas.

## Próxima fase: Fase 4 – Migración del conocimiento

Con el inventario definido, estaremos en condiciones de iniciar la migración propiamente dicha. Ahí estableceremos el procedimiento estándar para transformar conversaciones extensas en documentos consolidados, con reglas para extraer información, resolver duplicados, registrar decisiones y validar la calidad del resultado. Esa metodología será la que aplicaremos sistemáticamente a proyectos como **MIPSP**, **Kit Editorial Maestro**, **Condominios** y **SIM-PYME**. Una vez definida, podremos avanzar de forma repetible y con trazabilidad sobre cualquier proyecto futuro.
