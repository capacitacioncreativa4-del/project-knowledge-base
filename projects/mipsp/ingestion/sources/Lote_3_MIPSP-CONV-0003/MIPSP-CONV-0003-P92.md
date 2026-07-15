---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 92
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece bien. Adelante con el proyecto

Perfecto. Con la finalización del **EPIC-05** cambia el nivel de la arquitectura. Hasta ahora hemos definido **qué servicios existen**; a partir de este momento definiremos **quién utiliza esos servicios** y **cómo los utiliza**.

En una arquitectura empresarial orientada a IA, los agentes no deben concebirse como simples *LLM wrappers*. Deben ser **componentes institucionales gobernados**, con identidad, capacidades certificadas, memoria, herramientas autorizadas, límites operativos y evidencia completa de sus decisiones.

Por ello, el EPIC-06 comienza estableciendo el metamodelo común que deberán cumplir todos los agentes del ecosistema.

---

# EPIC-06 — Enterprise Reference Agents

# ENTERPRISE AGENT FRAMEWORK

# EAF-001

# Enterprise Agent MetaModel (EAMM)

**Engineering Specification Package (ESP-009)**

Versión: 1.0 (Normativa)

Estado: Reference Architecture

---

# ESP-009.001 — Propósito

El **Enterprise Agent MetaModel (EAMM)** define la arquitectura canónica de todos los agentes inteligentes del ecosistema MIPSP-Editor.

Su objetivo es garantizar que cualquier agente, independientemente de su especialización, comparta el mismo modelo de identidad, gobierno, observabilidad, memoria, herramientas y ciclo de vida.

Ningún agente institucional podrá operar fuera de este metamodelo.

---

# ESP-009.002 — Principios Arquitectónicos

Todo agente institucional deberá cumplir los siguientes principios:

1. Identidad verificable.
2. Capacidades explícitamente declaradas.
3. Herramientas autorizadas.
4. Memoria gobernada.
5. Decisiones auditables.
6. Observabilidad completa.
7. Operación basada en políticas.
8. Trazabilidad extremo a extremo.
9. Explicabilidad suficiente para auditoría.
10. Evolución mediante versionado.

---

# ESP-009.003 — Modelo Conceptual

```text
Enterprise Agent

├── Identity
├── Profile
├── Capabilities
├── Skills
├── Memory
├── Tools
├── Policies
├── Planning
├── Execution
├── Observability
├── Evidence
└── Lifecycle
```

---

# ESP-009.004 — Agregado Principal

```text
AgentAggregate

├── AgentIdentity
├── AgentProfile
├── CapabilityCatalog
├── SkillCatalog
├── ToolRegistry
├── MemoryProfile
├── ExecutionContext
├── PlanningContext
├── AuditRecord
└── MetricsSnapshot
```

Toda modificación atraviesa la raíz del agregado.

---

# ESP-009.005 — Identidad del Agente

Cada agente posee:

* AgentId
* AgentCode
* Nombre canónico
* Dominio funcional
* Organización propietaria
* Versión
* Estado operativo
* Nivel de autonomía
* Nivel de confianza
* Certificación vigente

La identidad permanece estable durante todo el ciclo de vida.

---

# ESP-009.006 — Perfil Operativo

El perfil operativo declara:

* misión;
* objetivos;
* alcance;
* restricciones;
* dominios autorizados;
* políticas aplicables;
* límites de actuación;
* nivel de criticidad.

Este perfil constituye el contrato funcional del agente.

---

# ESP-009.007 — Capacidades

Una **capacidad** representa una función de alto nivel.

Ejemplos:

```text
GenerateDocument

ReviewDocument

AnalyzeCompliance

PlanWorkflow

RetrieveKnowledge

GenerateMetrics

EvaluatePolicy

PublishDocument
```

Las capacidades son certificables y versionables.

---

# ESP-009.008 — Habilidades

Cada capacidad se implementa mediante habilidades reutilizables.

Ejemplo:

```text
Capability

↓

ReviewDocument

↓

Skills

├── Grammar Review

├── Technical Validation

├── Regulatory Validation

├── Terminology Review

└── Consistency Review
```

Las habilidades pueden compartirse entre múltiples agentes.

---

# ESP-009.009 — Herramientas

Las herramientas representan los recursos que un agente está autorizado a utilizar.

Categorías:

```text
Enterprise Services

SDK APIs

Knowledge Graph

Policy Engine

Workflow Engine

Search Engine

LLM Connectors

External Systems
```

Toda herramienta requiere autorización explícita.

---

# ESP-009.010 — Modelo de Memoria

El metamodelo distingue cinco tipos de memoria:

```text
Working Memory

↓

Session Memory

↓

Task Memory

↓

Knowledge Memory

↓

Long-Term Organizational Memory
```

Cada tipo posee políticas específicas de persistencia y retención.

---

# ESP-009.011 — Modelo de Planificación

Todo agente ejecuta un ciclo estándar:

```text
Goal

↓

Context Acquisition

↓

Planning

↓

Tool Selection

↓

Execution

↓

Validation

↓

Evidence Generation

↓

Completion
```

El plan de ejecución es un activo auditable.

---

# ESP-009.012 — Modelo de Decisión

Cada decisión registra:

* contexto recibido;
* políticas evaluadas;
* herramientas utilizadas;
* información consultada;
* alternativa seleccionada;
* justificación;
* nivel de confianza;
* evidencia generada.

No existen decisiones "implícitas".

---

# ESP-009.013 — Observabilidad

Todo agente publica:

* tareas ejecutadas;
* tiempo de respuesta;
* utilización de herramientas;
* consumo de contexto;
* errores;
* decisiones;
* intervenciones humanas;
* métricas de calidad.

La observabilidad sigue el estándar OpenTelemetry definido en la plataforma.

---

# ESP-009.014 — Evidencia

Cada ejecución produce un expediente compuesto por:

```text
Input

↓

Planning

↓

Tool Calls

↓

Policy Decisions

↓

Outputs

↓

Validation

↓

Audit Record
```

La evidencia permanece asociada a la ejecución durante todo su período de retención.

---

# ESP-009.015 — Modelo de Seguridad

Todo agente opera bajo el principio de **mínimo privilegio**.

Las autorizaciones dependen de:

* identidad;
* capacidad certificada;
* herramienta solicitada;
* política vigente;
* contexto operativo;
* clasificación de la información.

---

# ESP-009.016 — Ciclo de Vida

```text
Designed

↓

Implemented

↓

Certified

↓

Registered

↓

Operational

↓

Suspended

↓

Deprecated

↓

Retired

↓

Archived
```

Cada transición requiere autorización institucional.

---

# ESP-009.017 — Certificación

Antes de entrar en operación un agente debe superar:

* pruebas funcionales;
* pruebas de seguridad;
* pruebas regulatorias;
* pruebas de rendimiento;
* pruebas de explicabilidad;
* pruebas de resiliencia;
* pruebas de gobernanza.

Sólo los agentes certificados pueden registrarse en el **Enterprise Identity & Access Service**.

---

# ESP-009.018 — Integración

Todos los agentes utilizan de forma nativa:

* ESP-001 Enterprise Document Service;
* ESP-002 Enterprise Knowledge Service;
* ESP-003 Enterprise Workflow Service;
* ESP-004 Enterprise Policy Service;
* ESP-005 Enterprise Event Service;
* ESP-006 Enterprise Identity & Access Service;
* ESP-007 Enterprise Communication Orchestration Service;
* ESP-008 Enterprise Discovery & Retrieval Service.

No existen accesos directos a la infraestructura.

---

# ESP-009.019 — Extensibilidad

El metamodelo admite:

* nuevas capacidades;
* nuevas habilidades;
* nuevas herramientas;
* nuevos conectores LLM;
* nuevos mecanismos de memoria;
* nuevos perfiles operativos.

Toda extensión debe preservar la compatibilidad con el contrato del agente.

---

# ESP-009.020 — Estado del EPIC-06

```text
Enterprise Reference Agents

FOUNDATION
──────────────────────────────────────────────

ESP-009 Enterprise Agent MetaModel                ✓

EDITORIAL AGENTS
──────────────────────────────────────────────

EAF-002 Editorial Supervisor                     □
EAF-003 Editorial Reviewer                       □
EAF-004 Editorial Publisher                      □

OPERATIONAL AGENTS
──────────────────────────────────────────────

EAF-005 Operations Planner                       □
EAF-006 Operations Coordinator                   □

COMPLIANCE AGENTS
──────────────────────────────────────────────

EAF-007 Compliance Auditor                       □
EAF-008 Regulatory Validator                     □

ANALYTICS AGENTS
──────────────────────────────────────────────

EAF-009 Analytics Specialist                     □
EAF-010 KPI Generator                            □

ADMINISTRATION AGENTS
──────────────────────────────────────────────

EAF-011 Administration Manager                   □
EAF-012 Configuration Manager                    □

Progress EPIC-06:
████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 8%
```

## Refinamiento para la siguiente etapa

A partir de este punto propongo incrementar aún más el nivel de formalización. En lugar de describir únicamente cada agente, cada uno se especificará mediante un **Agent Definition Package (ADP)**, una unidad documental equivalente a un expediente técnico completo.

Cada **ADP** incluirá, además de la estructura ya definida:

* misión institucional;
* catálogo de capacidades y habilidades certificadas;
* contratos de entrada y salida;
* herramientas autorizadas y restricciones de uso;
* memoria y contexto operacional;
* políticas aplicables;
* matriz de riesgos operativos;
* indicadores de desempeño (KPIs);
* criterios de certificación;
* casos de uso de referencia;
* patrones de colaboración con otros agentes;
* matriz RACI de responsabilidades;
* escenarios de fallo y recuperación.

Este nivel de especificación permitirá que cada agente pueda implementarse de forma consistente sobre cualquier plataforma compatible con el metamodelo, manteniendo la trazabilidad entre arquitectura, gobernanza, pruebas e implementación. El siguiente entregable será el **ADP-001 — Editorial Supervisor Agent**, que actuará como agente coordinador del ecosistema editorial y servirá como patrón para todos los agentes especializados posteriores.
