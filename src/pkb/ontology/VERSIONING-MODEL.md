# Modelo de Versionado Semántico del PKB (v1.0.0)

El Project Knowledge Base adopta una variante estricta de **Semantic Versioning 2.0.0 (SemVer)** adaptada a la coexistencia de código fuente y grafos de conocimiento:

## 📌 Regla de Formato: `MAJOR.MINOR.PATCH`

1. **MAJOR (X.0.0):** Incrementos cuando se introduzcan cambios estructurales que rompan la compatibilidad hacia atrás en los esquemas esenciales o en las relaciones raíz del metamodelo. Requiere migración masiva de bases de datos de conocimiento anteriores.
2. **MINOR (0.Y.0):** Adición de nuevas capacidades funcionales (nuevos validadores, nuevas entidades en el catálogo, nuevos reportes) que mantienen total compatibilidad con los paquetes e ingestiones ya realizados.
3. **PATCH (0.0.Z):** Corrección de errores ortográficos en plantillas, ajustes menores de código o parches de bugs en el motor de renderizado que no alteran la estructura de los datos.