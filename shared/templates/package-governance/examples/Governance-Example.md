---
id: PKB-GOV-0011
title: "GOV-0011: Política de Ingeniería del Conocimiento por Incrementos Cohesivos"
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: GOV
domain: PKB
tags:
  - governance
  - methodology
---

# GOV-0011: Política de Ingeniería del Conocimiento por Incrementos Cohesivos

## Propósito
Transicionar la metodología de construcción del PKB desde un enfoque de redacción documental aislada hacia un marco de ingeniería de producto por módulos funcionales integrales.

---

# Objetivos
- Eliminar la proliferación de archivos de estándares o plantillas huérfanas en el repositorio.
- Garantizar que cada entrega metodológica sea utilizable y auditable de manera inmediata en entornos reales.

---

# Alcance
Esta política rige de forma obligatoria para todos los Sprints de desarrollo aplicados al núcleo del conocimiento, estándares técnicos y despliegues de paquetes compartidos dentro del PKB.

---

# Estructura del Módulo Cohesivo

A partir de la emisión de esta directiva, todo incremento o épica del repositorio deberá empaquetarse y entregarse conteniendo de forma mandatoria la siguiente suite de activos:
1. **Un (1) Estándar Técnico**: El marco regulatorio y matemático que define el proceso.
2. **Plantillas Reutilizables**: Los esqueletos limpios listos para su clonación.
3. **Ejemplos Reales**: Casos de uso de ingeniería completamente desarrollados para guiar al usuario.
4. **Un (1) Checklist de Validación**: Matriz de criterios de aceptación editorial y técnica.
5. **Un (1) README del Paquete**: Archivo de indexación, uso y dependencias cruzadas.

---

# Relaciones

## Documento superior
- PKB-MANIFEST-001

## Relacionados
- [DOCUMENT-TEMPLATE-STANDARD.md](../../../../docs/standards/DOCUMENT-TEMPLATE-STANDARD.md)
- [README.md](../README.md)

---

# Historial
| Versión | Fecha | Descripción |
|---------|-------|-------------|
| 1.0.0   | 2026-07-09 | Adopción del enfoque de producto modular por incrementos. |