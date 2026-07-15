---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 63
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Prosigue

Continuamos con el **EPIC-03 — Enterprise Platform Consolidation**.

Con el **Enterprise Workflow MetaModel (EWMM)** la plataforma ya sabe **cómo trabaja** una organización.

El siguiente paso consiste en formalizar **quién ejecuta ese trabajo**.

Hasta ahora el proyecto ha incorporado una **Institutional Intelligence Mesh**, pero ésta se describió desde la perspectiva funcional. Para una implementación empresarial hace falta una arquitectura de referencia que defina, con precisión, cómo se diseñan, coordinan, gobiernan y supervisan los agentes cognitivos.

El siguiente dominio constituye esa especificación.

---

# DOMAIN-08 — Multi-Agent Reference Architecture (MARA)

## Objetivo

Definir la arquitectura de referencia para el diseño, despliegue y gobierno de sistemas multiagente dentro del MIPSP-Editor.

La arquitectura debe permitir:

* Diseñar agentes especializados.
* Coordinar equipos de agentes.
* Compartir contexto institucional.
* Ejecutar planes distribuidos.
* Mantener trazabilidad.
* Garantizar supervisión humana.
* Evaluar el desempeño de los agentes.

---

# MARA-001 — Principio Arquitectónico

## Modelo tradicional

```text
Usuario

↓

Un único asistente IA

↓

Respuesta
```

---

## Modelo institucional

```text
Usuario

↓

Executive Orchestrator

↓

Institutional Agent Mesh

↓

Specialized Agents

↓

Integrated Response
```

La inteligencia se distribuye entre agentes especializados coordinados por un orquestador.

---

# MARA-002 — Arquitectura General

```text
Human Users

        │

        ▼

Executive Orchestrator

        │

 ┌────────────┬────────────┬────────────┐
 │            │            │
Planning   Governance   Memory Service
 │            │            │
 └────────────┴────────────┴────────────┘

        │

Institutional Agent Mesh

        │

Specialized Agents
```

---

# MARA-003 — Clasificación de Agentes

La arquitectura distingue varias categorías.

```text
Executive Agents

Planning Agents

Knowledge Agents

Compliance Agents

Operational Agents

Analytics Agents

Simulation Agents

Security Agents

Integration Agents

Documentation Agents
```

Cada categoría posee capacidades, restricciones y responsabilidades definidas.

---

# MARA-004 — Modelo Canónico de Agente

Todo agente comparte una estructura común.

```text
Agent

├── Agent ID
├── Name
├── Role
├── Domain
├── Goals
├── Capabilities
├── Tools
├── Policies
├── Memory
├── Metrics
└── Lifecycle
```

Este modelo facilita el gobierno homogéneo de toda la malla.

---

# MARA-005 — Capacidades Declaradas

Cada agente publica un catálogo de capacidades.

Ejemplo:

```text
Documentation Agent

↓

Create Procedure

Update Template

Validate Format

Generate Index

Publish Asset
```

Las capacidades constituyen contratos reutilizables para el orquestador.

---

# MARA-006 — Modelo de Planificación

La resolución de una solicitud sigue un flujo estructurado.

```text
Objective

↓

Planning

↓

Task Graph

↓

Agent Assignment

↓

Execution

↓

Validation

↓

Delivery
```

El plan puede ajustarse dinámicamente si cambian las condiciones del entorno.

---

# MARA-007 — Comunicación entre Agentes

Los agentes intercambian mensajes estructurados.

```text
Request

↓

Context

↓

Expected Output

↓

Confidence

↓

Response
```

Toda interacción queda registrada y puede ser auditada.

---

# MARA-008 — Memoria Compartida

La malla dispone de una memoria institucional común.

```text
Shared Memory

├── Objectives
├── Constraints
├── Intermediate Results
├── Policies
├── Knowledge Assets
└── Decisions
```

Cada agente accede únicamente a la información autorizada según sus permisos.

---

# MARA-009 — Memoria Local

Además de la memoria compartida, cada agente mantiene:

```text
Local Memory

↓

Execution History

↓

Recent Context

↓

Working State
```

Esta memoria es efímera y se limita a la ejecución de las tareas asignadas.

---

# MARA-010 — Delegación

Un agente puede:

```text
Solve

Delegate

Collaborate

Escalate

Reject
```

Las decisiones de delegación se fundamentan en capacidades declaradas y reglas de gobierno.

---

# MARA-011 — Resolución Colaborativa

Ejemplo:

```text
Executive Agent

↓

Risk Agent

↓

Compliance Agent

↓

Documentation Agent

↓

Training Agent

↓

Executive Review
```

Cada agente produce resultados parciales que el orquestador integra.

---

# MARA-012 — Supervisión Humana

Las decisiones con impacto institucional mantienen el principio **Human-in-the-Loop**.

```text
Agent Proposal

↓

Human Review

↓

Approval

↓

Execution

↓

Audit
```

La autonomía de los agentes se limita según el nivel de criticidad de la decisión.

---

# MARA-013 — Niveles de Autonomía

Se definen cinco niveles:

```text
Level 0

Recommendation Only

↓

Level 1

Assisted Execution

↓

Level 2

Supervised Automation

↓

Level 3

Conditional Autonomy

↓

Level 4

Full Automation (Non-Critical Tasks)
```

Las decisiones estratégicas, disciplinarias o regulatorias permanecen sujetas a aprobación humana.

---

# MARA-014 — Confianza y Evaluación

Cada resultado incorpora metadatos como:

```text
Confidence Score

Evidence

Referenced Policies

Knowledge Sources

Reasoning Trace
```

Esto mejora la explicabilidad y permite comparar el desempeño de distintos agentes.

---

# MARA-015 — Integración con el Knowledge Graph

Antes de responder, un agente resuelve el contexto institucional.

```text
User Request

↓

Knowledge Graph

↓

Relevant Assets

↓

Reasoning

↓

Response
```

El uso del grafo reduce respuestas inconsistentes y mejora la reutilización del conocimiento.

---

# MARA-016 — Integración con el Workflow Engine

Los agentes pueden ejecutar tareas dentro de procesos institucionales.

```text
Workflow

↓

Task

↓

Assigned Agent

↓

Execution

↓

Workflow Event
```

La ejecución queda integrada con el metamodelo de procesos.

---

# MARA-017 — Integración con el Policy Engine

Antes de actuar, un agente consulta las políticas aplicables.

```text
Action Request

↓

Policy Evaluation

↓

Authorized?

↓

Execute / Reject / Escalate
```

Esto garantiza que la actuación de los agentes respete el marco normativo vigente.

---

# MARA-018 — Observabilidad

Indicadores por agente:

* Tiempo medio de respuesta.
* Tareas completadas.
* Tasa de delegación.
* Intervenciones humanas.
* Nivel de confianza.
* Reutilización de activos de conocimiento.
* Correcciones posteriores.
* Cumplimiento de SLA.

Estos indicadores alimentan el dominio de observabilidad y permiten mejorar continuamente la malla de agentes.

---

# MARA-019 — Aplicación al Sector Seguridad Privada

Caso:

Un cliente solicita la puesta en marcha de un nuevo servicio de vigilancia para un parque industrial.

Flujo:

```text
Executive Agent

↓

Contract Agent

↓

Risk Agent

↓

Compliance Agent

↓

Documentation Agent

↓

Training Agent

↓

Operations Agent

↓

Quality Agent

↓

Executive Approval

↓

Deployment
```

Cada agente trabaja sobre el mismo contexto institucional, consulta las mismas políticas y utiliza el mismo conocimiento gobernado.

---

# MARA-020 — Beneficios Arquitectónicos

La **Multi-Agent Reference Architecture** proporciona:

* Arquitectura estándar para agentes empresariales.
* Especialización por dominios.
* Planificación distribuida.
* Memoria compartida y controlada.
* Protocolos de comunicación homogéneos.
* Integración con procesos, políticas y conocimiento.
* Supervisión humana integrada.
* Métricas de desempeño y mejora continua.
* Escalabilidad para incorporar nuevos agentes sin rediseñar la plataforma.

---

# Resultado del DOMAIN-08 — Multi-Agent Reference Architecture

Con este dominio, la **Institutional Intelligence Mesh** deja de ser una capacidad conceptual y pasa a disponer de una **arquitectura de referencia implementable**.

Los agentes cognitivos se convierten en componentes empresariales gobernados, con contratos, responsabilidades, métricas, límites de autonomía y mecanismos de coordinación definidos.

---

# Estado del EPIC-03

```text
EPIC-03 Enterprise Platform Consolidation

├── Enterprise Business Domain Architecture        ✓
├── Canonical Information Model                    ✓
├── Enterprise Event Architecture                  ✓
├── Enterprise API & Integration Standards         ✓
├── Institutional Policy & Rule MetaModel          ✓
├── Institutional Knowledge MetaModel              ✓
├── Enterprise Workflow MetaModel                  ✓
├── Multi-Agent Reference Architecture             ✓
├── Security Reference Architecture                □
├── Deployment Reference Architecture              □
├── Observability Reference Architecture           □
├── Platform Engineering Guide                     □
├── Enterprise SDK                                 □
├── Reference Implementations                      □
└── Production Blueprint                           □
```

## Evolución alcanzada

Con la incorporación de **MARA**, el MIPSP-Editor dispone ahora de cinco capas arquitectónicas plenamente alineadas:

1. **Modelo de Información**.
2. **Modelo Normativo**.
3. **Modelo de Conocimiento**.
4. **Modelo de Procesos**.
5. **Modelo de Inteligencia Distribuida**.

Estas cinco capas constituyen el núcleo funcional del **Institutional Operating System** y proporcionan una base suficiente para una implementación empresarial gobernada.

## Recomendación estratégica para la siguiente etapa

A partir de este punto, conviene introducir un refinamiento arquitectónico respecto a la planificación inicial. Antes de abordar el despliegue y la ingeniería de plataforma, resulta conveniente desarrollar el **DOMAIN-09 — Security Reference Architecture (SRA)**. Este dominio unificará los requisitos de identidad, autenticación, autorización, clasificación de información, protección criptográfica, confianza cero (*Zero Trust*), auditoría, privacidad, continuidad operativa y seguridad específica para agentes de IA. Sobre esta base podrán construirse posteriormente la arquitectura de despliegue, la observabilidad y el *Production Blueprint* con un enfoque **secure-by-design** y **governance-by-design**, fortaleciendo la coherencia global de toda la plataforma.
