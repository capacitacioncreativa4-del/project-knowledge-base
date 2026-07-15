# Ontología del Metamodelo PKB (v1.0.0)

Este documento define la coherencia semántica aplicable a todos los proyectos de conocimiento que hereden la plataforma PKB[cite: 5].

## 1. Axiomas de Integridad Relacional
* **Axioma 1 (No-Aislamiento):** No se permiten "nodos huérfanos" en el grafo. Todo objeto ingestión (salvo las conversaciones de entrada original) debe declarar al menos una relación de tipo `documents` o `implements` hacia su origen o destino[cite: 4, 5].
* **Axioma 2 (Alineación de Direccionalidad):** Las aristas son dirigidas para asegurar la traza desde la toma de decisiones hasta la implementación de componentes[cite: 3].

## 2. Matriz de Cardinalidades Esperadas
| Entidad Origen | Relación | Entidad Destino | Cardinalidad |
| :--- | :--- | :--- | :--- |
| `Standard` | `governs` | `Requirement` | 1:N |
| `Task` | `resolves` | `Risk` | 1:1 |
| `EngineeringSession` | `documents` | `ADR` | N:M |