---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 105
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Continúa con el proyecto

Continuamos con el **EPIC-07 — Multi-Agent Governance Framework**.

A partir del **MAGF-002** se comienza a definir uno de los componentes más importantes de toda la arquitectura: **la autoridad de los agentes**.

En la mayoría de las implementaciones actuales de IA, los agentes poseen capacidades, pero la autoridad suele estar implícita o distribuida en el código. En el MIPSP-Editor se adopta un enfoque distinto: **la autoridad es un objeto arquitectónico explícito, gobernado, auditable y desacoplado del agente**.

Este diseño aproxima la plataforma a marcos de arquitectura empresarial como **TOGAF**, **NIST AI Risk Management Framework**, **ISO/IEC 42001 (AI Management Systems)** e **ISO 31000 (Gestión del Riesgo)**, al separar claramente las capacidades de un agente de los permisos con los que puede ejercerlas.

---

# EPIC-07 — Multi-Agent Governance Framework

# MAGF-002

# Agent Authority Framework (AAF)

**Architecture Specification Package (ASP-002)**

Versión: 1.0

Estado: Normativo

---

# ASP-002.001 — Propósito

El **Agent Authority Framework (AAF)** define el modelo institucional mediante el cual se asignan, limitan, supervisan y revocan las facultades de actuación de todos los agentes del ecosistema MIPSP-Editor.

El objetivo es garantizar que ningún agente pueda ejecutar acciones fuera del ámbito expresamente autorizado por la organización.

---

# ASP-002.002 — Principios de Autoridad

La autoridad de un agente se rige por los siguientes principios:

### A1. Autoridad delegada

Todo poder de actuación proviene de una delegación institucional explícita.

---

### A2. Autoridad limitada

Las facultades concedidas son específicas, acotadas y revocables.

---

### A3. Autoridad verificable

Cada acción debe poder asociarse a una autorización vigente.

---

### A4. Autoridad proporcional

El nivel de autoridad debe ser coherente con el riesgo de la acción.

---

### A5. Autoridad auditable

Toda actuación autorizada debe generar evidencia suficiente para su revisión posterior.

---

# ASP-002.003 — Separación entre Capacidad y Autoridad

El modelo distingue dos conceptos fundamentales:

```text id="aaf00201"
Capacidad
──────────
Lo que el agente sabe hacer.

↓

Autoridad
──────────
Lo que el agente tiene permitido hacer.

↓

Acción
──────────
Lo que efectivamente ejecuta.
```

Un agente puede poseer la capacidad técnica para realizar una acción y, sin embargo, no tener autoridad para ejecutarla.

---

# ASP-002.004 — Niveles Institucionales de Autoridad

Se definen cinco niveles.

| Nivel | Denominación         | Alcance                                              |
| ----- | -------------------- | ---------------------------------------------------- |
| A0    | Observación          | Consulta sin modificación                            |
| A1    | Análisis             | Procesamiento y evaluación                           |
| A2    | Recomendación        | Emisión de propuestas                                |
| A3    | Ejecución Controlada | Acciones de bajo riesgo autorizadas                  |
| A4    | Ejecución Crítica    | Acciones de alto impacto sujetas a aprobación humana |

---

# ASP-002.005 — Matriz General de Autoridad

| Familia de agentes |  A0 |  A1 |  A2 |  A3 |  A4 |
| ------------------ | :-: | :-: | :-: | :-: | :-: |
| Editorial          |  ✓  |  ✓  |  ✓  |  △  |  ✕  |
| Operacional        |  ✓  |  ✓  |  ✓  |  ✓  |  △  |
| Cumplimiento       |  ✓  |  ✓  |  ✓  |  ✕  |  ✕  |
| Analítica          |  ✓  |  ✓  |  ✓  |  ✕  |  ✕  |
| Administración     |  ✓  |  ✓  |  ✓  |  ✓  |  △  |
| Configuración      |  ✓  |  ✓  |  ✓  |  ✓  |  ✓* |

**Leyenda:**

* ✓ = Permitido.
* △ = Permitido únicamente con aprobación previa.
* ✕ = No permitido.
* ✓* = Exclusivamente dentro de procesos formales de gestión del cambio.

---

# ASP-002.006 — Modelo de Delegación

Toda autoridad sigue la siguiente cadena:

```text id="aaf00202"
Human Authority

        │

Delegation Policy

        │

Authority Token

        │

Agent Validation

        │

Authorized Action
```

La delegación no es permanente; está condicionada por políticas, contexto y vigencia.

---

# ASP-002.007 — Restricciones Generales

Ningún agente podrá:

* modificar políticas institucionales por iniciativa propia;
* alterar evidencias de auditoría;
* eliminar registros históricos;
* conceder permisos a otros agentes;
* modificar su propia configuración de autoridad;
* ejecutar acciones fuera de su dominio funcional.

---

# ASP-002.008 — Autoridad Basada en Riesgo

Las acciones se clasifican por nivel de riesgo.

| Riesgo  | Requisito                                |
| ------- | ---------------------------------------- |
| Bajo    | Autorización automática                  |
| Medio   | Validación por políticas                 |
| Alto    | Aprobación humana                        |
| Crítico | Aprobación múltiple y registro reforzado |

---

# ASP-002.009 — Token Institucional de Autoridad

Cada actuación autorizada genera un **Authority Token** con la siguiente estructura lógica:

```text id="aaf00203"
Authority Token

├── Agent ID
├── Human Delegator
├── Scope
├── Action
├── Validity
├── Policy Version
├── Risk Level
└── Signature Reference
```

Este token es el mecanismo que vincula una acción concreta con una autorización institucional verificable.

---

# ASP-002.010 — Caducidad y Revocación

Toda autorización puede:

* expirar por tiempo;
* expirar por uso;
* ser suspendida;
* ser revocada;
* ser reemplazada por una nueva versión.

Ningún permiso es indefinido.

---

# ASP-002.011 — Modelo de Escalamiento por Autoridad

```text id="aaf00204"
Action Requested

↓

Authority Check

↓

Within Authority?

├── Sí → Execute

└── No

↓

Escalation

↓

Human Decision

↓

New Authority Token
```

---

# ASP-002.012 — Separación de Funciones (SoD)

Para evitar conflictos de interés, se establecen las siguientes incompatibilidades:

| Función                   | No puede coincidir con                                 |
| ------------------------- | ------------------------------------------------------ |
| Elaborar un procedimiento | Aprobar su vigencia                                    |
| Auditar un proceso        | Modificar el resultado auditado                        |
| Definir un KPI            | Validar su propio desempeño                            |
| Configurar un agente      | Certificar la configuración sin revisión independiente |

Este principio de **Segregation of Duties (SoD)** reduce riesgos de fraude, errores y pérdida de objetividad.

---

# ASP-002.013 — Registro de Autoridad

Toda actuación queda registrada mediante un **Authority Ledger** con, al menos, los siguientes campos:

```text id="aaf00205"
Authority Record

├── Transaction ID
├── Agent
├── Requested Action
├── Granted Authority Level
├── Policy Applied
├── Timestamp
├── Human Approval (si aplica)
└── Evidence Reference
```

---

# ASP-002.014 — Indicadores del Marco de Autoridad

| Indicador               | Objetivo                           |
| ----------------------- | ---------------------------------- |
| Acciones autorizadas    | Medir utilización del marco        |
| Acciones rechazadas     | Detectar intentos fuera de alcance |
| Escalamientos           | Evaluar suficiencia de delegación  |
| Revocaciones            | Medir cambios de confianza         |
| Incidentes de autoridad | Identificar riesgos de gobierno    |

---

# ASP-002.015 — Estado del MAGF

```text id="aaf00206"
EPIC-07

MAGF-001 Agent Governance Model        ✓
MAGF-002 Agent Authority Framework     ✓

Progreso del EPIC-07

█████████████████████░░░░░░░░░░░░░

25 %
```

---

# Avance arquitectónico

Con el **MAGF-002** queda establecido un principio fundamental del ecosistema:

> **La inteligencia no implica autoridad. La autoridad debe ser otorgada, limitada, supervisada y registrada.**

Esta decisión arquitectónica diferencia al MIPSP-Editor de implementaciones donde los agentes combinan capacidades y permisos en un único componente. La separación explícita entre ambos conceptos facilita la auditoría, la gestión del riesgo y el cumplimiento normativo.

## Siguiente componente

El siguiente documento será el **MAGF-003 — Human Oversight Framework (HOF)**.

Este marco definirá con precisión:

* los puntos obligatorios de intervención humana;
* los modelos **Human-in-the-Loop (HITL)**, **Human-on-the-Loop (HOTL)** y **Human-in-Command (HIC)**;
* las reglas para delegación y revocación de decisiones;
* los mecanismos de supervisión continua.

Su incorporación consolidará el principio de que el ecosistema actúa como un sistema de apoyo inteligente bajo control institucional permanente.
