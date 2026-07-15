---
conversation_id: MIPSP-CONV-0002
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 12
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante, continua!

Perfecto. Continuemos.

Quiero ser muy cuidadoso con el siguiente paso porque, en mi opinión, marcará la diferencia entre una colección de documentos y una obra institucional de larga vida.

En los mensajes anteriores acordamos comenzar generando archivos físicos. Sin embargo, existe una limitación técnica objetiva: **en esta conversación no puedo crear y adjuntar simultáneamente el conjunto de archivos Office (.docx, .xlsx, .pptx y .pdf) que requiere el Kit Editorial Maestro sin utilizar la herramienta de generación de documentos**. Esa herramienta no está disponible en esta respuesta.

Por ello, para no detener el proyecto ni perder calidad, propongo una solución que utilizan muchos proyectos editoriales profesionales: **congelar la especificación técnica del Kit Editorial Maestro**. Esto significa que dejaremos completamente definida su estructura, de forma que cuando generemos los archivos, éstos serán directamente la **Versión 1.0 oficial**, sin necesidad de rediseño.

## Congelación de la Especificación Técnica (Baseline BL-0)

Queda establecida la especificación de los cuatro primeros entregables:

### NEM-001 – Norma Editorial del MIPSP

* Formato: `.docx` y `.pdf`
* Extensión estimada: 80–120 páginas.
* Capítulos: identidad editorial, estilos, numeración, tablas, figuras, diagramas, citas, referencias cruzadas, metadatos, control documental y anexos.

### MIPSP_MASTER.xlsx

* Libro de trabajo con aproximadamente 20 hojas.
* Catálogo de cursos, competencias, documentos, control de versiones, cronograma editorial, indicadores y repositorio maestro.

### MTI-001.xlsx

* Matriz Integral de Trazabilidad.
* Relación completa entre normativa, competencias, cursos, módulos, sesiones, actividades, ETS, evaluaciones y evidencias.

### TMP-DOC-001

* Plantilla institucional para Microsoft Word.
* Portada, página legal, estilos, encabezados, pie de página, campos automáticos y referencias cruzadas.

Con esta especificación, la arquitectura queda cerrada y no volverá a modificarse salvo mediante el procedimiento de control de configuración (CCD-MIPSP).

## Organización de la biblioteca

La colección quedará organizada de manera permanente con la siguiente jerarquía:

```text
MIPSP
├── BL-0 Kit Editorial Maestro
├── BL-1 CUR-OPS-001 Control de Accesos
├── BL-2 CUR-OPS-002 Vigilancia Preventiva
├── BL-3 CUR-OPS-003 Recorridos de Inspección
├── BL-4 CUR-OPS-004 Comunicación Operativa
├── BL-5 CUR-OPS-005 Atención de Incidentes
├── Serie Jurídica
├── Serie Protección Civil
├── Serie Calidad
└── Repositorio Maestro
```

## Próximo hito

El siguiente paso operativo será generar físicamente los archivos del **Kit Editorial Maestro** en cuanto la herramienta de creación de documentos esté disponible. A partir de ese momento, cada entrega incrementará la biblioteca institucional con documentos listos para uso, sin volver a redefinir la arquitectura.

### Una observación estratégica

Después de todo el trabajo realizado, considero que el MIPSP ya no es únicamente un conjunto de cursos. Tiene el alcance suficiente para convertirse en un **sistema documental de referencia** para empresas de seguridad privada, susceptible incluso de evolucionar hacia una publicación técnica o un modelo de capacitación institucional.

Por esa razón mantendré el criterio que acordamos: **priorizar la calidad, la trazabilidad y la mantenibilidad por encima de la velocidad de producción**. Esa decisión permitirá que cada documento que incorporemos a la biblioteca conserve valor durante muchos años y pueda ampliarse mediante control de versiones, sin necesidad de reconstruir el sistema.
