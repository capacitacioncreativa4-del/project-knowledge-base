---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalization-Draft
type: Source
file_reference: MIPSP-CONV-0001-P07.md
source_part: 7
source_sha256: FB163096FFF67F50873E1BEB4670BF690E71E63FCAF543FEF2238AD0C84C2759
---

# Borrador de Fuente Normalizada — MIPSP-CONV-0001-P07

## Referencia y procedencia

Este borrador deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P07.md`.

La fuente original permanece intacta. Este documento no constituye análisis jurídico, matriz institucional aprobada ni autorización para crear IDs, Knowledge Objects, requisitos, ADR, estándares o documentos editoriales.

## 1. Cambio de enfoque del análisis

### ANALISIS_POR_COMPETENCIAS

- Tipo: `METODO_ANALISIS_PROPUESTO`.
- Estado: `Candidate`.
- Propuesta: analizar y consolidar por competencia, en lugar de revisar cada ley, reglamento o estándar de forma aislada.
- Justificación: una función operativa puede estar regulada simultáneamente por legislación federal, legislación estatal, reglamentos, EC0060 y normas complementarias; el enfoque por documentos puede producir repeticiones y dificultar la construcción curricular.

La propuesta busca reunir en un solo lugar las fuentes que sustentan una competencia, sin negar la necesidad de conservar cada referencia documental precisa.

## 2. Matriz Maestra de Obligaciones Formativas

### MMOF

- Tipo: `ESTRUCTURA_DE_EXTRACCION_PROPUESTA`.
- Estado: `Candidate`.
- Propósito: representar cada competencia obligatoria como una fila y consolidar sus fundamentos, obligaciones, componentes, riesgos, evidencias, evaluación y cursos.
- Unidad de registro propuesta: competencia, no artículo o ley.

### CAMPOS_PROPUESTOS_MMOF

1. Código de competencia.
2. Nombre.
3. Tipo: transversal, específica, crítica, especializada o liderazgo.
4. Nivel: inicial, operativo, profesional o especialista.
5. Descripción técnica.
6. Justificación.
7. Fundamento normativo con fuente, artículo o elemento y contenido relacionado.
8. Obligaciones derivadas.
9. Competencias específicas o subcompetencias.
10. Conocimientos.
11. Habilidades.
12. Destrezas.
13. Actitudes.
14. Valores.
15. Riesgos por falta de competencia.
16. Evidencias de conocimiento, desempeño y producto.
17. Instrumentos de evaluación.
18. Cursos donde deberá desarrollarse.

El ejemplo `COMP-001` se conserva como ejemplo editorial y no se crea como ID institucional.

## 3. Ejemplo de descomposición de competencia

La fuente ilustra que una competencia principal de control de accesos puede producir subcompetencias como verificar identidad, controlar visitantes, controlar vehículos, controlar materiales, registrar incidencias y aplicar protocolos.

El ejemplo es demostrativo; no constituye todavía un catálogo definitivo ni una competencia jurídicamente validada.

## 4. Estimación preliminar de volumen

La fuente estima, de manera conversacional, entre 175 y 230 competencias para el sistema completo:

| Tipo | Cantidad estimada |
|---|---:|
| Transversales | 35–45 |
| Operativas | 55–70 |
| Jurídicas | 15–20 |
| Actitudinales | 20–25 |
| De emergencia | 20–30 |
| Especializadas | 30–40 |
| Total | 175–230 |

Estas cantidades son estimaciones preliminares, no resultados de extracción ni compromisos de alcance.

## 5. Matriz de Criticidad de Competencias

### MCC

- Tipo: `MODELO_DE_PRIORIZACION_PROPUESTO`.
- Estado: `Candidate`.
- Propósito: clasificar cada competencia según su impacto operativo, jurídico y formativo para priorizar diseño, horas, actualización, auditoría y evaluación.

### DIMENSIONES_MCC

1. **Criticidad operativa:** impacto en la seguridad de personas, bienes y operaciones.
2. **Criticidad jurídica:** consecuencias legales o regulatorias de un desempeño deficiente.
3. **Criticidad formativa:** frecuencia con la que la competencia requiere refuerzo mediante práctica o actualización.

La calificación cuantitativa propuesta requiere escala, criterios, responsables, fuentes y validación antes de su uso.

## 6. Usos futuros propuestos

La MMOF y la MCC podrían apoyar la priorización de cursos, asignación de horas, definición de periodicidad de recertificación, planeación anual, auditorías internas, revisiones de desempeño y distribución de prácticas y evaluaciones en el Tomo II.

Estos usos son proyecciones de diseño y no evidencia de implementación.

## 7. Elementos excluidos

- No se realiza aquí análisis artículo por artículo ni se valida jurídicamente ninguna fuente.
- No se crean códigos de competencias; `COMP-001` es solo un ejemplo.
- No se convierten las cantidades estimadas en inventario institucional.
- No se crean la MMOF ni la MCC como registros definitivos.
- No se asignan competencias a cursos ni se definen cargas horarias o recertificaciones.
- No se crean requisitos, ADR, estándares, documentos editoriales ni Knowledge Objects.
- No se interpreta la propuesta como aprobación del Tomo I, del Tomo II o de un sistema institucional.

## 8. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P07 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 7 |
| Normalización | Borrador |
| Revisión humana P07 | Pendiente |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | No realizada |

## Criterio para cerrar el borrador

La revisión humana deberá confirmar la fidelidad respecto de P07, la clasificación del enfoque por competencias, la estructura de la MMOF, el carácter estimativo del volumen, la definición de la MCC y la ausencia de promoción o códigos prematuros.

# FIN DEL BORRADOR DE NORMALIZACIÓN P07
