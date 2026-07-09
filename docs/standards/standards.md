---
id: PKB-STANDARDS-0001
type: governance
status: draft
version: 0.1.0-alpha
owner: Tú (Implementation)
last_update: 2026-07-08
references: [CONTRIBUTING.md]
---

# Estándares de Formato Documental (Docs-as-Code)

## 1. Reglas Generales de Markdown
Para asegurar una legibilidad impecable tanto para humanos como para modelos de lenguaje (LLMs), se deben cumplir las siguientes directrices:
- **Títulos Únicos**: Cada documento debe comenzar con un único título principal `# (H1)`.
- **Anidación Jerárquica**: No se permite saltarse niveles de encabezados (ej. pasar de `##` directamente a `####`).
- **Lista de Elementos**: Utilizar guiones `*` o guiones medios `-` para viñetas desordenadas, manteniendo consistencia en todo el archivo.

## 2. Bloques de Código y Sintaxis
- Siempre se debe especificar el lenguaje de programación o formato inmediatamente después de las tres comillas invertidas superiores (ej. ` ```markdown `, ` ```bash `, ` ```json `).
- Para diagramas conceptuales o árboles de directorios planos, se utilizará el identificador ` ```text `.

## 3. Enlaces Relativos e Hiperconexión
- Queda prohibido el uso de URLs absolutas para navegar dentro del repositorio corporativo.
- Todo enlace interno debe estructurarse mediante rutas relativas al archivo actual (ej. `[Volver al inicio](../../README.md)` o `[Ver Guía](../standards.md)`).