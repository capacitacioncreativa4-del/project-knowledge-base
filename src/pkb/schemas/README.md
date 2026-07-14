# PKB Schema Repository — Autoridad Semántica

Este directorio contiene los esquemas técnicos, contratos de relaciones y reglas de integridad que gobiernan el Project Knowledge Base (PKB).

## 📌 Directrices de Gobernanza (DEC-0024)
1. **Obligatoriedad:** Ninguna entidad puede existir en el repositorio sin un esquema definido.
2. **Relaciones:** Todas las interacciones entre objetos deben estar formalizadas en el repositorio de relaciones.
3. **Evolución:** Cada cambio estructural en el metamodelo requiere un incremento de versión en este Schema Repository.
4. **Automatización:** Los scripts de validación y herramientas externas usan estos archivos como contrato de trabajo inmutable.