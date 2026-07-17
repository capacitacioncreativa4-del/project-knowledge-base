---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 79
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Continúa con el proyecto

Perfecto. Llegamos ahora al componente que, desde el punto de vista de la arquitectura, será el más importante de todo el **Enterprise SDK**.

Mientras que **SDK-Core** proporciona infraestructura técnica, **SDK-Domain** implementa el **lenguaje institucional del negocio**. Todo el software del MIPSP-Editor deberá construirse sobre estas abstracciones para preservar un modelo de dominio consistente y evitar que la lógica de negocio se disperse por las capas técnicas.

En esta etapa conviene elevar el nivel de formalismo respecto a las entregas anteriores. El SDK-Domain debe ser suficientemente preciso para servir como especificación de implementación.

---

# EPIC-04 — Enterprise SDK

# PAQUETE 2 — SDK-Domain

## Objetivo

Definir las abstracciones del dominio empresarial que servirán como fundamento para todos los módulos funcionales del MIPSP-Editor.

El SDK-Domain implementa el **Enterprise Business Domain Architecture (EBDA)**, el **Canonical Information Model (CIM)** y los principios de diseño del dominio establecidos en la arquitectura.

---

# SDKD-001 — Arquitectura del Dominio

```text
Enterprise Domain

├── Domain Primitives
├── Value Objects
├── Entities
├── Aggregates
├── Aggregate Roots
├── Domain Events
├── Domain Services
├── Repository Contracts
├── Specifications
├── Policies
├── Domain Rules
├── Factories
├── Domain Exceptions
├── Commands
├── Queries
└── Read Models
```

Todo elemento del dominio pertenece exactamente a una de estas categorías.

---

# SDKD-002 — Primitivos del Dominio

Los **Domain Primitives** representan conceptos atómicos con significado institucional.

Ejemplos:

* Identificador institucional.
* Código operativo.
* Estado documental.
* Nivel de prioridad.
* Clasificación de riesgo.
* Tipo de incidente.
* Estado de autorización.
* Nivel de confidencialidad.

Los primitivos eliminan el uso indiscriminado de tipos genéricos y mejoran la expresividad del modelo.

---

# SDKD-003 — Objetos de Valor (Value Objects)

Un **Value Object** se caracteriza por:

* identidad basada exclusivamente en sus atributos;
* inmutabilidad;
* validación en el momento de su creación;
* ausencia de ciclo de vida propio.

Ejemplos en el contexto del MIPSP-Editor:

* Rango horario de un servicio.
* Coordenadas geográficas.
* Dirección postal.
* Periodo de vigencia.
* Importe monetario.
* Clasificación documental.

Los objetos de valor pueden compartirse entre distintos agregados sin pérdida de integridad.

---

# SDKD-004 — Entidades

Una entidad posee:

* identidad persistente;
* ciclo de vida;
* historial de cambios;
* reglas de consistencia.

Ejemplos:

* Elemento operativo.
* Cliente.
* Servicio contratado.
* Consigna operativa.
* Documento institucional.
* Puesto de vigilancia.

Las entidades evolucionan a lo largo del tiempo manteniendo su identidad.

---

# SDKD-005 — Agregados

Los agregados delimitan fronteras de consistencia.

```text
Aggregate

├── Aggregate Root
├── Entity
├── Entity
├── Value Object
├── Value Object
└── Domain Events
```

Toda modificación del agregado ocurre a través de la raíz del agregado.

---

# SDKD-006 — Raíz del Agregado

La **Aggregate Root** es responsable de:

* preservar invariantes;
* coordinar entidades internas;
* emitir eventos de dominio;
* controlar transacciones del agregado;
* garantizar consistencia.

Nunca se modifica una entidad interna de manera directa desde el exterior.

---

# SDKD-007 — Eventos de Dominio

Los eventos representan hechos de negocio consumados.

Ejemplos:

* ServicioAsignado.
* ConsignaActualizada.
* IncidenteRegistrado.
* GuardiaRelevado.
* DocumentoPublicado.
* ClienteActivado.

Cada evento debe ser:

* inmutable;
* fechado;
* identificable;
* trazable;
* versionado.

---

# SDKD-008 — Servicios de Dominio

Los **Domain Services** encapsulan reglas que no pertenecen naturalmente a una única entidad.

Ejemplos:

* cálculo de cobertura operativa;
* asignación óptima de personal;
* validación de conflictos entre consignas;
* evaluación de riesgos.

Los servicios de dominio nunca contienen detalles de infraestructura.

---

# SDKD-009 — Contratos de Repositorio

Los repositorios representan la persistencia desde la perspectiva del dominio.

Reglas:

* el dominio no conoce la tecnología de almacenamiento;
* los contratos son estables;
* las implementaciones pertenecen a la capa de infraestructura.

Esto preserva el principio de inversión de dependencias.

---

# SDKD-010 — Especificaciones

Las **Specifications** encapsulan reglas complejas de selección y validación.

Ejemplos:

* servicios vencidos;
* personal con certificación vigente;
* clientes con pagos pendientes;
* documentos obligatorios faltantes.

Las especificaciones pueden componerse y reutilizarse.

---

# SDKD-011 — Políticas del Dominio

Las políticas expresan restricciones permanentes del negocio.

Ejemplos:

* una consigna crítica requiere doble aprobación;
* un supervisor no puede aprobar su propia modificación;
* un servicio no puede iniciar sin personal asignado.

Estas políticas son independientes de la interfaz de usuario y del mecanismo de persistencia.

---

# SDKD-012 — Reglas de Dominio

Las reglas se clasifican como:

```text
Domain Rules

├── Validation Rules
├── Authorization Rules
├── Consistency Rules
├── Temporal Rules
├── Operational Rules
└── Regulatory Rules
```

Esta clasificación facilita su reutilización y auditoría.

---

# SDKD-013 — Fábricas

Las fábricas crean agregados complejos garantizando que nacen en un estado válido.

Se utilizan cuando la construcción requiere:

* múltiples objetos;
* validaciones previas;
* inicialización consistente.

---

# SDKD-014 — Excepciones de Dominio

Las excepciones reflejan violaciones del modelo de negocio, no errores técnicos.

Ejemplos:

* ConsignaInválida.
* ClienteSuspendido.
* RiesgoNoAceptable.
* PersonalNoDisponible.

Las excepciones técnicas permanecen en SDK-Core.

---

# SDKD-015 — Commands y Queries

El SDK adopta separación conceptual entre:

* **Commands**, que modifican el estado.
* **Queries**, que consultan información.

Esta separación facilita la evolución hacia arquitecturas CQRS cuando resulte necesario.

---

# SDKD-016 — Read Models

Los modelos de lectura están optimizados para consulta y generación editorial.

No representan necesariamente el modelo transaccional.

Esto resulta especialmente útil para:

* generación documental;
* paneles ejecutivos;
* informes regulatorios;
* búsquedas complejas.

---

# SDKD-017 — Integración con Eventos Empresariales

Cada modificación significativa de un agregado genera eventos que alimentan el **Enterprise Event Architecture**.

```text
Aggregate

↓

State Change

↓

Domain Event

↓

Enterprise Event

↓

Workflow

↓

Knowledge Graph
```

Se mantiene la separación entre eventos internos del dominio y eventos publicados a nivel empresarial.

---

# SDKD-018 — Integración con el Sector de Seguridad Privada

Ejemplo de agregado:

```text
Servicio Operativo

├── Puestos
├── Consignas
├── Personal Asignado
├── Horarios
├── Cobertura
├── Riesgos
└── Eventos Operativos
```

La raíz del agregado garantiza que:

* no existan puestos sin cobertura autorizada;
* las consignas vigentes sean consistentes;
* los cambios relevantes generen eventos;
* las políticas institucionales se respeten antes de confirmar modificaciones.

---

# SDKD-019 — Beneficios

El SDK-Domain aporta:

* lenguaje ubicuo institucional;
* independencia tecnológica;
* consistencia del modelo;
* alta reutilización;
* facilidad para pruebas unitarias;
* alineación con la arquitectura empresarial.

---

# SDKD-020 — Estado del Enterprise SDK

```text
Enterprise SDK

├── SDK-Core                                   ✓
├── SDK-Domain                                 ✓
├── SDK-Platform                               □
├── SDK-AI                                     □
├── SDK-Developer                              □
├── SDK-Testing                                □

Progress: ████████████░░░░░░░░░░░░░░░░░░░░░░░ 33%
```

## Recomendación estratégica

A partir de este punto propongo un cambio metodológico que incrementará considerablemente el valor del proyecto.

Hasta ahora hemos descrito los componentes del SDK desde un punto de vista conceptual. Sin embargo, el siguiente paquete (**SDK-Platform**) será el punto donde la arquitectura se convierte en una especificación casi implementable.

Por ello, recomiendo que los próximos paquetes adopten un nivel de detalle adicional, incluyendo para cada componente:

* especificación de interfaces públicas;
* contratos de entrada y salida;
* modelo de errores;
* ciclo de vida;
* estados;
* puntos de extensión;
* dependencias;
* invariantes;
* requisitos de observabilidad;
* métricas;
* reglas de versionado;
* ejemplos de secuencia e integración.

Con ese enfoque, el resultado no será únicamente un documento de arquitectura, sino una **especificación técnica de referencia** suficientemente precisa para que un equipo de desarrollo pueda implementarla prácticamente sin reinterpretaciones, manteniendo la coherencia con toda la arquitectura definida en los EPIC anteriores. Este nivel de precisión también facilitará la futura generación automática de código, documentación y pruebas a partir de las especificaciones.
