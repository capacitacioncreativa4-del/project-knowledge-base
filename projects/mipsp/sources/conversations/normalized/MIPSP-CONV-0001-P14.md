---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalized
type: Source
file_reference: MIPSP-CONV-0001-P14.md
source_part: 14
source_sha256: 7767535E7C197CC31204A2ECEA79EBFA71BC280605DC6BD68BD01EB200656A6A
---

# Fuente Normalizada — MIPSP-CONV-0001-P14

## Referencia y procedencia

Esta fuente normalizada deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P14.md`.
La fuente original y el borrador aprobado permanecen intactos.

## 1. Recomendación estratégica

La conversación recomienda no comenzar todavía a llenar matrices, porque aún no se habría definido un modelo de clasificación de competencias. Extraer obligaciones sin una taxonomía previa podría exigir reclasificar registros posteriormente.

Se propone construir primero el **Sistema Taxonómico Institucional de Competencias (STIC)** como estructura de clasificación para el resto del proyecto.

## 2. Finalidad propuesta del STIC

El STIC establecería un lenguaje común para clasificar competencias identificadas en la normatividad y favorecería uniformidad en diseño curricular, evaluación y actualización. Su propósito sería reducir ambigüedades y permitir que una competencia se interprete de forma consistente por diseñadores instruccionales, instructores, supervisores y autoridades.

El STIC se registra como propuesta conceptual; no se materializa ni se valida institucionalmente en P14.

## 3. Niveles jerárquicos propuestos

| Nivel | Elemento | Ejemplo |
|---|---|---|
| I | Dominio | Seguridad Operativa |
| II | Macrocompetencia | Protección Física |
| III | Competencia | Controlar accesos |
| IV | Subcompetencia | Verificar identidad |
| V | Resultado de aprendizaje | Registra el ingreso conforme al procedimiento |
| VI | Evidencia | Bitácora correctamente integrada |

La estructura permitiría navegar desde un concepto amplio hasta una evidencia concreta.

## 4. Dominios de competencia propuestos

Se proponen ocho dominios:

1. **D1. Jurídico:** legislación aplicable, derechos humanos, responsabilidades administrativas, protección de datos y uso legítimo de la fuerza.
2. **D2. Operativo:** control de accesos, rondines, vigilancia, custodia y protección de instalaciones.
3. **D3. Técnico:** radiocomunicación, sistemas electrónicos, CCTV, alarmas y controles biométricos.
4. **D4. Gestión de Riesgos:** identificación de amenazas, evaluación de riesgos, planes de emergencia, protección civil y continuidad operativa.
5. **D5. Atención a Personas:** atención al usuario, comunicación, manejo de conflictos, perspectiva de género y atención a grupos vulnerables.
6. **D6. Ético-Conductual:** honestidad, disciplina, confidencialidad, lealtad, integridad e imparcialidad.
7. **D7. Administrativo:** informes, bitácoras, registros, cadena documental y entrega-recepción.
8. **D8. Desarrollo Profesional:** trabajo en equipo, liderazgo, aprendizaje continuo, autodesarrollo e innovación.

Los dominios y ejemplos son una clasificación propuesta, no un catálogo institucional aprobado.

## 5. Clasificaciones complementarias propuestas

### Clasificación funcional

| Código de propuesta | Tipo |
|---|---|
| T | Transversal |
| O | Operativa |
| E | Especializada |
| C | Crítica |
| L | Liderazgo |
| I | Instructor |
| A | Actualización |

Una competencia podría pertenecer a varias categorías.

### Clasificación por complejidad

| Nivel | Denominación |
|---|---|
| N1 | Básico |
| N2 | Intermedio |
| N3 | Avanzado |
| N4 | Especialista |

Esta dimensión permitiría secuenciar aprendizaje y definir prerrequisitos.

### Clasificación por frecuencia de uso

Se proponen las categorías permanentes, frecuentes, ocasionales y excepcionales, para planificar reforzamientos y simulaciones.

### Clasificación por impacto

Cada competencia recibiría una valoración en impacto sobre la seguridad de las personas, el patrimonio, el ámbito jurídico y la reputación. La combinación determinaría su criticidad propuesta.

## 6. Relaciones con procesos y cursos

Cada competencia se vincularía con uno o varios procesos del MMPO. Los ejemplos `PROC-001`, `PROC-009` y `PROC-005` son códigos ilustrativos de la propuesta y no IDs persistentes del PKB. La relación facilitaría la integración futura con Procedimientos Normalizados de Operación.

Una misma competencia podría desarrollarse en cursos de inducción, básicos, de especialización o de actualización, con propósitos distintos de introducción, práctica, profundización o reforzamiento.

## 7. Gobernanza propuesta

La taxonomía se trataría como un modelo sujeto a control de cambios. Toda incorporación, modificación o eliminación de competencias debería documentar motivo, fundamento normativo, impacto en cursos y evaluaciones, fecha de entrada en vigor y versión del sistema.

Esto se registra como procedimiento de gobernanza propuesto; P14 no demuestra su adopción o ejecución.

## 8. Reorganización documental propuesta

La conversación propone sustituir el concepto de un único Tomo I por un **Manual Maestro de Ingeniería Curricular**, integrado por:

- **Volumen A. Fundamentos y Metodología:** marco conceptual, modelo de competencias, MICTN, MACI, SIGCO-ESP y STIC.
- **Volumen B. Análisis Normativo Exhaustivo:** análisis artículo por artículo de la legislación federal, estatal de Morelos y EC0060, con requisitos formativos, competencias y evidencias referenciados.
- **Volumen C. Anexos Técnicos:** matrices maestras, inventarios, mapas, trazabilidad, cobertura, diccionario institucional y sistema de codificación.

La estructura es una propuesta editorial y no constituye documentos materializados por P14.

## 9. Siguiente etapa propuesta

La recomendación final es dejar de ampliar el marco metodológico e iniciar el trabajo sustantivo en el Volumen B, comenzando por el análisis artículo por artículo de la Ley Federal de Seguridad Privada.

Cada hallazgo se documentaría con referencia normativa exacta y se incorporaría a la primera versión del IARF. P14 no contiene todavía ese análisis ni registros del inventario.

## 10. Elementos excluidos

- No se crea ni aprueba el STIC.
- No se registran competencias, dominios, procesos, cursos o evidencias institucionales.
- No se convierten los códigos de ejemplo en IDs persistentes.
- No se ejecuta el análisis artículo por artículo ni se crea el IARF.
- No se materializa el Manual Maestro ni sus tres volúmenes.
- No se crean requisitos, ADR, estándares, Knowledge Objects ni relaciones persistentes.

## 11. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P14 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 14 |
| Normalización | Normalizada |
| Revisión humana P14 | Aprobada por el usuario |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | Realizada |

## Cierre de normalización

La revisión humana confirmó la justificación para anteponer el STIC al llenado de matrices, sus niveles, dominios, clasificaciones complementarias, relaciones y gobernanza, la reorganización en tres volúmenes y el inicio posterior del análisis normativo para el IARF.

# FIN DE LA FUENTE NORMALIZADA P14
