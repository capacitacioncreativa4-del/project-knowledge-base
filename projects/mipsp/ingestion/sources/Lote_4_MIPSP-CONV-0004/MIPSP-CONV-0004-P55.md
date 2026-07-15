---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 55
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Sigamos con el proyecto.

Excelente. Éste será el primer incremento donde el PKB empezará a **producir conocimiento** y no únicamente a organizarlo.

Quiero hacer un ajuste importante respecto al plan que habíamos planteado.

## Cambio metodológico

Hasta ahora hablábamos de "extraer objetos de conocimiento" de una conversación.

Sin embargo, eso sigue siendo demasiado ambiguo. Después de analizar cómo hemos trabajado durante meses en MIPSP, creo que nuestras conversaciones siguen un patrón muy consistente.

Cada conversación contiene cuatro capas de información:

1. **Contexto** (por qué surge el trabajo).
2. **Decisiones** (qué se acordó).
3. **Artefactos** (qué se produjo).
4. **Trabajo pendiente** (qué sigue).

Si extraemos esas cuatro capas por separado, la ingestión será mucho más precisa.

Éste será el modelo oficial del piloto.

---

# MIPSP Pilot

## Sprint P0

## Incremento P0.3

**Nombre**

**Knowledge Extraction Framework v1**

Objetivo:

Transformar la primera conversación de MIPSP en conocimiento estructurado utilizando un procedimiento repetible.

---

# Decisión importante

En lugar de intentar procesar automáticamente toda la conversación, definiremos una **Ficha de Extracción**.

Cada conversación producirá una ficha.

Cada ficha será revisable.

Cada ficha generará objetos.

Así podremos corregir errores antes de que entren al PKB.

---

# Nuevo directorio

```text
projects/mipsp/extraction/

├── EXTRACTION-GUIDE.md
├── EXTRACTION-TEMPLATE.md
├── REVIEW-CHECKLIST.md
└── sessions/
```

---

# Archivo 1

## `EXTRACTION-GUIDE.md`

Este documento definirá el procedimiento oficial de extracción.

### Paso 1

Identificar la conversación.

### Paso 2

Dividirla en sesiones de ingeniería.

### Paso 3

Para cada sesión identificar:

* objetivo;
* decisiones;
* entregables;
* pendientes;
* relaciones.

### Paso 4

Construir la ficha de extracción.

### Paso 5

Revisión.

### Paso 6

Generar objetos PKB.

---

# Archivo 2

## `EXTRACTION-TEMPLATE.md`

Éste será uno de los documentos más importantes del PKB.

```markdown
# Engineering Session Extraction

## Información general

Session ID:

Conversation:

Fecha:

Estado:

---

## Objetivo de la sesión

---

## Problema abordado

---

## Decisiones tomadas

- D-001
- D-002

---

## Artefactos producidos

- Código
- Documento
- ADR
- Plantilla

---

## Objetos candidatos

| Tipo | Identificador propuesto | Título |
|------|-------------------------|--------|

---

## Dependencias

---

## Riesgos

---

## Trabajo pendiente

---

## Observaciones
```

---

# Archivo 3

## `REVIEW-CHECKLIST.md`

Antes de registrar conocimiento verificaremos:

```markdown
# Checklist

□ El objetivo quedó identificado.

□ Las decisiones son claras.

□ Los entregables existen.

□ No hay duplicados.

□ Las dependencias fueron registradas.

□ Existen referencias hacia la conversación.

□ Se identificó el siguiente trabajo.
```

---

# La primera ficha de extracción

Aquí quiero hacer un cambio importante.

En lugar de comenzar con una conversación cualquiera, propongo iniciar con una conversación que marcó un cambio arquitectónico importante:

> **"MIPSP Editor – EPIC-02 Implementación"**

¿Por qué?

Porque esa conversación representa el inicio de la implementación del sistema y contiene una gran cantidad de decisiones arquitectónicas que siguen vigentes.

La registraremos como:

```text
Conversation

MIPSP-CONV-0001
```

y la primera sesión como:

```text
MIPSP-SES-000001
```

---

# Primer objeto de conocimiento

Durante la extracción no crearemos todavía todos los objetos.

Crearemos uno.

Y únicamente uno.

```text
MIPSP-ADR-000001

Decisión:

Adoptar el PKB como plataforma de administración del conocimiento del proyecto MIPSP.
```

Con este primer ADR validaremos todo el flujo:

Conversación → Ficha → ADR → Registro → Trazabilidad.

Si funciona, repetiremos el proceso para el resto de los objetos.

---

# Primer mapa de relaciones

```text
MIPSP-CONV-0001
        │
        ▼
MIPSP-SES-000001
        │
        ▼
MIPSP-ADR-000001
        │
        ▼
PROJECT.yaml
```

Éste será el primer subgrafo del proyecto.

---

# Criterios de aceptación del Incremento P0.3

El incremento se considerará completo cuando existan:

* El procedimiento oficial de extracción.
* La plantilla institucional de extracción.
* La lista de verificación.
* La primera conversación registrada.
* La primera sesión registrada.
* El primer ADR del proyecto.
* La primera relación de trazabilidad.

Con ello habremos demostrado que el PKB puede transformar una conversación en conocimiento gobernado.

---

# Un ajuste que considero necesario antes del siguiente incremento

Hay un aspecto que debemos resolver ahora, antes de continuar con la ingestión masiva.

Hasta este momento hemos supuesto que cada objeto de conocimiento se almacenará como un archivo Markdown independiente. Creo que esa decisión sigue siendo correcta, pero antes de crear cientos de objetos conviene definir **el estándar editorial definitivo** para esos archivos.

Éste será el único trabajo previo que considero estrictamente necesario, porque afectará a todos los objetos que creemos después. Mi propuesta es que el siguiente incremento (P0.4) se dedique exclusivamente a establecer el **PKB Knowledge Object Standard v1.0**: la estructura, metadatos, secciones obligatorias, convenciones de identificación y reglas de trazabilidad que tendrán todos los objetos del repositorio.

Una vez aprobado ese estándar, ya no volveremos a modificar el formato y podremos dedicar el resto del piloto a la ingestión efectiva de MIPSP, con la confianza de que cada objeto creado será estable y reutilizable durante toda la vida del proyecto. Creo que ése es el único prerrequisito técnico que merece la pena completar antes de acelerar la migración.
