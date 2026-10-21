---
id: MIPSP-CONV-0001
title: Candidata de reconciliación P01
status: Candidate
type: Source-Reconciliation-Candidate
file_reference: MIPSP-CONV-0001-P01.md
source_path: projects/mipsp/sources/conversations/original/MIPSP-CONV-0001-P01.md
source_sha256: 93E85A9A5F51C391183A0C77F22B88783C8086EABFC7CAA51988F92543D7A3B6
approval_required: true
---

# Candidata de reconciliación — MIPSP-CONV-0001-P01

Esta candidata identifica la copia histórica completa como base de procedencia para una nueva normalización de P01. El contenido fuente se conserva en:

`projects/mipsp/sources/conversations/original/MIPSP-CONV-0001-P01.md`

## Evidencia

- SHA-256 de la copia histórica completa: `93E85A9A5F51C391183A0C77F22B88783C8086EABFC7CAA51988F92543D7A3B6`.
- Fuente canónica actual: `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P01.md`.
- SHA-256 de la fuente canónica actual: `AE742B952E152137FEFC55E3A7490D63DB9C78AC387A384BCE16C1CEE0942388`.
- Normalizado actual defectuoso: `projects/mipsp/sources/conversations/normalized/MIPSP-CONV-0001-P01.md`.
- Antecedente histórico: commit `2413409`.

## Comparación

La copia histórica y la fuente canónica actual conservan el mismo contenido sustantivo de la conversación. Las diferencias observadas están limitadas a metadatos y al texto introductorio:

- `conversation_id` frente a `id`.
- Inclusión de `type`, `domain` y `part` en la fuente canónica actual.
- `(Contenido íntegro del chat)` frente a `(Contenido del chat correspondiente a esta parte)`.

La copia histórica se elige como base porque contiene la formulación completa y coincide con el artefacto conservado en el commit `2413409`.

## Estado y límites

Esta candidata no sustituye el normalizado actual, no modifica la fuente canónica, no actualiza índices y no crea Knowledge Objects. La normalización completa debe derivarse de la copia histórica y recibir aprobación humana explícita antes de promoverse a `status: Normalized`.
