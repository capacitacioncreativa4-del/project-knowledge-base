# PKB-GOVERNANCE-POLICY: Políticas de Gobierno del Conocimiento

## 1. Autoridad y Roles
* [cite_start]**Knowledge Engineer (Ingeniero de Conocimiento):** Responsable de la creación de objetos en estado `Draft` y su transición a `Review` [cite: 337-340].
* [cite_start]**Architecture Authority (Autoridad de Arquitectura):** Único rol con facultades para transicionar objetos a los estados `Approved` y `Published` [cite: 346-349].

## 2. Regla de Cambio Estructural Inmutable
[cite_start]Ningún cambio estructural en los contratos o en el metamodelo de la plataforma podrá realizarse de manera aislada [cite: 417-424]. [cite_start]Cada modificación debe impactar de forma sincronizada y obligatoria los siguientes cuatro elementos [cite: 417-424]:
1. [cite_start]Un Registro de Decisión Arquitectónica (**ADR**) justificando el cambio[cite: 420].
2. [cite_start]La Especificación técnica asociada (**Specification**)[cite: 421].
3. [cite_start]El esquema JSON/YAML de validación (**Schema**)[cite: 422].
4. [cite_start]El historial formal de modificaciones (**Changelog**)[cite: 423].