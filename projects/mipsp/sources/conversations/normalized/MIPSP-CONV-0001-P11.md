---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalized
type: Source
file_reference: MIPSP-CONV-0001-P11.md
source_part: 11
source_sha256: 93E1A2236C9123DFFD185ACFDCC8823F7D5CF211BF19DB9E448CCFF874644888
---

# Fuente Normalizada — MIPSP-CONV-0001-P11

## Referencia y procedencia

Esta fuente normalizada deriva exclusivamente de `projects/mipsp/ingestion/sources/Lote_1_MIPSP-CONV-0001/MIPSP-CONV-0001-P11.md`.
La fuente original y el borrador aprobado permanecen intactos.

## 1. Evolución hacia un sistema documental integrado

### MIP_PSP

- Tipo: `MODELO_INTEGRAL_PROPUESTO`.
- Estado: `Candidate`.
- Nombre propuesto: Modelo Integral de Profesionalización del Personal Operativo de Seguridad Privada.
- Finalidad propuesta: demostrar cumplimiento legal, técnico, pedagógico y operativo, además de mejora continua.
- Ámbitos de aplicación imaginados: empresa de seguridad privada, academia, centro evaluador, organismo certificador o despacho consultor.

Los ámbitos son posibilidades de uso expresadas en la conversación, no validaciones de alcance ni autorizaciones institucionales.

### SISTEMA_DOCUMENTAL_INTEGRADO

- Tipo: `ARQUITECTURA_DOCUMENTAL_PROPUESTA`.
- Estado: `Candidate`.
- Bloque A: Fundamentos, capítulos 1 a 5.
- Bloque B: Ingeniería Jurídica.
- Bloque C: Ingeniería Curricular.
- Bloque D: Ingeniería del Conocimiento.

## 2. Base de Conocimiento Institucional

### BCI

- Tipo: `MODELO_DE_GESTION_DEL_CONOCIMIENTO_PROPUESTO`.
- Estado: `Candidate`.
- Principio: cada elemento debe existir una sola vez y relacionarse con artículos, leyes, procesos, procedimientos, tareas, riesgos, evaluaciones, cursos y manuales.
- Consecuencia propuesta: los cursos serían vistas de la base de conocimiento, no unidades primarias duplicadas.

La BCI es una propuesta conceptual; no se crea como repositorio físico en esta fase.

## 3. Modelo relacional del conocimiento

### CADENA_RELACIONAL_BCI

Tipo: `MODELO_DE_TRAZABILIDAD_PROPUESTO`; estado: `Candidate`.

Cadena: `Ley → Artículo → Obligación → Competencia → Proceso → Procedimiento → Tarea → Resultado esperado → Curso → Unidad → Sesión → Actividad → Evaluación → Evidencia`.

La cadena expresa dependencias conceptuales y no constituye todavía un esquema de base de datos ni relaciones institucionales registradas.

## 4. Repositorios maestros propuestos

### REPOSITORIOS_MAESTROS

- Tipo: `ARQUITECTURA_DE_DATOS_PROPUESTA`.
- Estado: `Candidate`.
- Finalidad: convertir matrices y catálogos en repositorios maestros para reducir duplicidad y facilitar actualización.

La fuente anuncia 25 repositorios, pero enumera explícitamente los siguientes 20; no se inventan los cinco restantes:

| Código de propuesta | Repositorio |
|---|---|
| R-01 | Jurídico |
| R-02 | Obligaciones |
| R-03 | Competencias |
| R-04 | Procesos |
| R-05 | Procedimientos |
| R-06 | Tareas |
| R-07 | Riesgos |
| R-08 | Equipamiento |
| R-09 | Documentos |
| R-10 | Cursos |
| R-11 | Unidades |
| R-12 | Recursos Didácticos |
| R-13 | Casos |
| R-14 | Simulaciones |
| R-15 | Evaluaciones |
| R-16 | Instrumentos |
| R-17 | Evidencias |
| R-18 | Instructores |
| R-19 | Actualizaciones |
| R-20 | Indicadores |

Los códigos R-01 a R-20 son códigos internos de propuesta y no IDs persistentes del PKB.

## 5. Flujo de actualización propuesto

### ACTUALIZACION_EN_CASCADA

La fuente propone que un cambio normativo se propague conceptualmente desde el Repositorio Jurídico al Repositorio de Competencias y, desde allí, a los elementos relacionados. La finalidad sería evitar modificar manualmente múltiples cursos.

Esta automatización es una hipótesis de diseño y no evidencia de implementación ni garantía de actualización automática.

## 6. Compatibilidad digital propuesta

### SISTEMA_GESTION_COMPETENCIAS_DIGITAL

- Tipo: `ARQUITECTURA_TECNOLOGICA_PROPUESTA`.
- Estado: `Candidate`.
- Propuesta: dotar a competencias, cursos, evaluaciones y evidencias de identificadores únicos y almacenarlos posteriormente en una base de datos o LMS.
- Posibles destinos mencionados: PostgreSQL, SQL Server, Moodle, Power BI, expediente electrónico y alertas de recertificación/actualización.

Las tecnologías son ejemplos de implementación futura; no se seleccionan plataformas ni se crean integraciones.

## 7. Productos paralelos propuestos

### PRODUCTOS_DEL_SISTEMA

1. Documento narrativo: Tomo I, con modelo, metodología y conclusiones.
2. Anexo Técnico: matrices maestras de obligaciones, competencias, procesos, riesgos y trazabilidad.
3. Diccionario Institucional de Datos y Competencias: definiciones normalizadas de competencia, proceso, procedimiento, evidencia, curso, evaluación e indicador.

La estructura paralela busca robustez, mantenimiento, reutilización y evolución digital, pero permanece como propuesta de organización.

## 8. Elementos excluidos

- No se crea MIP-PSP, BCI, SIGCO-ESP ni un sistema de gestión digital.
- No se crean los 25 repositorios ni se inventan los cinco códigos no enumerados.
- No se registran R-01 a R-20 como IDs institucionales.
- No se seleccionan bases de datos, LMS, herramientas de inteligencia de negocios ni integraciones.
- No se crean identificadores únicos para competencias, cursos, evaluaciones o evidencias.
- No se ejecuta actualización en cascada ni se demuestra reducción de duplicidades.
- No se realizan análisis jurídicos ni se convierten las propuestas en requisitos, ADR, estándares, documentos editoriales o Knowledge Objects.

## 9. Estado de trazabilidad

| Elemento | Estado |
|---|---|
| Fuente P11 | Preservada |
| SHA-256 de fuente | Verificado en el encabezado |
| Conversación | MIPSP-CONV-0001 |
| Parte | 11 |
| Normalización | Normalizada |
| Revisión humana P11 | Aprobada por el usuario |
| Knowledge Objects nuevos | No creados |
| REQ / ADR / STD nuevos | No creados |
| Promoción a fuente normalizada | Realizada |

## Cierre de normalización

La revisión humana confirmó la fidelidad respecto de P11, el carácter propuesto de MIP-PSP y BCI, la cadena relacional, el conteo de repositorios, la separación entre códigos y IDs, la compatibilidad digital y los tres productos paralelos.

# FIN DE LA FUENTE NORMALIZADA P11
