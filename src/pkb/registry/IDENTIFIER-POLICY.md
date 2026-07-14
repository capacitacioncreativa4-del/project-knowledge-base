# Política de Identificadores Únicos (v1.0.0)

Todos los objetos de conocimiento integrados al PKB deben cumplir de manera estricta con la siguiente estructura de identificación:

## 📌 Reglas de Oro
1. **Longitud Fija:** El sufijo numérico consta exactamente de seis dígitos rellenados con ceros a la izquierda (ej. `000001`).
2. **Inmutabilidad:** Un identificador asignado nunca cambia ni se altera.
3. **No Reutilización:** Los identificadores son estrictamente secuenciales y globales; bajo ninguna circunstancia se reciclan identificadores de objetos eliminados.

## 🏷️ Ejemplos de Formato Estándar
* Decisions: `ADR-000001`
* Requirements: `REQ-000001`
* Standards: `STD-000001`
* Deliverables: `DOC-000001`
* Systems: `SYS-000001`
* Packages: `KP-000001`[cite: 12]