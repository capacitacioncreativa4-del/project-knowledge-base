---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalized
type: Source
file_reference: MIPSP-CONV-0001-P07.md
source_part: 7
source_sha256: FB163096FFF67F50873E1BEB4670BF690E71E63FCAF543FEF2238AD0C84C2759
---

# Fuente Normalizada — MIPSP-CONV-0001-P07

## Referencia y procedencia

Esta fuente normalizada deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P07.md`.
La fuente original y el borrador aprobado permanecen intactos.

## 1. Cambio de enfoque del análisis

### ANALISIS_POR_COMPETENCIAS

- Tipo: `METODO_ANALISIS_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Propuesta: analizar y consolidar por competencia, en lugar de revisar cada ley, reglamento o estándar de forma aislada.
- Justificación: una función puede estar regulada simultáneamente por legislación federal, estatal, reglamentos, EC0060 y normas complementarias; el enfoque documental puede producir repeticiones y dificultar la construcción curricular.

La propuesta reúne fuentes aplicables a una competencia sin sustituir las referencias documentales precisas.

## 2. Matriz Maestra de Obligaciones Formativas

### MMOF

- Tipo: `ESTRUCTURA_DE_EXTRACCION_PROPUESTA`.
- Estado: `Validated-As-Proposal`.
- Propósito: representar cada competencia obligatoria como una fila y consolidar fundamentos, obligaciones, componentes, riesgos, evidencias, evaluación y cursos.
- Unidad de registro: competencia, no artículo o ley.

### CAMPOS_PROPUESTOS_MMOF

Código; nombre; tipo; nivel; descripción técnica; justificación; fundamento normativo con fuente y artículo o elemento; obligaciones derivadas; subcompetencias; conocimientos; habilidades; destrezas; actitudes; valores; riesgos; evidencias de conocimiento, desempeño y producto; instrumentos de evaluación; y cursos de desarrollo.

El ejemplo `COMP-001` se conserva únicamente como ejemplo editorial y no se crea como ID institucional.

## 3. Ejemplo de descomposición

Una competencia principal de control de accesos puede producir subcompetencias de verificar identidad, controlar visitantes, controlar vehículos, controlar materiales, registrar incidencias y aplicar protocolos.

Es un ejemplo demostrativo, no un catálogo definitivo ni una competencia jurídicamente validada.

## 4. Estimación preliminar de volumen

La fuente estima entre 175 y 230 competencias para el sistema completo: 35–45 transversales, 55–70 operativas, 15–20 jurídicas, 20–25 actitudinales, 20–30 de emergencia y 30–40 especializadas.

Son estimaciones preliminares, no resultados de extracción ni compromisos de alcance.

## 5. Matriz de Criticidad de Competencias

### MCC

- Tipo: `MODELO_DE_PRIORIZACION_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Propósito: clasificar competencias según impacto operativo, jurídico y formativo para priorizar diseño, horas, actualización, auditoría y evaluación.

### DIMENSIONES_MCC

1. **Criticidad operativa:** impacto en personas, bienes y operaciones.
2. **Criticidad jurídica:** consecuencias legales o regulatorias del desempeño deficiente.
3. **Criticidad formativa:** frecuencia de refuerzo mediante actualización o práctica.

La calificación cuantitativa requiere escala, criterios, responsables, fuentes y validación antes de su uso.

## 6. Usos futuros propuestos

La MMOF y la MCC podrían apoyar la priorización de cursos, asignación de horas, periodicidad de recertificación, planeación anual, auditorías, revisiones de desempeño y distribución de prácticas y evaluaciones en el Tomo II.

Son proyecciones de diseño y no evidencia de implementación.

## 7. Elementos excluidos

- No se realiza análisis artículo por artículo ni se valida jurídicamente ninguna fuente.
- No se crean códigos de competencias; `COMP-001` es solo un ejemplo.
- No se convierten las cantidades estimadas en inventario institucional.
- No se crean la MMOF ni la MCC como registros definitivos.
- No se asignan competencias a cursos ni se definen cargas horarias o recertificaciones.
- No se crean requisitos, ADR, estándares, documentos editoriales ni Knowledge Objects.

## 8. Estado de normalización

| Elemento | Estado |
|---|---|
| Fuente P07 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 7 |
| Normalización | Normalized |
| Revisión humana P07 | Aprobada |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |

La aprobación no convierte las propuestas en estándares, requisitos, decisiones u objetos institucionales.
