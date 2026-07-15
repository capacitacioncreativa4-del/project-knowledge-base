# PKB-TRACEABILITY-POLICY: Política de Trazabilidad Bidireccional

## 1. Obligatoriedad de la Traza
Ningún objeto del PKB puede existir de forma aislada[cite: 2]. Es una condición obligatoria de calidad que todo artefacto de ingeniería sea completamente navegable en ambos sentidos del flujo de conocimiento[cite: 2]:

### Flujo Descendente (Forward Traceability)[cite: 2]:
`Conversation` ──► `Engineering Session` ──► `ADR` ──► `Requirement` ──► `Document` ──► `Knowledge Package`[cite: 2]

### Flujo Ascendente (Backward Traceability)[cite: 2]:
`Document` ──► `Requirement` ──► `ADR` ──► `Engineering Session` ──► `Conversation`[cite: 2]

## 2. Validación de Enlaces
El motor de validación semántica comprobará que los identificadores declarados en la propiedad `relationships` de cada manifiesto YAML existan físicamente en el repositorio.