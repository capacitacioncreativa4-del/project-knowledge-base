# PKB Domain Metamodel v1.0.0

* **Estado:** Baseline Inicial Validada por Evidencia Empírica.
* **Control de Cambios:** Cualquier modificación futura requerirá un ADR dedicado y un incremento de versión.

## 1. Registro Maestro de Identidades (Core Entities)
| Código | Entidad | Descripción |
| :--- | :--- | :--- |
| **CONV** | Conversation | Interacción origen que contiene sesiones de ingeniería.
| **KP** | Knowledge Package | Contenedor lógico de objetos de conocimiento extraídos.
| **SES** | Engineering Session | Unidad lógica de trabajo dentro de una conversación.
| **ADR** | Architecture Decision | Registro formal de decisiones de diseño y arquitectura.
| **REQ** | Requirement | Atributos funcionales o técnicos obligatorios del sistema.
| **STD** | Standard | Directrices, políticas o flujos uniformes que gobiernan el proyecto[cite: 11].
| **ART** | Conceptual Artifact | Modelos, mapas o marcos conceptuales de alto nivel[cite: 11].
| **DOC** | Editorial Document | Productos documentales finales e institucionales versionables[cite: 11].
| **SYS** | Institutional System | Componentes organizacionales con identidad y procesos propios[cite: 11].
| **TASK** | Task | Actividades de ingeniería y tareas operativas derivadas[cite: 11].
| **RSK** | Risk | Eventos identificados que puedan impactar al proyecto[cite: 11].

## 2. Matriz de Relaciones Oficiales (Core Relations)
* **CONV → contiene → SES:** Una conversación agrupa sesiones de ingeniería[cite: 11].
* **SES → produce → (Cualquier Objeto):** Las sesiones generan artefactos o decisiones[cite: 11].
* **ADR → origina → REQ:** Las decisiones arquitectónicas ramifican requisitos técnicos[cite: 11].
* **REQ → implementado por → DOC:** Los documentos materializan y satisfacen requisitos[cite: 11].
* **STD → regula → DOC:** Los estándares gobiernan el desarrollo formal de los documentos[cite: 11].
* **SYS → produce → DOC:** Los sistemas institucionales son propietarios de los entregables[cite: 11].
* **ART → organiza → DOC:** Los marcos conceptuales estructuran la entrega final[cite: 11].