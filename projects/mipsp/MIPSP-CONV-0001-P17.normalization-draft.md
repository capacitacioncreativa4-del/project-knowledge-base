---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalization-Draft
type: Source
file_reference: MIPSP-CONV-0001-P17.md
source_part: 17
source_sha256: 49DEC317DF3888209B5643D11CD808A70DB3D3F4913690D0AA3B6F7795E25925
---

# Borrador de Fuente Normalizada — MIPSP-CONV-0001-P17

## Referencia y procedencia

Este borrador deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P17.md`.

La fuente original permanece intacta. Este documento no constituye análisis jurídico ejecutado, catálogo curricular, sistema de trazabilidad ni autorización para crear IDs, Knowledge Objects, requisitos, ADR, estándares o software.

## 1. Inicio del desarrollo técnico

La conversación declara el inicio del desarrollo técnico del proyecto y propone construir una obra de consulta para empresas de seguridad privada, centros de capacitación y evaluación, consultores, autoridades verificadoras, instructores y diseñadores instruccionales.

Se establece una diferencia entre un manual que explica y una obra de referencia que demuestra. El objetivo propuesto es documentar la cadena:

**Qué exige la norma → qué competencia genera → cómo debe enseñarse → cómo debe evaluarse → cómo demostrar su cumplimiento.**

La cadena es un criterio de diseño; P17 no contiene resultados de análisis normativo.

## 2. Tomo II: Ingeniería Jurídica del Sistema de Capacitación

### Objetivo propuesto

Identificar las disposiciones de la Ley Federal de Seguridad Privada que generen obligaciones de formación para el personal operativo y traducirlas en competencias, contenidos curriculares, evidencias de desempeño e instrumentos de evaluación.

El análisis utilizaría la metodología de Ingeniería Jurídico-Curricular definida previamente.

### Perspectivas de análisis

Cada artículo se examinaría desde cinco perspectivas:

1. **Jurídica:** qué dispone la norma.
2. **Operativa:** cómo impacta la prestación del servicio.
3. **Competencial:** qué debe saber hacer el elemento operativo.
4. **Curricular:** qué debe enseñarse.
5. **Evaluativa:** cómo demostrar que la competencia fue adquirida.

## 3. Ficha FIJC propuesta

La **Ficha de Ingeniería Jurídico-Curricular (FIJC)** sería la estructura uniforme para documentar cada artículo. Sus campos propuestos son:

- identificador;
- fuente;
- artículo;
- naturaleza jurídica: definición, obligación, requisito, procedimiento, prohibición, facultad o sanción;
- texto analizado como síntesis técnica, con cita exacta en la versión definitiva cuando corresponda;
- impacto operativo;
- competencias derivadas;
- conocimientos;
- habilidades;
- actitudes;
- valores;
- evidencias de conocimiento, desempeño y producto;
- instrumentos, como examen, lista de cotejo, guía de observación, caso práctico o simulación;
- procesos afectados según el MMPO;
- cursos relacionados según el Tomo IV;
- nivel de criticidad: bajo, medio, alto o muy alto.

El identificador ilustrativo `FIJC-LFSP-001` es un código de ejemplo y no un ID persistente del PKB.

## 4. Modelo ilustrativo de extracción

La fuente incluye un registro modelo con fuente en la Ley Federal de Seguridad Privada, clasificación de obligación, competencia de aplicación normativa, dominio jurídico, nivel operativo, criticidad alta, curso, evidencia, instrumento y observaciones.

El ejemplo `FIJC-LFSP-0001`, así como `CUR-JUR-01`, son códigos ilustrativos. No representan artículos analizados, cursos creados ni registros institucionales.

## 5. Actualizaciones relacionadas propuestas

Se propone que, al completar una FIJC, se actualicen los demás tomos de forma coordinada:

- **Tomo III:** ficha de competencia correspondiente.
- **Tomo IV:** curso, unidad, resultados de aprendizaje y actividades.
- **Tomo V:** reactivos, rúbricas, listas de cotejo, simulaciones y casos.
- **Tomo VI:** matriz de trazabilidad, cobertura normativa, indicadores y expediente documental.

La actualización simultánea se registra como flujo propuesto; P17 no demuestra automatización ni materializa esos productos.

## 6. Matriz de Defendibilidad Curricular

Se propone una **Matriz de Defendibilidad Curricular (MDC)** para responder documentalmente preguntas sobre la existencia de un curso, su fundamento, duración, evaluación y recertificación.

Su estructura relacionaría cada elemento curricular con justificación jurídica, técnica y pedagógica:

| Elemento curricular | Justificación jurídica | Justificación técnica | Justificación pedagógica |
|---|---|---|---|
| Curso | Artículos aplicables | Función operativa | Competencias requeridas |
| Duración | Complejidad de la competencia | Riesgo operativo | Tiempo de práctica |
| Evaluación | Evidencias exigibles | Riesgos de desempeño deficiente | Validez del instrumento |
| Recertificación | Cambios normativos y criticidad | Riesgos operativos | Consolidación del aprendizaje |

La MDC se plantea como mecanismo para justificar decisiones curriculares en auditorías o verificaciones. No se crea ni se llena en P17.

## 7. Regla para la siguiente etapa

La conversación recomienda dejar de elaborar ejemplos genéricos y trabajar únicamente con documentos normativos oficiales del proyecto, analizando cada artículo y citando su fundamento exacto.

De cada disposición se derivarían competencias, cursos, evidencias e instrumentos de evaluación. Esta regla marca el inicio propuesto del contenido sustantivo de los seis tomos, pero P17 todavía no contiene dicho análisis.

## 8. Elementos excluidos

- No se ejecuta el análisis de la Ley Federal de Seguridad Privada.
- No se crean ni llenan fichas FIJC.
- No se convierten los códigos ilustrativos en IDs institucionales.
- No se crean competencias, cursos, unidades, evaluaciones, evidencias o indicadores.
- No se actualizan automáticamente los tomos.
- No se crea ni llena la MDC.
- No se crean requisitos, ADR, estándares, Knowledge Objects ni relaciones persistentes.

## 9. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P17 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 17 |
| Normalización | Borrador |
| Revisión humana P17 | Pendiente |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | No realizada |

## Criterio para cerrar el borrador

La revisión humana deberá confirmar el inicio del desarrollo técnico, la cadena de demostración, el objetivo y perspectivas del Tomo II, los campos de la FIJC, el carácter ilustrativo de sus códigos, las actualizaciones propuestas, la MDC y la regla de trabajar desde fuentes normativas oficiales.

# FIN DEL BORRADOR DE NORMALIZACIÓN P17
