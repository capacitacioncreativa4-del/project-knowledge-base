---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 23
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Continúa con el proyecto

De acuerdo. Continuemos exactamente donde quedó el proyecto.

En el hilo anterior del **MIPSP-Editor (EPIC-02)** ya habíamos establecido un flujo de trabajo incremental, produciendo componentes completos y reutilizables hasta disponer de una plataforma editorial sólida. El siguiente bloque lógico es completar la **infraestructura del editor**, de modo que posteriormente podamos incorporar las funciones de inteligencia documental sin tener que rediseñar la arquitectura.

## EPIC-02 · Siguiente incremento

### HITO 2.8 — Motor de Validación Documental

Este componente será el responsable de verificar automáticamente que cada documento elaborado cumpla las reglas editoriales e institucionales.

Su arquitectura comprende cinco validadores independientes:

```
Documento
     │
     ▼
┌──────────────────────┐
│ Validador Sintáctico │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Validador Editorial  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Validador Normativo  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Validador Semántico  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Validador Institucional│
└──────────┬───────────┘
           ▼
      Resultado Final
```

---

# 1. Validador sintáctico

Comprueba automáticamente:

* ortografía
* puntuación
* uso de mayúsculas
* concordancia
* abreviaturas
* espacios dobles
* numeración
* listas
* encabezados

Salida:

```
✓ Correcto

o

⚠ Error
Línea 48
Coma innecesaria.
```

---

# 2. Validador editorial

Verifica el cumplimiento del Manual Editorial.

Ejemplos:

```
✔ uso correcto de títulos

✔ estructura jerárquica

✔ longitud máxima de párrafos

✔ longitud de viñetas

✔ numeración institucional

✔ referencias cruzadas

✔ tablas

✔ figuras
```

---

# 3. Validador normativo

Busca referencias jurídicas.

Ejemplo:

```
Ley Federal del Trabajo

Ley General del Sistema Nacional
de Seguridad Pública

Reglamento Federal
...
```

Comprueba:

* existencia
* vigencia
* denominación oficial
* artículo citado
* consistencia

---

# 4. Validador semántico

Utiliza IA para detectar:

contradicciones

ejemplo

```
Capítulo II

El uniforme es obligatorio.

...

Capítulo VII

El uniforme podrá omitirse.
```

Resultado:

```
Conflicto detectado.

Nivel:
ALTO
```

---

También detecta:

duplicidades

omisiones

conceptos ambiguos

definiciones faltantes

inconsistencias

---

# 5. Validador institucional

Comprueba automáticamente:

* logotipos
* nombres oficiales
* cargos
* dependencias
* organigramas
* códigos documentales
* versión
* fecha
* clasificación documental

---

## Motor de reglas

Todas las validaciones estarán gobernadas mediante reglas declarativas:

```yaml
rule:
    id: DOC-0021
    severity: HIGH
    description: Todo procedimiento deberá incluir objetivo.

    applies_to:
        - Procedimiento

    check:
        exists:
            heading: Objetivo

    message:
        Falta el apartado Objetivo.
```

Con ello no será necesario modificar código cuando cambie el Manual Editorial.

---

# Reporte automático

Cada revisión generará un informe como:

```
CALIFICACIÓN

96.4 %

──────────────

Ortografía

100 %

Editorial

98 %

Normativa

93 %

Semántica

94 %

Institucional

97 %

──────────────

Errores críticos:
2

Advertencias:
6

Sugerencias:
14
```

---

# Integración con el Editor

Cada error aparecerá resaltado directamente en el documento:

```
El vigilante deberá portar...

                 ▲

Error Editorial

Se recomienda:

"El personal de seguridad deberá portar..."
```

---

# Beneficios de este componente

Al finalizar este hito, el MIPSP-Editor dejará de ser únicamente un editor de documentos para convertirse en un **sistema de aseguramiento de calidad documental**, capaz de:

* verificar automáticamente el cumplimiento del Manual Editorial Institucional;
* detectar errores de forma, estructura y contenido antes de la publicación;
* validar referencias normativas y su coherencia;
* identificar contradicciones y duplicidades mediante análisis semántico;
* generar reportes de calidad cuantificables y trazables para auditorías;
* separar las reglas editoriales del código mediante un motor declarativo, facilitando su mantenimiento y evolución.

Este hito prepara la plataforma para el siguiente incremento, en el que incorporaremos la **Capa de Inteligencia Documental**, responsable de la indexación semántica, búsqueda avanzada, generación asistida de contenido y reutilización inteligente de componentes documentales dentro del ecosistema del MIPSP.
