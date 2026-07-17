# ARCH-004: Organización del Código y Estructura del Repositorio (C4 - Nivel 4)

## 1. Mapeo de Capas de Ingeniería y Directorios
El diseño físico del repositorio refleja las directrices normativas del PKB:

* `/specifications`: Contiene las políticas de gobierno (`CAP-01`), especificaciones de plataforma y del metamodelo del dominio.
* `/architecture`: Resguarda los diagramas de contexto, contenedores y los registros de decisiones (ADR) internos de la plataforma.
* `/src/pkb/cli`: Contiene la interfaz de comandos unificada (`main.py`) para interactuar con el sistema.
* `/src/pkb/extraction`: Módulos de procesamiento y ensamblaje (`processor.py`, `assembler.py`).
* `/src/pkb/schemas`: Repositorio maestro de esquemas YAML/JSON y logs históricos (`CHANGELOG.md`).