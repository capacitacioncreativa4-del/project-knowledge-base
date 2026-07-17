# Reglas de Validación: Requirement

## 1. Reglas Sintácticas
* **VAL-REQ-001:** El ID debe seguir el patrón regular `^REQ-[A-Z0-9-]+$`.
* **VAL-REQ-002:** El atributo `type` solo puede tomar los valores `FUNCTIONAL` o `NON_FUNCTIONAL`.

## 2. Reglas Semánticas
* **VAL-REQ-003:** No se permiten arreglos de relaciones (`implements` o `governed_by`) vacíos al transicionar a estado `APPROVED`.