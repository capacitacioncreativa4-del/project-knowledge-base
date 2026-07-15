# PKB-SPEC-003: Especificación Normativa del Metamodelo de Dominio (MIPSP)

## 1. Catálogo de Entidades Core
Toda entidad registrada en la plataforma debe pertenecer estrictamente a uno de los siguientes tipos:
* **Requirement (Requerimiento):** Declaración ejecutable o funcional del sistema (ej. REQ-EXT-XXXX)[cite: 2].
* **Standard (Estándar):** Normativas de diseño, desarrollo o negocio que rigen sobre los requerimientos[cite: 2].
* **System (Sistema):** El software, proceso o infraestructura donde se implementa el requerimiento[cite: 2].
* **Knowledge Package (Paquete):** El contenedor atómico de entrega que agrupa un conjunto de entidades relacionadas[cite: 2].

## 2. Catálogo de Relaciones y Cardinalidades
Los enlaces semánticos entre entidades son estrictamente direccionales:
* **`implements` (Requirement ──► System):** Un requerimiento es implementado por uno o más sistemas. (Cardinalidad: M:N).
* **`governed_by` (Requirement ──► Standard):** Un requerimiento está gobernado o restringido por uno o más estándares. (Cardinalidad: M:N).
* **`derives` (Requirement ──► Requirement):** Un requerimiento detallado se deriva de un requerimiento o acuerdo macro. (Cardinalidad: M:1).

## 3. Reglas Semánticas y Restricciones
1. **No Circularidad:** Una relación `derives` no puede formar un ciclo infinito bajo ninguna circunstancia.
2. **Referencia Huérfana Prohibida:** Toda relación declarada en la metadata del objeto debe apuntar a un ID de entidad que exista físicamente dentro de un Paquete de Conocimiento del repositorio.