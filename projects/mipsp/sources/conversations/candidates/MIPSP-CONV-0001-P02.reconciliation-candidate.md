---
id: MIPSP-CONV-0001
title: Candidata de reconciliación P02
status: Candidate
type: Source-Reconciliation-Candidate
file_reference: MIPSP-CONV-0001-P02.md
source_path: projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P02.md
source_sha256: B3E29DE774416AC66A36CA49DE05DA2A0A1CD8ADA099B3FABB484624F2A28EA1
body_sha256: 1402D32FB80F60A1381E54C242B9392D0852830A648390A3F68BF48D58A73892
approval_required: true
---

# Candidata de reconciliación — MIPSP-CONV-0001-P02

Esta candidata propone reconciliar P02 con la fuente canónica actual de ingestión. El cuerpo de la fuente canónica y el cuerpo de la copia histórica aprobada son idénticos.

## Evidencia

- Fuente canónica actual: `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P02.md`.
- SHA-256 físico actual: `B3E29DE774416AC66A36CA49DE05DA2A0A1CD8ADA099B3FABB484624F2A28EA1`.
- SHA-256 del cuerpo actual: `1402D32FB80F60A1381E54C242B9392D0852830A648390A3F68BF48D58A73892`.
- Fuente histórica usada en la aprobación anterior: `projects/mipsp/sources/conversations/original/MIPSP-CONV-0001-P02.md`.
- SHA-256 físico histórico: `88EB5598D432EF0D9528AAFC71A58DDA8BD6126059EF84347DA216839307B26D`.
- SHA-256 del cuerpo histórico: `1402D32FB80F60A1381E54C242B9392D0852830A648390A3F68BF48D58A73892`.
- Normalizado aprobado actual: `projects/mipsp/sources/conversations/normalized/MIPSP-CONV-0001-P02.md`.
- Borrador aprobado actual: `projects/mipsp/MIPSP-CONV-0001-P02.normalization-draft.md`.

## Diferencia identificada

La divergencia de hash proviene del front matter: la fuente canónica usa `id`, `type` y `domain`, mientras que la copia histórica usa `conversation_id`. No se identificaron diferencias en el cuerpo de la conversación.

## Estado y límites

Esta candidata no sustituye el normalizado aprobado, no actualiza el reporte P02, no modifica los Knowledge Objects y no cambia el índice del paquete. Requiere aprobación humana antes de actualizar la procedencia declarada del normalizado, el borrador y el reporte.
