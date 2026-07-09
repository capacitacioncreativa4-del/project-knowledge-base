---
id: PKB-KERNEL-IDSCHEME-001
title: Identifier Scheme
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: KERNEL
domain: PKB
parent: PKB-KERNEL-MANIFEST-001
tags:
  - kernel
  - identity
  - scheme
---

# Esquema de Identificadores Únicos y Persistentes

## Propósito
Definir de forma matemática y sintáctica la estructura formal de las claves de identidad de todos los Objetos de Conocimiento del PKB. Esto garantiza que cada entidad posea un identificador persistente, unívoco e independiente de su ubicación física en el disco[cite: 1].

---

# Especificación Sintáctica (Estructura de Bloques)

Todos los identificadores oficiales del ecosistema se construirán de manera estricta bajo el siguiente patrón alfanumérico en mayúsculas separado por guiones medios:

$$\text{SISTEMA}-\text{DOMINIO}-\text{TIPO}-\text{SECUENCIAL}$$

### Definición de Componentes:
- **SISTEMA**: Código raíz invariable que identifica al ecosistema global: `PKB`[cite: 1].
- **DOMINIO**: Clave del dominio de conocimiento o capa arquitectónica base (`KERNEL`, `GOV`, `ARCH`, `MIPSP`, `SHARED`)[cite: 1].
- **TIPO**: Acrónimo normalizado de 3 a 4 letras correspondiente al tipo de Objeto de Conocimiento catalogado (Ej: `KOM`, `ADR`, `STD`, `REQ`, `EPIC`)[cite: 1].
- **SECUENCIAL**: Código numérico correlativo fijo de tres dígitos que inicia en `001`.

---

# Reglas de Persistencia e Inmutabilidad

Para asegurar que los agentes de IA y los grafos relacionales no sufran roturas de enlaces, se imponen las siguientes leyes sintácticas[cite: 1]:
1. **Inmutabilidad Absoluta**: Una vez asignado un identificador a un objeto, este jamás podrá ser modificado, editado o reasignado a otra entidad, incluso si el objeto pasa a estado `Archived` o `Deprecated`[cite: 1].
2. **Independencia de Ruta**: El identificador pertenece al objeto conceptual, no al archivo físico[cite: 1]. Si un archivo se mueve de carpeta, su `id` en el YAML permanece intacto.
3. **Mayúsculas Estrictas**: No se admiten caracteres en minúscula en la composición de la clave de identidad.

---

# Relaciones

## Documento superior
- PKB-KERNEL-MANIFEST.md[cite: 1]

## Documentos relacionados
- METADATA-MODEL.md[cite: 1]
- KNOWLEDGE-OBJECT-MODEL.md[cite: 1]
- TRACEABILITY-MODEL.md[cite: 1]

## Documentos derivados
- IDENTIFIER-REGISTRY.md[cite: 1]

---

# Historial de cambios
| Versión | Fecha | Descripción |
|----------|------------|----------------|
| 1.0.0 | 2026-07-09 | Primera versión del estándar sintáctico de identificadores[cite: 1]. |