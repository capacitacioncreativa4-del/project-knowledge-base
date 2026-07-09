---
id: PKB-KERNEL-METADATA-001
title: Metadata Model
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
type: Kernel
parent: PKB-KERNEL-MANIFEST-001
---

# Modelo de Metadatos del Project Knowledge Base

## Propósito
Definir el conjunto mínimo y obligatorio de metadatos que deberán acompañar a todos los activos del Project Knowledge Base (PKB), con independencia de su tipo, con el fin de garantizar su identificación única, trazabilidad, versionado, descubrimiento, automatización e interoperabilidad.

---

# Principios de los Metadatos
Los metadatos del sistema deberán cumplir estrictamente con los siguientes lineamientos:
- **Obligatorios**: Todo documento integrado al ecosistema debe poseer un bloque declarativo.
- **Legibles por personas**: Diseñados para una comprensión humana inmediata.
- **Procesables por herramientas**: Estructurados de manera simétrica para facilitar el procesamiento por parte de herramientas y sistemas de IA.
- **Compatibles**: Soportados de forma nativa a través de formatos Markdown y delimitadores YAML.
- **Estables a largo plazo**: Creados para escalar sin sufrir variaciones estructurales continuas.

---

# Encabezado YAML Institucional y Vocabulario Controlado
Todo activo comenzará obligatoriamente con un bloque YAML. Para evitar la degradación informativa y garantizar la consistencia, los campos principales se rigen bajo un **vocabulario controlado**:

```yaml
---
id: PKB-GOV-VISION-001
title: Vision
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: Governance
domain: PKB
parent: PKB-KERNEL-MANIFEST-001
tags:
  - governance
  - strategy
  - vision
---