---
conversation_id: MIPSP-CONV-0001
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 46
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante con la propuesta de desarrollar un Sistema Institucional de Codificación Documental (SICD-MIPSP). Continúa además con el contenido técnico que corresponda. 

Excelente. Considero que esta decisión marca un punto de inflexión en el proyecto.

Desde la perspectiva de un diseñador de sistemas documentales, el problema más frecuente que presentan los manuales de capacitación es que, con el paso del tiempo, se vuelven inmanejables. Se agregan cursos, formatos, procedimientos y versiones sin una estructura uniforme, lo que dificulta la actualización y la trazabilidad.

Si nuestro objetivo es construir una colección que pueda mantenerse vigente durante muchos años, el **Sistema Institucional de Codificación Documental del MIPSP (SICD-MIPSP)** debe convertirse en la "infraestructura invisible" que sostenga todo el proyecto.

Mi recomendación es diseñarlo con criterios similares a los utilizados en sistemas de gestión documental de organizaciones complejas, de modo que cualquier documento pueda identificarse, localizarse, relacionarse y versionarse sin ambigüedad.

---

# TOMO VI

# SISTEMA INSTITUCIONAL DE CODIFICACIÓN DOCUMENTAL

## SICD-MIPSP

**Versión:** 1.0 (Documento Maestro)

---

# CAPÍTULO I

# Filosofía del Sistema de Codificación

## 1.1 Propósito

El **Sistema Institucional de Codificación Documental (SICD-MIPSP)** es el conjunto de reglas que permiten identificar de manera única todos los activos documentales del Modelo Integral para la Profesionalización de la Seguridad Privada (MIPSP).

Su finalidad es garantizar:

* unicidad;
* trazabilidad;
* interoperabilidad;
* control de versiones;
* recuperación rápida;
* escalabilidad;
* auditoría documental;
* preservación histórica.

---

## 1.2 Principios del SICD-MIPSP

Todo identificador deberá cumplir ocho principios:

### P1. Unicidad

Cada código identifica un solo elemento documental.

Ejemplo:

```
CUR-OPS-001
```

Nunca podrá utilizarse para otro curso.

---

### P2. Permanencia

Una vez asignado, el código no se reutiliza, aunque el documento sea dado de baja.

---

### P3. Escalabilidad

El sistema permitirá crecer sin modificar la estructura existente.

Ejemplo:

```
CUR-OPS-001

CUR-OPS-245

CUR-OPS-1248
```

---

### P4. Legibilidad

El código deberá ser interpretable por un usuario capacitado.

---

### P5. Modularidad

Cada segmento tendrá un significado específico.

---

### P6. Compatibilidad

Será compatible con sistemas de calidad y gestión documental.

---

### P7. Independencia

El código no dependerá del nombre del documento.

---

### P8. Trazabilidad

Todo código podrá vincularse con:

* requisito legal;
* competencia;
* procedimiento;
* curso;
* sesión;
* evaluación;
* evidencia.

---

# CAPÍTULO II

# Arquitectura General

El código institucional estará compuesto por bloques.

```
TIPO

↓

FAMILIA

↓

SUBFAMILIA

↓

NÚMERO

↓

VERSIÓN

↓

ESTADO
```

Ejemplo:

```
CUR-OPS-001-V02-A
```

Interpretación:

Curso

↓

Operaciones

↓

Número 001

↓

Versión 2

↓

Aprobado

---

# CAPÍTULO III

# Catálogo Maestro de Prefijos

## 3.1 Documentos académicos

| Código | Documento                    |
| ------ | ---------------------------- |
| CUR    | Curso                        |
| PROG   | Programa                     |
| CD     | Carta Descriptiva            |
| GI     | Guía del Instructor          |
| MP     | Manual del Participante      |
| ETS    | Expediente Técnico de Sesión |
| PPT    | Presentación                 |
| CE     | Cuaderno de Ejercicios       |

---

## 3.2 Evaluación

| Código | Documento                 |
| ------ | ------------------------- |
| BR     | Banco de Reactivos        |
| EX     | Examen                    |
| LC     | Lista de Cotejo           |
| GO     | Guía de Observación       |
| RUB    | Rúbrica                   |
| EV     | Instrumento de Evaluación |
| PE     | Portafolio de Evidencias  |

---

## 3.3 Gestión Operativa

| Código | Documento                              |
| ------ | -------------------------------------- |
| PNO    | Procedimiento Normalizado de Operación |
| INS    | Instructivo                            |
| FRM    | Formato                                |
| REG    | Registro                               |
| BIT    | Bitácora                               |
| REP    | Reporte                                |
| KPI    | Indicador                              |

---

## 3.4 Competencias

| Código | Documento                       |
| ------ | ------------------------------- |
| COMP   | Competencia                     |
| UEC    | Unidad Elemental de Competencia |
| FARF   | Requisito Formativo             |
| MTI    | Matriz de Trazabilidad          |
| IRF    | Índice de Riesgo Formativo      |

---

## 3.5 Calidad

| Código | Documento         |
| ------ | ----------------- |
| AUD    | Auditoría         |
| AC     | Acción Correctiva |
| AP     | Acción Preventiva |
| MC     | Mejora Continua   |
| NC     | No Conformidad    |

---

# CAPÍTULO IV

# Familias documentales

## OPS

Operaciones.

---

## JUR

Marco Jurídico.

---

## ADM

Administración.

---

## SUP

Supervisión.

---

## COM

Comunicación.

---

## DOC

Gestión documental.

---

## RIE

Gestión del Riesgo.

---

## EVA

Evaluación.

---

## CAL

Calidad.

---

## INST

Instructores.

---

## TEC

Tecnología.

---

# CAPÍTULO V

# Reglas de numeración

Cada familia comenzará en:

```
001
```

Nunca se reutilizarán números.

Ejemplo:

```
CUR-OPS-001

CUR-OPS-002

CUR-OPS-003
```

Si un curso desaparece:

```
CUR-OPS-002

(BAJA)

El siguiente será:

CUR-OPS-004
```

Nunca vuelve a existir un nuevo CUR-OPS-002.

---

# CAPÍTULO VI

# Sistema de Versionado

Se propone el siguiente estándar:

| Código | Estado            |
| ------ | ----------------- |
| B      | Borrador          |
| RT     | Revisión técnica  |
| RJ     | Revisión jurídica |
| PI     | Piloto            |
| AP     | Aprobado          |
| VI     | Vigente           |
| OB     | Obsoleto          |
| HI     | Histórico         |

Ejemplo:

```
GI-OPS-001-V03-AP
```

Interpretación:

Guía del Instructor

↓

Curso Operaciones 001

↓

Versión 3

↓

Aprobada

---

# CAPÍTULO VII

# Relaciones documentales

Una de las fortalezas del SICD-MIPSP será la definición explícita de las relaciones entre documentos.

Ejemplo para **CUR-OPS-001**:

| Documento                         | Código              |
| --------------------------------- | ------------------- |
| Programa Institucional            | PROG-OPS-001        |
| Carta Descriptiva                 | CD-OPS-001          |
| Guía del Instructor               | GI-OPS-001          |
| Manual del Participante           | MP-OPS-001          |
| Expediente Técnico de Sesión 1    | ETS-OPS-001-M01-S01 |
| Presentación                      | PPT-OPS-001         |
| Cuaderno de Ejercicios            | CE-OPS-001          |
| Banco de Reactivos                | BR-OPS-001          |
| Examen Final                      | EX-OPS-001-F        |
| Rúbrica Principal                 | RUB-OPS-001         |
| Lista de Cotejo                   | LC-OPS-001          |
| Guía de Observación               | GO-OPS-001          |
| PNO asociado                      | PNO-OPS-001         |
| Formato de Registro de Visitantes | FRM-OPS-001-RV      |
| Bitácora                          | BIT-OPS-001         |
| Reporte de Incidencia             | REP-OPS-001         |
| Matriz de Trazabilidad            | MTI-OPS-001         |

---

# Integración con el CUR-OPS-001: Desarrollo del Documento 3

Con el SICD-MIPSP definido, el siguiente documento del paquete será el **GI-OPS-001**, la **Guía del Instructor**. Este documento ya no será una simple secuencia de actividades, sino un manual operativo para la impartición del curso. Su estructura incluirá:

1. Control documental y matriz de revisiones.
2. Perfil y competencias del instructor.
3. Preparación previa a la impartición (lista de verificación).
4. Guion metodológico por módulo y por sesión.
5. Estrategias de facilitación y manejo de grupos.
6. Preguntas detonadoras y respuestas esperadas.
7. Indicadores de desempeño del instructor.
8. Gestión de contingencias durante la capacitación.
9. Criterios para la retroalimentación efectiva.
10. Cierre del curso y elaboración del expediente de evidencias.
11. Anexos con listas de verificación, formatos y referencias cruzadas al ETS, la Carta Descriptiva y el Manual del Participante.

## Propuesta de fortalecimiento metodológico

A partir de esta fase sugiero incorporar una disciplina adicional propia de los sistemas de ingeniería: el **Control de Configuración Documental (CCD-MIPSP)**.

El SICD identifica y organiza los documentos; el CCD controlará sus cambios. Cada modificación quedará registrada con:

* identificador único del cambio;
* motivo (reforma legal, mejora pedagógica, hallazgo de auditoría, actualización operativa, etc.);
* documentos impactados;
* responsable de la modificación;
* fecha de entrada en vigor;
* evaluación del impacto en cursos, procedimientos, evaluaciones y materiales.

Esta capa adicional garantizará que toda la colección permanezca coherente a lo largo del tiempo y facilitará su mantenimiento frente a reformas normativas o cambios operativos. En organizaciones con sistemas maduros de gestión documental, esta práctica es un factor clave para asegurar la integridad y la confiabilidad del conocimiento institucional.
