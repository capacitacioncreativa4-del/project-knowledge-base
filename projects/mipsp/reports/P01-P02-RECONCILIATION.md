---
id: MIPSP-RECON-001
title: Reconciliación documental P01 y P02
version: 1.1.0
status: Open
owner: MIPSP
created: 2026-10-19
updated: 2026-10-20
type: Reconciliation Record
domain: MIPSP
tags:
  - P01
  - P02
  - reconciliation
  - provenance
---

# Reconciliación documental P01 y P02

## Estado actualizado

### P01 — Resuelto

- La copia histórica completa se conserva en `projects/mipsp/sources/conversations/original/MIPSP-CONV-0001-P01.md`.
- Hash de procedencia: `93E85A9A5F51C391183A0C77F22B88783C8086EABFC7CAA51988F92543D7A3B6`.
- La candidata de reconciliación fue aprobada y conservada en `projects/mipsp/sources/conversations/candidates/MIPSP-CONV-0001-P01.reconciliation-candidate.md`.
- El normalizado aprobado está en `projects/mipsp/sources/conversations/normalized/MIPSP-CONV-0001-P01.md`.
- El reporte de validación está en `projects/mipsp/reports/P01-NORMALIZATION-VALIDATION.md`.
- La fuente canónica actual se conservó sin modificar.
- No se crearon Knowledge Objects ni IDs institucionales nuevos.

### P02 — Abierto

- La fuente canónica actual es `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P02.md`.
- Hash actual de la fuente canónica: `B3E29DE774416AC66A36CA49DE05DA2A0A1CD8ADA099B3FABB484624F2A28EA1`.
- El borrador y el normalizado aprobados declaran el hash histórico `88EB5598D432EF0D9528AAFC71A58DDA8BD6126059EF84347DA216839307B26D`.
- La fuente histórica usada para el cierre P02 se conserva en `projects/mipsp/sources/conversations/original/MIPSP-CONV-0001-P02.md`.
- Sigue pendiente decidir si se conserva esa aprobación histórica o se genera una nueva aprobación para la fuente canónica actual.

## Criterio de cierre de P02

P02 permanecerá abierto hasta que la identidad de la fuente aprobada coincida con la fuente canónica actual o exista una nueva aprobación humana que resuelva expresamente la divergencia.

## Integridad

- No se sobrescribió la fuente canónica de P01 ni la de P02.
- Las diferencias de hash permanecen visibles.
- El índice y los Knowledge Objects no se modificaron como parte de la resolución de P01.
