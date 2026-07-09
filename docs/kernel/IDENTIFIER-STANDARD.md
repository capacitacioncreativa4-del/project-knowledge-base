---
id: PKB-KERNEL-IDSTD-001
title: Identifier Standard
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
type: Kernel
parent: PKB-KERNEL-MANIFEST-001
---

# Estándar de Identificadores Únicos y Persistentes

## Propósito
Definir la estructura formal, sintaxis y reglas de asignación para los identificadores únicos (`id`) de todos los activos del Project Knowledge Base (PKB), asegurando que cada objeto posea una clave persistente, predecible e inequívoca para humanos y agentes de IA.

---

# Estructura del Identificador (Sintaxis General)

Todos los identificadores oficiales del PKB seguirán de forma estricta un esquema de bloques alfanuméricos en mayúsculas separados por guiones medios:

$$\text{SISTEMA}-\text{CAPA/DOMINIO}-\text{COMPONENTE}-\text{SECUENCIAL}$$

### Campos del Esquema:
1. **SISTEMA**: El acrónimo raíz constante del repositorio: `PKB`.
2. **CAPA/DOMINIO**: Indica el dominio o subcapa de arquitectura donde reside el objeto (Ej: `KERNEL`, `GOV`, `ARCH`, `MIPSP`, `SHARED`).
3. **COMPONENTE**: Mapeo abreviado de 3 a 8 letras que define el propósito o tipo específico del activo (Ej: `MANIFEST`, `METADATA`, `OBJMODEL`, `VISION`).
4. **SECUENCIAL**: Código numérico correlativo de tres dígitos que inicia en `001`.

---

# Catálogo de Ejemplos Aplicados

Para garantizar consistencia absoluta, se normalizan los siguientes prefijos base de acuerdo a la capa del ecosistema:

| Ruta del Activo | Tipo de Objeto | Ejemplo de ID Estándar |
| :--- | :---: | :--- |
| `docs/kernel/PKB-MANIFEST.md` | MANIFEST | `PKB-KERNEL-MANIFEST-001` |
| `docs/kernel/METADATA-MODEL.md` | Kernel / Metadata | `PKB-KERNEL-METADATA-001` |
| `docs/governance/VISION.md` | Governance / Vision | `PKB-GOV-VISION-001` |
| `docs/architecture/ADR-0001-...` | ADR / Architecture | `PKB-ADR-0001` |

## Reglas de Persistencia e Inmutabilidad
* **No Reutilización**: Si un documento es marcado como `Archived` o `Deprecated`, su identificador queda congelado; jamás podrá asignarse a un nuevo activo.
* **Mayúsculas Estrictas**: Todos los caracteres alfabéticos del identificador deben declararse en mayúsculas fijas.
* **Sincronización YAML**: El identificador definido en el metadato `id` debe corresponder de manera unívoca con los registros de enlaces en las secciones de relaciones del ecosistema.

---

# Relaciones

## Documento superior
- [PKB-MANIFEST.md](PKB-MANIFEST.md)

## Documentos relacionados
- [METADATA-MODEL.md](METADATA-MODEL.md)
- [KNOWLEDGE-OBJECT-MODEL.md](KNOWLEDGE-OBJECT-MODEL.md)
- TRACEABILITY-MODEL.md

---

# Historial de cambios
| Versión | Fecha | Descripción |
|----------|------------|----------------|
| 1.0.0 | 2026-07-09 | Primera versión institucional del Estándar de Identificadores. |