# Principios de Diseño del Producto PKB (v0.1.0)

Cualquier adición de código, esquema o funcionalidad al núcleo del PKB debe regirse estrictamente por los siguientes cuatro principios fundacionales:

* **PRN-001: Semántica Primero.** Ninguna línea de código o script automatizado puede implementarse si no responde directamente a una entidad, relación o regla previamente declarada en la ontología.
* **PRN-002: Determinismo Rígido.** El sistema de validación debe ser binario y predecible. Un paquete de conocimiento o es 100% válido y cumple todos los contratos sintácticos, o es completamente rechazado. No existen estados intermedios.
* **PRN-003: Aislamiento Core-Dominio.** El código de la plataforma PKB es genérico y abstracto. Jamás debe incluir reglas duras o lógica específica de un dominio de negocio particular (como las reglas propias de MIPSP).
* **PRN-004: Trazabilidad Bidireccional Inmutable.** Todo objeto de conocimiento debe poder rastrearse hasta su fuente primaria original, y toda fuente debe declarar de forma explícita qué objetos produjo.