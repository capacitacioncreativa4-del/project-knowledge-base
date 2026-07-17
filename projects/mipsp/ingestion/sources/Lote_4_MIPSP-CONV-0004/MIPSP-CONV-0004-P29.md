---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 29
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Continuemos

Excelente. Ya hemos establecido la identidad del PKB. Ahora vamos a construir el documento que, en mi opinión, será el **"compás arquitectónico"** del proyecto.

A partir de este documento podremos evaluar objetivamente cualquier decisión futura. Si un cambio contradice uno de estos principios, deberá justificarse mediante un ADR.

---

# Sprint 0 — Incremento 2

## Documento 5 de 6

**Ruta**

```text
docs/governance/CORE-PRINCIPLES.md
```

---

```markdown
---
id: PKB-GOV-CORE-PRINCIPLES-001
title: Core Principles
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-08
type: Governance
parent: PKB-KERNEL-MANIFEST-001
---

# Principios Fundamentales del Project Knowledge Base

## Propósito

Este documento define los principios arquitectónicos y documentales que orientan todas las decisiones relativas al diseño, evolución y operación del Project Knowledge Base (PKB).

Estos principios son permanentes y deberán utilizarse como criterios de evaluación para cualquier cambio estructural del sistema.

---

# Principio 1
## Knowledge First

El objetivo principal del PKB es preservar conocimiento, no producir documentos.

Los documentos son únicamente una representación estructurada del conocimiento.

### Implicaciones

- El conocimiento tiene prioridad sobre el formato.
- Debe evitarse la fragmentación innecesaria.
- Toda información debe ser contextualizada.

---

# Principio 2
## Single Source of Truth

Cada dato institucional tendrá una única ubicación oficial.

### Implicaciones

- No duplicar contenido.
- Referenciar en lugar de copiar.
- Mantener consistencia entre documentos.

---

# Principio 3
## Documentation as Code

Toda la documentación será administrada como un activo de ingeniería.

### Implicaciones

- Git obligatorio.
- Versionado obligatorio.
- Revisiones documentales.
- Releases documentales.

---

# Principio 4
## AI First

El repositorio será comprensible tanto para personas como para sistemas inteligentes.

### Implicaciones

- Metadatos estructurados.
- Relaciones explícitas.
- Identificadores persistentes.
- Terminología consistente.

---

# Principio 5
## Trace Everything

Toda decisión importante deberá poder rastrearse.

La trazabilidad deberá permitir responder:

- ¿Qué cambió?
- ¿Por qué?
- ¿Cuándo?
- ¿Quién?
- ¿Qué impacto produjo?

---

# Principio 6
## Modularidad

Los proyectos deberán permanecer desacoplados.

Los componentes reutilizables vivirán fuera de los proyectos.

---

# Principio 7
## Reutilización

Todo conocimiento deberá diseñarse para poder utilizarse en múltiples proyectos.

Antes de crear un nuevo documento deberá verificarse si ya existe un activo reutilizable.

---

# Principio 8
## Evolución Incremental

Las modificaciones se realizarán mediante pequeños incrementos verificables.

Se evitarán cambios masivos difíciles de revisar.

---

# Principio 9
## Open Standards

Siempre que sea posible se utilizarán estándares abiertos.

Formatos preferidos:

- Markdown
- YAML
- Mermaid
- JSON
- CSV
- XLSX

---

# Principio 10
## Long-Term Sustainability

Toda decisión deberá considerar la mantenibilidad del PKB durante los próximos años.

Se privilegiarán soluciones simples, estables y bien documentadas.

---

# Criterios para evaluar decisiones

Antes de aprobar un cambio arquitectónico deberán responderse, como mínimo, las siguientes preguntas:

1. ¿Respeta el Manifest?
2. ¿Respeta estos principios?
3. ¿Mejora la trazabilidad?
4. ¿Reduce la complejidad?
5. ¿Favorece la reutilización?
6. ¿Es compatible con Git?
7. ¿Es compatible con IA?
8. ¿Puede mantenerse a largo plazo?

Si alguna respuesta es negativa, deberá elaborarse un ADR justificando la decisión.

---

# Relaciones

## Documento superior

- PKB-MANIFEST.md

## Documentos relacionados

- VISION.md
- MISSION.md
- ADR-0001-Repository-Architecture.md

## Documentos derivados

- DOCUMENT-STANDARD.md
- METADATA-STANDARD.md
- TRACEABILITY-MODEL.md
- QUALITY-STANDARD.md

---

# Historial de cambios

| Versión | Fecha | Descripción |
|----------|------------|----------------------------|
| 1.0.0 | 2026-07-08 | Primera versión institucional. |
```

---

# Justificación arquitectónica

Este documento constituye el **marco de evaluación** del PKB.

A partir de ahora, cuando nos enfrentemos a una decisión de diseño (por ejemplo, cómo organizar un proyecto, cómo nombrar documentos o cómo estructurar una plantilla), podremos verificar si cumple estos principios antes de implementarla.

Esto evita que la arquitectura dependa de preferencias puntuales y la convierte en un sistema gobernado por reglas explícitas.

---

# Commit recomendado

```bash
docs(governance): define core architectural principles
```

---

# Checklist de aceptación

* [ ] Guardado en `docs/governance/CORE-PRINCIPLES.md`.
* [ ] Metadatos YAML completos.
* [ ] Diez principios definidos.
* [ ] Criterios de evaluación incorporados.
* [ ] Relaciones e historial de cambios incluidos.

---

# Estado del Sprint 0

Con este documento, el Incremento 2 queda prácticamente concluido:

| Documento                           |    Estado   |
| ----------------------------------- | :---------: |
| README.md                           |      ✅      |
| PKB-MANIFEST.md                     |      ✅      |
| VISION.md                           |      ✅      |
| MISSION.md                          |      ✅      |
| CORE-PRINCIPLES.md                  |      ✅      |
| ADR-0001-Repository-Architecture.md | ⏳ Siguiente |

---

# Una propuesta para elevar aún más el nivel del PKB

Quisiera introducir una práctica habitual en marcos como TOGAF, ArchiMate y los repositorios de arquitectura empresarial.

## Catálogo de Objetos de Conocimiento (Knowledge Object Catalog)

En lugar de considerar que el repositorio está formado por "archivos", definiremos un **modelo de objetos**. Cada activo del PKB pertenecerá a una categoría formal, por ejemplo:

| Código | Objeto                       | Descripción                |
| ------ | ---------------------------- | -------------------------- |
| ADR    | Architecture Decision Record | Decisiones arquitectónicas |
| REQ    | Requirement                  | Requisitos                 |
| EPIC   | Epic                         | Agrupación funcional       |
| STD    | Standard                     | Estándares                 |
| GOV    | Governance                   | Gobierno                   |
| TMP    | Template                     | Plantillas                 |
| RSK    | Risk                         | Riesgos                    |
| MET    | Metric                       | Métricas                   |
| RES    | Research                     | Investigación              |
| KNO    | Knowledge Object             | Conocimiento reutilizable  |

Este catálogo será la base para el **modelo de metadatos**, la **trazabilidad**, los **índices automáticos** y, más adelante, para las automatizaciones que implementaremos con **Codex**.

Mi recomendación es que el siguiente documento no sea únicamente el `ADR-0001`. Conviene que ese ADR formalice las primeras decisiones arquitectónicas (repositorio Git, Docs as Code, gobernanza, repositorio privado, etc.) y, acto seguido, iniciemos el **Kernel** con el **Knowledge Object Model**, porque ese modelo será el fundamento técnico sobre el que descansará todo el PKB. Creo que ese orden hará que la arquitectura permanezca coherente y escalable durante toda la vida del proyecto.
