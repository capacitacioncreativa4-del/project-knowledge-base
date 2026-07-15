---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 11
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente decisión. Continúa con el proyecto.

Perfecto. Con esta decisión damos un paso que, en mi opinión, marca la diferencia entre un generador de documentos y una **plataforma editorial institucional**.

Hasta ahora habíamos pensado en generar archivos (.docx, .xlsx, .pptx). A partir de este momento el principio será distinto:

> **El documento existe primero como un modelo de información; los archivos son únicamente representaciones de ese modelo.**

Ese es el mismo principio utilizado por grandes sistemas editoriales, documentación técnica aeronáutica (DITA), publicaciones jurídicas y numerosos sistemas de gestión documental.

---

# Decisión Arquitectónica A-002

## Modelo Documental Intermedio (MDI)

Incorporaremos una nueva capa denominada **MDI (Modelo Documental Intermedio)**.

La arquitectura evolucionará así:

```text
                 Contenido
                     │
                     ▼
          Modelo Documental (MDI)
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 DOCX Exporter   XLSX Exporter   PPTX Exporter
      │              │              │
      └──────────────┼──────────────┘
                     ▼
              Biblioteca MIPSP
```

Esto significa que el contenido del **CUR-OPS-001** no pertenecerá al archivo Word.

El Word será simplemente una vista del contenido.

---

# ¿Qué es el MDI?

Será una representación completamente estructurada del documento.

Por ejemplo:

```text
Documento
│
├── Metadatos
├── Portada
├── Secciones
│      ├── Párrafos
│      ├── Listas
│      ├── Tablas
│      ├── Figuras
│      └── Diagramas
├── Referencias
├── Anexos
└── Historial
```

Los exportadores solamente recorrerán este árbol.

---

# Sprint 3

## Dominio documental

Antes de exportar cualquier archivo construiremos el modelo completo.

### document.py

La clase principal evolucionará.

```python
class Document:

    metadata

    cover

    sections

    annexes

    references

    history
```

---

### section.py

Nueva clase.

```python
class Section:

    title

    level

    elements
```

Una sección podrá contener cualquier tipo de elemento.

---

### paragraph.py

```python
class Paragraph:

    text

    style

    alignment
```

---

### table.py

```python
class Table:

    title

    columns

    rows

    style
```

---

### figure.py

```python
class Figure:

    caption

    image

    reference
```

---

### annex.py

```python
class Annex:

    code

    title

    elements
```

---

# Un principio importante

Todos estos objetos serán completamente independientes de Word.

Por ejemplo,

una tabla **no sabrá** cómo dibujarse.

Solamente contendrá información.

Después:

```text
Tabla
      │
      ▼
DOCX Exporter

XLSX Exporter

HTML Exporter

PDF Exporter
```

Cada exportador decidirá cómo representarla.

---

# Beneficios

Con esta arquitectura podremos hacer cosas muy interesantes.

Por ejemplo,

generar simultáneamente:

```
CUR-OPS-001-D01.docx

CUR-OPS-001-D01.pdf

CUR-OPS-001-D01.html

CUR-OPS-001-D01.md
```

utilizando exactamente el mismo contenido.

---

# Referencias cruzadas

Otro beneficio importante.

Actualmente los documentos contienen referencias como:

```
Véase ETS-CUR001-MOD03
```

En el MDI esa referencia será un objeto.

```python
Reference:

    source

    target

    type
```

Cuando el documento cambie de numeración, las referencias podrán actualizarse automáticamente.

---

# Historial documental

Cada documento incluirá internamente un historial.

```text
Documento

│

├── v1.0

├── v1.1

├── v1.2

└── v2.0
```

Esto permitirá producir automáticamente el:

* historial de cambios;
* tabla de versiones;
* registro maestro.

---

# Validación estructural

Antes de exportar:

```
Document
```

pasará por un validador.

Ejemplos.

✔ Tiene metadatos.

✔ Tiene portada.

✔ Tiene título.

✔ Todas las tablas tienen encabezado.

✔ Todas las figuras tienen pie.

✔ No existen referencias rotas.

✔ No existen códigos duplicados.

✔ Los anexos están correctamente numerados.

Sólo después se exportará.

---

# Próximo Sprint

Aquí comienza una parte especialmente importante del proyecto.

## Sprint 4

### Motor de Construcción Documental (Document Builder)

Hasta ahora el documento se crea "a mano".

En el Sprint 4 construiremos un **Builder** que permita describir un documento mediante instrucciones de alto nivel.

Por ejemplo:

```python
programa = (
    CourseProgramBuilder()
    .with_metadata(metadata)
    .with_cover()
    .with_objectives(objetivos)
    .with_competencies(competencias)
    .with_modules(modulos)
    .with_annexes(anexos)
    .build()
)
```

El resultado será un `Document` completamente válido, listo para exportarse a cualquiera de los formatos soportados.

## Visión a largo plazo

Conforme avance el proyecto, el MIPSP-Editor dejará de ser únicamente un generador de documentos y se convertirá en una **plataforma de publicación técnica**. Esto abrirá la posibilidad de incorporar, en fases posteriores, funcionalidades como:

* generación automática de bibliotecas completas;
* publicación en HTML para intranets;
* integración con sistemas de gestión documental (DMS);
* sincronización con plataformas LMS;
* validación continua mediante integración continua (CI/CD);
* firma digital y control de integridad de documentos.

En ese momento, el proyecto habrá evolucionado desde un conjunto de cursos hacia un ecosistema editorial institucional completo, sostenible y preparado para crecer durante muchos años.
