# PKB-LIFECYCLE-001: Ciclo de Vida Oficial de Objetos

## 1. Máquina de Estados Unificada
Todos los objetos informacionales (ADR, Requerimientos, Estándares, Sistemas, Esquemas) comparten el mismo ciclo de vida inmutable:

[Draft] ──► [Review] ──► [Validated] ──► [Approved] ──► [Published] ──► [Superseded] ──► [Archived]

## 2. Criterios de Transición y Evidencias[cite: 2]

### A. De Draft a Review[cite: 2]
* **Responsable:** Knowledge Engineer (Ingeniero de Conocimiento)[cite: 2].
* **Criterio de Entrada:** Estructura markdown básica redactada a partir de una sesión de origen[cite: 2].
* **Evidencia:** Archivo creado en el repositorio con un ID único[cite: 2].

### B. De Review a Validated[cite: 2]
* **Responsable:** Schema Repository Engine (Validador Automático)[cite: 2].
* **Criterio de Entrada:** El objeto pasa al 100% las pruebas de esquema[cite: 2].
* **Evidencia:** Log exitoso del pipeline de validación sintáctica[cite: 2].

### C. De Validated a Approved[cite: 2]
* **Responsable:** Architecture Authority (Autoridad de Arquitectura)[cite: 2].
* **Criterio de Entrada:** Consistencia semántica del metamodelo y relaciones válidas con el resto del grafo[cite: 2].
* **Evidencia:** Aprobación del commit o firma en el manifiesto del paquete[cite: 2].