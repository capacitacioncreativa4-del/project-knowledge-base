---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 26
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece muy bien. Adelante con lo que sigue

Excelente. En este punto el proyecto ya cuenta con tres pilares arquitectónicos:

* **EPIC-01:** Arquitectura general.
* **EPIC-02:** Núcleo del editor.
* **EPIC-03:** Persistencia y sistema de archivos.

El siguiente componente es el que, desde el punto de vista técnico, representa el mayor desafío del editor: el **motor de composición (layout)**. Este subsistema determina cómo un árbol lógico de contenido se convierte en páginas con tipografía, tablas, imágenes, encabezados y pies, preservando la fidelidad visual. Es, en esencia, el equivalente al motor que utilizan procesadores de texto profesionales.

Considero conveniente desarrollar esta EPIC con un nivel de especificación suficiente para que, en una etapa posterior, pueda implementarse sin rediseños.

---

# MIPSP-Editor

# EPIC-04 — Rendering & Layout Engine

## Objetivos

Implementar un motor WYSIWYG ("What You See Is What You Get") que:

* Componga el documento desde su modelo lógico.
* Calcule la distribución de elementos.
* Gestione paginación dinámica.
* Soporte impresión profesional.
* Sirva como base para la exportación a PDF y otros formatos de presentación.

---

# RLE-001 — Arquitectura General

```text
              Document Model
                     │
             Layout Manager
                     │
        ┌────────────┼────────────┐
        │            │            │
 Paragraph      Table Engine   Image Engine
        │            │            │
        └────────────┼────────────┘
                     │
             Pagination Engine
                     │
              Render Pipeline
                     │
            Screen / Printer / PDF
```

La separación entre composición y renderizado permite reutilizar el mismo cálculo de diseño para pantalla, impresión y exportación.

---

# RLE-002 — Modelo de Layout

Se distinguen tres niveles:

1. **Modelo lógico**: estructura del documento (secciones, párrafos, tablas).
2. **Modelo de composición**: líneas, cajas, columnas y páginas.
3. **Modelo gráfico**: glifos, trazos e imágenes listos para dibujarse.

Esta separación reduce el acoplamiento y facilita optimizaciones.

---

# RLE-003 — Flujo de Composición

```text
Documento
    │
Resolución de estilos
    │
Medición tipográfica
    │
Construcción de líneas
    │
Distribución en bloques
    │
Paginación
    │
Renderizado
```

Cada etapa opera sobre el resultado de la anterior y puede invalidarse parcialmente cuando el usuario edita el documento.

---

# RLE-004 — Motor Tipográfico

El motor debe soportar:

* Fuentes TrueType y OpenType.
* Ligaduras.
* Kerning.
* Tracking.
* Variantes tipográficas.
* Escritura bidireccional.
* Unicode completo.
* Escalado de alta resolución.

Se propone una capa de abstracción sobre el motor de fuentes para facilitar la portabilidad.

---

# RLE-005 — Modelo de Cajas (Box Model)

Todo elemento se representa como una caja con dimensiones y márgenes:

```text
┌─────────────────────────────┐
│ Margen                      │
│ ┌─────────────────────────┐ │
│ │ Borde                   │ │
│ │ ┌─────────────────────┐ │ │
│ │ │ Contenido           │ │ │
│ │ └─────────────────────┘ │ │
│ └─────────────────────────┘ │
└─────────────────────────────┘
```

Este modelo unifica el tratamiento de párrafos, tablas, imágenes y otros objetos.

---

# RLE-006 — Composición de Párrafos

Proceso:

1. Medición de glifos.
2. Cálculo de espacios.
3. Ajuste de líneas.
4. Aplicación de sangrías.
5. Alineación (izquierda, derecha, centrado, justificado).
6. Control de viudas y huérfanas.
7. Separación silábica (cuando esté habilitada).

El algoritmo de composición debe admitir sustitución futura por métodos más avanzados, como Knuth-Plass.

---

# RLE-007 — Motor de Tablas

Cada tabla se resuelve mediante:

* Cálculo de anchos mínimos y máximos.
* Distribución automática del espacio.
* Fusión de celdas.
* División entre páginas.
* Repetición de encabezados.
* Alineación vertical y horizontal.
* Estilos de borde independientes.

---

# RLE-008 — Gestión de Imágenes

Tipos:

* En línea.
* Flotantes.
* Ancladas al párrafo.
* Ancladas a la página.

Operaciones:

* Escalado.
* Recorte.
* Rotación.
* Ajuste de texto alrededor.
* Conservación de proporciones.

---

# RLE-009 — Paginación

El motor debe recalcular únicamente las páginas afectadas por una modificación.

Reglas:

* Saltos manuales.
* Saltos automáticos.
* Inicio de sección.
* Encabezados y pies.
* Numeración.
* Márgenes.
* Orientación.
* Columnas.

---

# RLE-010 — Caché de Layout

Para evitar recomponer el documento completo:

```text
Documento
   │
Página modificada
   │
Recalcular
   │
Actualizar caché
```

La caché almacenará métricas tipográficas, geometría de objetos y páginas ya compuestas.

---

# RLE-011 — Render Pipeline

```text
Layout Tree
      │
Display List
      │
Rasterización
      │
Canvas
      │
Pantalla
```

El renderizado debe ser independiente del sistema operativo.

---

# RLE-012 — Motor de Impresión

Funciones:

* Vista previa.
* Impresión directa.
* Escalado.
* Selección de rango.
* Dúplex.
* Bandejas.
* Marcas de corte (opcional).
* Compatibilidad con PDF.

---

# RLE-013 — Rendimiento

Metas iniciales:

| Operación                           |                                              Objetivo |
| ----------------------------------- | ----------------------------------------------------: |
| Recalcular un párrafo               |                                                < 5 ms |
| Recalcular una página               |                                               < 40 ms |
| Desplazamiento continuo             |                                                60 FPS |
| Apertura de documento (200 páginas) |                                                 < 3 s |
| Zoom                                | Fluido, sin recomposición completa cuando sea posible |

---

# RLE-014 — Gestión de Zoom

Niveles:

* 25 %
* 50 %
* 75 %
* 100 %
* 125 %
* 150 %
* 200 %
* 400 %

El zoom modifica únicamente la representación visual; el modelo lógico permanece inalterado.

---

# RLE-015 — API del Motor

Interfaces principales:

```text
ILayoutEngine
IPaginationEngine
IRenderEngine
ITextMeasurer
IGlyphCache
ITableLayout
IImageLayout
IPrintEngine
```

Cada interfaz puede sustituirse por una implementación alternativa sin afectar al resto del sistema.

---

# RLE-016 — Estrategia de Pruebas

Se recomienda una batería de pruebas automatizadas con documentos de referencia ("golden documents") que cubran:

* Párrafos largos.
* Tablas complejas.
* Imágenes de alta resolución.
* Cambios de orientación.
* Encabezados y pies.
* Notas al pie.
* Numeración multinivel.
* Documentos de más de 1 000 páginas.

Las salidas visuales deben compararse automáticamente para detectar regresiones.

---

# RLE-017 — Preparación para Funciones Avanzadas

El diseño del motor deja puntos de extensión para incorporar en fases posteriores:

* Seguimiento de cambios y marcas de revisión.
* Comentarios y anotaciones.
* Edición colaborativa en tiempo real.
* Campos dinámicos (fecha, autor, numeración automática).
* Referencias cruzadas y tablas de contenido.
* Validaciones normativas específicas del MIPSP.
* Asistencia mediante IA para redacción, revisión y cumplimiento.

## Resultado de la EPIC-04

Con esta EPIC, el MIPSP-Editor queda dotado del diseño de un motor de composición profesional, desacoplado y orientado a alto rendimiento. La arquitectura separa claramente el modelo documental, la composición tipográfica y el renderizado, permitiendo evolucionar el sistema sin comprometer su estabilidad.

## Propuesta de evolución del proyecto

A partir de este punto, considero conveniente abandonar una secuencia de EPIC centradas exclusivamente en componentes técnicos y pasar a una organización por **subsistemas funcionales**, similar a la empleada en proyectos de gran escala (por ejemplo, LibreOffice, Visual Studio Code o IntelliJ IDEA). Esto permitirá construir una **biblioteca de especificaciones de ingeniería** más coherente y directamente utilizable para la implementación.

La siguiente etapa sería el **Subsystem-01 — Editing Engine**, dedicado a todas las operaciones de edición avanzada (cursor, selección, operaciones estructurales, tablas, listas, deshacer/rehacer avanzado, macros y automatización). A partir de ese subsistema podrán integrarse, de forma ordenada, la colaboración, el control documental y las capacidades de inteligencia artificial previstas para el MIPSP-Editor.
