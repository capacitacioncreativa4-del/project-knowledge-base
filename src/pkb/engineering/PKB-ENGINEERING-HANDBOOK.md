# PKB Engineering Handbook (v0.1.0)

## 1. Filosofía de Desarrollo
El desarrollo de la plataforma PKB se basa en el rigor del software profesional. El PKB administra su propia ingeniería: cualquier decisión técnica se registra mediante ADRs y las especificaciones guían la implementación.

## 2. Flujo de Git y Ramas
* **Ramas estables (`main`):** Solo recibe fusiones de versiones productivas mediante Pull Requests formalizados.
* **Ramas de desarrollo (`develop`):** Integración continua de incrementos y releases[cite: 6].
* **Mensajes de commit:** Se requiere el estándar de Commits Convencionales (ej. `feat(pkb):`, `docs(pkb):`)[cite: 5].

## 3. Definition of Done (DoD)
Para que un incremento se considere finalizado y listo para integrarse en una release, debe cumplir:
1. Esquemas sintácticos YAML completos y validados[cite: 4, 5].
2. Documentación técnica actualizada en `specifications/` o `engineering/`[cite: 6].
3. Ejemplos de uso reales derivados del piloto de dominio (MIPSP) integrados[cite: 5, 6].