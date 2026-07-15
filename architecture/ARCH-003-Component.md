# ARCH-003: Modelo de Componentes (C4 - Nivel 3)

## 1. Desglose del Contenedor Core Engine
El núcleo de procesamiento en Python ejecuta su lógica a través de tres componentes especializados:

1. **Parser Semántico (`SemanticProcessor`):** Lee archivos Markdown desde las fuentes de ingesta (`projects/mipsp/ingestion/sources/`), extrae bloques semánticos delimitados y genera las entidades estructuradas intermedias.
2. **Validador sintáctico (`Engine` / `SchemaRepository`):** Toma los archivos generados y los confronta mediante JSON-Schema para certificar el cumplimiento del metamodelo.
3. **Ensamblador de Manifiestos (`KnowledgePackageAssembler`):** Agrupa los artefactos validados, vincula sus identificadores y genera el archivo maestro `manifest.yaml` para su empaquetado final.