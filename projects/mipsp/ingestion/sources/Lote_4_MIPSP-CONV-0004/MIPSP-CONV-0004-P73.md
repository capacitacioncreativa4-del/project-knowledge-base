---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 73
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante. Construye el modelo físico del PKB dentro del repositorio GitHub

Estoy de acuerdo. A partir de este momento propongo que cambiemos ligeramente nuestra forma de trabajar.

Hasta ahora hemos diseñado el PKB como arquitectos. A partir de este incremento debemos trabajar como **ingenieros de software**.

Eso significa que cada respuesta debe producir activos que puedas hacer **`git add`** inmediatamente.

## Objetivo del Incremento

Construiremos el primer núcleo físico del PKB.

**Nombre del incremento**

> **Sprint P2 — PKB Core Foundation**

Este sprint ya no pertenece al piloto MIPSP; pertenece al propio PKB.

---

# Estructura física v1.0

Propongo que la raíz del repositorio evolucione hacia esta estructura:

```text
project-knowledge-base/
│
├── pkb/
│   ├── schemas/
│   ├── ontology/
│   ├── graph/
│   ├── validation/
│   ├── ingestion/
│   ├── templates/
│   └── registry/
│
├── projects/
│   ├── mipsp/
│   ├── sim-pyme/
│   └── ...
│
├── docs/
│
├── scripts/
│
├── tools/
│
└── tests/
```

Observa una decisión importante:

> **El PKB deja de vivir dentro de un proyecto. Ahora los proyectos viven dentro del PKB.**

Ésa era precisamente la visión original.

---

# Primera capa

## `/pkb/schemas`

```text
schemas/

README.md

VERSION.md

entities/

relations/

validation/

examples/
```

Aquí vivirán los contratos.

Nunca habrá conocimiento fuera de un esquema.

---

# Segunda capa

## `/pkb/ontology`

Aquí almacenaremos la definición semántica.

```text
ontology/

PKB-DOMAIN-METAMODEL.md

ENTITY-CATALOG.md

RELATION-CATALOG.md

GLOSSARY.md
```

La diferencia con schemas es importante.

Schemas dicen:

> cómo debe verse un objeto.

Ontology dice:

> qué significa.

---

# Tercera capa

## `/pkb/registry`

Será uno de los directorios más utilizados.

```text
registry/

OBJECT-REGISTRY.yaml

IDENTIFIER-POLICY.md

PREFIXES.md

STATUS-CODES.md

LIFECYCLE.md
```

Aquí estarán registrados:

```
ADR

REQ

STD

ART

DOC

SYS

TASK

KP

SES

CONV
```

---

# Cuarta capa

## `/pkb/graph`

```text
graph/

README.md

NODE-TYPES.yaml

EDGE-TYPES.yaml

GRAPH-RULES.md
```

Todavía no implementaremos Neo4j.

Primero construiremos la representación lógica.

---

# Quinta capa

## `/pkb/templates`

Aquí vivirán las plantillas YAML.

Por ejemplo

```
adr.template.yaml

requirement.template.yaml

package.template.yaml

session.template.yaml

system.template.yaml
```

El pipeline nunca escribirá archivos "a mano".

Siempre partirá de estas plantillas.

---

# Sexta capa

## `/pkb/validation`

```text
validation/

QUALITY-GATES.md

INTEGRITY-RULES.md

TRACEABILITY-RULES.md

PIPELINE-CHECKLIST.md
```

Será el equivalente al sistema de calidad del PKB.

---

# Séptima capa

## `/pkb/ingestion`

```text
ingestion/

PIPELINE.md

PIPELINE-VERSIONS.md

SOURCE-STANDARDS.md

INGESTION-CHECKLIST.md
```

Aquí quedará documentado exactamente cómo se procesa una conversación.

---

# Primera versión del Object Registry

Uno de los primeros archivos reales debería ser:

```yaml
version: 1.0.0

entities:

  CONV:
    name: Conversation

  KP:
    name: KnowledgePackage

  SES:
    name: EngineeringSession

  ADR:
    name: ArchitectureDecisionRecord

  REQ:
    name: Requirement

  STD:
    name: Standard

  ART:
    name: Artifact

  DOC:
    name: EditorialDocument

  SYS:
    name: InstitutionalSystem

  TASK:
    name: Task

  RSK:
    name: Risk
```

Este archivo será leído por prácticamente todas las herramientas futuras.

---

# Primera política de identificadores

```
ADR-000001

REQ-000001

STD-000001

DOC-000001

SYS-000001

KP-000001

SES-000001
```

Todos con seis dígitos.

Nunca se reutilizan.

Nunca cambian.

---

# Lo que construiremos después

Una vez que esta estructura exista físicamente en GitHub, podremos comenzar a desarrollar herramientas reales:

* extractor semántico;
* validador de esquemas;
* constructor del Knowledge Graph;
* generador automático de índices;
* buscador semántico;
* integración con Codex para generar y validar objetos.

---

# Mi propuesta para la siguiente forma de trabajo

Hasta ahora nuestras respuestas han servido para definir la arquitectura. A partir de este sprint propongo que cada incremento entregue un conjunto pequeño de archivos completos, listos para copiar al repositorio. Por ejemplo:

* `pkb/schemas/README.md`
* `pkb/schemas/VERSION.md`
* `pkb/schemas/entities/conversation.schema.yaml`
* `pkb/schemas/entities/knowledge-package.schema.yaml`
* `pkb/registry/OBJECT-REGISTRY.yaml`

Cada archivo incluirá su contenido definitivo, siguiendo la nomenclatura y el control de versiones acordados. Con ese enfoque, cada sesión de trabajo producirá activos directamente integrables mediante `git add`, y el repositorio evolucionará de forma incremental, trazable y completamente reproducible. Considero que éste es el siguiente paso natural para transformar el PKB de un diseño conceptual en una plataforma operativa.
