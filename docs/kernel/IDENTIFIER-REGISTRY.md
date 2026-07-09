---
id: PKB-KERNEL-IDREG-001
title: Identifier Registry
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
  - registry
---

# Registro y Mecanismo de Asignación de Identificadores

## Propósito
Establecer el procedimiento operativo y las reglas de gobernanza para la administración, reserva y auditoría de los identificadores únicos dentro del PKB[cite: 1]. Este mecanismo asegura el control de asignación, previniendo colisiones antes de la integración de nuevos Objetos de Conocimiento[cite: 1].

---

# Proceso Operativo de Asignación

Para dar de alta o reservar un identificador unívoco de forma manual (previo a la automatización del ecosistema), todo autor o sistema deberá seguir el flujo normativo:

1. **Consulta del Estado de Bloques**: Examinar el índice maestro del dominio correspondiente para identificar el último secuencial numérico utilizado (Ej: si el último es `002`, el nuevo será `003`)[cite: 1].
2. **Declaración en YAML**: Registrar la clave construida bajo las reglas de `IDENTIFIER-SCHEME.md` dentro del bloque de metadatos del archivo local[cite: 1].
3. **Validación del Pull Request**: Durante la fase de `Review`, los revisores o scripts automáticos validarán mediante una búsqueda global (`grep` o similar) que el `id` propuesto no colisione con ningún activo preexistente[cite: 1].

---

# Reglas de Control de Registro y Conflictos

* **Resolución de Colisiones**: En caso de que dos Pull Requests concurrentes propongan el mismo identificador numérico secuencial, el PR que se fusione primero en `main` conservará la clave; el segundo deberá reindexarse de forma obligatoria[cite: 1].
* **Reservas Estratégicas**: Los secuenciales del `001` al `010` de cada tipo de Objeto de Conocimiento quedan reservados exclusivamente para los marcos de trabajo estructurales y manifiestos del núcleo (Kernel)[cite: 1].

---

# Relaciones

## Documento superior
- PKB-KERNEL-MANIFEST.md[cite: 1]

## Documentos relacionados
- [IDENTIFIER-SCHEME.md](IDENTIFIER-SCHEME.md)[cite: 1]
- [KNOWLEDGE-OBJECT-MODEL.md](KNOWLEDGE-OBJECT-MODEL.md)[cite: 1]

---

# Historial de cambios
| Versión | Fecha | Descripción |
|----------|------------|----------------|
| 1.0.0 | 2026-07-09 | Primera versión del mecanismo de gestión y asignación de registros[cite: 1]. |