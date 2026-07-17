# PKB-VERSIONING-POLICY: Política de Versionado Semántico del PKB

## 1. Reglas de SemVer para la Plataforma
El PKB adopta estrictamente el estándar `MAJOR.MINOR.PATCH`:
* **MAJOR (Mayor):** Cambios incompatibles en el metamodelo de base o contratos JSON/YAML.
* **MINOR (Menor):** Adición de nuevas capacidades, validadores o entidades compatibles de forma retroactiva.
* **PATCH (Parche):** Corrección de errores en código, esquemas o aclaraciones de documentación.

## 2. Versionado de Paquetes de Conocimiento (KP)
Cada `Knowledge Package` (ej. `KP-000001`) se versionará de manera independiente en su manifiesto de entrega, ligando su versión al estado del metamodelo que soporta.