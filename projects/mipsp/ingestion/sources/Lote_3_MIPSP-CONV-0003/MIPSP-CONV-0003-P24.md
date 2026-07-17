---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 24
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

MIPSP-Editor — EPIC-02 Core (Implementación)

Entendido. Continuamos con el proyecto **MIPSP-Editor**, en la **EPIC-02 — Core (Implementación)**.

Dado el contexto acumulado del proyecto, el objetivo de esta EPIC es construir el núcleo del editor institucional sobre el que posteriormente se integrarán las funciones de IA, cumplimiento normativo, control documental, publicación y colaboración.

Propongo desarrollar la EPIC con una arquitectura incremental, produciendo componentes completos, revisables y reutilizables.

---

# EPIC-02

## Core (Implementación)

Objetivo:

Construir el motor de edición documental que servirá como plataforma para todo el ecosistema MIPSP.

---

# Entregable CORE-01

## Arquitectura del Núcleo

```
MIPSP Editor

│
├── Presentation Layer
│      Editor UI
│      Ribbon
│      Panels
│      Context Menu
│
├── Application Layer
│      Commands
│      Undo/Redo
│      Clipboard
│      Sessions
│      Autosave
│
├── Document Layer
│      Document Model
│      Paragraph Model
│      Styles
│      Sections
│      Tables
│      Images
│
├── Formatting Engine
│      Typography
│      Lists
│      Numbering
│      TOC
│      References
│
├── Storage Layer
│      JSON
│      DOCX
│      PDF
│      Markdown
│
└── Infrastructure
       Logging
       Config
       Cache
       Plugins
```

---

# CORE-02

## Modelo del Documento

El documento se representa mediante un árbol.

```
Document

├── Metadata
├── Settings
├── Sections
│      ├── Paragraphs
│      ├── Tables
│      ├── Images
│      ├── Lists
│      └── Blocks
└── Resources
```

Cada nodo posee:

```
ID

Tipo

Padre

Hijos

Estilo

Propiedades

Estado

Versiones
```

---

# CORE-03

## Clases Principales

```
Document

Section

Paragraph

Run

Text

Table

Row

Cell

Image

Style

Theme

Reference

Bookmark

Comment

Revision

Footnote

Header

Footer

PageBreak

List

ListItem
```

---

# CORE-04

## Motor de Comandos

Todo cambio será un Command.

```
Command

Execute()

Undo()

Redo()

Validate()

Serialize()
```

Ejemplos

```
InsertTextCommand

DeleteTextCommand

PasteCommand

CutCommand

SplitParagraphCommand

MergeParagraphCommand

InsertImageCommand

InsertTableCommand

DeleteTableCommand

ApplyStyleCommand
```

Ventajas

* Undo infinito
* Redo
* Colaboración
* Sincronización
* Auditoría

---

# CORE-05

## Undo/Redo

Modelo

```
Undo Stack

↓

Command

↓

Document

↓

Redo Stack
```

Algoritmo

```
Execute

↓

Push Undo

↓

Clear Redo
```

Undo

```
Pop Undo

↓

Undo()

↓

Push Redo
```

Redo

```
Pop Redo

↓

Execute()

↓

Push Undo
```

---

# CORE-06

## Sistema de Selección

Tipos

```
Caret

Range

Block

Table

Image

Multiple Selection
```

Cada selección almacena

```
Nodo

Offset

Longitud

Dirección

Ancla
```

---

# CORE-07

## Cursor Engine

Responsabilidades

```
Mover cursor

Seleccionar

Expandir

Contraer

Palabras

Líneas

Párrafos

Documento completo
```

---

# CORE-08

## Clipboard

Operaciones

```
Copy

Cut

Paste

Paste Special
```

Formatos

```
Texto

HTML

Markdown

DOCX

Imagen

JSON interno
```

---

# CORE-09

## Motor de Estilos

Jerarquía

```
Theme

↓

Base Style

↓

Paragraph Style

↓

Character Style

↓

Direct Formatting
```

Prioridad

```
Formato directo

>

Carácter

>

Párrafo

>

Tema
```

---

# CORE-10

## Motor Tipográfico

Soporte para

```
Bold

Italic

Underline

Strike

Subscript

Superscript

Caps

Small Caps

Kerning

Tracking

Ligatures

OpenType
```

---

# CORE-11

## Layout Engine

Responsabilidades

```
Paginación

Saltos

Márgenes

Encabezados

Pies

Columnas

Orientación

Numeración

Notas

Tablas
```

---

# CORE-12

## Render Pipeline

```
Document

↓

Layout

↓

Pagination

↓

Glyph Generation

↓

Rendering

↓

Screen
```

---

# CORE-13

## Autosave

Estados

```
Dirty

Saving

Saved

Conflict
```

Frecuencia

```
cada 10 segundos

+

al perder foco

+

antes de imprimir

+

antes de exportar
```

---

# CORE-14

## Gestión de Sesión

```
Open

Close

Recover

Snapshot

Restore

Backup
```

---

# CORE-15

## Sistema de Eventos

Eventos

```
DocumentOpened

DocumentClosed

TextInserted

TextDeleted

SelectionChanged

StyleChanged

Undo

Redo

Save

Export

Import
```

---

# CORE-16

## Registro (Logging)

Niveles

```
Trace

Debug

Info

Warning

Error

Critical
```

Destino

```
Archivo

Consola

Diagnóstico

Telemetría
```

---

# CORE-17

## Arquitectura de Plugins

```
Editor

↓

Plugin Host

↓

API

↓

Plugin

↓

Commands

↓

Panels

↓

Menus
```

Tipos

```
Panel

Exportador

Importador

IA

Ortografía

Normativa

Plantillas

Firmas
```

---

# CORE-18

## Árbol de Dependencias

```
Editor

↓

Application

↓

Document Model

↓

Layout Engine

↓

Rendering

↓

Storage

↓

Infrastructure
```

No se permiten dependencias inversas.

---

# Resultado de la EPIC-02

Con esta implementación conceptual queda definida la base del editor:

* Modelo de documento basado en árbol con nodos tipados.
* Patrón **Command** para todas las operaciones editables, habilitando deshacer/rehacer, auditoría y colaboración.
* Motor de selección y cursor desacoplado del renderizado.
* Sistema jerárquico de estilos y formato.
* Pipeline de maquetación y renderizado independiente del almacenamiento.
* Infraestructura para autoguardado, recuperación de sesiones, registro y extensibilidad mediante plugins.

Este núcleo proporciona una base sólida para las siguientes fases del proyecto. La **EPIC-03** podrá incorporar el motor de persistencia (DOCX, PDF, Markdown y formato interno), mientras que las EPIC posteriores integrarán colaboración, revisión normativa y capacidades de inteligencia artificial sin modificar la arquitectura fundamental del editor.
