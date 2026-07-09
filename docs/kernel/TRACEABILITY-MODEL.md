---
id: PKB-STD-0002
title: Traceability Model
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: STD
domain: PKB
parent: PKB-STD-0001
tags:
  - traceability
  - relationships
  - graph
---

# Modelo Institucional de Trazabilidad

## Propósito
Definir las relaciones oficiales entre los Objetos de Conocimiento del Project Knowledge Base (PKB). La trazabilidad permite conocer cómo un objeto se relaciona con otros a lo largo de su ciclo de vida, formando una red de conocimiento navegable.

---

# Objetivos y Principios del Modelo

### Objetivos Fundamentales:
- Garantizar la consistencia integral entre objetos.
- Facilitar la navegación documental fluida.
- Permitir análisis de impacto precisos antes de realizar cambios.
- Soportar automatización avanzada y habilitar grafos de conocimiento.

### Principios Rectores:
1. **Relaciones Explícitas**: Toda relación deberá declararse de forma explícita; las dependencias implícitas no son válidas.
2. **Relaciones Dirigidas**: Cada relación posee un origen y un destino ($\text{Origen} \rightarrow \text{Relación} \rightarrow \text{Destino}$).
3. **Relaciones Tipificadas**: No se permiten relaciones libres; toda relación debe pertenecer al catálogo institucional.

---

# Catálogo Oficial y Matriz de Relaciones

El ecosistema reconoce los siguientes tipos de enlace controlados:
* **Parent Of / Child Of**: Relaciones jerárquicas verticales e inversas.
* **Depends On**: El objeto requiere obligatoriamente de otro para existir o completarse.
* **Related To**: Conexión temática o de contexto sin implicar dependencia directa.
* **Implements**: Representa la materialización de un requisito o directiva.
* **References / Derived From**: Consultas documentales o derivaciones directas[cite: 2].
* **Supersedes / Replaces**: Sustituciones oficiales o reemplazos operativos de activos[cite: 2].
* **Validates / Mitigates / Produces / Uses**: Enlaces operacionales de ingeniería[cite: 2].

### Matriz de Relaciones Permitidas
| Origen | Relación | Destino |
|:---|:---:|:---|
| EPIC | Parent Of | REQ[cite: 2] |
| REQ | Implemented By | DES[cite: 2] |
| DES | Produces | PROC[cite: 2] |
| PROC | Produces | REG[cite: 2] |
| ADR | References | STD[cite: 2] |
| STD | Governs | TMP[cite: 2] |
| TMP | Produces | DOC[cite: 2] |
| RSK | Mitigated By | PROC[cite: 2] |

```text
Evolución Lógica:
EPIC ──[Parent Of]──> REQ ──[Implemented By]──> DES ──[Produces]──> PROC ──[Produces]──> REG