---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 36
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Vamos muy bien. Continuemos con el proyecto

Excelente. En este punto considero que ya hemos superado la fase de "diseño del repositorio". A partir de ahora comenzaremos a construir un **producto**: una plataforma de ingeniería del conocimiento.

Voy a proponerte un pequeño cambio metodológico que creo que aumentará mucho la calidad del proyecto.

## Cambio de metodología

Hasta ahora cada respuesta generó un documento.

A partir de esta épica generaremos **incrementos completos**, similares a un sprint de ingeniería profesional.

Cada incremento contendrá:

* 1 estándar.
* 1 plantilla reutilizable.
* 1 ejemplo completamente desarrollado.
* 1 checklist de validación.
* 1 README del paquete.

Así, cada entrega será utilizable inmediatamente y no habrá piezas "huérfanas".

En otras palabras, dejaremos de construir documentos aislados y comenzaremos a construir **módulos completos**.

---

# EPIC S0-004

## Package 1 — Governance Templates

## Estructura

```text
shared/
└── templates/
    └── package-governance/
        ├── README.md
        ├── ADR-TEMPLATE.md
        ├── GOVERNANCE-TEMPLATE.md
        ├── POLICY-TEMPLATE.md
        ├── CHANGELOG-TEMPLATE.md
        ├── CHECKLIST.md
        └── examples/
            ├── ADR-Example.md
            └── Governance-Example.md
```

Este será el primer paquete institucional del PKB.

---

# Archivo 1

## Ruta

```text
shared/templates/package-governance/README.md
```

```markdown
---
id: PKB-TMP-0001
title: Governance Template Package
version: 1.0.0
status: Approved
owner: Architecture
type: TMP
domain: PKB
---

# Governance Template Package

## Propósito

Este paquete proporciona las plantillas oficiales para la elaboración de documentos de gobierno institucional del Project Knowledge Base.

Incluye modelos para:

- Architecture Decision Records (ADR)
- Documentos de Gobierno
- Políticas
- Registro de Cambios

---

# Contenido

| Archivo | Propósito |
|----------|-----------|
| ADR-TEMPLATE.md | Registrar decisiones arquitectónicas |
| GOVERNANCE-TEMPLATE.md | Crear documentos de gobierno |
| POLICY-TEMPLATE.md | Definir políticas institucionales |
| CHANGELOG-TEMPLATE.md | Registrar cambios importantes |
| CHECKLIST.md | Validación editorial |

---

# Dependencias

Este paquete depende de:

- PKB-MANIFEST
- METADATA-MODEL
- IDENTIFIER-SCHEME
- TRACEABILITY-MODEL
- DOCUMENT-TEMPLATE-STANDARD

---

# Compatibilidad

Versión mínima del PKB:

1.0

---

# Uso

1. Copiar la plantilla requerida.
2. Asignar un identificador.
3. Completar el YAML.
4. Elaborar el contenido.
5. Validar mediante CHECKLIST.
6. Registrar en Git.

---

# Historial

|Versión|Descripción|
|--------|-----------|
|1.0.0|Versión inicial|
```

---

# Archivo 2

## Ruta

```text
shared/templates/package-governance/CHECKLIST.md
```

```markdown
# Governance Checklist

## Metadatos

- [ ] ID válido
- [ ] Versión
- [ ] Owner
- [ ] Estado
- [ ] Dominio
- [ ] Tags

---

## Contenido

- [ ] Propósito
- [ ] Alcance
- [ ] Relaciones
- [ ] Historial

---

## Calidad

- [ ] Ortografía
- [ ] Markdown válido
- [ ] YAML válido
- [ ] Relaciones existentes
- [ ] Referencias correctas

---

## Git

- [ ] Commit realizado
- [ ] Pull Request
- [ ] Revisión aprobada
```

---

# Archivo 3

## Ruta

```text
shared/templates/package-governance/ADR-TEMPLATE.md
```

```markdown
---
id:
title:
version: 1.0.0
status: Draft
owner:
created:
updated:
type: ADR
domain:
tags:
---

# Título

## Estado

Draft

---

# Contexto

...

---

# Problema

...

---

# Decisión

...

---

# Alternativas consideradas

## Alternativa A

...

## Alternativa B

...

---

# Consecuencias

## Beneficios

...

## Riesgos

...

---

# Relaciones

## Documento superior

-

## Relacionados

-

## Derivados

-

---

# Historial

|Versión|Fecha|Descripción|
|--------|-----|-----------|
```

---

# Archivo 4

## Ruta

```text
shared/templates/package-governance/GOVERNANCE-TEMPLATE.md
```

```markdown
---
id:
title:
version:
status:
owner:
created:
updated:
type: GOV
domain:
tags:
---

# Propósito

...

---

# Objetivos

...

---

# Alcance

...

---

# Responsabilidades

...

---

# Indicadores

...

---

# Relaciones

...

---

# Historial

...
```

---

# Archivo 5

## Ruta

```text
shared/templates/package-governance/POLICY-TEMPLATE.md
```

```markdown
---
id:
title:
version:
status:
owner:
type: POLICY
domain:
---

# Política

## Objetivo

...

## Alcance

...

## Responsables

...

## Cumplimiento

...

## Excepciones

...

## Revisión

...
```

---

# Archivo 6

## Ruta

```text
shared/templates/package-governance/CHANGELOG-TEMPLATE.md
```

```markdown
# Registro de Cambios

|Fecha|Versión|Autor|Descripción|Aprobado|
|------|--------|-----|-----------|---------|
```

---

# Commit recomendado

```bash
feat(templates): add governance template package v1
```

---

# Estado del proyecto

Con este incremento ya no estamos creando únicamente documentación; estamos construyendo una **biblioteca institucional reutilizable**.

## Progreso global estimado

| Área                 | Avance |
| -------------------- | :----: |
| Gobernanza           |  100%  |
| Kernel               |   80%  |
| Estándares           |   40%  |
| Plantillas           |   15%  |
| Automatización       |   0%   |
| GitHub Actions       |   0%   |
| Knowledge Graph      |   10%  |
| Calidad              |   20%  |
| Proyectos de ejemplo |   0%   |

## Propuesta para la siguiente fase

A partir del próximo incremento propongo un cambio importante: **cada plantilla irá acompañada de un validador automático**.

Crearemos una carpeta como esta:

```text
tools/
└── validators/
    ├── validate_yaml.py
    ├── validate_links.py
    ├── validate_identifiers.py
    ├── validate_metadata.py
    └── validate_templates.py
```

Estos validadores permitirán verificar automáticamente que cualquier documento incorporado al PKB cumple los estándares institucionales. Más adelante podremos integrarlos en **GitHub Actions**, de modo que cada *Pull Request* ejecute las comprobaciones de calidad antes de aceptarse. Esa será la transición natural desde un repositorio bien documentado hacia una plataforma de ingeniería del conocimiento con controles automáticos de calidad.
