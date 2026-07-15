# Release Notes — PKB Version 0.1.0-beta

## 📦 Resumen de la Versión
Esta es la primera release oficial estable de la plataforma **Project Knowledge Base (PKB)**. Establece las bases normativas, los contratos de datos y el motor sintáctico inicial que regirán toda la captura y validación de conocimiento futuro.

## 🛠️ Componentes Entregados
* **Core Foundation (I01):** Estructura del repositorio, manual de desarrollo (`PKB-ENGINEERING-HANDBOOK.md`) y especificación raíz (`PKB-SPEC-001.md`).
* **Entity Schemas (I02):** 11 esquemas YAML definitivos para la validación rígida de objetos.
* **Relation Schemas (I03):** Definición de restricciones y aristas en `relation-types.yaml` y manifiesto ontológico.
* **Registry & Lifecycle (I04):** Gobernanza de identificadores únicos y máquina de estados lógicos (DRAFT, REVIEW, APPROVED, etc.).
* **Templates (I05):** Moldes estructurados para la instanciación de ADRs, requerimientos y estándares.
* **Validation Engine (I06):** Primer motor en Python (`engine.py`) listo para parsear y validar la integridad sintáctica.
* **MIPSP Pilot (I07):** Primer lote de datos del mundo real completamente adaptado al nuevo estándar.

## 🚀 Próximos Pasos (Roadmap 0.2.0)
Diseño e integración del motor de extracción semántica utilizando IA avanzada.