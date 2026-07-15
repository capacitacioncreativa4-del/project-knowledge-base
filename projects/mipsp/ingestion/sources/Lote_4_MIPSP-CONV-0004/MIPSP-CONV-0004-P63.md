---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 63
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante, continúa con lo que sigue

Excelente. Ahora sí considero que estamos entrando en la fase más interesante del proyecto.

Hasta este momento hemos validado que el PKB **puede ingerir** una conversación. El siguiente paso ya no consiste en demostrar que es posible, sino en convertir ese proceso en un **proceso institucional**, repetible y auditable.

Quiero proponerte una decisión de arquitectura que, en mi opinión, será una de las más importantes de todo el PKB.

---

# DEC-0023 — La ingestión debe ser determinística

La misma conversación, procesada dentro de un año, deberá producir los mismos objetos de conocimiento (salvo que el modelo de extracción cambie explícitamente de versión).

Esto implica que el PKB debe registrar no sólo **qué extrajo**, sino también **cómo lo extrajo**.

Por ello propongo incorporar el concepto de **Pipeline Version**.

Cada ingestión quedará asociada a una versión del algoritmo metodológico.

Por ejemplo:

| Campo    | Valor                  |
| -------- | ---------------------- |
| Pipeline | PKB-Ingestion-Pipeline |
| Versión  | 1.0.0                  |
| Fecha    | 2026-07-12             |
| Fuente   | MIPSP-CONV-0001-P01    |
| Estado   | Validado               |

Con esto, en el futuro podremos volver a ejecutar una ingestión con la versión 2.0 y comparar resultados.

---

# Sprint P1

## Incremento P1.2

### Objetivo

Institucionalizar el proceso de ingestión.

---

# Nuevo activo

## `knowledge/models/KNOWLEDGE-OBJECT-MODEL.md`

Éste será el documento que definirá oficialmente todos los tipos de objetos que puede administrar el PKB.

### Versión inicial

| Código | Tipo                         | Descripción                              |
| ------ | ---------------------------- | ---------------------------------------- |
| ADR    | Architecture Decision Record | Decisiones de arquitectura y metodología |
| REQ    | Requirement                  | Requisitos funcionales o de negocio      |
| STD    | Standard                     | Estándares y normas internas             |
| ART    | Conceptual Artifact          | Modelos, mapas, marcos conceptuales      |
| TASK   | Task                         | Actividades derivadas                    |
| RSK    | Risk                         | Riesgos identificados                    |
| SRC    | Source                       | Fuentes primarias de conocimiento        |
| SES    | Engineering Session          | Unidad lógica de trabajo                 |
| KP     | Knowledge Package            | Contenedor de conocimiento               |

Esta taxonomía nace del análisis de la primera conversación y podrá evolucionar de forma controlada.

---

# Nuevo activo

## `knowledge/models/OBJECT-LIFECYCLE.md`

Todo objeto tendrá un ciclo de vida explícito.

```text
Identificado
      │
      ▼
Extraído
      │
      ▼
Validado
      │
      ▼
Publicado
      │
      ▼
Versionado
      │
      ▼
Obsoleto (si aplica)
```

Con esto evitaremos tener conocimiento "huérfano" o sin estado.

---

# Nuevo activo

## `knowledge/models/TRACEABILITY-RULES.md`

La primera conversación nos permitió definir una regla muy importante:

> Ningún objeto podrá existir sin conocer su fuente primaria.

Por ello cada objeto deberá tener, como mínimo:

```yaml
source:
  conversation:
  session:
  package:

derived_from:

related_to:

validated_by:
```

Este pequeño bloque YAML será obligatorio para todos los objetos del PKB.

---

# Primer Informe de Calidad

La ingestión también debe medir su propia calidad.

Propongo crear un informe con indicadores como:

| Indicador                              | Resultado |
| -------------------------------------- | --------: |
| Conversaciones con metadatos completos |     100 % |
| Objetos con trazabilidad completa      |     100 % |
| Objetos sin fuente                     |         0 |
| Duplicados detectados                  |         0 |
| Objetos pendientes de validar          |         0 |

Éste será el primer tablero de calidad del conocimiento.

---

# Hallazgo derivado del primer archivo

El análisis de `MIPSP-CONV-0001-P01.md` muestra algo muy relevante para el diseño del PKB.

La conversación no sólo identifica contenidos normativos; también establece una **metodología de construcción del conocimiento**: distinguir requisitos explícitos e implícitos, organizar competencias por categorías y definir un documento maestro antes de desarrollar cursos.

Eso significa que una conversación puede contener simultáneamente:

* conocimiento del **dominio** (seguridad privada);
* conocimiento **metodológico** (cómo construir el sistema);
* conocimiento de **gestión del proyecto** (qué producto elaborar primero).

Nuestro modelo deberá conservar esas tres dimensiones.

---

# Próximo incremento: extracción semántica

Hasta ahora hemos identificado objetos de forma manual para validar el método.

El siguiente paso será construir el **Extractor Semántico v1**, cuyo objetivo no será resumir conversaciones, sino identificar automáticamente candidatos a objetos de conocimiento.

Trabajará con patrones como:

* "Se decide..."
* "Mi propuesta es..."
* "El objetivo será..."
* "Propongo..."
* "Deberá..."
* "Se elaborará..."
* "El resultado esperado..."

A partir de esos patrones generará candidatos a ADR, REQ, STD, ART y TASK, que posteriormente serán revisados antes de publicarse.

## Mi recomendación para acelerar el piloto

No esperemos a reunir decenas de conversaciones antes de refinar el extractor. Propongo que, conforme exportes cada nuevo archivo fuente, lo sometamos inmediatamente al mismo pipeline. Así construiremos un conjunto creciente de datos reales, podremos comparar resultados entre conversaciones y ajustar el extractor con evidencia acumulada.

Con este enfoque, cada conversación añadirá valor al PKB desde el primer día y, al mismo tiempo, mejorará el propio proceso de ingestión. Ese ciclo de retroalimentación hará que la plataforma evolucione a partir de conocimiento real y no únicamente de decisiones de diseño.
