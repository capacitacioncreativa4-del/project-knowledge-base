# Release Notes — PKB Version 0.2.0-beta

## 📦 Resumen de la Versión
Esta release establece el **Motor de Extracción Semántica (Semantic Extraction Engine)** de la plataforma PKB. Permite transicionar de la definición puramente documental y sintáctica hacia la ingesta automatizada de fuentes primarias en Markdown.

## 🛠️ Componentes Entregados
* **Pipeline Governance (I01):** Especificación técnica `PKB-SPEC-003-Ingestion-Pipeline-Specification.md` y esquema base de Sistema (`system.yaml`).
* **Prompt Engineering Framework (I02):** Directrices e instrucciones maestras de extracción en `PKB-SPEC-004` junto al esquema de Artefacto (`artifact.yaml`).
* **Core Processing Engine (I03):** Componente base de software en Python (`processor.py`) y esquema de módulo (`system_module.yaml`).
* **Knowledge Package Assembler (I04):** Motor de empaquetado y generación de manifiestos (`assembler.py`) respaldado por `knowledge_package.yaml`.
* **Pilot Execution (I05):** Script de orquestación y runner de pruebas (`test_pipeline.py`) verificado.

## 🚀 Próximos Pasos (Roadmap 0.3.0)
Construcción de la interfaz de línea de comandos (CLI) unificada e integración activa con APIs de producción para la ingesta masiva del Lote 1 al Lote 4.