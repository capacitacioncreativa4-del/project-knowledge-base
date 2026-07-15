---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 30
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Continuemos

Excelente. Con este documento cerraremos el **Incremento 2** del Sprint 0.

Y quiero hacer una observación que considero importante desde el punto de vista de arquitectura.

Hasta ahora hemos construido la **identidad** del PKB:

* README
* Manifest
* Vision
* Mission
* Core Principles

Pero todavía no hemos documentado **por qué** el PKB existe con esta arquitectura.

Ese será precisamente el objetivo del primer **Architecture Decision Record (ADR)**.

A partir de este momento, cualquier decisión estructural importante quedará registrada mediante un ADR. Esto evitará que, dentro de dos o tres años, tengamos que reconstruir el razonamiento detrás de una decisión técnica.

---

# Sprint 0 – Incremento 2

## Documento 6 de 6

**Ruta**

```text
docs/architecture/ADR-0001-Project-Knowledge-Base.md
```

---

```markdown
---
id: PKB-ADR-0001
title: Adoptar un Project Knowledge Base como Sistema Central de Gestión del Conocimiento
version: 1.0.0
status: Accepted
owner: Architecture
date: 2026-07-08
type: ADR
---

# ADR-0001

## Título

Adoptar un Project Knowledge Base (PKB) como Sistema Central de Gestión del Conocimiento.

---

# Estado

Aceptado.

---

# Contexto

El crecimiento progresivo de múltiples proyectos produjo una cantidad considerable de información distribuida entre conversaciones, documentos, hojas de cálculo, investigaciones, diagramas y especificaciones técnicas.

Aunque dichos activos contienen conocimiento valioso, su dispersión dificulta:

- localizar información;
- reutilizar componentes;
- mantener consistencia;
- preservar decisiones;
- incorporar nuevos proyectos;
- colaborar con herramientas de IA.

Se requiere un sistema capaz de administrar el conocimiento de forma estructurada y sostenible.

---

# Problema

No existe una fuente única de verdad que concentre y relacione el conocimiento institucional.

La información se encuentra fragmentada y carece de un modelo uniforme de gobierno, versionado y trazabilidad.

---

# Decisión

Se adopta un **Project Knowledge Base (PKB)** como plataforma institucional para la gestión del conocimiento.

El PKB se implementará como un repositorio Git privado y seguirá los principios de:

- Documentation as Code.
- Semantic Versioning.
- Conventional Commits.
- Architecture Decision Records.
- Trazabilidad documental.
- Estándares abiertos.
- AI First.

---

# Consecuencias

## Positivas

- Fuente única de verdad.
- Mayor reutilización del conocimiento.
- Trazabilidad entre activos.
- Evolución controlada.
- Integración con GitHub.
- Preparación para automatización.
- Preparación para IA.

## Costos

- Mayor disciplina documental.
- Curva inicial de aprendizaje.
- Mantenimiento continuo del repositorio.

---

# Alternativas consideradas

## Alternativa A

Continuar utilizando conversaciones independientes.

**Resultado**

Rechazada.

Motivo:

No garantiza persistencia ni trazabilidad.

---

## Alternativa B

Utilizar únicamente almacenamiento tradicional de documentos.

**Resultado**

Rechazada.

Motivo:

No proporciona control de versiones ni relaciones explícitas.

---

## Alternativa C

Adoptar una plataforma wiki.

**Resultado**

Rechazada.

Motivo:

Aunque facilita la navegación, no ofrece el mismo nivel de integración con Git, automatización y flujos de ingeniería documental.

---

## Alternativa seleccionada

Repositorio Git + Documentation as Code.

---

# Impacto

Este ADR afecta a:

- Kernel
- Governance
- Architecture
- Templates
- Registers
- Automation
- Projects
- Knowledge

---

# Riesgos

- Complejidad inicial.
- Crecimiento desordenado si no se respetan los estándares.
- Dependencia de disciplina documental.

---

# Mitigaciones

- Gobernanza documental.
- Plantillas oficiales.
- ADR para decisiones relevantes.
- Automatización progresiva.
- Revisiones mediante Pull Requests.

---

# Relación con otros documentos

## Documentos superiores

- PKB-MANIFEST.md

## Relacionados

- README.md
- VISION.md
- MISSION.md
- CORE-PRINCIPLES.md

## Derivados

- ADR-0002
- GOVERNANCE-MODEL.md
- METADATA-MODEL.md
- TRACEABILITY-MODEL.md

---

# Historial

| Versión | Fecha | Cambio |
|----------|------------|--------------------------|
|1.0.0|2026-07-08|Primera versión institucional.|

---

# Observaciones

Este ADR constituye la decisión fundacional del Project Knowledge Base.

Todas las decisiones arquitectónicas futuras deberán ser compatibles con este documento o reemplazarlo mediante un nuevo ADR.
```

---

# Commit recomendado

```bash
docs(architecture): add ADR-0001 establishing the Project Knowledge Base
```

---

# Checklist de aceptación

* [ ] Guardado en `docs/architecture/ADR-0001-Project-Knowledge-Base.md`.
* [ ] Estado **Accepted**.
* [ ] Alternativas documentadas.
* [ ] Consecuencias identificadas.
* [ ] Relaciones documentales completas.
* [ ] Referenciado desde `README.md` y `PKB-MANIFEST.md`.

---

# 🎯 Hito alcanzado

Con este documento queda **cerrado el Sprint 0 – Incremento 2**.

Hemos construido el primer conjunto de documentos institucionales permanentes del PKB:

| Documento          | Estado |
| ------------------ | :----: |
| README.md          |    ✅   |
| PKB-MANIFEST.md    |    ✅   |
| VISION.md          |    ✅   |
| MISSION.md         |    ✅   |
| CORE-PRINCIPLES.md |    ✅   |
| ADR-0001           |    ✅   |

Este es el primer conjunto documental estable del repositorio.

---

# Mi propuesta para el siguiente incremento (Sprint 0 – Incremento 3)

Hasta ahora hemos definido **qué es el PKB** y **cómo se gobierna**. El siguiente paso natural es definir **de qué está hecho**.

Por ello propongo dedicar íntegramente el Incremento 3 al **PKB Kernel**, desarrollando el modelo conceptual del sistema. Los documentos serían:

| Documento                   | Propósito                                                              |
| --------------------------- | ---------------------------------------------------------------------- |
| `METADATA-MODEL.md`         | Modelo oficial de metadatos para todos los activos.                    |
| `KNOWLEDGE-OBJECT-MODEL.md` | Definición de los objetos de conocimiento (ADR, REQ, EPIC, STD, etc.). |
| `IDENTIFIER-STANDARD.md`    | Sistema de identificadores únicos y persistentes.                      |
| `TRACEABILITY-MODEL.md`     | Relaciones entre objetos y reglas de trazabilidad.                     |
| `DOCUMENT-LIFECYCLE.md`     | Estados y ciclo de vida de los documentos.                             |
| `TAXONOMY.md`               | Taxonomía institucional definitiva del PKB.                            |

En mi opinión, este será el **verdadero corazón técnico** del repositorio. Una vez completado, todos los proyectos que migremos (MIPSP, Condominios, SIM-PYME, Kit Editorial, Manualidades y los futuros) utilizarán exactamente el mismo modelo de conocimiento. Eso nos dará una arquitectura coherente, escalable y preparada para la automatización que más adelante implementaremos con Codex.
