# ARCH-002: Modelo de Contenedores (C4 - Nivel 2)

## 1. Arquitectura de Contenedores
El PKB está compuesto por los siguientes contenedores lógicos independientes:

1. **Interfaz de Línea de Comandos (CLI Runner):** Aplicación de consola en Python que actúa como el punto de entrada principal para el usuario.
2. **Core Processing & Extraction Engine:** Módulo encargado de parsear archivos Markdown y estructurar entidades semi-automatizadas.
3. [cite_start]**Schema Repository & Validator:** Componente encargado de confrontar cada archivo YAML contra sus contratos JSON-Schema para asegurar consistencia sintáctica [cite: 383-390].
4. [cite_start]**Knowledge Package Assembler:** Encargado de empaquetar conjuntos de artefactos validados y generar manifiestos de liberación [cite: 233-250, 316].