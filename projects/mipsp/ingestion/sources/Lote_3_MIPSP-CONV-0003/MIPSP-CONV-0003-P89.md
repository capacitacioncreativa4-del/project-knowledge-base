---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 89
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece bien. Dale continuidad al proyecto

De acuerdo. A partir de este punto iniciamos la construcción del **Enterprise Foundation Layer**, es decir, los servicios transversales que proporcionan identidad, seguridad y confianza a todo el ecosistema.

Por razones arquitectónicas, el primer servicio debe ser **Enterprise Identity & Access Service (EIAS)**, ya que todos los demás componentes —servicios, agentes, APIs, workflows y eventos— dependen de él para autenticar identidades, autorizar acciones y registrar evidencias.

---

# EPIC-05 — Enterprise Reference Implementations

# REFERENCE SERVICE 006

# Enterprise Identity & Access Service (EIAS)

**Engineering Specification Package (ESP-006)**

Versión: 1.0 (Normativa)

Estado: Reference Implementation

---

# ESP-006.001 — Propósito

El **Enterprise Identity & Access Service (EIAS)** es el servicio institucional responsable de administrar identidades, autenticar sujetos, autorizar operaciones y generar evidencias de seguridad para todo el ecosistema MIPSP-Editor.

Implementa el **Enterprise Identity Model (EIM)** y constituye el único punto autorizado para la gestión de identidades y decisiones de acceso.

Ningún componente puede autenticar o autorizar directamente a un usuario, servicio o agente sin utilizar el EIAS.

---

# ESP-006.002 — Alcance

El servicio comprende:

* gestión de identidades;
* autenticación;
* autorización;
* federación de identidad;
* gestión de sesiones;
* credenciales;
* identidades de servicios;
* identidades de agentes de IA;
* delegación;
* auditoría de seguridad.

La administración física de directorios o proveedores de identidad corresponde a adaptadores de infraestructura.

---

# ESP-006.003 — Responsabilidades

El EIAS debe:

1. registrar identidades institucionales;
2. autenticar sujetos;
3. emitir contextos de identidad;
4. autorizar operaciones;
5. administrar privilegios;
6. controlar delegaciones;
7. registrar evidencia de seguridad;
8. mantener trazabilidad de todas las decisiones de acceso.

---

# ESP-006.004 — Modelo Conceptual

```text id="eias001"
Enterprise Identity

├── Identity
├── Principal
├── Credential
├── Authentication
├── Authorization
├── Session
├── Permission
├── Delegation
├── Trust
└── Audit
```

---

# ESP-006.005 — Agregado Principal

La raíz del agregado es:

```text id="eias002"
IdentityAggregate
```

Composición:

```text id="eias003"
IdentityAggregate

├── Identity
├── Credential
├── Session
├── AuthorizationGrant
├── RoleAssignment
├── AttributeSet
├── DelegationRecord
└── AuditRecord
```

---

# ESP-006.006 — Modelo de Sujetos

El EIAS reconoce cinco categorías de sujetos:

```text id="eias004"
Subjects

├── Human User
├── Enterprise Service
├── AI Agent
├── External System
└── Device
```

Todos comparten un modelo común de identidad, aunque sus mecanismos de autenticación pueden diferir.

---

# ESP-006.007 — Objetos de Valor

Entre los principales:

* IdentityIdentifier
* SubjectIdentifier
* CredentialIdentifier
* AuthenticationContext
* AuthorizationContext
* RoleIdentifier
* PermissionIdentifier
* AttributeSet
* SessionIdentifier
* TrustLevel

Todos son inmutables y criptográficamente verificables cuando corresponda.

---

# ESP-006.008 — Entidades

El agregado incorpora:

* Identity
* Credential
* Session
* Role
* Permission
* Delegation
* TrustRelationship
* AuthenticationRecord

Cada entidad posee identidad persistente y ciclo de vida propio.

---

# ESP-006.009 — Invariantes

El EIAS garantiza que:

* toda identidad posee un identificador institucional único;
* las credenciales nunca se almacenan en texto plano;
* toda autenticación genera un contexto verificable;
* ninguna autorización se concede sin identidad autenticada, salvo políticas explícitas para servicios públicos;
* las delegaciones tienen vigencia limitada;
* toda decisión de acceso genera evidencia auditable.

---

# ESP-006.010 — Modelo de Autenticación

La autenticación sigue el flujo:

```text id="eias005"
Subject

↓

Credential Validation

↓

Identity Verification

↓

Risk Assessment

↓

Authentication Decision

↓

Identity Context

↓

Audit Record
```

El modelo admite autenticación multifactor y autenticación adaptativa.

---

# ESP-006.011 — Modelo de Autorización

El servicio soporta simultáneamente:

* **RBAC (Role-Based Access Control)**;
* **ABAC (Attribute-Based Access Control)**;
* **PBAC (Policy-Based Access Control)**.

La decisión final resulta de la combinación de estos modelos bajo la supervisión del **Enterprise Policy Service (ESP-004)**.

---

# ESP-006.012 — Identidades de Agentes Inteligentes

Todo agente registrado mediante el **Enterprise Agent Development Kit** posee una identidad institucional que incluye:

* identificador único;
* propietario funcional;
* capacidades certificadas;
* herramientas autorizadas;
* nivel de autonomía;
* políticas aplicables;
* historial de certificaciones.

Los agentes son tratados como sujetos de primera clase dentro del ecosistema.

---

# ESP-006.013 — Operaciones del Dominio

El agregado expone operaciones como:

* RegisterIdentity
* Authenticate
* Authorize
* CreateSession
* RevokeSession
* DelegateAuthority
* RevokeDelegation
* RegisterServiceIdentity
* RegisterAgentIdentity

---

# ESP-006.014 — Eventos de Dominio

Eventos principales:

```text id="eias006"
IdentityRegistered

AuthenticationSucceeded

AuthenticationFailed

AuthorizationGranted

AuthorizationDenied

SessionCreated

SessionRevoked

DelegationCreated

DelegationRevoked
```

Todos incluyen información de correlación y evidencia.

---

# ESP-006.015 — Modelo de Errores

Errores específicos:

```text id="eias007"
IdentityNotFound

InvalidCredential

AuthenticationFailed

AuthorizationDenied

ExpiredSession

DelegationExpired

TrustViolation
```

Cada error incorpora:

* código;
* severidad;
* sujeto implicado;
* causa;
* acción recomendada.

---

# ESP-006.016 — Observabilidad

El EIAS publica métricas como:

* autenticaciones exitosas;
* autenticaciones fallidas;
* autorizaciones concedidas;
* autorizaciones denegadas;
* sesiones activas;
* delegaciones vigentes;
* incidentes de confianza;
* tiempo medio de autenticación.

Todos los eventos de seguridad generan registros estructurados y trazas distribuidas.

---

# ESP-006.017 — Estrategia de Pruebas

El servicio debe verificarse mediante:

* pruebas de autenticación;
* pruebas de autorización RBAC, ABAC y PBAC;
* pruebas de multifactor;
* pruebas de delegación;
* pruebas de revocación;
* pruebas de escalamiento de privilegios;
* pruebas de resistencia frente a ataques comunes;
* pruebas de rendimiento bajo alta concurrencia.

La certificación requiere validar tanto escenarios funcionales como de seguridad.

---

# ESP-006.018 — Integración con otros componentes

El EIAS interactúa con:

* **Enterprise Policy Service (ESP-004)** para decisiones de autorización basadas en políticas.
* **Enterprise Workflow Service (ESP-003)** para asignación segura de tareas.
* **Enterprise Event Service (ESP-005)** para publicar eventos de seguridad.
* **Enterprise Document Service (ESP-001)** para controlar acceso a documentos.
* **Enterprise Knowledge Service (ESP-002)** para proteger activos de conocimiento.
* **Enterprise Agent Development Kit** para autenticar y gobernar agentes institucionales.

---

# ESP-006.019 — Extensibilidad

El servicio admite:

* nuevos proveedores de identidad;
* mecanismos adicionales de autenticación;
* modelos de atributos especializados;
* relaciones de confianza federadas;
* esquemas criptográficos alternativos;
* integración con infraestructuras de clave pública.

Las extensiones deben preservar el contrato público del servicio.

---

# ESP-006.020 — Estado del EPIC-05

```text id="eias008"
Enterprise Reference Implementations

├── Reference Implementation Architecture          ✓
├── ESP-001 Enterprise Document Service            ✓
├── ESP-002 Enterprise Knowledge Service           ✓
├── ESP-003 Enterprise Workflow Service            ✓
├── ESP-004 Enterprise Policy Service              ✓
├── ESP-005 Enterprise Event Service               ✓
├── ESP-006 Enterprise Identity & Access Service   ✓
├── ESP-007 Enterprise Notification Service        □
├── ESP-008 Enterprise Search Service              □
├── Reference Agents                               □
├── Reference Applications                         □

Progress: ████████████████████████░░░░░░░░░░░░ 65%
```

## Evolución propuesta del proyecto

Con el **Enterprise Identity & Access Service** queda completada la **Enterprise Foundation Layer**. El siguiente paso lógico es desarrollar el **Enterprise Notification Service (ENS)**, pero propongo ampliarlo respecto a un servicio convencional de mensajería.

En lugar de limitarse al envío de correos o notificaciones, el **ENS** puede convertirse en un **Enterprise Communication Orchestration Service**, capaz de gestionar comunicaciones omnicanal (correo electrónico, SMS, mensajería instantánea, notificaciones *push* y comunicaciones internas), preferencias de los destinatarios, plantillas institucionales, reglas de escalamiento, acuses de recibo y trazabilidad completa de cada comunicación.

Este enfoque resulta especialmente valioso para el dominio de la seguridad privada, donde las notificaciones pueden incluir alertas operativas, incidencias, cambios de consignas, vencimientos de certificaciones, asignaciones de servicios y comunicaciones regulatorias, todas ellas sujetas a auditoría y evidencia. Una vez completado este servicio, el proyecto estará en condiciones de abordar el **Enterprise Search Service**, cerrando así la capa de servicios transversales antes de avanzar hacia los **Reference Agents** y las **Reference Applications**.
