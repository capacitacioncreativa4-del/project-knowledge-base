---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalization-Draft
type: Source
file_reference: MIPSP-CONV-0001-P08.md
source_part: 8
source_sha256: 4BCA5DD91FFDD1F40F51C3E3FD4C36018BDF9787BFDE8AB4A7C9F9ECC59B1402
---

# Borrador de Fuente Normalizada — MIPSP-CONV-0001-P08

## Referencia y procedencia

Este borrador deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P08.md`.

La fuente original permanece intacta. Este documento no constituye una arquitectura institucional aprobada, análisis jurídico, registro de matrices ni autorización para crear IDs, Knowledge Objects, requisitos, ADR, estándares o documentos editoriales.

## 1. Reestructuración propuesta del Tomo I

### ESTRUCTURA_TOMO_I_FUNDAMENTOS_E_INGENIERIA

- Tipo: `ARQUITECTURA_DOCUMENTAL_PROPUESTA`.
- Estado: `Candidate`.
- Parte I: Fundamentos, capítulos 1 a 4.
- Parte II: Ingeniería Curricular, organizada mediante diez matrices técnicas.

La propuesta prioriza matrices de ingeniería sobre capítulos narrativos para demostrar cumplimiento y administrar el sistema de formación.

## 2. Diez matrices maestras propuestas

### INI — Inventario Normativo Integral

Tipo: `MATRIZ_DE_INVENTARIO`; estado: `Candidate`.

Inventariar disposiciones relacionadas con capacitación, con código, fuente, artículo o elemento, tema, indicador de generación de capacitación y observaciones. Se propone como índice técnico del proyecto.

### MOF — Matriz de Obligaciones Formativas

Tipo: `MATRIZ_DE_EXTRACCION`; estado: `Candidate`.

Representar cada obligación legal en una fila para evitar pérdidas durante el análisis.

### MATRIZ_DE_COMPETENCIAS

Tipo: `MATRIZ_COMPETENCIAL`; estado: `Candidate`.

Registrar las competencias estimadas con código, definición, tipo, nivel, criticidad, modalidad y evaluación. La cantidad de 175–230 procede de una estimación anterior y no es un resultado confirmado.

### MATRIZ_DE_CONOCIMIENTOS

Tipo: `MATRIZ_COMPETENCIAL`; estado: `Candidate`.

Separar conocimientos requeridos, como identificación oficial, gafetes, listas de acceso, autorizaciones y protocolos.

### MATRIZ_DE_HABILIDADES

Tipo: `MATRIZ_COMPETENCIAL`; estado: `Candidate`.

Registrar habilidades como verificar documentos, operar radios, observar, reportar y controlar vehículos.

### MATRIZ_DE_ACTITUDES

Tipo: `MATRIZ_COMPETENCIAL`; estado: `Candidate`.

Registrar disciplina, autocontrol, lealtad, confidencialidad, servicio, respeto y ética.

### MATRIZ_DE_RIESGOS

Tipo: `MATRIZ_DE_RIESGO`; estado: `Candidate`.

Asociar cada competencia con riesgos derivados de su ausencia o desempeño deficiente, incluyendo accesos indebidos, robo, sabotaje, accidentes, responsabilidad administrativa e incumplimiento contractual.

### MATRIZ_DE_CRITICIDAD

Tipo: `MODELO_MULTICRITERIO`; estado: `Candidate`.

Evaluar competencias mediante riesgo operativo, jurídico y reputacional para obtener una criticidad global y justificar prioridades de capacitación. La escala y sus umbrales requieren definición posterior.

### MATRIZ_DE_TRAZABILIDAD

Tipo: `MODELO_TRAZABILIDAD`; estado: `Candidate`.

Cadena propuesta: `Artículo → Competencia → Curso → Unidad → Sesión → Práctica → Evaluación → Evidencia → Expediente`.

Su finalidad es demostrar la traducción de cada obligación normativa dentro del sistema formativo.

### MATRIZ_CURRICULAR

Tipo: `ESTRUCTURA_CURRICULAR`; estado: `Candidate`.

Organizar las competencias en cursos y funcionar como resultado integrador de las matrices anteriores.

## 3. Mapa de Procesos Operativos

### MAPA_PROCESOS_OPERATIVOS

- Tipo: `MODELO_PROCESOS_PROPUESTO`.
- Estado: `Candidate`.
- Propuesta: construir el sistema curricular sobre procesos operativos y no únicamente sobre una lista de temas.
- Cadena: `Procesos Operativos → Funciones → Competencias → Procedimientos → Tareas → Conocimientos → Habilidades → Evaluación`.

El mapa permitiría asociar artículos con procesos como control de accesos, rondines, emergencias, protección de instalaciones, comunicación operativa y elaboración de informes. No constituye todavía un mapa institucional aprobado.

## 4. Sistema Integral de Gestión del Conocimiento Operativo

### SIGCO

- Tipo: `SISTEMA_CONCEPTUAL_PROPUESTO`.
- Estado: `Candidate`.
- Propósito propuesto: integrar capacitación, procesos operativos, procedimientos normalizados de operación, evaluación del desempeño y mejora continua.

La fuente presenta SIGCO como una evolución del catálogo de cursos hacia un sistema de gestión del conocimiento operativo. La afirmación es conceptual y no demuestra existencia, alcance o implementación.

## 5. Recomendación de continuidad

Antes de extraer competencias de los ordenamientos jurídicos, se propone diseñar un Mapa Maestro de Procesos Operativos del Personal de Seguridad Privada. Este mapa serviría para asociar cada artículo con un proceso específico y facilitar la construcción de matrices posteriores y del Tomo II.

La recomendación es una decisión editorial/metodológica propuesta y no extracción jurídica realizada.

## 6. Elementos excluidos

- No se realiza el inventario normativo ni el análisis de artículos.
- No se crean las diez matrices como registros definitivos.
- No se convierten INI, MOF, SIGCO o el mapa de procesos en objetos institucionales.
- No se confirma la cobertura jurídica ni la suficiencia de las fuentes mencionadas.
- No se convierten las estimaciones de competencias en inventario.
- No se definen escalas de criticidad, cargas horarias, cursos, PNO o expedientes.
- No se crean códigos de competencias; cualquier código ilustrativo permanece como ejemplo.
- No se crean requisitos, ADR, estándares, documentos editoriales ni Knowledge Objects.

## 7. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P08 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 8 |
| Normalización | Borrador |
| Revisión humana P08 | Pendiente |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | No realizada |

## Criterio para cerrar el borrador

La revisión humana deberá confirmar la estructura de las diez matrices, la distinción entre inventario y extracción, el carácter propuesto del mapa de procesos y SIGCO, la criticidad multicriterio, el uso de estimaciones y la ausencia de promoción prematura.

# FIN DEL BORRADOR DE NORMALIZACIÓN P08
