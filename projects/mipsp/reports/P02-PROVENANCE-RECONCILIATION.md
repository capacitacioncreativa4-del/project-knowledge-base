---
id: MIPSP-P02-RECONCILIATION-001
title: Reconciliación de procedencia P02
version: 1.0.0
status: Approved
owner: MIPSP
created: 2026-10-20
updated: 2026-10-20
type: Reconciliation Record
domain: MIPSP
tags:
  - P02
  - provenance
  - reconciliation
---

# Reconciliación de procedencia P02

## Hallazgo

La fuente canónica actual y la copia histórica utilizada para aprobar P02 tienen cuerpos idénticos. Sus hashes físicos difieren porque el front matter no es igual.

| Representación | SHA-256 físico | SHA-256 del cuerpo |
| --- | --- | --- |
| Fuente canónica actual | `B3E29DE774416AC66A36CA49DE05DA2A0A1CD8ADA099B3FABB484624F2A28EA1` | `1402D32FB80F60A1381E54C242B9392D0852830A648390A3F68BF48D58A73892` |
| Copia histórica aprobada | `88EB5598D432EF0D9528AAFC71A58DDA8BD6126059EF84347DA216839307B26D` | `1402D32FB80F60A1381E54C242B9392D0852830A648390A3F68BF48D58A73892` |

## Propuesta

Se reconoce la fuente canónica actual como identidad vigente de P02. El `source_sha256` del borrador, el normalizado y el reporte de validación fue actualizado a `B3E29DE774416AC66A36CA49DE05DA2A0A1CD8ADA099B3FABB484624F2A28EA1`. El contenido normalizado y los cinco Knowledge Objects no requieren cambios de contenido.

## Estado

La reconciliación queda aprobada. La copia histórica se conserva como evidencia y no se presenta como la identidad vigente de la fuente.
