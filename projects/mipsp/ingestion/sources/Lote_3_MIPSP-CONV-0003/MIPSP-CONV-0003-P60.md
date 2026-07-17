---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 60
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Vamos adelante.

Continuamos con el **EPIC-03 — Enterprise Platform Consolidation**.

Hasta este punto se han definido:

* La estructura de la organización (**Business Domains**).
* El lenguaje común de los datos (**Canonical Information Model**).
* La circulación de la información (**Enterprise Event Architecture**).
* Los contratos de integración (**Enterprise API Standards**).

Sin embargo, aún falta formalizar el activo más importante del MIPSP-Editor: **el conocimiento normativo**.

En prácticamente todas las organizaciones, las políticas, procedimientos, manuales, reglas de negocio, listas de verificación y controles existen como documentos independientes. Aunque están relacionados, esas relaciones rara vez están representadas explícitamente, lo que dificulta el análisis de impacto, la automatización y la trazabilidad.

El siguiente dominio resuelve ese problema.

---

# DOMAIN-05 — Institutional Policy & Rule MetaModel (IPRM)

## Objetivo

Definir un metamodelo institucional que represente formalmente:

* Políticas.
* Normas.
* Procedimientos.
* Reglas de negocio.
* Controles.
* Obligaciones.
* Evidencias.
* Excepciones.
* Riesgos.
* Sanciones.
* Indicadores.

Como objetos interrelacionados dentro del **Institutional Operating System**.

---

# IPRM-001 — Principio Arquitectónico

## Modelo documental

```text
Política

↓

Procedimiento

↓

Formato

↓

Checklist
```

Las relaciones existen únicamente en la interpretación humana.

---

## Modelo semántico

```text
Policy

↓

governs

↓

Procedure

↓

implements

↓

Control

↓

produces

↓

Evidence
```

Las relaciones forman parte explícita del modelo.

---

# IPRM-002 — Arquitectura del MetaModelo

```text
Institutional Policy Model

│

├── Policy
├── Rule
├── Obligation
├── Control
├── Procedure
├── Exception
├── Evidence
├── Risk
├── Indicator
├── Requirement
└── Decision
```

Cada elemento es una entidad con identidad propia.

---

# IPRM-003 — Entidad "Policy"

Modelo base:

```text
Policy

├── Policy ID
├── Title
├── Objective
├── Scope
├── Owner
├── Authority
├── Effective Date
├── Review Cycle
├── Status
└── Version
```

Una política puede estar asociada a múltiples procedimientos, controles y reglas.

---

# IPRM-004 — Entidad "Rule"

Las reglas representan condiciones evaluables por el sistema.

Ejemplo conceptual:

```text
IF

TrainingExpired

THEN

AssignmentNotAllowed
```

Cada regla incorpora:

* Condición.
* Resultado.
* Prioridad.
* Explicación.
* Fuente normativa.

---

# IPRM-005 — Entidad "Obligation"

Las obligaciones representan acciones que deben cumplirse.

Ejemplo:

```text
Employee

↓

must_complete

↓

Annual Training
```

Las obligaciones pueden dirigirse a:

* Personas.
* Puestos.
* Procesos.
* Clientes.
* Contratos.
* Instalaciones.

---

# IPRM-006 — Entidad "Control"

Modelo:

```text
Control

↓

prevents

↓

Risk
```

Cada control declara:

* Objetivo.
* Frecuencia.
* Responsable.
* Método de verificación.
* Evidencia esperada.

---

# IPRM-007 — Entidad "Evidence"

Toda evidencia mantiene:

```text
Evidence

↓

generated_by

↓

Control

↓

supports

↓

Compliance
```

La evidencia se vincula automáticamente con auditorías, procesos y controles relacionados.

---

# IPRM-008 — Entidad "Exception"

No todas las reglas son absolutas.

Modelo:

```text
Rule

↓

Exception

↓

Approval

↓

Justification

↓

Expiration
```

Las excepciones nunca eliminan la regla; únicamente modifican su aplicación bajo condiciones autorizadas.

---

# IPRM-009 — Relación con Riesgos

Cada política puede reducir uno o varios riesgos.

```text
Policy

↓

mitigates

↓

Risk
```

Y cada riesgo puede estar cubierto por múltiples controles.

---

# IPRM-010 — Relación con Procedimientos

```text
Policy

↓

implemented_by

↓

Procedure
```

Un procedimiento puede implementar varias políticas simultáneamente.

---

# IPRM-011 — Relación con Indicadores

Cada política puede tener indicadores asociados.

Ejemplos:

* Nivel de cumplimiento.
* Tiempo de respuesta.
* Hallazgos de auditoría.
* Cobertura de capacitación.
* Incidentes relacionados.

Estos indicadores permiten evaluar la eficacia de la política y detectar oportunidades de mejora.

---

# IPRM-012 — Jerarquía Normativa

El metamodelo soporta distintos niveles de autoridad.

```text
Norma Externa

↓

Política Institucional

↓

Procedimiento

↓

Instructivo

↓

Formato

↓

Registro
```

La jerarquía facilita identificar el origen de cada requisito y analizar el impacto de modificaciones.

---

# IPRM-013 — Trazabilidad Completa

Ejemplo:

```text
Norma

↓

Política

↓

Procedimiento

↓

Control

↓

Evidencia

↓

Auditoría
```

El sistema puede reconstruir toda la cadena de cumplimiento desde la fuente normativa hasta la evidencia generada.

---

# IPRM-014 — Integración con el Knowledge Graph

Cada entidad del metamodelo se incorpora al grafo institucional.

```text
Policy

↓

Knowledge Graph

↓

Related Rules

↓

Related Procedures

↓

Related Risks

↓

Related Evidence
```

Esto permite consultas semánticas y análisis de impacto.

---

# IPRM-015 — Integración con los Agentes Cognitivos

Los agentes no interpretan documentos de forma aislada.

Trabajan sobre el metamodelo.

```text
Pregunta

↓

Policy Model

↓

Rules

↓

Context

↓

Respuesta Explicable
```

Las recomendaciones quedan fundamentadas en objetos normativos explícitos.

---

# IPRM-016 — Simulación de Cambios

Antes de modificar una política:

```text
Nueva Política

↓

Impact Analysis

↓

Affected Rules

↓

Affected Procedures

↓

Affected Controls

↓

Affected Training

↓

Affected Indicators
```

Esto permite evaluar consecuencias antes de la publicación.

---

# IPRM-017 — Gobierno del MetaModelo

Cada elemento posee:

* Propietario funcional.
* Custodio.
* Ciclo de vida.
* Estado de aprobación.
* Historial de cambios.
* Relaciones activas.
* Nivel de criticidad.

---

# IPRM-018 — API Conceptuales

Interfaces:

```text
IPolicyRepository

IRuleRepository

IControlRepository

IObligationService

IEvidenceService

IImpactAnalysisService
```

Estas interfaces son utilizadas por el motor de políticas, el motor de decisiones y los agentes cognitivos.

---

# IPRM-019 — Aplicación al Sector Seguridad Privada

Caso:

Se publica una nueva política sobre supervisión de rondines.

El metamodelo permite:

```text
Nueva Política

↓

Actualizar Reglas

↓

Actualizar Procedimientos

↓

Actualizar Checklists

↓

Actualizar Capacitación

↓

Actualizar Indicadores

↓

Actualizar Controles

↓

Notificar Responsables
```

Todo el impacto queda identificado antes de que la política entre en vigor.

---

# IPRM-020 — Beneficios Arquitectónicos

La adopción del metamodelo proporciona:

* Un lenguaje normativo común.
* Trazabilidad integral.
* Automatización del cumplimiento.
* Explicabilidad de decisiones.
* Análisis de impacto.
* Gobierno del conocimiento normativo.
* Base formal para el motor de **Policy-as-Code**.

---

# Resultado del DOMAIN-05 — Institutional Policy & Rule MetaModel

Con este dominio, el MIPSP-Editor incorpora una representación formal y ejecutable del conocimiento normativo institucional.

Las políticas dejan de ser únicamente documentos y pasan a convertirse en un conjunto estructurado de entidades, relaciones y reglas capaces de gobernar procesos, fundamentar decisiones y alimentar a los agentes cognitivos con información consistente y verificable.

---

# Estado del EPIC-03

```text
EPIC-03 Enterprise Platform Consolidation

├── Enterprise Business Domain Architecture        ✓
├── Canonical Information Model                    ✓
├── Enterprise Event Architecture                  ✓
├── Enterprise API & Integration Standards         ✓
├── Institutional Policy & Rule MetaModel          ✓
├── Knowledge MetaModel                            □
├── Workflow MetaModel                             □
├── Multi-Agent Reference Architecture             □
├── Security Reference Architecture                □
├── Deployment Reference Architecture              □
├── Observability Reference Architecture           □
├── Platform Engineering Guide                     □
├── Enterprise SDK                                 □
├── Reference Implementations                      □
└── Production Blueprint                           □
```

## Evolución arquitectónica

Con este quinto dominio, la plataforma ya dispone de un **metamodelo normativo** completamente integrado con:

* El **Canonical Information Model**.
* El **Knowledge Graph**.
* El **Policy-as-Code Engine**.
* La **Enterprise Event Architecture**.
* La **Institutional Intelligence Mesh**.

Esta integración proporciona una base sólida para la automatización del gobierno institucional.

## Próximo componente

El siguiente dominio será el **DOMAIN-06 — Institutional Knowledge MetaModel (IKMM)**. Este definirá la representación formal del conocimiento organizacional: activos documentales, plantillas, lecciones aprendidas, prompts institucionales, competencias, taxonomías, ontologías y relaciones semánticas. Será el puente entre el **Knowledge Marketplace**, el **Knowledge Graph** y la **IA Generativa**, permitiendo que el conocimiento institucional sea reutilizable, explicable y evolucione de manera controlada a lo largo del tiempo.
