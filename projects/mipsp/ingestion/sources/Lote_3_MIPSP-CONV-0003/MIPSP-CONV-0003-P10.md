---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 10
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. A partir de esta entrega comenzaremos el **Sprint 2**, que, desde mi perspectiva, es el más importante de todo el MIPSP-Editor. Si el Sprint 1 construyó el modelo de dominio, el Sprint 2 construirá el **motor de generación DOCX**, sobre el cual descansará toda la producción editorial del proyecto.

No comenzaremos escribiendo documentos específicos (como el CUR-OPS-001-D01), sino desarrollando primero un **framework documental** reutilizable. Esta decisión permitirá que cualquier documento futuro (manuales, procedimientos, formatos, ETS, etc.) se genere mediante el mismo conjunto de componentes.

---

# Sprint 2 — Framework de generación DOCX

## Objetivo

Desarrollar un conjunto de clases que encapsulen toda la lógica de creación de documentos Word utilizando `python-docx`, de forma desacoplada del contenido.

Arquitectura propuesta:

```text
builders/
    course_builder.py
          │
          ▼
exporters/
    docx_exporter.py
          │
          ▼
framework/
    document_writer.py
    style_manager.py
    section_writer.py
    table_writer.py
    header_footer.py
    toc_writer.py
    cover_page.py
```

Los *builders* describen **qué** documento construir. El *framework* decide **cómo** escribirlo en Word.

---

# Módulo FW-001 — DocumentWriter

Este será el punto de entrada para la creación de cualquier documento.

Responsabilidades:

* Crear el documento.
* Aplicar la configuración institucional.
* Registrar metadatos.
* Delegar la escritura de las distintas secciones.
* Invocar el guardado.

Interfaz prevista:

```python
writer = DocumentWriter(configuration)

writer.create(metadata)

writer.add_cover()

writer.add_table_of_contents()

writer.add_section(...)

writer.save("CUR-OPS-001-D01.docx")
```

El resto del sistema nunca interactuará directamente con `python-docx`.

---

# Módulo FW-002 — StyleManager

Una de las principales fuentes de inconsistencias en proyectos documentales es la aplicación manual de estilos. Para evitarlo, centralizaremos su definición en un único administrador.

Responsabilidades:

* Registrar estilos institucionales.
* Verificar su existencia.
* Aplicarlos de forma uniforme.
* Evitar la creación de estilos duplicados.

Catálogo inicial:

| Código        | Descripción             |
| ------------- | ----------------------- |
| MIPSP-Title-1 | Título de capítulo      |
| MIPSP-Title-2 | Sección                 |
| MIPSP-Title-3 | Subsección              |
| MIPSP-Body    | Texto principal         |
| MIPSP-Table   | Contenido de tablas     |
| MIPSP-Caption | Pie de figuras y tablas |
| MIPSP-Note    | Notas técnicas          |
| MIPSP-Warning | Advertencias            |
| MIPSP-Annex   | Encabezados de anexos   |

Con ello, cualquier cambio tipográfico afectará automáticamente a toda la colección.

---

# Módulo FW-003 — CoverPage

Toda publicación del MIPSP tendrá una portada normalizada.

Elementos previstos:

* Nombre institucional.
* Título del documento.
* Código documental.
* Versión.
* Clasificación.
* Estado.
* Fecha de emisión.
* Responsable del documento.
* Espacio reservado para logotipo.
* Código QR (opcional en versiones futuras).

La portada se generará a partir de `DocumentMetadata`, sin necesidad de editarla manualmente.

---

# Módulo FW-004 — HeaderFooterManager

Encabezados y pies de página institucionales.

Encabezado:

```text
MIPSP | CUR-OPS-001-D01 | Versión 1.0
```

Pie:

```text
Clasificación: Uso interno | Página X de Y
```

En versiones posteriores podremos incorporar campos automáticos y numeración avanzada cuando el documento se abra en Microsoft Word.

---

# Módulo FW-005 — SectionWriter

La escritura de secciones no dependerá del documento específico.

Interfaz conceptual:

```python
section = Section(
    title="Objetivo",
    level=1,
    paragraphs=[...]
)

writer.add_section(section)
```

Esto permitirá reutilizar la misma lógica en cualquier tipo documental.

---

# Módulo FW-006 — TableWriter

Las tablas serán un componente independiente.

Capacidades previstas:

* Creación de tablas con encabezado institucional.
* Aplicación de estilos.
* Ajuste automático de ancho.
* Repetición del encabezado en cambios de página (cuando el formato lo permita).
* Numeración correlativa.

---

# Módulo FW-007 — FigureManager

Aunque inicialmente utilizaremos imágenes estáticas, prepararemos el sistema para administrar figuras.

Cada figura dispondrá de:

* identificador;
* pie descriptivo;
* texto alternativo;
* referencia cruzada;
* ruta del recurso.

Esto facilitará la accesibilidad y la reutilización de diagramas.

---

# Módulo FW-008 — TableOfContentsManager

La generación del índice seguirá una estrategia híbrida.

El documento contendrá los campos necesarios para que Microsoft Word pueda actualizar automáticamente la tabla de contenido, mientras que el motor editorial mantendrá la estructura jerárquica de títulos.

---

# Pruebas del Sprint 2

Cada componente tendrá pruebas unitarias específicas. Algunos ejemplos:

* Verificar que el documento se crea correctamente.
* Comprobar que la portada contiene los metadatos esperados.
* Confirmar que los estilos se aplican a los títulos.
* Validar que las tablas mantienen el formato institucional.
* Comprobar que el encabezado y el pie se generan en todas las secciones.

---

# Primera aplicación del framework

Una vez finalizado este framework, el primer documento que produciremos será:

```text
CUR-OPS-001-D01
Programa Institucional
```

El objetivo es que el código para construirlo sea declarativo, por ejemplo:

```python
programa = CourseProgram(...)
builder = CourseBuilder(programa)
builder.build()
```

Es decir, el contenido del documento estará completamente separado de la lógica de generación.

## Decisión estratégica adicional

Antes de pasar al generador de Excel, propongo desarrollar un **módulo de serialización documental**. Este componente permitirá almacenar el contenido de un documento en un formato neutral (por ejemplo, JSON o YAML) antes de exportarlo. Con ello, el mismo contenido podrá transformarse posteriormente en `.docx`, `.pdf`, `.pptx`, HTML o Markdown sin duplicar la lógica de negocio.

Esta decisión convertirá al MIPSP-Editor en una plataforma editorial multiformato y reforzará la sostenibilidad del proyecto a largo plazo. Es una inversión de arquitectura que incrementará la reutilización del código y facilitará futuras integraciones con sistemas de gestión documental (DMS) o plataformas de aprendizaje (LMS).
