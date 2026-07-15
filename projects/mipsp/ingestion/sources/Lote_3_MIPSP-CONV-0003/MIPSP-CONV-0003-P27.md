---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 27
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Continúa con lo que sigue

Continuamos con el desarrollo del **MIPSP-Editor**. Después de completar:

* **EPIC-02 — Core (Implementación)**
* **EPIC-03 — Persistence & File System**
* **EPIC-04 — Rendering & Layout Engine**

el siguiente paso natural es construir el subsistema que conecta la arquitectura interna con la experiencia real del usuario: el **motor de edición**.

Este componente será el encargado de transformar el editor de un visor documental en una herramienta profesional de creación y mantenimiento de documentos institucionales.

---

# MIPSP-Editor

# SUBSYSTEM-01 — Editing Engine

## Objetivo

Implementar el núcleo operativo de edición mediante el cual el usuario puede:

* Insertar y modificar contenido.
* Navegar dentro del documento.
* Seleccionar elementos.
* Aplicar formato.
* Manipular estructuras complejas.
* Ejecutar operaciones reversibles.
* Automatizar tareas repetitivas.

---

# EE-001 — Arquitectura del Motor de Edición

```text
                  User Input
                      │
        ┌─────────────┼─────────────┐
        │             │             │
    Keyboard       Mouse        Commands
        │             │             │
        └─────────────┼─────────────┘
                      │
              Editing Controller
                      │
        ┌─────────────┼─────────────┐
        │             │             │
 Cursor Engine   Selection     Command Engine
        │             │             │
        └─────────────┼─────────────┘
                      │
              Document Model
                      │
              Layout Engine
```

---

# EE-002 — Controlador de Edición

El **Editing Controller** será el coordinador central.

Responsabilidades:

* Interpretar acciones del usuario.
* Crear comandos.
* Validar operaciones.
* Actualizar el modelo documental.
* Solicitar recomposición del layout.
* Gestionar estados de edición.

Ejemplo:

```text
Usuario escribe "A"

↓

Keyboard Event

↓

InsertTextCommand

↓

Document Model

↓

Layout Update

↓

Render Refresh
```

---

# EE-003 — Modelo de Cursor

El cursor no debe ser una coordenada visual, sino una referencia lógica.

Modelo:

```text
Cursor

├── Document ID
├── Node ID
├── Offset
├── Position Type
└── Affinity
```

Ejemplo:

```text
Paragraph-015

Offset: 37

Affinity: Forward
```

Esto permite mantener la posición incluso cuando cambia la distribución visual.

---

# EE-004 — Tipos de Cursor

El sistema soportará:

## Cursor de texto

Para escritura normal.

## Cursor estructural

Para seleccionar:

* Párrafos.
* Secciones.
* Tablas.
* Bloques.

## Cursor de objeto

Para:

* Imágenes.
* Diagramas.
* Elementos embebidos.

---

# EE-005 — Motor de Selección

Modelo:

```text
Selection

├── Anchor
├── Active Point
├── Direction
├── Scope
└── Type
```

Tipos:

```text
Character Selection

Word Selection

Line Selection

Paragraph Selection

Block Selection

Table Selection

Document Selection
```

---

# EE-006 — Navegación Documental

Soporte:

## Movimiento básico

* Carácter.
* Palabra.
* Línea.
* Párrafo.

## Movimiento estructural

* Inicio de sección.
* Fin de sección.
* Inicio del documento.
* Marcadores.
* Referencias.

## Navegación profesional

* Historial de posiciones.
* Última edición.
* Comentarios.
* Revisiones.

---

# EE-007 — Inserción de Contenido

Tipos soportados:

```text
Text

Paragraph

Heading

List

Table

Image

Reference

Footnote

Comment

Page Break

Section Break
```

Cada inserción genera un comando.

Ejemplo:

```text
InsertParagraphCommand

Execute()

↓

Document Tree Update

↓

Layout Reflow

↓

Render
```

---

# EE-008 — Eliminación Inteligente

El borrado debe considerar contexto.

Ejemplos:

Eliminar texto:

```text
"Seguridad|Privada"

↓

"Seguridad Privada"
```

Eliminar párrafo:

```text
Paragraph A

Paragraph B

↓

Merge automático
```

Eliminar tabla:

```text
Tabla completa

↓

Confirmación

↓

Command reversible
```

---

# EE-009 — Portapapeles Avanzado

El sistema manejará múltiples representaciones:

```text
Clipboard Object

├── Plain Text
├── Rich Text
├── HTML
├── Markdown
├── Internal XML
├── Image
└── MIPSP Fragment
```

Esto permite copiar contenido entre documentos conservando estructura.

---

# EE-010 — Formato y Aplicación de Estilos

Aplicación:

```text
Selection

↓

Style Command

↓

Document Model

↓

Layout Refresh
```

Ejemplos:

```text
ApplyHeadingStyle

ApplyTableStyle

ApplyCharacterFormat

ApplyParagraphFormat
```

---

# EE-011 — Listas y Numeración

Motor especializado para:

* Listas simples.
* Listas multinivel.
* Numeración jurídica.
* Incisos.
* Anexos.
* Apartados normativos.

Ejemplo institucional:

```text
1.
   1.1
      1.1.1
         a)
         b)
```

Debe mantener continuidad aunque existan inserciones intermedias.

---

# EE-012 — Operaciones de Bloque

Permite manipular grandes estructuras:

* Mover capítulos completos.
* Reordenar anexos.
* Duplicar procedimientos.
* Convertir secciones.
* Aplicar plantillas.

Ejemplo:

```text
Mover Capítulo III

↓

Actualizar referencias

↓

Actualizar índice

↓

Actualizar numeración
```

---

# EE-013 — Undo/Redo Profesional

Evolución del modelo anterior:

## Nivel usuario

Acciones visibles:

```text
Escribir

Borrar

Cambiar formato
```

## Nivel sistema

Operaciones internas:

```text
Actualizar layout

Actualizar referencias

Actualizar índice
```

El usuario únicamente ve acciones semánticas.

---

# EE-014 — Transacciones de Edición

Operaciones complejas se ejecutan como una unidad.

Ejemplo:

Cambiar título de capítulo:

```text
BEGIN TRANSACTION

Cambiar texto

Actualizar índice

Actualizar referencias

Actualizar numeración

Actualizar historial

COMMIT
```

Si falla:

```text
ROLLBACK
```

---

# EE-015 — Editor Multicapa

El usuario trabajará sobre capas:

```text
Contenido

↓

Estructura

↓

Formato

↓

Revisión

↓

Metadatos

↓

Cumplimiento
```

Esto es fundamental para documentos institucionales.

---

# EE-016 — Automatización

Se incorpora un sistema de macros:

```text
Macro

├── Name
├── Commands
├── Parameters
└── Permissions
```

Ejemplos:

* Generar portada.
* Insertar índice.
* Aplicar formato institucional.
* Preparar publicación.

---

# EE-017 — API del Editing Engine

Interfaces:

```text
IEditingController

ICursorManager

ISelectionManager

ICommandManager

IClipboardManager

IStyleManager

ITransactionManager

IMacroEngine
```

---

# EE-018 — Preparación para IA

El motor queda preparado para recibir asistencia inteligente:

Ejemplos:

* "Reescribe este procedimiento con lenguaje normativo".
* "Detecta inconsistencias".
* "Compara contra una norma".
* "Sugiere estructura documental".
* "Genera índice automáticamente".

La IA no modificará directamente el documento; siempre actuará mediante comandos auditables.

---

# Resultado del SUBSYSTEM-01 — Editing Engine

Con este subsistema se completa la capa de interacción profesional del editor:

✅ Edición estructurada.
✅ Cursor lógico independiente del renderizado.
✅ Selección avanzada.
✅ Operaciones reversibles.
✅ Transacciones seguras.
✅ Manipulación de documentos complejos.
✅ Base para automatización e IA controlada.

---

## Siguiente etapa recomendada

El siguiente bloque debe ser:

# SUBSYSTEM-02 — Document Intelligence Layer

Aquí se construirá la capa diferencial del MIPSP-Editor:

* Análisis semántico del documento.
* Clasificación automática.
* Metadatos inteligentes.
* Reglas institucionales.
* Detección de incumplimientos.
* Motor de trazabilidad.
* Preparación para IA generativa especializada.

Esta capa es la que convertirá al editor de un procesador de textos avanzado en una plataforma de gestión documental inteligente.
