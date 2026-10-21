---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalized
type: Source
file_reference: MIPSP-CONV-0001-P09.md
source_part: 9
source_sha256: 06B6F77316CDAD11961694C7C870DE5BFC093E56282D29AD40D959FCCC27D3D3
---

# Fuente Normalizada — MIPSP-CONV-0001-P09

## Referencia y procedencia

Esta fuente normalizada deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P09.md`.
La fuente original y el borrador aprobado permanecen intactos.

## 1. Sistema Integral de Gestión del Conocimiento Operativo

### SIGCO_ESP

- Tipo: `SISTEMA_CONCEPTUAL_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Propósito: identificar, organizar, desarrollar, evaluar y actualizar competencias profesionales del personal operativo, vinculando marco jurídico, procesos, capacitación y evidencias.
- Resultado buscado: transformar el cumplimiento normativo en desarrollo, mejora continua y gestión del conocimiento.

El nombre SIGCO-ESP y su definición se conservan como propuesta; no demuestran la existencia de un sistema institucional.

## 2. Arquitectura general de nueve capas

### CAPAS_SIGCO_ESP

1. Misión Institucional.
2. Marco Jurídico.
3. Procedimientos Normalizados de Operación (PNO).
4. Procesos Operativos.
5. Mapa Maestro de Competencias.
6. Sistema de Capacitación.
7. Evaluación y Certificación.
8. Indicadores y Mejora Continua.
9. Gobierno del Conocimiento.

La capacitación se ubica como medio para desarrollar competencias requeridas por procesos y marco jurídico. Las capas son una propuesta de arquitectura.

## 3. Mapa Maestro de Procesos Operativos

### MMPO

- Tipo: `MAPA_DE_PROCESOS_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Función: organizar la capacitación alrededor de procesos operativos y no solo de cursos.
- Nivel estratégico: Dirección, Planeación, Cumplimiento Legal, Gestión de Riesgos y Gestión del Talento.

### PROCESOS_OPERATIVOS_PROPUESTOS

La fuente enumera: P-01 Control de accesos; P-02 Control vehicular; P-03 Recepción de visitantes; P-04 Registro de incidencias; P-05 Rondines; P-06 Protección de instalaciones; P-07 Monitoreo; P-08 Atención de emergencias; P-09 Primeros auxilios; P-10 Prevención y combate de incendios; P-11 Radiocomunicación; P-12 Manejo de conflictos; P-13 Custodia de bienes; P-14 Protección de personas; P-15 Control documental; P-16 Entrega-recepción de turno; P-17 Elaboración de informes; P-18 Atención al cliente; P-19 Protección civil; y P-20 Uso de tecnología.

Los códigos P-01 a P-20 son identificadores internos de ejemplo/propuesta y no se registran como IDs institucionales.

## 4. Descomposición de procesos

### SUBPROCESOS_CONTROL_ACCESOS

Para P-01 se proponen control peatonal, control vehicular, control de materiales, control documental, control de visitantes, control de contratistas y control de proveedores.

Cada subproceso podría generar competencias, procedimientos, listas de verificación y evidencias. Es una propuesta de diseño, no un inventario validado.

### MATRIZ_DESCOMPOSICION_FUNCIONAL

- Tipo: `MATRIZ_DE_DISEÑO_PROPUESTA`.
- Estado: `Validated-As-Proposal`.
- Campos: proceso, subproceso, función, tarea, competencia, evidencia y curso.
- Uso: enlazar operación diaria con formación y evaluación.

Los ejemplos `COMP-001`, `COMP-002`, `COMP-003` y `CUR-04` permanecen como ejemplos editoriales y no se crean como IDs.

## 5. Cadena de Valor de la Competencia Operativa

### CVCO

- Tipo: `MODELO_DE_GESTION_PROPUESTO`.
- Estado: `Validated-As-Proposal`.
- Cadena: `Requisito normativo → Competencia requerida → Diseño curricular → Capacitación → Evaluación → Aplicación en el servicio → Supervisión → Retroalimentación → Actualización → Mejora continua`.
- Finalidad: integrar la capacitación con la gestión operativa y evitar que sea un evento aislado.

## 6. Propuesta de análisis jurídico exhaustivo

### CAPITULO_6_ANALISIS_JURIDICO_SISTEMICO

- Tipo: `PROPUESTA_DE_TRABAJO`.
- Estado: `Validated-As-Proposal`.
- Enfoque: ingeniería inversa de la normatividad, no resumen general de leyes.

Pasos propuestos: identificar cada disposición relevante; clasificarla; extraer competencias; descomponerlas en conocimientos, habilidades, actitudes, evidencias y criterios; asignarlas a procesos, cursos y rutas; y registrarlas en la Matriz Maestra de Trazabilidad.

La fuente propone iniciar con el Inventario Normativo Integral y la Matriz Maestra de Obligaciones Formativas. Esta fuente no realiza ese análisis ni crea esas matrices.

## 7. Ajuste metodológico

Se propone trabajar exclusivamente con productos verificables, comenzando por el inventario normativo y la matriz de obligaciones, con citas precisas de legislación federal, estatal, reglamentos y EC0060. Es una recomendación futura, no evidencia de ejecución.

## 8. Elementos excluidos

- No se confirma la vigencia, interpretación o suficiencia jurídica de las normas mencionadas.
- No se crea SIGCO-ESP, MMPO, CVCO ni la Matriz de Descomposición como sistema o registro institucional.
- No se registran P-01 a P-20, COMP-001 a COMP-003 ni CUR-04 como IDs.
- No se realiza extracción artículo por artículo.
- No se crean INI, MOF, Matriz de Trazabilidad ni cursos definitivos.
- No se convierten procesos, subprocesos o ejemplos en procedimientos autorizados.
- No se crean requisitos, ADR, estándares, documentos editoriales ni Knowledge Objects.

## 9. Estado de normalización

| Elemento | Estado |
|---|---|
| Fuente P09 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 9 |
| Normalización | Normalized |
| Revisión humana P09 | Aprobada |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |

La aprobación no convierte las propuestas en estándares, requisitos, decisiones u objetos institucionales.
