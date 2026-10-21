---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
project: MIPSP
type: NORMALIZATION-DRAFT
domain: MIPSP
source: ChatGPT
status: Normalization-Draft
part: 29
source_file: projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P29.md
source_sha256: 18B3A6CD2EBE4EE65AEB747B03CD33F23BA7AC442D72AEC7FD39D70CC88FA135
---

# Borrador de normalización P29

## 1. Alcance y cambio de fase

P29 declara concluida la fase de arquitectura y propone iniciar la redacción técnica y el desarrollo del Inventario Analítico de Requisitos Formativos (IARF) a partir de las cinco fuentes normativas.

La propuesta metodológica principal se denomina Ingeniería de Competencias Basada en Evidencia Normativa (ICBEN) y busca mantener trazabilidad desde la norma hasta la auditoría y la mejora continua.

## 2. Cadena de trazabilidad ICBEN

La cadena propuesta contiene los siguientes niveles:

1. norma;
2. disposición jurídica;
3. Elemento Normativo Formativo (ENF);
4. requisito formativo;
5. competencia;
6. criterio de desempeño;
7. proceso operativo;
8. procedimiento normalizado;
9. actividad observable;
10. evidencia;
11. indicador;
12. auditoría; y
13. mejora continua.

La cadena se presenta como arquitectura de trazabilidad pendiente de especificación formal y validación.

## 3. Unidad Elemental de Competencia (UEC)

La UEC se define como la capacidad mínima, observable y evaluable que el personal debe demostrar durante la ejecución de un proceso operativo. Una competencia puede integrarse por varias UEC y cada unidad puede evaluarse de forma independiente.

La fuente ejemplifica la competencia de controlar el acceso de personas mediante UEC relacionadas con verificar identidad, corroborar autorización, registrar ingreso, detectar inconsistencias, aplicar un protocolo de rechazo e informar incidencias.

## 4. Arquitectura jerárquica

La estructura propuesta es:

Familia de Competencias → Competencia → Subcompetencia → UEC → Actividad observable → Evidencia.

Esta jerarquía pretende administrar un volumen amplio de actividades sin perder coherencia entre niveles.

## 5. Ficha técnica de una UEC

La ficha propuesta incluye:

- identificación: código, nombre, familia y competencia asociada;
- finalidad: resultado esperado;
- fundamento jurídico: disposiciones aplicables;
- riesgos mitigados: operativos, jurídicos, patrimoniales y reputacionales;
- actividades observables;
- condiciones de ejecución: recursos, equipamiento, escenario, tiempo y restricciones;
- evidencias de conocimiento, desempeño, producto y resultado;
- instrumentos: lista de cotejo, guía de observación, simulación, caso práctico y rúbrica; y
- nivel de dominio: inicial, operativo, avanzado o especialista.

## 6. Diccionario de Actividades Observables (DAO)

El DAO se propone como un documento central para sustituir la evaluación de conceptos abstractos por actividades concretas. Los ejemplos incluyen verificar credencial, solicitar identificación, comparar fotografía, consultar listados autorizados, registrar ingresos, revisar vehículos, observar conductas, reportar anomalías, solicitar apoyo, redactar informes y entregar evidencias.

Cada actividad debería registrar definición, procedimiento, estándar esperado, errores frecuentes, criterios de aceptación y tiempo estimado.

## 7. Sistema de codificación propuesto

La fuente propone códigos para familias de competencias, competencias, UEC, actividades, indicadores e instrumentos. Los ejemplos incluyen `CJ` para competencias jurídicas, `CO` para competencias operativas, `CT` para competencias técnicas, `UEC-CO-014`, `ACT-UEC-CO-014-05`, `IND-UEC-CO-014-05` e `INS-UEC-CO-014-05`.

Estos ejemplos son convenciones propuestas y no deben interpretarse como IDs institucionales ya asignados.

## 8. Dependencias y progresión

El mapa de dependencias deberá documentar los conocimientos previos necesarios para dominar una competencia. Para control de accesos, la fuente propone como dependencias identificación, observación, comunicación, registro documental y atención al usuario.

La curva institucional de aprendizaje propuesta avanza por conocimiento, comprensión, práctica guiada, práctica supervisada, desempeño autónomo, desempeño competente, dominio y capacidad para instruir a otros.

## 9. Índice de Complejidad Operativa (ICO)

El ICO se propone para clasificar cada competencia mediante complejidad técnica, frecuencia, riesgo, autonomía requerida y consecuencias del error.

| ICO | Nivel |
| --- | --- |
| 1 | Muy bajo |
| 2 | Bajo |
| 3 | Medio |
| 4 | Alto |
| 5 | Crítico |

La clasificación podría influir en la duración del curso, el número de prácticas, el tipo de evaluación y la periodicidad de recertificación. El método de cálculo y sus umbrales quedan pendientes de validación.

## 10. Diccionario Técnico de Competencias para la Seguridad Privada

P29 propone un DTC-SP como anexo de la colección. Para cada competencia contendría definición técnica, fundamentos jurídico y operativo, nivel de dominio, actividades observables, errores críticos, evidencias aceptables, criterios e indicadores de evaluación, competencias relacionadas y referencias cruzadas con procesos y programas.

Las estimaciones de volumen incluidas en la fuente —300 a 400 competencias, 1,500 a 2,000 UEC y más de 6,000 actividades— se conservan como proyecciones, no como inventario confirmado.

## 11. Límites de esta normalización

- No se crean UEC, competencias, actividades, indicadores ni instrumentos concretos.
- No se asignan IDs institucionales nuevos.
- No se valida jurídicamente la cadena ICBEN, la jerarquía, la codificación ni el ICO.
- No se confirma el volumen proyectado del DTC-SP.
- No se inicia todavía el análisis artículo por artículo de las fuentes normativas.

## 12. Siguiente etapa propuesta

Iniciar el IARF con las cinco fuentes normativas, identificar ENF, elaborar Fichas Analíticas de Requisito Formativo (FARF), definir competencias, UEC y actividades observables, y conservar trazabilidad hacia las disposiciones de origen.
