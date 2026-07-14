# Guía del Desarrollador — PKB Core (v0.1.0)

## 📌 Flujo de Trabajo Basado en Releases (DEC-0025)
1. **Ramas Protegidas:** La rama `main` contiene únicamente versiones estables de producción. Todo desarrollo activo se integra y estabiliza en la rama `develop`.
2. **Ciclo de Incrementos:** Una Release (ej. `0.1.0`) se compone de incrementos secuenciales controlados. Cada incremento debe entregar activos funcionales y coherentes probados localmente.
3. **Nomenclatura de Commits:** Se adopta el estándar de Commits Convencionales:
   * `feat(pkb):` para nuevas capacidades funcionales o esquemas.
   * `docs(pkb):` para documentación técnica e infraestructura documental.
   * `test(pkb):` para añadir o modificar suites de pruebas unitarias.