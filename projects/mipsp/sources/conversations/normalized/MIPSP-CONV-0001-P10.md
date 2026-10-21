---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalized
type: Source
file_reference: MIPSP-CONV-0001-P10.md
source_part: 10
source_sha256: 67734C757F687551DDEC3DB09516C7A7D7B36F258920FC003DBDC179219549BE
---

# Fuente Normalizada — MIPSP-CONV-0001-P10

## Referencia y procedencia

Esta fuente normalizada deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P10.md`.
La fuente original y el borrador aprobado permanecen intactos.

## 1. Cambio de fase del proyecto

### TRANSICION_ARQUITECTURA_A_ANALISIS

- Tipo: `DECISION_DE_ENFOQUE_PROPUESTA`.
- Estado: `Validated-As-Proposal`.
- La fuente propone considerar concluida la fase de arquitectura y pasar al análisis documental exhaustivo.
- La estimación conversacional del 70 % de valor técnico se conserva como percepción, no como métrica validada.

## 2. Sistema de Codificación del SIGCO-ESP

### SISTEMA_CODIFICACION_SIGCO_ESP

- Tipo: `MODELO_DE_IDENTIFICACION_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Objetivo: identificar uniformemente fuentes jurídicas, procesos, competencias, cursos, unidades, sesiones, prácticas, evaluaciones, evidencias y documentos durante el ciclo de vida formativo.

### CODIFICACION_PROPUESTA

Se proponen códigos para fuentes jurídicas (`LFSP`, `RLFSP`, `LMSPM`, `RLMSPM`, `EC0060`, `LFT`, `STPS`, `CONOCER`), procesos (`PROC`), competencias (`COMP-T`, `COMP-O`, `COMP-E`, `COMP-L`), cursos (`CUR`), unidades (`UN`), sesiones (`SES`), prácticas (`PRA`), evaluaciones (`EVA-C`, `EVA-D`, `EVA-P`), evidencias (`EV-C`, `EV-D`, `EV-P`) y documentos (`MAN`, `GUI`, `LC`, `RUB`, `EXA`).

Los ejemplos de códigos permanecen como nomenclatura de diseño y no como identificadores oficiales o IDs persistentes del PKB. La aplicabilidad de las fuentes jurídicas requiere validación documental.

## 3. Repositorio Maestro de Competencias

### RMC

- Tipo: `REPOSITORIO_CONCEPTUAL_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Propósito: almacenar una ficha técnica completa por competencia.
- Campos propuestos: código, proceso, nombre, nivel, criticidad, fuentes normativas, resultados de aprendizaje, conocimientos, habilidades, destrezas, actitudes, valores, errores críticos, riesgos, evidencias, instrumentos, cursos, horas, recertificación y observaciones.

El ejemplo de control de accesos se conserva como estructura demostrativa y no como competencia institucional.

## 4. Diccionario Institucional de Competencias

### DIC

- Tipo: `DICCIONARIO_CONCEPTUAL_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Propósito: proporcionar una definición normalizada por competencia, con alcance, límites, ejemplos, relaciones y fuentes normativas.
- Beneficios propuestos: evitar interpretaciones divergentes, duplicidades, evaluaciones inconsistentes y pérdida de trazabilidad ante cambios legales.

La definición única y oficial requiere una fase específica de diseño, validación y aprobación.

## 5. Próximo producto técnico propuesto

### MATRIZ_MAESTRA_OBLIGACIONES_FORMATIVAS

- Tipo: `PRODUCTO_DE_EXTRACCION_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Propósito: inventariar exhaustivamente obligaciones formativas a partir de legislación federal, legislación de Morelos, reglamentos y EC0060.
- Campos conceptuales: fundamento normativo, obligación de formación, competencia derivada y ubicación en SIGCO-ESP.

La fuente propone que sea el siguiente entregable; esta normalización no realiza el análisis jurídico ni crea la matriz.

## 6. Elementos excluidos

- No se valida jurídicamente la vigencia, interpretación o aplicabilidad de las fuentes codificadas.
- No se adopta el sistema de codificación como estándar oficial.
- No se registran códigos LFSP, PROC, COMP, CUR, UN, SES, PRA, EVA, EV o documentales como IDs persistentes.
- No se crea el RMC ni el DIC como repositorio o diccionario institucional.
- No se crean fichas de competencias, cursos, documentos, horas o reglas de recertificación.
- No se realiza la Matriz Maestra de Obligaciones Formativas ni extracción artículo por artículo.
- No se crean requisitos, ADR, estándares, documentos editoriales ni Knowledge Objects.

## 7. Estado de normalización

| Elemento | Estado |
|---|---|
| Fuente P10 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 10 |
| Normalización | Normalized |
| Revisión humana P10 | Aprobada |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |

La aprobación no convierte las propuestas en estándares, requisitos, decisiones u objetos institucionales.
