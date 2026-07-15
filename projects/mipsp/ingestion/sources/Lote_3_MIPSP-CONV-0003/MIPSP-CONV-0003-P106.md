---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 106
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Prosigue con el proyecto

Continuamos con el **EPIC-07 — Multi-Agent Governance Framework**.

El siguiente componente constituye uno de los pilares del modelo de gobierno. Mientras el **MAGF-002** definió **qué autoridad puede recibir un agente**, el **MAGF-003** define **cuándo, cómo y con qué intensidad interviene el ser humano**.

Este documento adopta un enfoque alineado con los principios de supervisión humana presentes en marcos internacionales como **ISO/IEC 42001**, el **NIST AI Risk Management Framework** y el **AI Act de la Unión Europea**, adaptándolos al contexto específico del MIPSP-Editor y de organizaciones de seguridad privada.

---

# EPIC-07 — Multi-Agent Governance Framework

# MAGF-003

# Human Oversight Framework (HOF)

**Architecture Specification Package (ASP-003)**

Versión: 1.0

Estado: Normativo

---

# ASP-003.001 — Propósito

El **Human Oversight Framework (HOF)** establece el modelo institucional mediante el cual las personas conservan el control efectivo sobre el ecosistema multiagente.

Su finalidad es garantizar que las decisiones con impacto operativo, jurídico, financiero, disciplinario o estratégico permanezcan bajo responsabilidad humana, utilizando a los agentes como sistemas de apoyo y no como sustitutos de la autoridad institucional.

---

# ASP-003.002 — Principios Rectores

El HOF se fundamenta en ocho principios.

### H1. Primacía de la decisión humana

Toda decisión crítica corresponde a un responsable humano.

---

### H2. Supervisión continua

La supervisión debe mantenerse durante todo el ciclo de vida de la actividad.

---

### H3. Intervención proporcional al riesgo

El grado de supervisión aumenta conforme aumenta el riesgo.

---

### H4. Comprensibilidad

Toda recomendación emitida por un agente debe ser entendible para quien la aprueba.

---

### H5. Capacidad de veto

La autoridad humana puede aceptar, modificar o rechazar cualquier recomendación.

---

### H6. Responsabilidad institucional

La responsabilidad jurídica nunca se transfiere al agente.

---

### H7. Evidencia obligatoria

Toda intervención humana deberá quedar documentada.

---

### H8. Revisión posterior

Las decisiones relevantes podrán ser auditadas posteriormente.

---

# ASP-003.003 — Modelos de Supervisión

El marco adopta tres modelos complementarios.

## Modelo 1 — Human-in-the-Loop (HITL)

Aplicable cuando toda decisión requiere aprobación humana previa.

```text id="hof00301"
Solicitud

↓

Agente

↓

Recomendación

↓

Revisión Humana

↓

Autorización

↓

Ejecución
```

Uso recomendado:

* aprobación de procedimientos;
* modificaciones regulatorias;
* decisiones disciplinarias;
* cambios estratégicos.

---

## Modelo 2 — Human-on-the-Loop (HOTL)

El agente puede ejecutar acciones previamente autorizadas, pero una persona mantiene supervisión continua y puede intervenir.

```text id="hof00302"
Agente

↓

Acción

↓

Supervisión Continua

↓

Intervención si es necesario
```

Uso recomendado:

* monitoreo operativo;
* seguimiento de indicadores;
* coordinación de servicios.

---

## Modelo 3 — Human-in-Command (HIC)

La autoridad humana mantiene el control estratégico permanente sobre todo el sistema.

```text id="hof00303"
Dirección Institucional

↓

Políticas

↓

Agentes

↓

Resultados

↓

Retroalimentación
```

Uso recomendado:

* gobierno institucional;
* administración del ecosistema;
* gestión de riesgos.

---

# ASP-003.004 — Matriz de Supervisión por Nivel de Riesgo

| Nivel de riesgo | Supervisión requerida                    | Modelo predominante |
| --------------- | ---------------------------------------- | ------------------- |
| Bajo            | Supervisión diferida                     | HOTL                |
| Medio           | Validación por excepción                 | HOTL + HITL         |
| Alto            | Aprobación obligatoria                   | HITL                |
| Crítico         | Aprobación múltiple y registro reforzado | HIC + HITL          |

---

# ASP-003.005 — Puntos de Control Obligatorios

La intervención humana será obligatoria, entre otros casos, cuando se trate de:

* aprobación o modificación de políticas;
* creación o eliminación de agentes;
* cambios de configuración críticos;
* emisión de dictámenes regulatorios finales;
* aprobación de auditorías institucionales;
* aceptación de riesgos residuales;
* decisiones con impacto contractual;
* autorización de acciones extraordinarias.

---

# ASP-003.006 — Facultades del Supervisor Humano

El supervisor podrá:

* aprobar recomendaciones;
* rechazarlas;
* solicitar información adicional;
* modificar parámetros;
* ordenar un nuevo análisis;
* suspender la ejecución;
* escalar el asunto a otra autoridad;
* revocar autorizaciones previamente otorgadas.

---

# ASP-003.007 — Registro de Supervisión

Cada intervención genera un registro con la siguiente estructura:

```text id="hof00304"
Oversight Record

├── Oversight ID
├── Human Supervisor
├── Agent Involved
├── Request ID
├── Recommendation
├── Decision
├── Justification
├── Timestamp
└── Evidence References
```

---

# ASP-003.008 — Escalamiento Institucional

```text id="hof00305"
Agent Recommendation

↓

Operational Supervisor

↓

Manager

↓

Executive Authority

↓

Institutional Board
```

Cada nivel interviene únicamente cuando el asunto excede las competencias del nivel anterior.

---

# ASP-003.009 — Derecho de Interrupción (Kill Switch)

El marco incorpora un mecanismo institucional de interrupción controlada.

Puede ser activado cuando:

* exista comportamiento inesperado;
* se detecte riesgo elevado;
* exista sospecha de compromiso de seguridad;
* aparezcan resultados inconsistentes;
* una autoridad competente lo ordene.

Efectos:

* suspensión inmediata del agente o flujo afectado;
* preservación de evidencias;
* notificación a los responsables;
* inicio del procedimiento de revisión.

---

# ASP-003.010 — Requisitos de Explicabilidad

Antes de aprobar una recomendación, el supervisor deberá disponer, como mínimo, de:

* objetivo de la recomendación;
* datos utilizados;
* políticas aplicadas;
* nivel de confianza;
* riesgos identificados;
* alternativas consideradas;
* impacto esperado.

---

# ASP-003.011 — Competencias del Supervisor

Los responsables humanos deberán acreditar competencias acordes con su función, incluyendo:

* comprensión del dominio operativo;
* conocimiento de las políticas institucionales;
* capacidad para interpretar evidencia;
* formación en gestión del riesgo;
* conocimiento básico del funcionamiento del ecosistema multiagente.

---

# ASP-003.012 — Indicadores del Marco

| Indicador                      | Finalidad                              |
| ------------------------------ | -------------------------------------- |
| Recomendaciones aprobadas      | Medir adopción                         |
| Recomendaciones rechazadas     | Detectar oportunidades de mejora       |
| Tiempo de revisión             | Evaluar eficiencia                     |
| Intervenciones extraordinarias | Identificar riesgos                    |
| Activaciones del Kill Switch   | Medir estabilidad del ecosistema       |
| Reversiones de decisiones      | Evaluar calidad de las recomendaciones |

---

# ASP-003.013 — Integración con Otros Componentes

El HOF interactúa con:

* **MAGF-001** para respetar la estructura organizacional.
* **MAGF-002** para verificar niveles de autoridad.
* **MAGF-004** para controlar las comunicaciones entre agentes.
* **MAGF-006** para asegurar la trazabilidad de todas las decisiones.
* **MAGF-007** para supervisar cambios durante el ciclo de vida de los agentes.

---

# ASP-003.014 — Criterios de Conformidad

El ecosistema será conforme con este marco cuando pueda demostrar que:

1. toda decisión crítica tiene un responsable humano identificable;
2. las intervenciones están registradas y son auditables;
3. existe capacidad efectiva de veto;
4. los mecanismos de interrupción funcionan correctamente;
5. la supervisión es proporcional al riesgo;
6. la responsabilidad institucional permanece en la organización.

---

# ASP-003.015 — Estado del MAGF

```text id="hof00306"
EPIC-07

MAGF-001 Agent Governance Model          ✓
MAGF-002 Agent Authority Framework       ✓
MAGF-003 Human Oversight Framework       ✓

Progreso del EPIC-07

██████████████████████████████░░░░░░░

37.5 %
```

---

# Hito arquitectónico

Con el **Human Oversight Framework** queda formalizado un principio central del MIPSP-Editor:

> **Los agentes aportan capacidad de análisis y ejecución gobernada; la autoridad institucional y la responsabilidad final permanecen siempre en las personas.**

Este principio servirá como referencia para todos los componentes posteriores del ecosistema, incluyendo auditoría, gestión de riesgos, cumplimiento normativo y seguridad.

## Próximo componente

El siguiente desarrollo será el **MAGF-004 — Agent Communication Governance (ACG)**.

Este documento establecerá el protocolo institucional de comunicación entre agentes, definiendo:

* contratos de intercambio de mensajes;
* niveles de confianza;
* autenticidad e integridad de las comunicaciones;
* patrones de coordinación;
* manejo de errores;
* comunicación síncrona y asíncrona;
* interoperabilidad con servicios empresariales.

Este componente será la base del **Enterprise Agent Communication Bus (EACB)**, que actuará como el mecanismo oficial de intercambio de información del ecosistema multiagente.
