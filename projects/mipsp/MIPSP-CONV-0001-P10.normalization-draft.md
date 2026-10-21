---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalization-Draft
type: Source
file_reference: MIPSP-CONV-0001-P10.md
source_part: 10
source_sha256: 67734C757F687551DDEC3DB09516C7A7D7B36F258920FC003DBDC179219549BE
---

# Borrador de Fuente Normalizada — MIPSP-CONV-0001-P10

## Referencia y procedencia

Este borrador deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P10.md`.

La fuente original permanece intacta. Este documento no constituye un sistema de codificación aprobado, análisis jurídico, repositorio institucional ni autorización para crear IDs, Knowledge Objects, requisitos, ADR, estándares o documentos editoriales.

## 1. Cambio de fase del proyecto

### TRANSICION_ARQUITECTURA_A_ANALISIS

- Tipo: `DECISION_DE_ENFOQUE_PROPUESTA`.
- Estado: `Candidate`.
- La fuente propone considerar concluida la fase de arquitectura y pasar al análisis documental exhaustivo.
- Justificación: el valor técnico se desplaza de la redacción de capítulos a la construcción de productos verificables y trazables.

La estimación conversacional del 70 % de valor técnico se conserva como percepción, no como métrica validada.

## 2. Sistema de Codificación del SIGCO-ESP

### SISTEMA_CODIFICACION_SIGCO_ESP

- Tipo: `MODELO_DE_IDENTIFICACION_PROPUESTO`.
- Estado: `Candidate`.
- Objetivo: identificar uniformemente fuentes jurídicas, procesos, competencias, cursos, unidades, sesiones, prácticas, evaluaciones, evidencias y documentos durante el ciclo de vida formativo.

### CODIFICACION_FUENTES_JURIDICAS

La fuente propone códigos para Ley Federal de Seguridad Privada (LFSP), su Reglamento (RLFSP), Ley de Seguridad Privada del Estado de Morelos (LMSPM), reglamento estatal (RLMSPM), EC0060, Ley Federal del Trabajo (LFT), disposiciones STPS y CONOCER. Ejemplos conversacionales: `LFSP-45`, `RLFSP-18`, `LMSPM-46` y `EC0060-E2-CR3`.

Los códigos y la aplicabilidad de las fuentes requieren validación documental. No se registran aquí como identificadores oficiales.

### CODIFICACION_PROCESOS

Se propone codificar procesos con el prefijo `PROC`, incluyendo control de accesos, control vehicular, rondines, protección de instalaciones, radiocomunicación, primeros auxilios, incendios, emergencias, informes y atención al usuario.

Los ejemplos `PROC-001` a `PROC-010` son códigos ilustrativos y no se crean como IDs institucionales.

### CODIFICACION_COMPETENCIAS

Se proponen códigos independientes de los cursos, con familias para competencias transversales (`COMP-T`), operativas (`COMP-O`), especializadas (`COMP-E`) y de liderazgo (`COMP-L`). Los ejemplos son nomenclatura de diseño, no registros aprobados.

### CODIFICACION_CURSOS_Y_UNIDADES

Se propone el prefijo `CUR` para cursos y `UN` para unidades, con ejemplos de inducción, marco jurídico, control de accesos, rondines, radiocomunicación, primeros auxilios y unidades de control peatonal, vehicular y documental.

### CODIFICACION_SESIONES_Y_PRACTICAS

Se proponen `SES` para sesiones y `PRA` para prácticas, incluyendo simulación, caso práctico y role playing.

### CODIFICACION_EVALUACIONES_Y_EVIDENCIAS

Se proponen `EVA-C`, `EVA-D` y `EVA-P` para evaluaciones de conocimiento, desempeño y producto, y `EV-C`, `EV-D` y `EV-P` para sus evidencias correspondientes.

### CODIFICACION_DOCUMENTAL

Se propone codificar documentos institucionales como manual del instructor, manual del participante, guía de observación, lista de cotejo, rúbrica y examen, con ejemplos `MAN-INS-001`, `MAN-PAR-001`, `GUI-OBS-001`, `LC-001`, `RUB-001` y `EXA-001`.

Todos los códigos anteriores permanecen en estado de propuesta y no deben confundirse con IDs persistentes del PKB.

## 3. Repositorio Maestro de Competencias

### RMC

- Tipo: `REPOSITORIO_CONCEPTUAL_PROPUESTO`.
- Estado: `Candidate`.
- Propósito: almacenar una ficha técnica completa por competencia, en lugar de una tabla simple.

### FICHA_DE_COMPETENCIA

Campos propuestos: código, proceso, nombre, nivel, criticidad, fuentes normativas, resultados de aprendizaje, conocimientos, habilidades, destrezas, actitudes, valores, errores críticos, riesgos asociados, evidencias, instrumentos, cursos, horas, recertificación y observaciones.

El ejemplo de control de ingreso y salida de personas se conserva como demostración de estructura. No se crea como competencia institucional.

## 4. Diccionario Institucional de Competencias

### DIC

- Tipo: `DICCIONARIO_CONCEPTUAL_PROPUESTO`.
- Estado: `Candidate`.
- Propósito: proporcionar una definición normalizada para cada competencia, con alcance, límites, ejemplos, relaciones y fuentes normativas.
- Beneficios propuestos: evitar interpretaciones divergentes, duplicidades, evaluaciones inconsistentes y pérdida de trazabilidad ante cambios legales.

La definición única y oficial de competencias requiere una fase específica de diseño, validación y aprobación.

## 5. Próximo producto técnico propuesto

### MATRIZ_MAESTRA_OBLIGACIONES_FORMATIVAS

- Tipo: `PRODUCTO_DE_EXTRACCION_PROPUESTO`.
- Estado: `Candidate`.
- Propósito: inventariar exhaustivamente obligaciones formativas a partir de legislación federal, legislación de Morelos, reglamentos y EC0060.
- Campos conceptuales: fundamento normativo, obligación de formación, competencia derivada y ubicación dentro del SIGCO-ESP.

La fuente propone que esta matriz sea el siguiente entregable y piedra angular del sistema curricular. Este borrador no realiza el análisis jurídico ni crea la matriz.

## 6. Elementos excluidos

- No se valida jurídicamente la vigencia, interpretación o aplicabilidad de las fuentes codificadas.
- No se adopta el sistema de codificación como estándar oficial.
- No se registran códigos LFSP, PROC, COMP, CUR, UN, SES, PRA, EVA, EV o documentales como IDs persistentes.
- No se crea el RMC ni el DIC como repositorio o diccionario institucional.
- No se crean fichas de competencias, cursos, documentos, horas o reglas de recertificación.
- No se realiza la Matriz Maestra de Obligaciones Formativas ni extracción artículo por artículo.
- No se crean requisitos, ADR, estándares, documentos editoriales ni Knowledge Objects.
- No se interpreta el siguiente producto propuesto como trabajo ya ejecutado.

## 7. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P10 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 10 |
| Normalización | Borrador |
| Revisión humana P10 | Pendiente |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | No realizada |

## Criterio para cerrar el borrador

La revisión humana deberá confirmar la transición de fase, el sistema de codificación, la separación entre códigos ilustrativos e IDs persistentes, la estructura del RMC y DIC, el carácter futuro de la matriz de obligaciones y la ausencia de promoción prematura.

# FIN DEL BORRADOR DE NORMALIZACIÓN P10
