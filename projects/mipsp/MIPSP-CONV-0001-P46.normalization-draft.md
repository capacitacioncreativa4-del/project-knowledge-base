---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
project: MIPSP
type: NORMALIZATION-DRAFT
domain: MIPSP
source: ChatGPT
status: Normalization-Draft
part: 46
source_file: projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P46.md
source_sha256: A8B5066D7851C6EFD55873595B098FA28B5CADE13ADAFBEDEF217A4A763C1DF3
---

# Borrador de normalización P46

## 1. Propósito del SICD-MIPSP

P46 propone el Sistema Institucional de Codificación Documental del MIPSP como infraestructura para identificar, localizar, relacionar y versionar los activos documentales de la colección.

Sus finalidades son unicidad, trazabilidad, interoperabilidad, control de versiones, recuperación, escalabilidad, auditoría y preservación histórica.

## 2. Principios de codificación

Todo identificador debería cumplir:

1. Unicidad: un código corresponde a un solo elemento.
2. Permanencia: no se reutiliza aunque el documento cause baja.
3. Escalabilidad: permite crecimiento sin alterar la estructura.
4. Legibilidad: es interpretable por usuarios capacitados.
5. Modularidad: cada segmento tiene significado.
6. Compatibilidad: puede integrarse con gestión documental y calidad.
7. Independencia: no depende del nombre del documento.
8. Trazabilidad: se relaciona con requisitos, competencias, procedimientos, cursos, sesiones, evaluaciones y evidencias.

## 3. Arquitectura del código

La estructura propuesta se compone de tipo, familia, subfamilia, número, versión y estado. Un ejemplo conceptual combina un tipo de documento, una familia operativa, un número secuencial, una versión y un estado de aprobación.

Los ejemplos incluidos en la fuente son ilustrativos y no deben interpretarse como nuevas asignaciones institucionales.

## 4. Prefijos y familias

El catálogo propuesto agrupa prefijos académicos —curso, programa, carta descriptiva, guía, manual, ETS, presentación y ejercicios—; de evaluación —reactivos, examen, lista, guía, rúbrica, instrumento y portafolio—; de gestión operativa —PNO, instructivo, formato, registro, bitácora, reporte y KPI—; de competencias —competencia, UEC, requisito, MTI e IRF—; y de calidad —auditoría, acciones correctiva y preventiva, mejora y no conformidad—.

Las familias documentales propuestas incluyen operaciones, jurídico, administración, supervisión, comunicación, gestión documental, riesgo, evaluación, calidad, instructores y tecnología.

## 5. Numeración y versionado

Cada familia comenzaría en 001 y los números no se reutilizarían después de una baja. El versionado propuesto distingue borrador, revisión técnica, revisión jurídica, piloto, aprobado, vigente, obsoleto e histórico.

El estado de un documento debería distinguirse de su versión y registrarse en control documental.

## 6. Relaciones documentales

El SICD-MIPSP definiría relaciones entre programa, carta descriptiva, guía, manual, ETS, presentación, ejercicios, reactivos, examen, rúbrica, lista, guía de observación, PNO, formatos, bitácoras, reportes y matriz de trazabilidad.

El objetivo es que los elementos de un curso puedan localizarse y mantenerse vinculados sin ambigüedad.

## 7. Desarrollo posterior y control de configuración

Con el SICD definido, la siguiente propuesta es desarrollar la Guía del Instructor como manual operativo para impartir el curso. Incluiría control documental, perfil del instructor, preparación, guion por módulo y sesión, facilitación, preguntas, indicadores, contingencias, retroalimentación, cierre y anexos.

P46 propone además el Control de Configuración Documental del MIPSP para registrar cada modificación, su motivo, documentos afectados, responsable, entrada en vigor e impacto en cursos, procedimientos, evaluaciones y materiales.

## 8. Límites de esta normalización

- No se implementa el SICD-MIPSP.
- No se asignan códigos, números, versiones o estados nuevos.
- No se materializan relaciones documentales ni el CCD-MIPSP.
- No se crea la Guía del Instructor.
- No se validan compatibilidad, gobernanza o reglas de aprobación.
