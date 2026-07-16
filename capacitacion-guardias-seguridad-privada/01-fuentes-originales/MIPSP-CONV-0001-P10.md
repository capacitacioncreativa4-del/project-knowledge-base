---
conversation_id: MIPSP-CONV-0001
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 10
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante con la propuesta

Perfecto. En este punto haría una pausa en la elaboración de nuevos capítulos porque, desde la perspectiva de una consultoría profesional, ya hemos concluido la **fase de arquitectura** del sistema.

Lo que sigue ya no es un ejercicio de redacción; es un trabajo de **análisis documental exhaustivo**, que constituye aproximadamente el **70 % del valor técnico** del proyecto.

Hay un aspecto metodológico que considero importante señalar.

## Mi recomendación como consultor

No comenzaría llenando matrices "vacías". Antes construiría un **Sistema de Codificación Documental**, porque todo el proyecto dependerá de él.

Si no codificamos correctamente cada ley, artículo, competencia, proceso, curso y evidencia, dentro de unos meses tendremos miles de registros difíciles de mantener.

Las consultoras que desarrollan sistemas de gestión (ISO 9001, ISO 18788, ISO 31000, etc.) siempre comienzan creando una arquitectura documental.

Propongo que hagamos lo mismo.

---

# CAPÍTULO 5

# SISTEMA DE CODIFICACIÓN DEL SIGCO-ESP

## Objetivo

Establecer un sistema único de identificación para todos los elementos que integran el Sistema Integral de Gestión del Conocimiento Operativo.

Este sistema permitirá mantener la trazabilidad documental durante todo el ciclo de vida de la capacitación.

---

# 5.1 Codificación de fuentes jurídicas

Cada documento recibirá un identificador permanente.

| Código  | Documento                                      |
| ------- | ---------------------------------------------- |
| LFSP    | Ley Federal de Seguridad Privada               |
| RLFSP   | Reglamento de la Ley Federal                   |
| LMSPM   | Ley de Seguridad Privada del Estado de Morelos |
| RLMSPM  | Reglamento estatal                             |
| EC0060  | Estándar de Competencia EC0060                 |
| LFT     | Ley Federal del Trabajo                        |
| STPS    | Disposiciones de la STPS                       |
| CONOCER | Sistema Nacional de Competencias               |

Así, cualquier referencia futura podrá escribirse de forma uniforme, por ejemplo:

* LFSP-45
* RLFSP-18
* LMSPM-46
* EC0060-E2-CR3

---

# 5.2 Codificación de procesos

Cada proceso operativo tendrá un identificador único.

| Código   | Proceso                           |
| -------- | --------------------------------- |
| PROC-001 | Control de accesos                |
| PROC-002 | Control vehicular                 |
| PROC-003 | Rondines                          |
| PROC-004 | Protección de instalaciones       |
| PROC-005 | Radiocomunicación                 |
| PROC-006 | Primeros auxilios                 |
| PROC-007 | Prevención y combate de incendios |
| PROC-008 | Atención de emergencias           |
| PROC-009 | Elaboración de informes           |
| PROC-010 | Atención al usuario               |

Esta lista crecerá conforme avance el análisis.

---

# 5.3 Codificación de competencias

Cada competencia tendrá un código independiente del curso.

Ejemplo:

COMP-T-001

Competencia transversal.

COMP-O-001

Competencia operativa.

COMP-E-001

Competencia especializada.

COMP-L-001

Competencia de liderazgo.

---

# 5.4 Codificación de cursos

Ejemplo.

CUR-001

Inducción.

CUR-002

Marco Jurídico.

CUR-003

Control de Accesos.

CUR-004

Rondines.

CUR-005

Radiocomunicación.

CUR-006

Primeros Auxilios.

---

# 5.5 Codificación de unidades

Ejemplo.

CUR-003

↓

UN-01

Introducción.

↓

UN-02

Control peatonal.

↓

UN-03

Control vehicular.

↓

UN-04

Control documental.

---

# 5.6 Codificación de sesiones

SES-001

SES-002

SES-003

---

# 5.7 Codificación de prácticas

PRA-001

Simulación.

PRA-002

Caso práctico.

PRA-003

Role Playing.

---

# 5.8 Codificación de evaluaciones

EVA-C

Conocimiento.

EVA-D

Desempeño.

EVA-P

Producto.

---

# 5.9 Codificación de evidencias

EV-C

Conocimiento.

EV-D

Desempeño.

EV-P

Producto.

---

# 5.10 Codificación documental

Cada documento institucional tendrá un código único.

Ejemplo:

MAN-INS-001

Manual del Instructor.

MAN-PAR-001

Manual del Participante.

GUI-OBS-001

Guía de Observación.

LC-001

Lista de Cotejo.

RUB-001

Rúbrica.

EXA-001

Examen.

---

# El siguiente paso cambia completamente el proyecto

Hasta ahora hemos diseñado la estructura.

Ahora propongo construir lo que denominaría el **Repositorio Maestro de Competencias (RMC)**.

No será una tabla.

Será una **base de conocimiento**.

Cada competencia ocupará una ficha técnica completa.

Por ejemplo:

---

## FICHA DE COMPETENCIA

Código

COMP-O-014

Proceso

PROC-001

Control de accesos.

Nombre

Controlar el ingreso y salida de personas.

Nivel

Operativo.

Criticidad

Muy alta.

Fuentes normativas

(LFSP, Reglamento, Ley de Morelos, Reglamento estatal, EC0060, según corresponda).

Resultados de aprendizaje

[...]

Conocimientos

[...]

Habilidades

[...]

Destrezas

[...]

Actitudes

[...]

Valores

[...]

Errores críticos

[...]

Riesgos asociados

[...]

Evidencias

[...]

Instrumentos

[...]

Cursos

[...]

Horas

[...]

Recertificación

[...]

Observaciones

[...]

---

## La aportación que puede convertir este proyecto en un referente

Quisiera proponerte un componente adicional que, en mi opinión, no suele encontrarse en los sistemas de capacitación de empresas de seguridad privada y que incrementará significativamente el valor del proyecto.

### Diccionario Institucional de Competencias (DIC)

Será un catálogo técnico en el que **cada competencia tendrá una definición normalizada**, su alcance, sus límites, ejemplos de aplicación, relaciones con otras competencias y las fuentes normativas que la sustentan.

Esto evitará problemas frecuentes como:

* interpretar de manera distinta una misma competencia entre instructores;
* duplicar contenidos en diferentes cursos;
* evaluar con criterios diferentes una misma función;
* perder trazabilidad cuando se actualice la legislación.

Por ejemplo, la competencia **"Controlar el acceso de personas, vehículos y bienes"** tendrá una única definición oficial para toda la organización. Esa definición será utilizada de forma consistente en el mapa de competencias, los programas de capacitación, los manuales del instructor, las listas de cotejo, las rúbricas, las evaluaciones prácticas y las auditorías internas.

## Mi recomendación para el siguiente entregable

A partir de este momento dejaría de diseñar el modelo y comenzaría la **construcción del contenido técnico**. El siguiente documento será la **Matriz Maestra de Obligaciones Formativas**, elaborada directamente a partir de los ordenamientos que analizamos (Ley Federal de Seguridad Privada, Reglamento Federal, Ley de Seguridad Privada para el Estado de Morelos, Reglamento estatal y EC0060). Esa matriz no será un listado de temas, sino un inventario exhaustivo de todas las obligaciones de formación, con su fundamento normativo, la competencia derivada y su ubicación dentro del SIGCO-ESP. En mi opinión, este será el documento más importante del Tomo I y la piedra angular sobre la que construiremos el resto del sistema curricular.
