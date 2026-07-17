---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 25
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Continuemos con lo que sigue.

Perfecto. El siguiente paso lógico no es añadir funcionalidades visibles, sino construir la infraestructura que permitirá que el editor sea robusto, interoperable y escalable. Corresponde desarrollar la **EPIC-03 — Persistence & File System**, donde se define cómo el editor representa, almacena, importa, exporta y versiona los documentos.

Esta EPIC es especialmente importante porque condiciona todas las posteriores (colaboración, IA, control documental y publicación institucional). Una mala arquitectura de persistencia suele ser muy difícil de corregir más adelante.

---

# MIPSP-Editor

# EPIC-03 — Persistence & File System

## Objetivos

Diseñar e implementar el subsistema encargado de:

* Modelo de persistencia.
* Formato nativo.
* Importación.
* Exportación.
* Versionado.
* Recuperación.
* Integridad.
* Compatibilidad.

---

# PFS-001 — Arquitectura de Persistencia

```text
                  Editor Core
                      │
              Document Model
                      │
            Persistence Manager
       ┌─────────┼──────────┬──────────┐
       │         │          │          │
 Native Format  DOCX      PDF     Markdown
       │         │          │          │
       └─────────┴──────────┴──────────┘
                      │
              Storage Provider
                      │
        Local / Network / Cloud
```

### Componentes

| Componente          | Responsabilidad                         |
| ------------------- | --------------------------------------- |
| Persistence Manager | Coordinar lectura y escritura           |
| Serializer          | Convertir objetos a formato persistente |
| Deserializer        | Reconstruir el árbol documental         |
| Storage Provider    | Acceso al medio físico                  |
| Recovery Manager    | Recuperación ante fallos                |
| Version Manager     | Control de revisiones                   |
| Integrity Checker   | Validación del archivo                  |

---

# PFS-002 — Formato Nativo (.mipsp)

Se propone un formato abierto basado en ZIP, similar en concepto a DOCX u ODT.

```text
Manual.mipsp

├── manifest.json
├── document.json
├── metadata.json
├── styles.json
├── settings.json
├── revisions.json
├── resources/
│     logo.png
│     imagen01.jpg
│     firma.svg
├── fonts/
├── attachments/
└── signatures/
```

Ventajas:

* Compresión.
* Facilidad de inspección.
* Extensibilidad.
* Recuperación parcial.
* Compatibilidad entre versiones.

---

# PFS-003 — Manifest

```json
{
  "formatVersion": "1.0",
  "documentId": "...",
  "created": "...",
  "modified": "...",
  "generator": "MIPSP Editor",
  "encoding": "UTF-8",
  "compression": "ZIP",
  "checksum": "SHA-256"
}
```

---

# PFS-004 — Document Serializer

Flujo:

```text
Document

↓

Tree Walker

↓

Serializer

↓

JSON

↓

ZIP

↓

Archivo .mipsp
```

Cada nodo se serializa de forma independiente.

---

# PFS-005 — Deserializer

```text
Archivo

↓

ZIP

↓

JSON

↓

Object Factory

↓

Document Tree

↓

Validation

↓

Editor
```

---

# PFS-006 — Modelo de Versionado

Cada documento mantiene un historial estructurado.

```text
Documento

↓

Versión 1

↓

Versión 2

↓

Versión 3

↓

Versión N
```

Cada revisión contiene:

* Identificador único.
* Autor.
* Fecha y hora.
* Descripción.
* Operaciones realizadas.
* Hash de integridad.

---

# PFS-007 — Snapshot Manager

Dos tipos de almacenamiento:

## Snapshots completos

```text
Documento completo
```

Uso:

* Recuperación rápida.
* Copias de seguridad.

## Snapshots incrementales

```text
Versión 1

↓

Cambios

↓

Versión 2

↓

Cambios

↓

Versión 3
```

Reduce el consumo de almacenamiento.

---

# PFS-008 — Recovery Journal

Antes de modificar un documento:

```text
Documento

↓

Journal

↓

Operación

↓

Commit
```

Si ocurre un fallo:

```text
Recovery Journal

↓

Rollback

↓

Documento consistente
```

Este mecanismo evita corrupción por cierres inesperados.

---

# PFS-009 — Autosave Repository

```text
Autosave/

Documento01/

Snapshot01

Snapshot02

Snapshot03
```

Política recomendada:

* Últimos 20 autoguardados.
* Eliminación automática de los más antiguos.
* Compresión en segundo plano.

---

# PFS-010 — Integrity Manager

Cada archivo incorpora:

* SHA-256 del contenido.
* Hash por recurso.
* Validación del manifiesto.
* Comprobación de dependencias.

Proceso:

```text
Abrir archivo

↓

Validar manifest

↓

Validar recursos

↓

Validar hashes

↓

Abrir documento
```

---

# PFS-011 — Import Framework

Arquitectura basada en adaptadores:

```text
Importer

↓

DOCX Adapter

PDF Adapter

Markdown Adapter

HTML Adapter

TXT Adapter

ODT Adapter
```

Cada adaptador implementa una interfaz común.

---

# PFS-012 — Export Framework

```text
Exporter

↓

PDF

DOCX

HTML

Markdown

ODT

TXT

EPUB
```

Permite incorporar nuevos formatos sin modificar el núcleo.

---

# PFS-013 — Recursos Embebidos

Todos los recursos se gestionan mediante un catálogo interno.

```text
Resources

↓

Images

↓

Fonts

↓

Attachments

↓

Media

↓

Signatures
```

Cada recurso mantiene:

* UUID.
* Tipo MIME.
* Tamaño.
* Hash.
* Referencias en el documento.

---

# PFS-014 — Compatibilidad entre Versiones

Reglas:

1. Una versión nueva debe abrir documentos antiguos.
2. La migración será automática cuando sea posible.
3. Las funciones no soportadas se conservarán como metadatos.
4. Toda migración quedará registrada en el historial del documento.

---

# PFS-015 — API de Persistencia

Interfaces propuestas:

```text
IDocumentSerializer

IDocumentDeserializer

IImporter

IExporter

IStorageProvider

IRecoveryManager

IVersionManager

IIntegrityValidator
```

Esta separación permite sustituir implementaciones sin afectar al resto del sistema.

---

# PFS-016 — Estrategia de Almacenamiento

Se definen tres proveedores principales:

| Proveedor       | Uso previsto                                |
| --------------- | ------------------------------------------- |
| Local Storage   | Trabajo individual y operación sin conexión |
| Network Storage | Repositorios institucionales compartidos    |
| Cloud Storage   | Sincronización y colaboración distribuida   |

Todos deben implementar la misma interfaz para garantizar independencia del medio físico.

---

# PFS-017 — Requisitos No Funcionales

| Requisito                                | Meta                                                    |
| ---------------------------------------- | ------------------------------------------------------- |
| Apertura de documentos de 100 MB         | < 5 s                                                   |
| Guardado incremental                     | < 2 s                                                   |
| Recuperación tras fallo                  | < 30 s                                                  |
| Integridad verificada                    | 100 %                                                   |
| Compatibilidad hacia atrás               | Sí                                                      |
| Consumo de memoria durante serialización | Controlado mediante procesamiento por flujo (streaming) |

---

## Resultado de la EPIC-03

Al concluir esta etapa, el MIPSP-Editor dispondrá de un subsistema de persistencia con las siguientes capacidades:

* Formato nativo abierto, extensible y verificable (.mipsp).
* Arquitectura desacoplada para importación y exportación de múltiples formatos.
* Versionado estructurado y recuperación ante fallos mediante journaling y snapshots.
* Validación criptográfica de integridad.
* Gestión unificada de recursos embebidos.
* Compatibilidad evolutiva entre versiones del formato.

Con la EPIC-03 finalizada, el proyecto contará con una base de almacenamiento preparada para soportar edición colaborativa, control documental institucional y trazabilidad completa. La siguiente fase natural será la **EPIC-04 — Rendering & Layout Engine**, donde se implementará el motor de composición tipográfica, paginación y renderizado WYSIWYG de calidad profesional, equivalente al de un procesador de textos de escritorio.
