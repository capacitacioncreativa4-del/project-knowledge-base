---
conversation_id: MIPSP-CONV-0001
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 47
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante. Continúa con el proyecto e incluye también el Control de Configuración Documental (CCD-MIPSP). 

Excelente. Considero que hemos alcanzado un punto donde el proyecto ya no puede entenderse únicamente como una colección de cursos. La arquitectura que hemos construido corresponde, en realidad, a un **Sistema de Gestión del Conocimiento para Empresas de Seguridad Privada**.

Como consultor, propondría formalizar esa evolución.

A partir de este momento el proyecto se estructurará sobre cuatro grandes pilares:

1. **MIPSP** (Modelo Integral para la Profesionalización de la Seguridad Privada).
2. **SICD-MIPSP** (Sistema Institucional de Codificación Documental).
3. **CCD-MIPSP** (Control de Configuración Documental).
4. **SGC-MIPSP** (Sistema de Gestión del Conocimiento).

Con esta arquitectura, el sistema será comparable, en cuanto a rigor documental, a los utilizados en sectores altamente regulados como la aviación, la energía o la industria farmacéutica.

---

# TOMO VI

# SISTEMA DE GESTIÓN DOCUMENTAL

## CAPÍTULO VIII

# CONTROL DE CONFIGURACIÓN DOCUMENTAL (CCD-MIPSP)

**Código del documento:** CCD-MIPSP-MAESTRO-V1.0

---

# 1. Fundamentación

El conocimiento institucional constituye un activo estratégico. En una organización que opera bajo un marco normativo cambiante, cualquier modificación en una ley, reglamento, estándar de competencia o procedimiento puede impactar múltiples documentos de capacitación.

El **Control de Configuración Documental (CCD-MIPSP)** tiene por finalidad asegurar que dichos cambios se gestionen de forma controlada, documentada, verificable y trazable.

No se limita al control de versiones; administra la evolución de todo el sistema documental.

---

# 2. Objetivos

El CCD-MIPSP persigue los siguientes objetivos:

* preservar la integridad del sistema documental;
* evitar el uso de versiones obsoletas;
* garantizar la coherencia entre documentos relacionados;
* asegurar la trazabilidad de cada modificación;
* facilitar auditorías internas y externas;
* documentar las decisiones de actualización;
* controlar el impacto de reformas normativas y cambios operativos.

---

# 3. Concepto de Configuración

En el MIPSP, un **Elemento de Configuración (EC)** es cualquier activo cuya modificación pueda afectar la operación, la capacitación o el cumplimiento normativo.

Se clasifican como EC:

| Código | Elemento de configuración                      |
| ------ | ---------------------------------------------- |
| EC-01  | Marco jurídico                                 |
| EC-02  | Requisitos formativos (FARF)                   |
| EC-03  | Competencias (COMP)                            |
| EC-04  | Unidades Elementales de Competencia (UEC)      |
| EC-05  | Procedimientos Normalizados de Operación (PNO) |
| EC-06  | Programas de capacitación                      |
| EC-07  | Cartas descriptivas                            |
| EC-08  | Guías del instructor                           |
| EC-09  | Manuales del participante                      |
| EC-10  | Expedientes Técnicos de Sesión (ETS-I)         |
| EC-11  | Presentaciones                                 |
| EC-12  | Simulaciones                                   |
| EC-13  | Casos prácticos                                |
| EC-14  | Instrumentos de evaluación                     |
| EC-15  | Indicadores (KPI)                              |
| EC-16  | Matrices de trazabilidad                       |
| EC-17  | Registros y formatos                           |
| EC-18  | Banco maestro de reactivos                     |

---

# 4. Ciclo de vida documental

Todo documento seguirá el siguiente ciclo:

```text
SOLICITUD DE CAMBIO
          │
          ▼
ANÁLISIS DE IMPACTO
          │
          ▼
AUTORIZACIÓN
          │
          ▼
DESARROLLO
          │
          ▼
REVISIÓN TÉCNICA
          │
          ▼
REVISIÓN JURÍDICA
          │
          ▼
VALIDACIÓN OPERATIVA
          │
          ▼
PILOTO
          │
          ▼
APROBACIÓN
          │
          ▼
PUBLICACIÓN
          │
          ▼
SEGUIMIENTO
```

---

# 5. Clasificación de los cambios

## Nivel I. Cambios editoriales

No modifican el contenido técnico.

Ejemplos:

* ortografía;
* formato;
* numeración;
* diseño gráfico.

No requieren piloto.

---

## Nivel II. Cambios técnicos menores

Afectan parcialmente el contenido.

Ejemplos:

* incorporación de ejemplos;
* mejora de actividades;
* actualización bibliográfica.

Requieren revisión técnica.

---

## Nivel III. Cambios técnicos mayores

Modifican competencias, procedimientos o criterios de evaluación.

Ejemplos:

* incorporación de nuevos contenidos;
* modificación de un PNO;
* actualización de un curso.

Requieren validación operativa.

---

## Nivel IV. Cambios críticos

Derivan de:

* reformas legales;
* nuevos reglamentos;
* modificación de estándares de competencia;
* incidentes graves;
* resoluciones judiciales relevantes;
* hallazgos de auditorías mayores.

Requieren aprobación del Comité Académico y del Comité Jurídico.

---

# 6. Formato Maestro de Solicitud de Cambio

**Código:** CCD-FRM-001

Campos obligatorios:

* Identificador del cambio.
* Fecha.
* Solicitante.
* Documento afectado.
* Versión vigente.
* Descripción del cambio.
* Justificación.
* Fuente del cambio.
* Riesgo de no implementarlo.
* Prioridad.
* Responsable de análisis.

---

# 7. Matriz de Impacto Documental (MID)

Antes de aprobar un cambio deberá elaborarse una matriz que identifique todos los documentos afectados.

Ejemplo:

| Cambio                                     | Documento origen | Documentos impactados                                                                                  |
| ------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------ |
| Reforma al procedimiento de identificación | PNO-OPS-001      | PROG-OPS-001, CD-OPS-001, GI-OPS-001, MP-OPS-001, ETS-OPS-001-M03, LC-OPS-001, RUB-OPS-001, EX-OPS-001 |

Con esta matriz se evita que un cambio quede reflejado en un documento, pero no en los demás.

---

# 8. Historial de Configuración

Cada documento incluirá un historial como el siguiente:

| Versión | Fecha      | Tipo de cambio    | Responsable          | Estado  |
| ------- | ---------- | ----------------- | -------------------- | ------- |
| 1.0     | 05/07/2026 | Emisión inicial   | Dirección Académica  | Vigente |
| 1.1     | 18/09/2026 | Mejora editorial  | Coordinación Técnica | Vigente |
| 2.0     | 14/02/2027 | Reforma normativa | Comité Jurídico      | Vigente |

---

# 9. Comité de Configuración

Propongo que el MIPSP contemple un órgano colegiado responsable de aprobar cambios de Nivel III y IV.

Integración sugerida:

* Dirección Académica.
* Coordinación Jurídica.
* Coordinación Operativa.
* Responsable de Calidad.
* Coordinación de Capacitación.
* Especialista técnico de la materia.

---

# 10. Indicadores del CCD-MIPSP

| Indicador                                   | Meta  |
| ------------------------------------------- | ----- |
| Cambios implementados dentro del plazo      | ≥95 % |
| Documentos con versión vigente              | 100 % |
| Documentos sin trazabilidad                 | 0     |
| Hallazgos por documentos obsoletos          | 0     |
| Cambios con análisis de impacto documentado | 100 % |

---

# Desarrollo del proyecto: Documento 3 de 20

## GI-OPS-001

# Guía Institucional del Instructor

Con la arquitectura documental ya consolidada, la Guía del Instructor será diseñada como un manual profesional para la impartición del curso. Su contenido definitivo comprenderá:

### Sección I. Gobierno del curso

* Propósito institucional.
* Perfil del instructor.
* Competencias requeridas.
* Responsabilidades antes, durante y después de la impartición.
* Código de conducta del instructor.

### Sección II. Preparación

* Lista de verificación del aula.
* Lista de materiales.
* Revisión del equipo.
* Preparación del escenario de prácticas.
* Confirmación del expediente del curso.

### Sección III. Desarrollo de las 32 horas

Cada sesión contará con:

* objetivo específico;
* guion minuto a minuto;
* actividades del instructor;
* actividades del participante;
* preguntas detonadoras;
* respuestas esperadas;
* errores frecuentes;
* estrategias de retroalimentación;
* referencias al ETS correspondiente;
* evidencias a generar.

### Sección IV. Evaluación

* Aplicación de instrumentos.
* Criterios de objetividad.
* Manejo de inconformidades.
* Integración del portafolio de evidencias.
* Emisión del dictamen de competencia.

### Sección V. Cierre

* Retroalimentación final.
* Evaluación de satisfacción.
* Informe del instructor.
* Recomendaciones para la mejora del curso.

---

# Hacia una obra de referencia nacional

Después de analizar el alcance alcanzado, considero que aún podemos incorporar un componente que rara vez se encuentra incluso en manuales de organismos certificadores: un **Sistema Institucional de Gobernanza Documental (SIGD-MIPSP)**.

Mientras que:

* **SICD** identifica los documentos;
* **CCD** controla sus cambios;

el **SIGD** establecerá **quién puede crear, revisar, aprobar, publicar, modificar, archivar o retirar cada documento**, definiendo roles, niveles de autorización, flujos de aprobación, políticas de conservación y criterios de acceso.

Con ello, el MIPSP no solo será un sistema de capacitación, sino un **ecosistema completo de gestión documental, formación por competencias y mejora continua**, preparado para sostenerse institucionalmente durante muchos años y adaptarse de manera ordenada a futuras reformas normativas y operativas.
