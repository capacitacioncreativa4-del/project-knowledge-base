# Traceability Rules

Establece las directrices y el bloque obligatorio YAML que cada objeto del PKB debe integrar para garantizar una auditoría determinística[cite: 11].

## Regla de Oro
> Ningún objeto de conocimiento podrá existir en el repositorio sin conocer de forma explícita su fuente primaria de origen.[cite: 11]

## Bloque YAML Obligatorio (Esquema)
```yaml
source:
  conversation: "ID-DE-CONVERSACION"
  session: "ID-DE-SESION"
  package: "ID-DE-PAQUETE"
derived_from: "ID-PADRE"
related_to: "ID-RELACIONADO"
validated_by: "RESPONSABLE"
pipeline_version: "1.0.0" # DEC-0023 Garantía Determinística
```[cite: 11]