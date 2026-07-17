# PKB-SPEC-003: Ingestion Pipeline Specification

## 1. Propósito y Alcance
Esta especificación define el flujo de datos que transforma las transcripciones y archivos en Markdown de origen en objetos semánticos de conocimiento YAML validados sintácticamente.

## 2. Arquitectura del Extractor Semántico
El Extractor Semántico lee archivos de orígenes primarios (`projects/mipsp/ingestion/sources/`), segmenta el contexto histórico, realiza llamadas estructuradas al LLM aplicando el Framework de Prompts Técnicos y genera archivos independientes por cada entidad extraída.

## 3. Criterios de Calidad de Extracción
* **Fidelidad Literal:** Toda regla, decisión o requerimiento extraído debe mantener estricta concordancia semántica con lo expresado en la fuente Markdown original.
* **Trazabilidad Obligatoria:** Ningún objeto YAML será generado sin poblar la lista `relationships.documents` mapeando explícitamente el ID de la conversación fuente.