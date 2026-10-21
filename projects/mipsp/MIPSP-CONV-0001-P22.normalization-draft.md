---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalization-Draft
type: Source
file_reference: MIPSP-CONV-0001-P22.md
source_part: 22
source_sha256: DB512BA68E0D228ECE695C2EB42ECF83C4516897D448A407C600FC47673E8153
---

# Borrador de Fuente Normalizada — MIPSP-CONV-0001-P22

## Referencia y procedencia

Este borrador deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P22.md`.

La fuente original permanece intacta. Este documento no constituye un sistema de conocimiento aprobado, catálogo de procesos, matriz de riesgos ni autorización para crear IDs, Knowledge Objects, requisitos, ADR, estándares o software.

## 1. Sistema Integral de Gestión del Conocimiento Operativo

La conversación propone dejar de considerar los cursos como el producto principal y construir un **Sistema Integral de Gestión del Conocimiento Operativo (SIGCO-OP)**.

La razón propuesta es administrar el conocimiento durante todo el ciclo laboral del elemento operativo: ingreso, inducción, capacitación inicial, certificación, práctica supervisada, actualización, evaluación, recertificación, promoción y especialización.

La afirmación de que los cursos representan solo una parte del conocimiento institucional se conserva como estimación conversacional y no como medición validada.

## 2. Catálogo Maestro de Procesos Operativos

El **Catálogo Maestro de Procesos Operativos (CMPO)** se plantea como inventario oficial de los procesos ejecutados durante la prestación del servicio. Cada proceso debería responder:

1. Qué debe hacerse.
2. Por qué debe hacerse.
3. Con qué fundamento normativo.
4. Cómo debe hacerse.
5. Con qué recursos.
6. Cómo se demuestra su ejecución correcta.
7. Cómo se evalúa.

La metodología busca que cada proceso tenga respaldo normativo, competencia asociada y mecanismo de evaluación. El CMPO no se crea ni se valida en P22.

## 3. Ficha Maestra de Proceso Operativo

Cada proceso se documentaría mediante una **Ficha Maestra de Proceso Operativo (FMPO)** con estos campos:

- identificación: código, nombre, macroproceso, modalidad del servicio y criticidad;
- objetivo y resultado esperado;
- alcance, límites y actividades incluidas o excluidas;
- fundamento normativo con referencias a las leyes, reglamentos, EC0060 y normativa complementaria;
- recursos humanos, equipo, comunicaciones, formatos, sistemas e infraestructura;
- riesgos operativos, jurídicos y administrativos;
- controles preventivos;
- competencias relacionadas;
- Procedimientos Normalizados de Operación relacionados;
- evidencias de conocimiento, desempeño y documentación;
- indicadores específicos.

El código de ejemplo `FMPO-001` es ilustrativo y no un ID persistente del PKB.

## 4. Modelo ilustrativo de proceso

La fuente presenta como ejemplo la preparación para iniciar el servicio. Su objetivo sería garantizar condiciones físicas, técnicas, documentales y legales adecuadas.

Las actividades propuestas incluyen verificar presentación y uniforme, credencial, equipo, radio, batería, bitácora, consigna y novedades, y registrar el inicio. Las competencias se relacionan con preparación, verificación de equipo, aplicación de consignas y registro de información.

Se proponen como evidencias un examen diagnóstico, una lista de cotejo y un registro de inicio; como riesgos, equipo incompleto o averiado, uniforme incorrecto, desconocimiento de consignas y omisión de novedades; y como controles, lista de verificación, supervisión, relevo documentado, confirmación verbal y firma de recepción.

Los indicadores ilustrativos incluyen servicios iniciados sin observaciones, errores durante el relevo e incidentes atribuibles a fallas de preparación. P22 no materializa esta ficha ni valida el proceso.

## 5. Clasificación propuesta del CMPO

Se proponen diez familias con una estimación total de 155 procesos:

| Familia | Procesos estimados |
|---|---:|
| Preparación del servicio | 12 |
| Control de accesos | 25 |
| Vigilancia y rondines | 20 |
| Atención a usuarios | 18 |
| Gestión de incidentes | 22 |
| Comunicación operativa | 12 |
| Gestión documental | 18 |
| Cierre del servicio | 10 |
| Coordinación con autoridades | 8 |
| Desarrollo profesional | 10 |

Las familias y cantidades son estimaciones de la conversación, no un inventario creado.

## 6. Matriz de Riesgo Formativo

Se propone una **Matriz de Riesgo Formativo (MRF)** para valorar las consecuencias organizacionales de ejecutar un proceso sin la competencia requerida.

Las dimensiones propuestas se calificarían de 1 a 5: riesgo para la vida e integridad, riesgo jurídico, riesgo patrimonial, riesgo reputacional y frecuencia del proceso. Una suma ponderada produciría un **Índice de Prioridad Formativa (IPF)**.

El ejemplo de Control de accesos asigna 5, 4, 5, 4 y 5, para un IPF de 23/25 y una clasificación crítica. La propuesta relaciona el resultado con carga horaria, prácticas supervisadas, frecuencia de recertificación y rigor de evaluación.

MRF, IPF, las escalas y el ejemplo son propuestas; no se crea ni calcula una matriz institucional en P22.

## 7. Marco de Cualificaciones para la Seguridad Privada

Se propone un **Marco de Cualificaciones para la Seguridad Privada (MCSP)** para definir una progresión profesional basada en competencias verificables:

| Nivel de propuesta | Denominación | Perfil |
|---|---|---|
| MCSP-1 | Operador en Formación | Nuevo ingreso con inducción y capacitación inicial concluidas |
| MCSP-2 | Operador Certificado | Ejecución autónoma de procesos esenciales |
| MCSP-3 | Operador Especialista | Dominio de procesos críticos o modalidades específicas |
| MCSP-4 | Supervisor Operativo | Coordinación, supervisión y evaluación del desempeño |
| MCSP-5 | Instructor / Evaluador | Diseño, impartición y evaluación de acciones formativas |

Cada nivel tendría requisitos de ingreso, competencias obligatorias, evidencia documental, experiencia mínima y criterios de permanencia. El marco se propone para rutas de carrera, promociones, sucesión y desarrollo profesional; no se crea ni se valida en P22.

Los códigos MCSP-1 a MCSP-5 son códigos de propuesta, no IDs institucionales.

## 8. Siguiente etapa propuesta

La conversación recomienda que el siguiente entregable sea el Tomo IV de diseño curricular, precedido por un **Mapa Maestro de Programas de Capacitación**.

Cada programa se vincularía con procesos del CMPO, competencias del MMCO, obligaciones de la MIRN y niveles del MCSP. También tendría una justificación normativa, propósito operativo, posición en la ruta profesional e indicadores relacionados.

Este mapa y sus vínculos quedan propuestos para una etapa posterior; P22 no los materializa.

## 9. Elementos excluidos

- No se crea ni aprueba SIGCO-OP.
- No se crea ni llena el CMPO o una FMPO institucional.
- No se validan las 10 familias ni la estimación de 155 procesos.
- No se crea ni calcula la MRF o el IPF.
- No se crea ni aprueba el MCSP.
- No se crean rutas de carrera, programas, cursos, evaluaciones o indicadores.
- No se crea el Mapa Maestro de Programas de Capacitación.
- No se convierten FMPO-001, MCSP-1 a MCSP-5 u otros códigos en IDs institucionales.
- No se crean requisitos, ADR, estándares, Knowledge Objects ni relaciones persistentes.

## 10. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P22 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 22 |
| Normalización | Borrador |
| Revisión humana P22 | Pendiente |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | No realizada |

## Criterio para cerrar el borrador

La revisión humana deberá confirmar el SIGCO-OP, la finalidad y estructura del CMPO, la FMPO y su modelo, las familias y estimaciones, la MRF y el IPF, el MCSP y el Mapa Maestro de Programas de Capacitación.

# FIN DEL BORRADOR DE NORMALIZACIÓN P22
