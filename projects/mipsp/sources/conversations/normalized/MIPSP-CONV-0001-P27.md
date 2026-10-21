---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalized
type: Source
file_reference: MIPSP-CONV-0001-P27.md
source_part: 27
source_sha256: 7C676010DBFE097245607D533B9886BDF8844430F2B0ABBAB13AF1F581A90371
---

# Fuente Normalizada — MIPSP-CONV-0001-P27

## Referencia y procedencia

Esta fuente normalizada deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P27.md`.
La fuente original y el borrador aprobado permanecen intactos.

## 1. Sistema de Demostración de Competencias

La conversación propone dejar de preguntar solamente qué debe aprender un guardia y preguntar qué debe demostrar para acreditar objetiva y documentalmente el cumplimiento de la legislación.

El eje propuesto es un **Sistema de Demostración de Competencias**, orientado a vincular requisitos normativos, competencias, cursos, evaluaciones, evidencias e indicadores.

La propuesta se registra como enfoque metodológico; P27 no contiene resultados jurídicos validados.

## 2. Clasificación de disposiciones del IARF

Se propone clasificar cada disposición de las cinco fuentes:

### Nivel A. Requisito Formativo Directo (RFD)

Generaría capacitación obligatoria para el personal operativo. Los ejemplos incluyen actuación, equipo, control de accesos, rondines, radiocomunicación, bitácoras y atención al usuario.

### Nivel B. Requisito Formativo Indirecto (RFI)

No obligaría directamente al guardia, pero condicionaría su actuación. Los ejemplos incluyen obligaciones del prestador, supervisión, manuales y registros. Podría producir competencias para supervisores, instructores o responsables operativos.

### Nivel C. Requisito Administrativo (RA)

Generaría procedimientos administrativos, pero no contenidos curriculares para personal operativo. Los ejemplos incluyen autorizaciones, renovaciones y avisos, aunque podrían incorporarse en cursos directivos o administrativos.

### Nivel D. Requisito Estratégico (RE)

No produciría cursos específicos, pero determinaría políticas institucionales. Los ejemplos incluyen principios, coordinación y obligaciones generales del prestador, que alimentarían el sistema de gestión del Tomo VI.

La clasificación es propuesta y deberá aplicarse con fundamento en cada disposición. Los acrónimos RFD, RFI, RA y RE son categorías de la conversación, no IDs institucionales.

## 3. Matriz de Extracción de Competencias

La **Matriz de Extracción de Competencias (MEC)** procesaría cada artículo de las cinco fuentes mediante campos de código FARF, fuente, artículo, tipo de requisito, tema, competencias, procesos CMPO, riesgos, curso, evidencia, instrumento e indicador SIEC.

El código `FARF-0001` y los códigos de curso, instrumento e indicador son ejemplos de estructura. No se crean registros institucionales en P27.

## 4. Matriz de Cobertura Normativa

La **Matriz de Cobertura Normativa (MCN)** demostraría que los requisitos formativos identificados han sido atendidos mediante la cadena:

`Norma → Artículo → Requisito Formativo → Competencia → Proceso Operativo → Programa de Capacitación → Unidad Didáctica → Actividad de Aprendizaje → Instrumento de Evaluación → Evidencia → Indicador`.

La MCN se propone como base para auditorías, verificaciones y mejora continua. P27 no crea ni llena la matriz.

## 5. Catálogo Maestro de Evidencias

El **Catálogo Maestro de Evidencias (CME)** clasificaría:

- **E1. Conocimiento:** exámenes, casos y análisis normativo.
- **E2. Desempeño:** observación directa, simulaciones y prácticas supervisadas.
- **E3. Documentales:** bitácoras, informes, registros y reportes.
- **E4. Resultado:** indicadores, auditorías, retroalimentación de clientes y disminución de incidentes atribuibles a errores de actuación.

La categoría E4 se presenta como aportación metodológica para valorar el impacto operativo, además del aprendizaje inmediato. El CME no se crea ni se valida en P27.

## 6. Índice de Cobertura Curricular

Se propone un **Índice de Cobertura Curricular (ICC-N)** con la fórmula:

`ICC-N = Requisitos Formativos Cubiertos / Requisitos Formativos Identificados × 100`

Los requisitos identificados serían las obligaciones de capacitación extraídas de las cinco fuentes; los cubiertos contarían con competencia, curso, evaluación y evidencia.

La meta propuesta sería 100 % de cobertura para RFD, cobertura documentada para RFI aplicables y justificación formal para RA y RE que no generen capacitación operativa.

La fuente usa el acrónimo RFI tanto para **Requisito Formativo Indirecto** como en la expresión **Requisitos Formativos Identificados**. Esta ambigüedad deberá resolverse antes de adoptar la fórmula institucionalmente. P27 no calcula el ICC-N.

## 7. Siguiente fase propuesta

Se propone iniciar el desarrollo exhaustivo del IARF mediante análisis secuencial de las cinco fuentes, disposición por disposición, elaborando una FARF para cada requisito identificado.

El trabajo alimentaría simultáneamente la MCN, el DMC, el CMPO, el Catálogo Maestro de Programas de Capacitación y el Sistema Integral de Evaluación.

P27 no contiene el análisis jurídico ni los productos derivados.

## 8. Elementos excluidos

- No se ejecuta la clasificación de disposiciones en RFD, RFI, RA y RE.
- No se crea ni llena el IARF, la FARF, la MEC o la MCN.
- No se crea el CME ni se clasifican evidencias reales.
- No se calcula ni se adopta el ICC-N.
- No se resuelve institucionalmente la ambigüedad del acrónimo RFI.
- No se crean competencias, cursos, procesos, evaluaciones, indicadores o evidencias.
- No se convierten los acrónimos o códigos ilustrativos en IDs institucionales.
- No se crean requisitos, ADR, estándares, Knowledge Objects ni relaciones persistentes.

## 9. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P27 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Rama observada | `feat/mipsp-p06-normalize-2026-10`; discrepante de la rama esperada anterior |
| Conversación | MIPSP-CONV-0001 |
| Parte | 27 |
| Normalización | Normalizada |
| Revisión humana P27 | Aprobada por el usuario |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | Realizada |

## Cierre de normalización

La revisión humana confirmó el Sistema de Demostración de Competencias, los cuatro niveles de requisitos, la MEC, la MCN, las categorías del CME, el ICC-N, la ambigüedad de RFI y la siguiente fase de desarrollo del IARF.

# FIN DE LA FUENTE NORMALIZADA P27
