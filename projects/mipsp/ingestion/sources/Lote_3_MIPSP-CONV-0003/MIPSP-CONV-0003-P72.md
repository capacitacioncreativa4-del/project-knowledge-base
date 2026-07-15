---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 72
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante, continúa

Perfecto. A partir de este punto, el **Platform Engineering Guide (PEG)** deja de describir principios generales y comienza a establecer **normas de ingeniería verificables**. Este cambio es importante: una arquitectura sólo puede preservarse en el tiempo si sus reglas pueden auditarse de manera objetiva.

---

# EPIC-03 — Platform Engineering Guide

# CAPÍTULO 2 — Engineering Standards Catalog (ESC)

## Objetivo

El **Engineering Standards Catalog (ESC)** constituye el catálogo normativo de ingeniería del MIPSP-Editor.

Cada estándar posee:

* un identificador único;
* un objetivo;
* un alcance;
* reglas obligatorias;
* criterios de verificación;
* excepciones permitidas;
* referencias a otros estándares.

Esto permite automatizar revisiones y evaluaciones de conformidad.

---

# ESC-001 — Estructura de un Estándar

Todos los estándares adoptan el siguiente metamodelo:

```text
Engineering Standard

├── Standard ID
├── Name
├── Category
├── Objective
├── Scope
├── Mandatory Rules
├── Recommendations
├── Verification Method
├── Exceptions
├── Related Standards
└── Version
```

Con esta estructura, el catálogo puede integrarse posteriormente con el **Policy Engine**, permitiendo verificar automáticamente el cumplimiento de normas de ingeniería.

---

# ESC-002 — Clasificación del Catálogo

Los estándares se organizan por familias.

```text
ESC

├── Coding Standards
├── API Standards
├── Event Standards
├── Workflow Standards
├── Knowledge Standards
├── Agent Standards
├── Security Standards
├── Testing Standards
├── Documentation Standards
├── Deployment Standards
├── Observability Standards
└── Governance Standards
```

Cada familia corresponde a uno o más dominios arquitectónicos definidos anteriormente.

---

# ESC-003 — Coding Standards (CS)

## Objetivo

Garantizar uniformidad en la implementación del código fuente.

### Reglas generales

* El código expresa el dominio de negocio.
* Los nombres deben ser semánticos.
* Se evita la duplicación de lógica.
* Los métodos mantienen una única responsabilidad.
* Las dependencias se inyectan mediante interfaces.
* No se permite lógica institucional fuera del dominio o del motor de políticas.

### Verificación

* Análisis estático.
* Revisión por pares.
* Validación automática en CI.

---

# ESC-004 — API Standards (AS)

Toda API debe definir explícitamente:

```text
API

↓

Contract

↓

Version

↓

Authentication

↓

Authorization

↓

Observability

↓

Documentation
```

Reglas:

* Compatibilidad hacia atrás cuando proceda.
* Versionado explícito.
* Contratos independientes de la implementación.
* Identificadores de correlación.
* Instrumentación desde la primera versión.

---

# ESC-005 — Event Standards (ES)

Cada evento institucional deberá incluir, como mínimo:

```text
Event

├── Event ID
├── Event Type
├── Timestamp
├── Source
├── Correlation ID
├── Aggregate ID
├── Payload
└── Metadata
```

Los eventos son inmutables y no se modifican después de su publicación.

---

# ESC-006 — Workflow Standards (WS)

Todo flujo institucional debe demostrar:

* inicio claramente definido;
* finalización explícita;
* tratamiento de excepciones;
* tiempos objetivo;
* responsables;
* eventos generados;
* políticas aplicables.

No se admiten procesos con estados ambiguos.

---

# ESC-007 — Knowledge Standards (KS)

Cada activo de conocimiento mantiene:

```text
Knowledge Asset

↓

Classification

↓

Owner

↓

Version

↓

Lifecycle

↓

Traceability
```

Los activos sin responsable o sin control de versiones no pueden publicarse.

---

# ESC-008 — Agent Standards (AGS)

Todo agente declara:

* propósito;
* capacidades;
* herramientas autorizadas;
* restricciones;
* políticas aplicables;
* nivel de autonomía;
* métricas;
* responsable funcional.

Además, debe poder auditarse cada decisión relevante.

---

# ESC-009 — Security Standards (SS)

Todo componente verifica:

* autenticación;
* autorización;
* protección de secretos;
* cifrado cuando corresponda;
* generación de evidencias;
* registros de auditoría;
* clasificación de datos.

El incumplimiento de estos controles bloquea la promoción a producción.

---

# ESC-010 — Testing Standards (TS)

Se establecen niveles mínimos de pruebas:

```text
Static Analysis

↓

Unit Tests

↓

Integration Tests

↓

Contract Tests

↓

System Tests

↓

Acceptance Tests
```

Cada componente define objetivos mínimos de cobertura y criterios de aceptación acordes con su criticidad.

---

# ESC-011 — Documentation Standards (DS)

Todo módulo debe incluir:

* descripción funcional;
* arquitectura;
* contratos;
* dependencias;
* decisiones relevantes (ADR);
* guía de despliegue;
* historial de cambios.

La documentación forma parte del entregable.

---

# ESC-012 — Deployment Standards (DPS)

Cada despliegue requiere:

* automatización;
* validación previa;
* reversión definida;
* trazabilidad;
* registro de versión;
* evidencia de aprobación.

No se permiten despliegues manuales en producción salvo procedimientos excepcionales documentados.

---

# ESC-013 — Observability Standards (OS)

Todo servicio expone:

* métricas;
* registros;
* trazas distribuidas;
* eventos de negocio;
* indicadores de salud;
* identificadores de correlación.

La ausencia de instrumentación constituye una no conformidad.

---

# ESC-014 — Governance Standards (GS)

Cada módulo mantiene:

* propietario técnico;
* propietario funcional;
* estándares aplicables;
* estado de cumplimiento;
* excepciones autorizadas;
* deuda técnica registrada;
* ADR asociados.

Esto asegura la trazabilidad de su evolución.

---

# ESC-015 — Verificación Automática

Los estándares deben ser verificables mediante herramientas automáticas siempre que sea posible.

```text
Source Code

↓

Static Analysis

↓

Policy Validation

↓

Architecture Rules

↓

Compliance Report
```

La conformidad deja de depender exclusivamente de revisiones manuales.

---

# ESC-016 — Matriz de Trazabilidad

Cada estándar se vincula con:

* dominios arquitectónicos;
* políticas institucionales;
* pruebas automatizadas;
* controles de calidad;
* métricas de observabilidad.

Esto crea una cadena continua de gobernanza desde el diseño hasta la operación.

---

# ESC-017 — Gestión de Excepciones

Las excepciones a un estándar deben:

1. estar justificadas;
2. incluir análisis de riesgos;
3. definir medidas compensatorias;
4. tener una fecha de revisión;
5. contar con aprobación del órgano de gobierno arquitectónico.

Las excepciones son temporales y auditables.

---

# ESC-018 — Certificación de Cumplimiento

Cada componente recibe un estado:

```text
Certified

Conditionally Certified

Under Remediation

Non-Compliant
```

Este estado condiciona su incorporación a los siguientes entornos de despliegue.

---

# ESC-019 — Integración con EQVA

El **Enterprise Quality & Verification Architecture** utiliza el catálogo para evaluar automáticamente la conformidad de componentes, procesos y artefactos.

De esta manera, el catálogo no sólo documenta reglas; también sirve como base para la certificación continua.

---

# ESC-020 — Resultado del Capítulo

Con el **Engineering Standards Catalog**, el MIPSP-Editor dispone de un marco normativo de ingeniería que conecta arquitectura, desarrollo, calidad y operación. Cada componente puede evaluarse de forma objetiva respecto a estándares institucionales, reduciendo variabilidad entre equipos y facilitando auditorías técnicas.

---

# Estado del Platform Engineering Guide

```text
Platform Engineering Guide

├── Filosofía de Ingeniería                         ✓
├── Organización del Repositorio                    ✓
├── Arquitectura de Capas                           ✓
├── Organización Modular                            ✓
├── Convenciones Generales                          ✓
├── Engineering Standards Catalog                   ✓
├── Development Lifecycle                           □
├── CI/CD Engineering Handbook                      □
├── Engineering Playbooks                           □
├── Architecture Compliance Manual                  □
├── Enterprise Templates                            □
└── Engineering Checklists                          □
```

## Evaluación

Con los dos primeros capítulos, el **Platform Engineering Guide** ya define **qué principios rigen la ingeniería** y **qué normas deben cumplirse**. El siguiente capítulo dará un paso adicional: describirá el **Development Lifecycle (DLC)**, especificando el ciclo de vida completo de un cambio, desde la identificación de una necesidad hasta su despliegue, monitoreo y retroalimentación. Ese capítulo enlazará directamente con los dominios de gobernanza, calidad, observabilidad y resiliencia definidos durante la fase arquitectónica, convirtiéndose en la guía operativa para todos los equipos de desarrollo.
