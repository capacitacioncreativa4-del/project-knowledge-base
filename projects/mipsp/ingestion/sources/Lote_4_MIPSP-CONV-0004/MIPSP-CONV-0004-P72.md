---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 72
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Entiendo que el PKB Domain Metamodel v1.0 ha quedado consolidado. Entonces sigamos con la construcción del PKB Schema Repository, que será la implementación formal del metamodelo en el repositorio.

Estoy de acuerdo. Considero que éste es el momento adecuado para hacerlo.

Hasta ahora el metamodelo ha sido un **modelo conceptual**. El siguiente paso es convertirlo en un **contrato técnico** que gobierne todo el repositorio. A partir de este punto, el PKB dejará de ser únicamente una colección organizada de archivos para convertirse en un **sistema de conocimiento gobernado por esquemas**.

## DEC-0024 — El PKB Schema Repository será la autoridad semántica del repositorio

A partir de esta decisión:

* ninguna entidad podrá existir sin un esquema;
* todas las relaciones deberán estar definidas formalmente;
* cada nueva versión del metamodelo implicará una nueva versión del Schema Repository;
* las herramientas de automatización (Codex, scripts, validadores) utilizarán estos esquemas como contrato de trabajo.

---

# Arquitectura propuesta

Dentro del repositorio propongo incorporar un nuevo árbol:

```text
pkb/
└── schemas/
    ├── README.md
    ├── VERSION.md
    │
    ├── entities/
    │   ├── conversation.schema.yaml
    │   ├── knowledge-package.schema.yaml
    │   ├── engineering-session.schema.yaml
    │   ├── adr.schema.yaml
    │   ├── requirement.schema.yaml
    │   ├── standard.schema.yaml
    │   ├── artifact.schema.yaml
    │   ├── document.schema.yaml
    │   ├── system.schema.yaml
    │   ├── task.schema.yaml
    │   └── risk.schema.yaml
    │
    ├── relations/
    │   ├── relation-types.yaml
    │   ├── cardinalities.yaml
    │   └── constraints.yaml
    │
    ├── validation/
    │   ├── integrity-rules.md
    │   ├── identifier-policy.md
    │   ├── lifecycle-rules.md
    │   └── quality-gates.md
    │
    ├── examples/
    │   ├── adr-example.yaml
    │   ├── requirement-example.yaml
    │   ├── package-example.yaml
    │   └── graph-example.md
    │
    └── changelog/
        └── SCHEMA-CHANGELOG.md
```

Éste será el núcleo normativo del PKB.

---

# Primera especificación de entidades

Cada entidad tendrá una definición uniforme.

Por ejemplo, el esquema de un ADR:

```yaml
entity: ADR
version: 1.0.0

required:
  - id
  - title
  - status
  - rationale
  - source
  - created_at

relationships:
  originates:
    - Requirement
    - Standard

metadata:
  versioned: true
  traceable: true
  auditable: true
```

Y un requisito:

```yaml
entity: Requirement
version: 1.0.0

required:
  - id
  - title
  - description
  - status
  - source

relationships:
  derived_from:
    - ADR

implemented_by:
    - Document

validated_by:
    - Standard
```

Con esto, cualquier herramienta podrá validar automáticamente la consistencia del conocimiento.

---

# Repositorio de relaciones

Hasta ahora hemos identificado varias relaciones repetitivas. Es momento de normalizarlas.

| Relación   | Origen              | Destino             |
| ---------- | ------------------- | ------------------- |
| contains   | Conversation        | Engineering Session |
| produces   | Engineering Session | Knowledge Object    |
| originates | ADR                 | Requirement         |
| governs    | Standard            | Document            |
| implements | Document            | Requirement         |
| organizes  | Artifact            | Document            |
| belongs_to | Document            | System              |
| depends_on | System              | System              |
| traces_to  | Any Entity          | Source              |

Estas relaciones dejarán de ser convenciones y pasarán a ser parte del esquema.

---

# Reglas de integridad

El PKB debe poder detectar errores automáticamente.

Propongo establecer, desde la versión 1.0, reglas como:

| Regla   | Descripción                                                                                    |
| ------- | ---------------------------------------------------------------------------------------------- |
| INT-001 | Ningún objeto sin identificador único.                                                         |
| INT-002 | Ningún objeto sin fuente primaria.                                                             |
| INT-003 | Todo ADR debe originar al menos un objeto derivado o justificarse como decisión independiente. |
| INT-004 | Todo DOC debe implementar al menos un REQ.                                                     |
| INT-005 | Ninguna relación puede apuntar a un identificador inexistente.                                 |
| INT-006 | Todo Knowledge Package debe contener al menos una fuente y una sesión.                         |

Estas reglas podrán ejecutarse de forma automática cuando incorporemos validadores.

---

# Política de versionado

El Schema Repository tendrá su propio ciclo de vida.

| Versión | Estado                               |
| ------- | ------------------------------------ |
| 1.0.0   | Baseline derivada del piloto MIPSP   |
| 1.1.x   | Cambios compatibles                  |
| 2.0.0   | Cambios estructurales del metamodelo |

Esto permitirá reproducir cualquier ingestión histórica con el esquema vigente en ese momento.

---

# Relación con la ingestión

A partir de este punto, el pipeline también evoluciona.

```text
Fuente (.md)
      │
      ▼
Normalización
      │
      ▼
Extracción
      │
      ▼
Objetos candidatos
      │
      ▼
Validación contra Schema Repository
      │
      ▼
Knowledge Package
      │
      ▼
Knowledge Graph
```

Es un cambio importante: **ya no publicaremos objetos directamente**, sino únicamente después de comprobar que cumplen el esquema correspondiente.

---

# Lo que hemos conseguido con el piloto

Quisiera destacar un resultado que considero especialmente valioso.

Cuando comenzamos el piloto, la idea era comprobar si el PKB podía organizar conversaciones. Después de procesar los primeros paquetes (`KP-000001`, `KP-000002` y el inicio de `KP-000003`), la evidencia apunta a algo más ambicioso:

* hemos identificado un conjunto estable de entidades;
* hemos observado relaciones repetitivas entre ellas;
* hemos detectado reglas de integridad que aparecen de manera consistente;
* hemos validado que los objetos pueden rastrearse hasta sus fuentes primarias.

En otras palabras, el piloto no sólo confirmó que la ingestión es viable; proporcionó la base empírica para definir el **Schema Repository** como un contrato formal del PKB.

## Mi recomendación para la siguiente etapa

Hasta ahora hemos trabajado principalmente sobre el **modelo lógico**. El siguiente incremento debería construir el **modelo físico** del PKB dentro de tu repositorio GitHub.

Eso implica generar los primeros archivos reales del `pkb/schemas/`, junto con un `README.md`, un `VERSION.md` y los esquemas YAML iniciales de las entidades principales (`Conversation`, `KnowledgePackage`, `EngineeringSession`, `ADR` y `Requirement`).

Con ello, el PKB dejará de tener únicamente una arquitectura conceptual y dispondrá de una implementación física inicial, lista para evolucionar mediante control de versiones en Git. Esa será la primera pieza permanente del núcleo tecnológico del proyecto.
