# Package: Governance Templates (v1.0.0)

## Propósito
Este paquete provee las plantillas oficiales, guías de calidad y estructuras base obligatorias para el desarrollo de activos de gobierno, estándares normativos y registros de decisiones (ADRs) en el PKB.

## Contenido del Paquete
- **`TMP-001-GOVERNANCE.md`**: Estructura general para manifiestos, políticas y visiones estratégicas.
- **`TMP-002-ADR.md`**: Modelo normalizado para el registro de Decisiones Arquitectónicas.
- **`TMP-003-STANDARD.md`**: Plantilla base para la redacción de estándares técnicos[cite: 3].

## Criterios de Aceptación y Calidad (Checklist)
Antes de promover un objeto derivado de este paquete a estado `Approved`, verifique[cite: 3]:
- [ ] Bloque de metadatos YAML completo, con `type: GOV` o `type: STD` según corresponda[cite: 3].
- [ ] Identificador único generado bajo las reglas de `IDENTIFIER-SCHEME.md`[cite: 3].
- [ ] Enlaces relativos a documentos superiores e inversos completamente funcionales[cite: 3].