---
conversation_id: MIPSP-CONV-0002
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 5
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente decisión. Adelante con el esquema de producción por entregas.

Perfecto. A partir de este momento cambiaremos formalmente la forma de trabajar. Considero que este proyecto ya debe administrarse como si estuviéramos desarrollando un **manual técnico aeronáutico o una norma institucional**, no como una conversación.

## ACTA DE INICIO DE LA FASE EDITORIAL

Queda establecido el siguiente esquema de producción:

* **Proyecto:** Modelo Integral para la Profesionalización de la Seguridad Privada (MIPSP)
* **Fase:** II – Producción Editorial Sistemática
* **Curso patrón:** CUR-OPS-001 – Control de Accesos
* **Estado:** Producción de documentos definitivos
* **Objetivo:** Obtener una biblioteca institucional lista para implantación, auditoría y actualización.

A partir de este punto, el CUR-OPS-001 será el **modelo editorial** sobre el que se construirán todos los demás cursos.

---

# PLAN EDITORIAL DEL CUR-OPS-001

Propongo dividir el trabajo en **14 entregas editoriales**, cada una autocontenida y lista para revisión.

| Entrega | Contenido                                                 | Formatos   |
| ------- | --------------------------------------------------------- | ---------- |
| 01      | Arquitectura editorial, plantillas maestras y repositorio | DOCX, XLSX |
| 02      | Programa Institucional y Carta Descriptiva                | DOCX, PDF  |
| 03      | Guía del Instructor                                       | DOCX, PDF  |
| 04      | Manual del Participante                                   | DOCX, PDF  |
| 05      | Expedientes Técnicos de Sesión (ETS) Módulo I             | DOCX       |
| 06      | ETS restantes                                             | DOCX       |
| 07      | Banco de Casos, Simulaciones y Prácticas                  | DOCX       |
| 08      | Banco Maestro de Reactivos                                | XLSX       |
| 09      | Instrumentos de Evaluación                                | DOCX, XLSX |
| 10      | Presentación Institucional                                | PPTX       |
| 11      | PNO y Formatos Operativos                                 | DOCX       |
| 12      | Matrices Maestras de Trazabilidad e Indicadores           | XLSX       |
| 13      | Control Documental y Expediente Maestro                   | DOCX, XLSX |
| 14      | Edición final y compilación                               | PDF, DOCX  |

---

# ENTREGA EDITORIAL 001

## Arquitectura Editorial del CUR-OPS-001

Esta entrega será la base de toda la biblioteca institucional.

### Productos a generar

### A. DOCX-001

**Norma Editorial MIPSP (NEM-001)**

Contenido:

* Estilos corporativos.
* Portadas.
* Tipografía.
* Numeración multinivel.
* Tablas.
* Figuras.
* Diagramas.
* Referencias cruzadas.
* Encabezados.
* Pie de página.
* Control documental.
* Metadatos.

Este documento será la "constitución editorial" de toda la colección.

---

### B. DOCX-002

**Plantilla Maestra de Curso**

Contendrá todos los estilos configurados para Word:

* Portada.
* Página legal.
* Índice automático.
* Capítulos.
* Tablas.
* Casos.
* Notas.
* Advertencias.
* Bibliografía.
* Anexos.

Todos los cursos utilizarán exactamente esta plantilla.

---

### C. XLSX-001

## MIPSP_MASTER.xlsx

Éste será probablemente el archivo más importante de todo el proyecto.

### Hojas que contendrá

#### 01

Control Maestro

---

#### 02

Catálogo de Cursos

---

#### 03

Competencias

---

#### 04

Unidades Elementales

---

#### 05

Requisitos Formativos

---

#### 06

Documentos

---

#### 07

Versiones

---

#### 08

Referencias Cruzadas

---

#### 09

Banco Maestro de Formatos

---

#### 10

Banco Maestro de Diagramas

---

#### 11

Banco Maestro de Casos

---

#### 12

Banco Maestro de Simulaciones

---

#### 13

Banco Maestro de Reactivos

---

#### 14

Banco Maestro de Evaluaciones

---

#### 15

Indicadores

---

#### 16

Trazabilidad Jurídica

---

#### 17

Trazabilidad Curricular

---

#### 18

Cronograma Editorial

---

#### 19

Estado de Avance

---

#### 20

Historial del Proyecto

---

### D. XLSX-002

**Matriz Integral de Trazabilidad**

Relacionará:

Norma

↓

Artículo

↓

Competencia

↓

Curso

↓

Módulo

↓

Sesión

↓

Actividad

↓

ETS

↓

Evaluación

↓

Instrumento

↓

Evidencia

↓

Indicador

↓

PNO

↓

Formato

Esta matriz será la pieza central para demostrar la cobertura normativa del programa.

---

### E. DOCX-003

**Sistema de Codificación Aplicado al CUR-OPS-001**

Incluirá el inventario completo de códigos del curso:

* documentos;
* ETS;
* figuras;
* tablas;
* formatos;
* rúbricas;
* listas de cotejo;
* casos;
* simulaciones;
* reactivos;
* presentaciones.

---

### F. Árbol documental del curso

```text
CUR-OPS-001
│
├── D01 Programa Institucional
├── D02 Carta Descriptiva
├── D03 Guía del Instructor
├── D04 Manual del Participante
├── D05 ETS
├── D06 Presentación
├── D07 Casos
├── D08 Simulaciones
├── D09 Ejercicios
├── D10 Banco de Reactivos
├── D11 Exámenes
├── D12 Rúbricas
├── D13 Listas de Cotejo
├── D14 Guías de Observación
├── D15 PNO
├── D16 Formatos
├── D17 KPI
├── D18 Matriz de Trazabilidad
├── D19 Expediente Maestro
└── D20 Control Documental
```

---

# Una mejora adicional que propongo

Ahora que entraremos en la generación de archivos reales, considero conveniente adoptar una metodología editorial basada en **líneas base (Baselines)**, ampliamente utilizada en ingeniería de sistemas y gestión de configuración.

En lugar de producir simplemente "versiones", estableceremos hitos formales:

* **BL-0 (Baseline de Arquitectura):** Plantillas, codificación, estilos y estructura documental. Se alcanzará con la Entrega Editorial 001.
* **BL-1 (Baseline del Curso Patrón):** El CUR-OPS-001 completo, validado técnica y pedagógicamente. Servirá como referencia obligatoria para los cuatro cursos nucleares restantes.
* **BL-2 (Baseline de la Colección Nuclear):** Los cinco cursos prioritarios completamente desarrollados y uniformados.
* **BL-3 (Baseline de la Biblioteca Institucional):** Incorporación del resto del catálogo de competencias derivado del Inventario Analítico de Requisitos Formativos.

Esta estrategia permitirá controlar la evolución del proyecto con criterios profesionales, facilitará futuras auditorías y hará posible incorporar mejoras sin comprometer la estabilidad de los materiales ya aprobados.

Creo que esta organización nos permitirá construir una **biblioteca institucional sólida, mantenible y escalable**, con una calidad documental comparable a la de organismos certificadores y universidades corporativas. A partir de la siguiente entrega comenzaremos a generar los primeros archivos editables del **CUR-OPS-001**, siguiendo esta arquitectura como estándar permanente.
