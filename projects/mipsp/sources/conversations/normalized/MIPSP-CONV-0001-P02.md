---
id: MIPSP-CONV-0001
title: Revisión normativa capacitación
status: Normalized
type: Source
file_reference: MIPSP-CONV-0001-P02.md
source_part: 2
source_sha256: 88EB5598D432EF0D9528AAFC71A58DDA8BD6126059EF84347DA216839307B26D
---

# Fuente Normalizada — MIPSP-CONV-0001

Derivada de `projects/mipsp/sources/conversations/original/MIPSP-CONV-0001-P02.md`.

## Unidades normalizadas

### MARCO_NORMATIVO_REFERENCIAL
- Tipo: `CONOCIMIENTO_REFERENCIAL`; estado: `Validated`.
- Base referencial para relacionar normatividad, obligaciones, competencias y diseño de capacitación.
- Una referencia conversacional no equivale a validación jurídica externa.

### CADENA_NORMATIVIDAD_COMPETENCIA_CURSO
- Tipo: `MODELO_CONCEPTUAL`; estado: `Validated`.
- Relación: `Normatividad → Obligación → Competencia → Curso`.
- Estructura conceptual reutilizable para ingeniería curricular posterior.

### INGENIERIA_CURRICULAR_NORMATIVA
- Tipo: `MODELO_METODOLOGICO`; estado: `Validated`.
- Transformación: `Normatividad → Obligaciones → Competencias → Conductas observables → Contenidos → Evidencias → Evaluación → Curso`.
- Es una propuesta metodológica, no disposición jurídica ni estándar externo aprobado.

### MATRIZ_MAESTRA_COMPETENCIAS
- Tipo: `ESTRUCTURA_PROPUESTA`; estado: `Validated`.
- Campos: competencia, código, fuente normativa, obligación, resultado esperado, conducta observable, conocimiento, habilidad, actitud o criterio, tema, subtema, evidencia, instrumento de evaluación y curso relacionado.
- Estructura de trabajo, no registro institucional definitivo.

### DESCOMPOSICION_EXHAUSTIVA_TEMAS
- Tipo: `METODO_DESCOMPOSICION`; estado: `Validated`.
- Parte de la competencia y desciende hacia conocimientos, habilidades, procedimientos, conductas, criterios, evidencias y evaluación.
- No depende exclusivamente de títulos tradicionales de cursos.

### MATRIZ_TRAZABILIDAD_NORMATIVA
- Tipo: `MODELO_TRAZABILIDAD`; estado: `Validated`.
- Cadena: `Fuente → Artículo / disposición → Obligación → Competencia → Tema → Evidencia → Evaluación → Curso`.
- Cada elemento pedagógico relevante debe poder regresar a su fuente de origen.

### ARQUITECTURA_SISTEMA_CAPACITACION
- Tipo: `ARQUITECTURA_PROPUESTA`; estado: `Validated-With-Reservation`.
- Cursos planteados: Control de Accesos, Vigilancia Preventiva, Recorridos de Inspección, Comunicación Operativa y Atención de Incidentes.
- La relación de cursos es propuesta y no asignación definitiva de contenidos.

### MAPA_CURRICULAR_COMPLETO
- Tipo: `MODELO_CONCEPTUAL`; estado: `Validated-With-Reservation`.
- Relaciona competencias, cursos, módulos, temas, subtemas, evidencias, instrumentos, evaluación y trazabilidad normativa.
- Su construcción detallada queda pendiente de las matrices correspondientes.

### RECOMENDACIONES_PEDAGOGICAS
- Tipo: `CONOCIMIENTO_METODOLOGICO`; estado: `Validated`.
- Transformar obligaciones en comportamientos observables; mantener trazabilidad entre competencia y evidencia; vincular evaluación con desempeño; descomponer contenidos exhaustivamente; y organizar el desarrollo progresivamente.

### EVALUACION_Y_EVIDENCIAS
- Tipo: `COMPONENTE_PEDAGOGICO`; estado: `Validated`.
- Cadena: `Competencia → Desempeño esperado → Evidencia → Instrumento → Criterio de evaluación`.
- Requiere desarrollo posterior en artefactos pedagógicos.

### COMPONENTES_DE_COMPETENCIA
- Tipo: `MODELO_COMPETENCIAL`; estado: `Validated`.
- Componentes: conocimiento, habilidad, conducta observable, criterio, evidencia y evaluación.

### PLAN_DESARROLLO_TOMOS
- Tipo: `PROPUESTA_DESARROLLO`; estado: `Validated-As-Proposal`.
- Organización documental mediante tomos o bloques de contenido; no arquitectura documental definitiva.

## Trazabilidad

Los objetos derivados son `ART-000002`, `ART-000003`, `ART-000004`, `ART-000005` y `ART-000006`; `ART-000005` contiene estructuralmente a los otros cuatro.

Las propuestas permanecen identificadas como propuestas y las referencias normativas requieren verificación documental externa.
