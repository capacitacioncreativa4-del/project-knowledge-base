---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 76
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Prosigue

Perfecto. A partir de este punto entramos en uno de los capítulos más importantes de todo el **Platform Engineering Guide**.

En proyectos de gran escala, la arquitectura suele degradarse con el tiempo (*architecture erosion*): aparecen dependencias no previstas, excepciones permanentes, duplicación de lógica y pérdida de coherencia. El objetivo del **Architecture Compliance Manual (ACM)** es evitar ese fenómeno mediante controles verificables y automatizables.

---

# EPIC-03 — Platform Engineering Guide

# CAPÍTULO 6 — Architecture Compliance Manual (ACM)

## Objetivo

Definir el marco institucional para verificar de forma continua que toda evolución del MIPSP-Editor mantiene conformidad con la arquitectura de referencia.

El ACM convierte la arquitectura en un conjunto de reglas comprobables mediante procesos manuales y automatizados.

---

# ACM-001 — Principio de Conformidad Arquitectónica

## Arquitectura tradicional

```text
Arquitectura

↓

Implementación

↓

Desviaciones

↓

Refactorización costosa
```

## Arquitectura gobernada

```text
Arquitectura

↓

Reglas de conformidad

↓

Validación continua

↓

Corrección temprana

↓

Arquitectura preservada
```

La conformidad se verifica durante todo el ciclo de vida, no únicamente en auditorías puntuales.

---

# ACM-002 — Modelo de Cumplimiento

```text
Architecture Principles

↓

Reference Architectures

↓

Engineering Standards

↓

Compliance Rules

↓

Automated Validation

↓

Compliance Dashboard

↓

Continuous Improvement
```

---

# ACM-003 — Niveles de Conformidad

Se establecen cuatro niveles de evaluación:

| Nivel   | Alcance                                  |
| ------- | ---------------------------------------- |
| Nivel 1 | Código y estructura de módulos           |
| Nivel 2 | Integración entre componentes            |
| Nivel 3 | Cumplimiento de arquitectura empresarial |
| Nivel 4 | Gobierno institucional y operación       |

Cada nivel posee criterios específicos de aceptación.

---

# ACM-004 — Categorías de Reglas

Las reglas se agrupan en:

```text
Compliance Rules

├── Domain Rules
├── Dependency Rules
├── API Rules
├── Event Rules
├── Security Rules
├── Workflow Rules
├── Knowledge Rules
├── Agent Rules
├── Deployment Rules
└── Documentation Rules
```

Cada categoría se vincula con los dominios arquitectónicos correspondientes.

---

# ACM-005 — Reglas de Dependencias

Ejemplos:

* La capa **Domain** no depende de **Infrastructure**.
* Los módulos no acceden directamente a bases de datos ajenas.
* Los servicios sólo utilizan contratos públicos de otros módulos.
* Las referencias circulares están prohibidas.

Estas reglas pueden verificarse mediante análisis estático.

---

# ACM-006 — Reglas para APIs

Toda API debe demostrar:

* contrato vigente;
* versionado válido;
* documentación actualizada;
* autenticación y autorización configuradas;
* observabilidad habilitada;
* compatibilidad con el modelo canónico.

Las APIs que incumplan estos requisitos no pueden certificarse.

---

# ACM-007 — Reglas para Eventos

Cada evento debe cumplir:

```text
Business Meaning

↓

Canonical Schema

↓

Version

↓

Owner

↓

Documentation

↓

Traceability
```

No se permiten eventos sin propietario funcional.

---

# ACM-008 — Reglas para el Knowledge Graph

Todo activo de conocimiento verifica:

* clasificación;
* responsable;
* vigencia;
* relaciones semánticas;
* historial de cambios;
* evidencia documental.

Esto preserva la integridad del conocimiento institucional.

---

# ACM-009 — Reglas para Agentes de IA

Cada agente mantiene un expediente de conformidad con:

* propósito autorizado;
* herramientas permitidas;
* políticas aplicables;
* límites de autonomía;
* métricas de desempeño;
* historial de certificaciones.

Los agentes sólo operan dentro de los límites definidos por las políticas institucionales.

---

# ACM-010 — Reglas para Workflows

Cada flujo debe garantizar:

* inicio y fin definidos;
* estados consistentes;
* responsables identificados;
* manejo de excepciones;
* cumplimiento de SLA;
* generación de eventos de negocio.

---

# ACM-011 — Validación Automatizada

La conformidad se verifica automáticamente en el pipeline:

```text
Source Code

↓

Architecture Rules Engine

↓

Compliance Validation

↓

Evidence

↓

Approval / Rejection
```

Las desviaciones se detectan antes del despliegue.

---

# ACM-012 — Matriz de Trazabilidad

Todo componente mantiene relaciones explícitas con:

```text
Business Requirement

↓

ADR

↓

Domain Model

↓

Implementation

↓

Tests

↓

Deployment

↓

Observability
```

Esta trazabilidad facilita auditorías y análisis de impacto.

---

# ACM-013 — Gestión de Desviaciones

Cuando se detecta una no conformidad:

```text
Finding

↓

Risk Assessment

↓

Corrective Plan

↓

Temporary Exception (si aplica)

↓

Verification

↓

Closure
```

Las desviaciones no pueden permanecer indefinidamente abiertas.

---

# ACM-014 — Indicadores de Conformidad

Ejemplos:

* porcentaje de componentes conformes;
* excepciones activas;
* desviaciones críticas;
* deuda arquitectónica;
* tiempo medio de corrección;
* cumplimiento por dominio.

Estos indicadores alimentan los paneles ejecutivos definidos en la ORA.

---

# ACM-015 — Integración con el EGADF

El **Enterprise Governance & Architecture Decision Framework** utiliza el ACM para:

* supervisar el cumplimiento de principios;
* revisar excepciones;
* priorizar la reducción de deuda técnica;
* evaluar la evolución arquitectónica.

La gobernanza se apoya en evidencias objetivas.

---

# ACM-016 — Integración con EQVA

El **Enterprise Quality & Verification Architecture** incorpora la conformidad arquitectónica como un criterio de certificación.

Un componente puede superar las pruebas funcionales y, aun así, ser rechazado por incumplir reglas de arquitectura.

---

# ACM-017 — Auditorías Arquitectónicas

Se establecen tres tipos:

1. **Preventivas**, durante el desarrollo.
2. **Periódicas**, sobre componentes en producción.
3. **Extraordinarias**, tras incidentes relevantes o cambios estratégicos.

Cada auditoría produce un informe y recomendaciones.

---

# ACM-018 — Caso de Uso en Seguridad Privada

Se incorpora un nuevo módulo para la gestión de inspecciones operativas.

Antes de su liberación:

1. Se valida el modelo de dominio.
2. Se revisan contratos API y eventos.
3. Se verifica el cumplimiento de políticas.
4. Se comprueba la observabilidad.
5. Se ejecutan pruebas de conformidad arquitectónica.
6. Se emite un certificado de cumplimiento.

Sólo entonces el módulo puede promoverse a producción.

---

# ACM-019 — Beneficios

El Architecture Compliance Manual aporta:

* preservación de la arquitectura a largo plazo;
* detección temprana de desviaciones;
* automatización de revisiones;
* reducción de deuda técnica;
* trazabilidad completa;
* soporte para auditorías internas y externas;
* confianza en la evolución de la plataforma.

---

# ACM-020 — Resultado del Capítulo

Con el ACM, el MIPSP-Editor incorpora un mecanismo permanente para proteger la integridad de su arquitectura. La conformidad deja de depender de revisiones ocasionales y pasa a verificarse de forma continua, integrada con el ciclo de desarrollo, las pruebas, la observabilidad y la gobernanza.

---

# Estado actualizado del Platform Engineering Guide

```text
Platform Engineering Guide

├── Filosofía de Ingeniería                         ✓
├── Organización del Repositorio                    ✓
├── Engineering Standards Catalog                   ✓
├── Development Lifecycle Framework                 ✓
├── CI/CD Engineering Handbook                      ✓
├── Engineering Playbooks                           ✓
├── Architecture Compliance Manual                  ✓
├── Enterprise Templates                            □
├── Engineering Checklists                          □
└── Engineering Reference Catalog                   □
```

## Evolución del plan

Propongo un ajuste menor respecto al esquema inicial. En lugar de finalizar el PEG únicamente con **Enterprise Templates** y **Engineering Checklists**, conviene añadir un último componente:

**Engineering Reference Catalog (ERC).**

Este catálogo reunirá todas las implementaciones de referencia de bajo nivel que servirán como base para el siguiente entregable (**Enterprise SDK**):

* estructuras estándar de módulos;
* plantillas de APIs;
* plantillas de eventos;
* plantillas de agentes;
* plantillas de workflows;
* plantillas de políticas;
* modelos de telemetría;
* componentes reutilizables.

Con ello, el **Platform Engineering Guide** no sólo describirá cómo debe desarrollarse el sistema, sino que proporcionará los patrones concretos que los equipos utilizarán para iniciar la implementación del SDK y de las implementaciones de referencia. Este será el último paso antes de entrar en la fase de construcción del software.
