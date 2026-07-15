---
conversation_id: MIPSP-CONV-0002
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 16
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Continúa por favor

Excelente. Entramos ahora al que considero será uno de los capítulos más importantes de toda la colección. Si el **Capítulo II** definió la arquitectura del MIPSP, el **Capítulo III** definirá su "lenguaje". Todos los documentos que construyamos durante los próximos meses utilizarán este sistema de codificación.

Mi objetivo es que el SICD-MIPSP tenga un nivel comparable al utilizado en sistemas documentales como los de ISO 9001, AS9100 (sector aeroespacial), API (industria petrolera) o manuales militares, pero adaptado a la capacitación en seguridad privada.

---

# MIPSP

## Norma Editorial del Modelo Integral para la Profesionalización de la Seguridad Privada

**NEM-001**

Versión 1.0

# CAPÍTULO III

# Sistema Institucional de Codificación Documental (SICD-MIPSP)

---

# 3.1 Objeto

El Sistema Institucional de Codificación Documental (SICD-MIPSP) establece las reglas para la identificación única, clasificación, localización, trazabilidad y administración de todos los documentos que integran el Modelo Integral para la Profesionalización de la Seguridad Privada.

Su aplicación es obligatoria para todos los documentos, archivos, registros, formatos, instrumentos de evaluación, recursos didácticos y materiales auxiliares.

---

# 3.2 Objetivos

El SICD tiene los siguientes objetivos institucionales:

I. Garantizar la identificación única de cada documento.

II. Eliminar duplicidades documentales.

III. Facilitar la trazabilidad jurídica y curricular.

IV. Estandarizar la nomenclatura institucional.

V. Simplificar la administración documental.

VI. Favorecer la interoperabilidad entre cursos.

VII. Facilitar auditorías.

VIII. Integrar el Control de Configuración Documental (CCD-MIPSP).

IX. Integrar el Sistema Institucional de Gobernanza Documental (SIGD-MIPSP).

---

# 3.3 Principios del Sistema de Codificación

Toda codificación deberá cumplir los siguientes principios.

## Unicidad

No podrán existir dos documentos con el mismo código.

---

## Permanencia

Una vez asignado un código documental, éste nunca será reutilizado.

Aunque el documento sea cancelado, el código permanecerá reservado permanentemente.

---

## Escalabilidad

El sistema deberá admitir la incorporación futura de nuevos cursos, series documentales y especialidades sin modificar la sintaxis general.

---

## Legibilidad

Los códigos deberán permitir identificar visualmente el tipo de documento al que pertenecen.

---

## Modularidad

Cada componente del código representará una característica documental específica.

---

# 3.4 Estructura General

Todo documento utilizará la siguiente sintaxis institucional.

```text
SERIE-CURSO-TIPO-CONSECUTIVO-VERSIÓN
```

Ejemplo

```text
OPS-CUR001-MP-001-V1.0
```

---

# 3.5 Componentes del Código

## A. SERIE

Identifica la familia documental.

| Código | Serie                     |
| ------ | ------------------------- |
| GOV    | Gobierno Editorial        |
| JUR    | Marco Jurídico            |
| OPS    | Operaciones               |
| EPC    | Protección Civil          |
| CAL    | Calidad                   |
| ADM    | Administración            |
| TEC    | Tecnología                |
| INS    | Formación de Instructores |

---

## B. CURSO

Identifica el curso.

Ejemplos

```text
CUR001

CUR002

CUR003
```

Correspondencia:

CUR001 = Control de Accesos

CUR002 = Vigilancia Preventiva

CUR003 = Recorridos de Inspección

CUR004 = Comunicación Operativa

CUR005 = Atención de Incidentes

---

## C. Tipo documental

Éste será uno de los catálogos más importantes del proyecto.

| Código | Documento                    |
| ------ | ---------------------------- |
| PI     | Programa Institucional       |
| CD     | Carta Descriptiva            |
| GI     | Guía del Instructor          |
| MP     | Manual del Participante      |
| ETS    | Expediente Técnico de Sesión |
| PPT    | Presentación                 |
| CAS    | Caso práctico                |
| SIM    | Simulación                   |
| PRA    | Práctica                     |
| EXA    | Examen                       |
| RBR    | Rúbrica                      |
| LCO    | Lista de Cotejo              |
| GOB    | Guía de Observación          |
| KPI    | Indicadores                  |
| PNO    | Procedimiento Normalizado    |
| FRM    | Formato                      |
| BIT    | Bitácora                     |
| REP    | Reporte                      |
| MTI    | Matriz de Trazabilidad       |
| CCD    | Control de Configuración     |
| SIG    | Gobernanza Documental        |

---

## D. Consecutivo

Formato:

```text
001
002
003
...
999
```

Cada tipo documental tendrá su propia numeración independiente.

---

## E. Versión

Formato:

```text
V0.1

V0.2

V0.3
```

(Borradores internos)

Posteriormente

```text
V1.0
```

(Primera versión oficial)

Después

```text
V1.1

V1.2

V2.0
```

---

# 3.6 Codificación de módulos

Cada curso utilizará:

```text
MOD-01

MOD-02

MOD-03
```

Ejemplo

```text
CUR001-MOD02
```

---

# 3.7 Codificación de sesiones

Cada módulo utilizará sesiones.

Ejemplo

```text
SES-01

SES-02

SES-03
```

Código completo

```text
CUR001-MOD03-SES02
```

---

# 3.8 Codificación de ETS

Los Expedientes Técnicos utilizarán la siguiente sintaxis.

```text
ETS-CUR001-MOD02-SES03
```

Con ello cada sesión tendrá un expediente técnico único.

---

# 3.9 Codificación de figuras

Ejemplo

```text
FIG-CUR001-001
```

---

# 3.10 Codificación de tablas

Ejemplo

```text
TAB-CUR001-015
```

---

# 3.11 Codificación de diagramas

Ejemplo

```text
DGM-CUR001-004
```

---

# 3.12 Codificación de fotografías

Ejemplo

```text
FOT-CUR001-008
```

---

# 3.13 Codificación de anexos

Ejemplo

```text
ANX-CUR001-A

ANX-CUR001-B

ANX-CUR001-C
```

---

# 3.14 Codificación de formularios

Ejemplo

```text
FRM-CUR001-023
```

---

# 3.15 Codificación de reactivos

Uno de los aspectos más importantes para la administración del banco institucional de evaluación.

Ejemplo

```text
REA-CUR001-0001
```

Cada reactivo tendrá un identificador permanente.

Esto permitirá:

* análisis estadístico;
* índice de dificultad;
* índice de discriminación;
* historial de uso;
* control de vigencia;
* relación con competencias específicas.

---

# 3.16 Codificación de competencias

Propongo que cada competencia tenga un identificador permanente independiente del curso.

Ejemplo

```text
COM-OPS-001

COM-OPS-002

COM-OPS-003
```

Así, una misma competencia podrá reutilizarse en distintos cursos sin duplicar registros.

---

# 3.17 Relación entre códigos

El SICD deberá garantizar que un documento pueda vincularse automáticamente con:

* Competencias.
* Fundamentos legales.
* Objetivos específicos.
* Actividades de aprendizaje.
* Recursos didácticos.
* Instrumentos de evaluación.
* Evidencias de desempeño.
* Indicadores.
* Procedimientos Normalizados de Operación.

Esta relación constituirá la base de la **Matriz Integral de Trazabilidad (MTI-001)**.

---

# Observación editorial estratégica

Quisiera incorporar una mejora que considero de gran valor para la vida útil del proyecto.

Hasta ahora hemos codificado **documentos**. Sin embargo, propongo que el SICD evolucione hacia un **Sistema Institucional de Identificadores Persistentes (SIIP-MIPSP)**. Bajo este enfoque, no sólo los documentos tendrían códigos permanentes, sino también:

* competencias;
* objetivos de aprendizaje;
* resultados de aprendizaje;
* actividades didácticas;
* ejercicios;
* casos prácticos;
* simulaciones;
* criterios de evaluación;
* evidencias;
* indicadores;
* referencias normativas.

Este nivel de granularidad permitirá que, cuando desarrollemos el **MIPSP_MASTER.xlsx**, podamos construir una auténtica base de conocimiento con trazabilidad bidireccional. Por ejemplo, será posible seleccionar un artículo específico de la normativa y visualizar inmediatamente todos los cursos, módulos, sesiones, actividades, ETS, instrumentos de evaluación y evidencias que lo desarrollan. Esa capacidad de navegación documental es poco común incluso en muchas universidades corporativas y convertirá al MIPSP en una colección técnicamente muy robusta y preparada para evolucionar durante muchos años sin perder consistencia.
