---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalization-Draft
type: Source
file_reference: MIPSP-CONV-0001-P09.md
source_part: 9
source_sha256: 06B6F77316CDAD11961694C7C870DE5BFC093E56282D29AD40D959FCCC27D3D3
---

# Borrador de Fuente Normalizada — MIPSP-CONV-0001-P09

## Referencia y procedencia

Este borrador deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P09.md`.

La fuente original permanece intacta. Este documento no constituye arquitectura institucional aprobada, análisis jurídico, inventario operativo definitivo ni autorización para crear IDs, Knowledge Objects, requisitos, ADR, estándares o documentos editoriales.

## 1. Sistema Integral de Gestión del Conocimiento Operativo

### SIGCO_ESP

- Tipo: `SISTEMA_CONCEPTUAL_PROPUESTO`.
- Estado: `Candidate`.
- Propósito: identificar, organizar, desarrollar, evaluar y actualizar competencias profesionales del personal operativo, vinculando marco jurídico, procesos, capacitación y evidencias.
- Resultado buscado: transformar el cumplimiento normativo en un sistema permanente de desarrollo, mejora continua y gestión del conocimiento.

El nombre SIGCO-ESP y su definición se conservan como propuesta de la conversación; no demuestran la existencia de un sistema institucional.

## 2. Arquitectura general de nueve capas

### CAPAS_SIGCO_ESP

Tipo: `ARQUITECTURA_CONCEPTUAL_PROPUESTA`; estado: `Candidate`.

1. Misión Institucional.
2. Marco Jurídico.
3. Procedimientos Normalizados de Operación (PNO).
4. Procesos Operativos.
5. Mapa Maestro de Competencias.
6. Sistema de Capacitación.
7. Evaluación y Certificación.
8. Indicadores y Mejora Continua.
9. Gobierno del Conocimiento.

La capacitación se ubica como medio para desarrollar competencias requeridas por procesos y marco jurídico, no como fin aislado. Las capas son una propuesta de arquitectura.

## 3. Mapa Maestro de Procesos Operativos

### MMPO

- Tipo: `MAPA_DE_PROCESOS_PROPUESTO`.
- Estado: `Candidate`.
- Función: organizar la capacitación alrededor de procesos operativos y no solo de cursos.
- Nivel estratégico: Dirección, Planeación, Cumplimiento Legal, Gestión de Riesgos y Gestión del Talento.

### PROCESOS_OPERATIVOS_PROPUESTOS

La fuente enumera: P-01 Control de accesos; P-02 Control vehicular; P-03 Recepción de visitantes; P-04 Registro de incidencias; P-05 Rondines; P-06 Protección de instalaciones; P-07 Monitoreo; P-08 Atención de emergencias; P-09 Primeros auxilios; P-10 Prevención y combate de incendios; P-11 Radiocomunicación; P-12 Manejo de conflictos; P-13 Custodia de bienes; P-14 Protección de personas; P-15 Control documental; P-16 Entrega-recepción de turno; P-17 Elaboración de informes; P-18 Atención al cliente; P-19 Protección civil; y P-20 Uso de tecnología.

Los códigos P-01 a P-20 son identificadores internos de ejemplo/propuesta y no se registran como IDs institucionales.

## 4. Descomposición de procesos

### SUBPROCESOS_CONTROL_ACCESOS

Para P-01 se proponen subprocesos de control peatonal, control vehicular, control de materiales, control documental, control de visitantes, control de contratistas y control de proveedores.

Cada subproceso podría generar competencias específicas, procedimientos, listas de verificación y evidencias. La relación es una propuesta de diseño, no un inventario validado.

### MATRIZ_DESCOMPOSICION_FUNCIONAL

- Tipo: `MATRIZ_DE_DISEÑO_PROPUESTA`.
- Estado: `Candidate`.
- Campos: proceso, subproceso, función, tarea, competencia, evidencia y curso.
- Uso: enlazar operación diaria con formación y evaluación.

Los ejemplos `COMP-001`, `COMP-002`, `COMP-003` y `CUR-04` se conservan solo como ejemplos editoriales y no se crean como IDs.

## 5. Cadena de Valor de la Competencia Operativa

### CVCO

- Tipo: `MODELO_DE_GESTION_PROPUESTO`.
- Estado: `Candidate`.
- Cadena: `Requisito normativo → Competencia requerida → Diseño curricular → Capacitación → Evaluación → Aplicación en el servicio → Supervisión → Retroalimentación → Actualización → Mejora continua`.
- Finalidad propuesta: integrar la capacitación con la gestión operativa y evitar que sea un evento aislado.

## 6. Propuesta de análisis jurídico exhaustivo

### CAPITULO_6_ANALISIS_JURIDICO_SISTEMICO

- Tipo: `PROPUESTA_DE_TRABAJO`.
- Estado: `Candidate`.
- Enfoque: ingeniería inversa de la normatividad, no resumen general de leyes.

### PASOS_PROPUESTOS

1. Identificar cada disposición relevante: artículo, fracción, inciso, elemento o criterio EC0060.
2. Clasificarla como obligación, prohibición, requisito, principio, procedimiento o criterio de desempeño.
3. Extraer competencias derivadas.
4. Descomponer cada competencia en conocimientos, habilidades, actitudes, evidencias y criterios.
5. Asignarla a proceso, curso y ruta formativa.
6. Registrarla en la Matriz Maestra de Trazabilidad.

La fuente propone iniciar con el Inventario Normativo Integral y la Matriz Maestra de Obligaciones Formativas como productos verificables. Este borrador no realiza ese análisis ni crea dichas matrices.

## 7. Elementos excluidos

- No se confirma la vigencia, interpretación o suficiencia jurídica de las normas mencionadas.
- No se crea SIGCO-ESP, MMPO, CVCO ni la Matriz de Descomposición como sistema o registro institucional.
- No se registran P-01 a P-20, COMP-001 a COMP-003 ni CUR-04 como IDs.
- No se realiza extracción artículo por artículo.
- No se crean la INI, la MOF, la Matriz Maestra de Trazabilidad ni cursos definitivos.
- No se convierten procesos, subprocesos o ejemplos en procedimientos autorizados.
- No se crean requisitos, ADR, estándares, documentos editoriales ni Knowledge Objects.
- No se interpreta la recomendación del Capítulo 6 como trabajo jurídico ya realizado.

## 8. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P09 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 9 |
| Normalización | Borrador |
| Revisión humana P09 | Pendiente |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | No realizada |

## Criterio para cerrar el borrador

La revisión humana deberá confirmar la fidelidad respecto de P09, el carácter propuesto de SIGCO-ESP y sus capas, la lista de procesos, la matriz funcional, CVCO, el enfoque de análisis jurídico y la ausencia de promoción o códigos prematuros.

# FIN DEL BORRADOR DE NORMALIZACIÓN P09
