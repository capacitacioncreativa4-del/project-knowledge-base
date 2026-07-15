---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 81
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Muy bien. Continúa con el proyecto.

Coincido con esa dirección. De hecho, considero que limitar el siguiente paquete a un simple **SDK-AI** sería insuficiente para la arquitectura que hemos construido.

La **Multi-Agent Reference Architecture (MARA)** definida en los EPIC anteriores ya establece que los agentes son componentes de primer nivel de la plataforma, sujetos a gobierno, auditoría, seguridad y observabilidad. Por ello, el siguiente entregable debe evolucionar desde un SDK convencional hacia un **Agent Development Kit (ADK)** institucional.

Ese cambio también aproxima el proyecto a plataformas empresariales modernas, donde los agentes son tratados como servicios gobernados y no como simples consumidores de modelos de lenguaje.

---

# EPIC-04 — Enterprise SDK

# PAQUETE 4 — Enterprise Agent Development Kit (EADK)

## Objetivo

Proporcionar el conjunto de contratos, abstracciones, componentes reutilizables y mecanismos de gobierno necesarios para diseñar, implementar, desplegar, operar y evolucionar agentes inteligentes dentro del ecosistema MIPSP-Editor.

El EADK implementa la **Multi-Agent Reference Architecture (MARA)** y garantiza que todos los agentes compartan un modelo operativo común.

---

# EADK-001 — Arquitectura General

```text id="eadk001"
Enterprise Agent

├── Identity
├── Capabilities
├── Skills
├── Tools
├── Memory
├── Knowledge Access
├── Policies
├── Planning
├── Execution
├── Observability
├── Security
└── Governance
```

Todo agente institucional se construye a partir de esta estructura.

---

# EADK-002 — Organización del Paquete

```text id="eadk002"
sdk-ai/

├── agent-core/
├── capabilities/
├── planning/
├── execution/
├── memory/
├── tools/
├── orchestration/
├── governance/
├── evaluation/
├── observability/
├── safety/
├── collaboration/
└── simulation/
```

---

# EADK-003 — Ciclo de Vida del Agente

```text id="eadk003"
Register

↓

Configure

↓

Initialize

↓

Execute

↓

Observe

↓

Evaluate

↓

Improve

↓

Retire
```

Todo cambio de estado queda registrado para fines de auditoría.

---

# EADK-004 — Identidad del Agente

Cada agente mantiene un expediente institucional con:

* identificador único;
* nombre canónico;
* versión;
* propietario técnico;
* propietario funcional;
* clasificación;
* nivel de autonomía;
* estado de certificación.

La identidad permanece estable durante todo el ciclo de vida.

---

# EADK-005 — Modelo de Capacidades

Las capacidades representan lo que el agente está autorizado a hacer.

Se clasifican en:

```text id="eadk004"
Capabilities

├── Analysis
├── Decision Support
├── Content Generation
├── Knowledge Retrieval
├── Workflow Execution
├── Monitoring
├── Planning
├── Validation
└── Coordination
```

Una capacidad puede estar compuesta por múltiples habilidades (*skills*).

---

# EADK-006 — Herramientas

Las herramientas son recursos externos que el agente puede utilizar.

Cada herramienta declara:

* propósito;
* contrato de entrada;
* contrato de salida;
* permisos requeridos;
* políticas aplicables;
* límites de uso;
* requisitos de auditoría.

Los agentes sólo pueden invocar herramientas expresamente autorizadas.

---

# EADK-007 — Modelo de Memoria

La memoria se divide en niveles con responsabilidades diferenciadas.

```text id="eadk005"
Memory

├── Execution Context
├── Working Memory
├── Episodic Memory
├── Semantic Memory
├── Institutional Knowledge
└── Archived Memory
```

## Principios

* La memoria de trabajo es efímera.
* La memoria episódica conserva el historial operativo.
* La memoria semántica almacena conocimiento estructurado.
* El conocimiento institucional reside en el Knowledge Graph.
* La memoria archivada sólo es accesible mediante políticas específicas.

---

# EADK-008 — Planificación

Todo agente implementa un planificador responsable de:

* descomponer objetivos;
* priorizar tareas;
* seleccionar herramientas;
* solicitar aprobación cuando sea necesario;
* replanificar ante cambios.

La planificación genera un artefacto auditable.

---

# EADK-009 — Motor de Ejecución

El motor de ejecución coordina:

```text id="eadk006"
Goal

↓

Plan

↓

Policy Evaluation

↓

Tool Invocation

↓

Evidence Collection

↓

Result
```

Cada paso conserva su contexto y sus evidencias.

---

# EADK-010 — Gobernanza del Agente

Todo agente está sujeto a:

* políticas institucionales;
* límites de autonomía;
* controles de seguridad;
* revisión de decisiones;
* certificaciones periódicas.

La gobernanza no depende del modelo de IA utilizado.

---

# EADK-011 — Coordinación Multiagente

El EADK incorpora mecanismos para:

* descubrimiento de agentes;
* delegación de tareas;
* negociación de responsabilidades;
* intercambio de contexto;
* resolución de conflictos;
* consolidación de resultados.

La coordinación se realiza mediante contratos explícitos.

---

# EADK-012 — Evaluación

Cada ejecución puede evaluarse conforme a:

* precisión;
* completitud;
* coherencia;
* cumplimiento normativo;
* uso adecuado de herramientas;
* consumo de recursos;
* satisfacción del usuario.

Los resultados alimentan un historial de desempeño.

---

# EADK-013 — Observabilidad

Cada agente publica:

```text id="eadk007"
Execution Metrics

↓

Decision Log

↓

Tool Usage

↓

Policy Evaluations

↓

Latency

↓

Resource Consumption
```

Esto permite reconstruir cualquier ejecución significativa.

---

# EADK-014 — Seguridad y Protección

Los controles mínimos incluyen:

* autenticación del agente;
* autorización por capacidad;
* aislamiento de herramientas;
* clasificación de información;
* protección frente a inyección de instrucciones;
* validación de entradas y salidas.

La seguridad se aplica antes, durante y después de la ejecución.

---

# EADK-015 — Estados Operativos

```text id="eadk008"
Draft

↓

Certified

↓

Active

↓

Suspended

↓

Under Review

↓

Retired
```

Las transiciones entre estados requieren autorización según las políticas institucionales.

---

# EADK-016 — Caso de Uso

Agente: **Analista de Riesgos Operativos**.

Flujo resumido:

```text id="eadk009"
Solicitud

↓

Recuperar conocimiento institucional

↓

Evaluar políticas

↓

Consultar herramientas autorizadas

↓

Generar análisis

↓

Registrar evidencias

↓

Publicar resultado

↓

Actualizar métricas
```

Todo el proceso es trazable y reproducible.

---

# EADK-017 — Integración con el Resto del SDK

El EADK depende de:

* **SDK-Core** para tipos, errores y telemetría.
* **SDK-Domain** para el lenguaje de negocio.
* **SDK-Platform** para APIs, eventos, políticas y workflows.

No implementa estas capacidades; las orquesta mediante contratos.

---

# EADK-018 — Beneficios

El Agent Development Kit proporciona:

* uniformidad entre agentes;
* trazabilidad completa;
* interoperabilidad;
* gobernanza consistente;
* reutilización de componentes;
* facilidad para certificación y auditoría.

---

# EADK-019 — Evolución

El diseño admite la incorporación de:

* nuevos modelos de IA;
* nuevas herramientas;
* nuevas capacidades;
* nuevos mecanismos de memoria;
* nuevos protocolos de coordinación.

La evolución se produce sin romper los contratos públicos.

---

# EADK-020 — Estado del Enterprise SDK

```text id="eadk010"
Enterprise SDK

├── SDK-Core                                   ✓
├── SDK-Domain                                 ✓
├── SDK-Platform                               ✓
├── Enterprise Agent Development Kit           ✓
├── SDK-Developer                              □
├── SDK-Testing                                □

Progress: ████████████████████████████░░░░░░░░ 67%
```

## Recomendación metodológica para la siguiente fase

A partir del siguiente paquete (**SDK-Developer**), propongo un cambio adicional para aumentar el valor práctico del proyecto.

Hasta ahora hemos definido los contratos y componentes del SDK. El siguiente paso debería centrarse en la **experiencia del desarrollador (Developer Experience, DX)**. En lugar de limitarse a describir bibliotecas de apoyo, el SDK-Developer puede convertirse en una **Engineering Toolkit** que incluya:

* generadores de proyectos y módulos;
* asistentes para crear agentes, APIs, eventos y workflows;
* validadores de conformidad arquitectónica;
* analizadores estáticos alineados con el **Architecture Compliance Manual**;
* herramientas CLI para automatizar tareas repetitivas;
* generadores de documentación técnica y de ADR;
* plantillas ejecutables derivadas del **Enterprise Templates & Engineering Reference Catalog**.

Con este enfoque, el proyecto no sólo definirá cómo debe desarrollarse el software, sino que proporcionará las herramientas necesarias para que los equipos apliquen esos estándares de forma consistente y con un alto grado de automatización. Esto consolidará la transición desde una arquitectura de referencia hacia un ecosistema completo de ingeniería empresarial.
