---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 4
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Continúa con lo planeado, tal cual.

Perfecto. A partir de este punto considero que el proyecto debe administrarse exactamente como lo haría una editorial técnica o una oficina de gestión documental (Document Control Office). Eso significa que dejaremos de pensar en "documentos individuales" y comenzaremos a producir **paquetes editoriales cerrados**, cada uno con criterios de aceptación, control de calidad y trazabilidad.

## Estado del proyecto

Con el cierre del **CUR-OPS-001** hemos alcanzado lo que, en ingeniería documental, se denomina una **Línea Base Editorial (Editorial Baseline 1.0)**.

A partir de ella, todos los entregables deberán cumplir los mismos estándares de:

* codificación documental;
* estructura editorial;
* identidad institucional;
* metadatos;
* control de versiones;
* referencias cruzadas;
* trazabilidad.

Esto permitirá que dentro de algunos años el MIPSP pueda seguir creciendo sin necesidad de rediseñar su arquitectura.

---

# Inicio del Paquete Editorial KEM-001

## Infraestructura Editorial Institucional

La primera entrega física del Kit Editorial Maestro quedará integrada por los siguientes componentes.

### KEM-001 — Plantilla Institucional de Documento Maestro

Esta plantilla será la base de todos los documentos del MIPSP y contendrá, como mínimo:

**Portada institucional**

* Logotipo institucional (marcador de posición).
* Nombre del MIPSP.
* Código documental.
* Título del documento.
* Versión.
* Clasificación documental.
* Estado del documento.
* Fecha de emisión.

**Página de control**

* Historial de versiones.
* Aprobaciones.
* Distribución controlada.
* Lista de revisiones.

**Ficha Técnica Editorial (FTE)**

| Campo             | Contenido                    |
| ----------------- | ---------------------------- |
| Código documental | Conforme al SICD-MIPSP       |
| Título            | Nombre oficial del documento |
| Versión           | Controlada por CCD-MIPSP     |
| Clasificación     | Uso interno / Controlado     |
| Elaboró           | Equipo Editorial             |
| Revisó            | Comité Técnico               |
| Aprobó            | Dirección Académica          |
| Fecha de emisión  | AAAA-MM-DD                   |
| Próxima revisión  | AAAA-MM-DD                   |

**Cuerpo del documento**

Con estilos normalizados para:

* Título de nivel 1 a 6.
* Texto normal.
* Procedimientos.
* Notas.
* Advertencias.
* Tablas.
* Figuras.
* Diagramas.
* Listas.
* Anexos.

**Elementos automáticos**

* Tabla de contenido.
* Índice de figuras.
* Índice de tablas.
* Referencias cruzadas.
* Numeración multinivel.
* Encabezados.
* Pies de página.
* Numeración automática de páginas.

---

## KEM-002 — Manual Editorial Institucional

Este documento establecerá las reglas de edición para toda la biblioteca.

Capítulos previstos:

1. Principios editoriales.
2. Convenciones tipográficas.
3. Estructura documental.
4. Normas para tablas.
5. Normas para figuras.
6. Uso de diagramas.
7. Referencias internas.
8. Control de versiones.
9. Reglas de nomenclatura.
10. Preparación para publicación PDF.

---

## KEM-003 — Catálogo Institucional de Estilos

Este documento definirá todos los estilos utilizados por Microsoft Word.

Ejemplo:

| Estilo              | Uso                     |
| ------------------- | ----------------------- |
| MIPSP-Título-1      | Capítulos               |
| MIPSP-Título-2      | Secciones               |
| MIPSP-Título-3      | Subsecciones            |
| MIPSP-Procedimiento | Procedimientos          |
| MIPSP-Tabla         | Tablas                  |
| MIPSP-Figura        | Figuras                 |
| MIPSP-Anexo         | Anexos                  |
| MIPSP-Nota          | Notas técnicas          |
| MIPSP-Advertencia   | Advertencias operativas |

Con ello, cualquier documento podrá modificarse globalmente sin alterar su consistencia.

---

## KEM-004 — Convención Institucional de Codificación

Propongo formalizar una sintaxis única para todos los documentos del MIPSP.

**Estructura general:**

```text
MIPSP-[Área]-[Proceso]-[Documento]-[Versión]
```

**Ejemplos:**

```text
CUR-OPS-001-D01-V1.0

CUR-OPS-001-D05-ETS01-V1.0

PNO-OPS-004-V1.0

FOR-OPS-012-V1.0

INS-OPS-003-V1.0

MAN-INS-001-V1.0
```

Esta convención facilitará búsquedas, auditorías, control de cambios y automatización.

---

## KEM-005 — Sistema Maestro de Metadatos

Todos los documentos compartirán un conjunto mínimo de metadatos.

| Campo                     | Obligatorio |
| ------------------------- | :---------: |
| Código documental         |      Sí     |
| Título                    |      Sí     |
| Autor responsable         |      Sí     |
| Unidad propietaria        |      Sí     |
| Versión                   |      Sí     |
| Estado                    |      Sí     |
| Fecha de emisión          |      Sí     |
| Fecha de revisión         |      Sí     |
| Nivel de confidencialidad |      Sí     |
| Palabras clave            |      Sí     |
| Documentos relacionados   |      Sí     |

---

# Criterios de calidad editorial

Antes de considerarse aprobado, cada documento deberá superar una lista de verificación con criterios como:

* codificación correcta;
* estructura conforme a la plantilla;
* estilos aplicados de manera consistente;
* numeración automática;
* referencias cruzadas válidas;
* tablas y figuras correctamente identificadas;
* historial de versiones actualizado;
* ortografía y terminología revisadas;
* correspondencia con el Registro Maestro Documental;
* conformidad con el Manual Editorial.

Este control permitirá que toda la colección mantenga un nivel homogéneo de calidad.

## Producción de archivos nativos

El siguiente hito será comenzar la **materialización** de esta infraestructura en archivos editables reales. La estrategia será generar un conjunto reducido de archivos por entrega (por ejemplo, la plantilla maestra en **.docx**, el registro documental en **.xlsx** y la plantilla de presentación en **.pptx**), validarlos y utilizarlos como base para toda la producción posterior.

Ese enfoque preservará la consistencia de la biblioteca y evitará retrabajos, manteniendo el estándar editorial que hemos definido para el MIPSP.
