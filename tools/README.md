# PKB Quality Assurance Framework

## Propósito
Este módulo contiene las herramientas encargadas de validar automáticamente la calidad del Project Knowledge Base. Los validadores comprueban el cumplimiento de los estándares institucionales antes de aceptar cambios en el repositorio.

---

## Objetivos
- Validar metadatos.
- Verificar identificadores.
- Detectar enlaces rotos.
- Validar plantillas.
- Generar reportes automáticos.
- Facilitar la integración con GitHub Actions.

---

## Componentes
| Herramienta | Función |
|-------------|---------|
| validate_metadata.py | Verifica YAML institucional[cite: 4] |
| validate_identifiers.py | Comprueba unicidad y formato[cite: 4] |
| validate_links.py | Revisa referencias internas[cite: 4] |
| validate_templates.py | Valida estructura documental[cite: 4] |
| validate_repository.py | Ejecuta todas las validaciones[cite: 4] |

---

## Flujo
```text
Repositorio ──> Validadores ──> Reporte ──> GitHub Actions ──> Pull Request