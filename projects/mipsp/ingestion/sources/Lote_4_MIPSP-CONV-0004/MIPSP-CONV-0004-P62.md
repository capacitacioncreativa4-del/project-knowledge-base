---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 62
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Listo, aquí está el primer archivo MIPSP-CONV-0001-P01.md. Procedamos!

Excelente. **Acabamos de completar el primer hito operativo del PKB.**

El archivo fue localizado correctamente y pude leer su contenido. Eso significa que ya tenemos una **fuente primaria** sobre la cual podemos ejecutar el pipeline de ingestión. 

Quiero hacer una observación importante antes de continuar.

## Primer hallazgo del piloto

La conversación no comienza diseñando cursos.

Comienza tomando una **decisión de ingeniería**:

> En lugar de extraer únicamente temas explícitos, se propone construir un **Mapa Curricular Normativo** que integre requisitos explícitos e implícitos derivados de la legislación y del estándar de competencia. 

Ese descubrimiento confirma que el PKB **no debe almacenar respuestas**, sino **decisiones de diseño**.

Éste es exactamente el tipo de conocimiento que queremos preservar.

---

# Resultado de la Fase 1 — Verificación

| Verificación     | Resultado |
| ---------------- | --------- |
| Archivo legible  | ✔         |
| Encabezado YAML  | ✔         |
| Identificador    | ✔         |
| Proyecto         | ✔         |
| Estado           | Original  |
| Formato Markdown | ✔         |
| Ingestión        | Aprobada  |

**Resultado:** PASS. 

---

# Resultado de la Fase 2 — Identificación de sesiones

En esta primera conversación identifico **tres sesiones de ingeniería**.

## SES-000001 — Definición del enfoque metodológico

**Objetivo**

Determinar cómo abordar la revisión normativa.

**Producto**

Se decide construir un mapa curricular normativo y considerar requisitos explícitos e implícitos. 

---

## SES-000002 — Descubrimiento del dominio

**Objetivo**

Identificar los bloques de capacitación exigidos por la normativa.

**Producto**

Se reconocen categorías de competencias, contenidos obligatorios y principios rectores. 

---

## SES-000003 — Definición del entregable maestro

**Objetivo**

Definir el producto que servirá de base para todo el proyecto.

**Producto**

Se propone desarrollar un **Mapa Maestro de Competencias y Contenidos Curriculares Obligatorios**, estructurado con fundamentos jurídicos, competencias, niveles, horas sugeridas y cursos asociados. 

---

# Resultado de la Fase 3 — Primeros objetos de conocimiento

Con esta primera conversación ya es posible registrar los siguientes objetos.

## ADR-000002

**Título**

Adoptar un Mapa Curricular Normativo como núcleo del proyecto MIPSP.

**Justificación**

La conversación establece que el objetivo inicial no es crear cursos, sino construir primero una ingeniería curricular basada en las fuentes normativas.

---

## REQ-000004

**Título**

El sistema deberá identificar tanto requerimientos formativos explícitos como implícitos.

**Origen**

SES-000001. 

---

## REQ-000005

**Título**

Toda competencia curricular deberá conservar su fundamento jurídico.

**Origen**

SES-000003. 

---

## STD-000001

**Título**

Clasificación curricular por naturaleza del contenido.

Categorías identificadas:

* Temas obligatorios.
* Competencias técnicas.
* Competencias procedimentales.
* Competencias actitudinales.
* Conocimientos jurídicos.
* Habilidades operativas.
* Capacitación especializada.
* Actualización periódica.
* Evaluaciones. 

---

## ART-000001

**Título**

Mapa Maestro de Competencias y Contenidos Curriculares Obligatorios.

Este es el primer artefacto conceptual del proyecto y constituye el documento base para desarrollar posteriormente cursos, manuales y materiales didácticos. 

---

# Resultado de la Fase 4 — Relaciones

El primer subgrafo del proyecto queda así:

```text
MIPSP-CONV-0001-P01
        │
        ▼
MIPSP-SES-000001
        │
        ├──► ADR-000002
        │
        ├──► REQ-000004
        │
        └──► STD-000001
                │
                ▼
ART-000001
```

Este es el primer fragmento del **grafo de conocimiento** construido a partir de una fuente primaria.

---

# Resultado de la Fase 5 — Métricas del piloto

| Indicador                 | Valor |
| ------------------------- | ----: |
| Conversaciones procesadas |     1 |
| Sesiones identificadas    |     3 |
| ADR nuevos                |     1 |
| Requisitos nuevos         |     2 |
| Estándares nuevos         |     1 |
| Artefactos conceptuales   |     1 |
| Relaciones identificadas  |     6 |
| Estado de validación      |  PASS |

---

# Un hallazgo arquitectónico muy importante

La ingestión reveló algo que no habíamos previsto.

Hasta ahora pensábamos que el conocimiento se componía principalmente de ADR, requisitos y estándares. Sin embargo, esta conversación demuestra que existe una cuarta categoría que aparece desde el inicio del proyecto: los **Artefactos Conceptuales**.

Ejemplos:

* Mapa Maestro de Competencias.
* Arquitectura Curricular.
* Modelo de Dominio.
* Marco Metodológico.

Estos no son decisiones ni requisitos; son modelos de alto nivel que organizan el resto del conocimiento. Mi propuesta es incorporarlos como una categoría formal del PKB, con el prefijo **ART** (*Artifact*), ya que serán reutilizables en múltiples proyectos y servirán como puntos de referencia para la trazabilidad.

## Mi propuesta para el siguiente incremento

En lugar de pasar inmediatamente a la siguiente conversación, sugiero consolidar este aprendizaje creando el **PKB Knowledge Object Model v1.0**, basado en evidencia obtenida del piloto. Ese modelo incorporará oficialmente las categorías:

* ADR (Architecture Decision Record)
* REQ (Requirement)
* STD (Standard)
* ART (Conceptual Artifact)
* TASK (Task)
* RSK (Risk)

Con ese modelo estabilizado podremos ingerir el resto de las conversaciones con una taxonomía validada por datos reales, no por hipótesis de diseño. Creo que éste será el primer resultado científico del piloto MIPSP y el punto a partir del cual podremos escalar la ingestión de manera consistente.
