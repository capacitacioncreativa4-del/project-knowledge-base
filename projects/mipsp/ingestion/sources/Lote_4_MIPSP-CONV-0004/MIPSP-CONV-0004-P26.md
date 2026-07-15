---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 26
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Prosigamos

Excelente. A partir de este punto comenzamos a construir el **núcleo documental** del PKB. Ya no voy a describir qué haremos: voy a producir contenido que permanecerá en el repositorio durante años.

Coincido con la estrategia de no usar Codex todavía. En esta etapa, el valor está en la arquitectura y la gobernanza, no en la automatización.

---

# Sprint 0 – Incremento 2

## Documento 2 de 6

**Ruta**

```text
docs/kernel/PKB-MANIFEST.md
```

---

```markdown
---
id: PKB-KERNEL-MANIFEST-001
title: Project Knowledge Base Manifest
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-08
type: Manifest
---

# Project Knowledge Base Manifest

## Preámbulo

El Project Knowledge Base (PKB) constituye el sistema institucional para la organización, preservación, evolución y reutilización del conocimiento generado durante el desarrollo de proyectos.

Este documento establece los principios permanentes que gobiernan la evolución del PKB.

Todo documento, proyecto, plantilla, automatización o decisión arquitectónica deberá ser consistente con este Manifest o justificar explícitamente su excepción mediante un Architecture Decision Record (ADR).

---

# Misión del sistema

Preservar el conocimiento de manera estructurada, trazable, reutilizable y verificable durante todo su ciclo de vida.

---

# Visión

Convertirse en una plataforma de conocimiento capaz de integrar proyectos de diferentes dominios, manteniendo consistencia documental, trazabilidad completa y colaboración efectiva entre personas y herramientas de inteligencia artificial.

---

# Principios Fundamentales

## 1. El conocimiento es un activo institucional

Los documentos son representaciones del conocimiento.

El conocimiento tiene prioridad sobre el formato.

---

## 2. Una única fuente de verdad

Toda información oficial existirá en un único lugar del repositorio.

No se permitirán duplicidades.

---

## 3. Todo posee versión

Cada activo tendrá:

- identificador
- versión
- estado
- historial
- responsable

---

## 4. La documentación es código

La documentación seguirá las mismas prácticas utilizadas para el desarrollo de software:

- Git
- Pull Requests
- Revisiones
- Releases
- Versionado

---

## 5. Todo cambio es trazable

Toda modificación importante deberá poder responder:

- ¿Qué cambió?
- ¿Por qué cambió?
- ¿Quién lo aprobó?
- ¿Qué impacto tiene?

---

## 6. Arquitectura antes que implementación

Las decisiones arquitectónicas preceden al desarrollo.

---

## 7. Reutilización

Todo conocimiento deberá diseñarse para poder reutilizarse.

---

## 8. Modularidad

Cada proyecto será independiente.

Los componentes compartidos vivirán fuera de los proyectos.

---

## 9. Estándares abiertos

El PKB utilizará formatos abiertos siempre que sea posible.

Ejemplos:

- Markdown
- YAML
- Mermaid
- CSV
- JSON
- XLSX

---

## 10. Preparado para IA

Los documentos deberán poder ser comprendidos por personas y agentes inteligentes.

---

# Objetivos Estratégicos

1. Centralizar el conocimiento.

2. Reducir duplicidad.

3. Mejorar trazabilidad.

4. Facilitar mantenimiento.

5. Preservar decisiones.

6. Incrementar reutilización.

7. Automatizar tareas repetitivas.

8. Escalar sin reorganización.

---

# Alcance

El PKB administra:

- proyectos
- investigación
- arquitectura
- plantillas
- registros
- decisiones
- activos compartidos
- automatización

No administra:

- código fuente de aplicaciones (salvo utilidades del propio PKB)
- información temporal sin valor documental
- archivos personales ajenos a los proyectos

---

# Gobierno

La evolución del PKB se realiza mediante:

- Releases
- ADR
- Control de versiones
- Revisiones documentales
- Gestión de cambios

---

# Política de Calidad

Todo activo deberá cumplir:

- identificación única;
- metadatos completos;
- relaciones explícitas;
- historial de cambios;
- responsable asignado;
- estado documental.

---

# Política de Evolución

El PKB evolucionará mediante incrementos pequeños, verificables y compatibles hacia atrás siempre que sea posible.

Las decisiones estructurales deberán documentarse mediante ADR.

---

# Vigencia

Este Manifest constituye el documento rector del PKB.

Toda excepción deberá justificarse mediante una decisión arquitectónica aprobada.
```

---

# Justificación arquitectónica

Este documento tiene un papel similar al de una **constitución**. Debe cambiar muy poco a lo largo del tiempo. Mientras que el `README.md` explica qué es el proyecto, el `PKB-MANIFEST.md` define **las reglas que gobiernan su evolución**.

---

# Commit recomendado

```bash
docs(kernel): add Project Knowledge Base Manifest
```

---

# Checklist de aceptación

* [ ] Guardado en `docs/kernel/PKB-MANIFEST.md`.
* [ ] Incluye metadatos YAML.
* [ ] No contiene referencias a conversaciones.
* [ ] Es consistente con el `README.md`.
* [ ] Puede citarse como documento rector del repositorio.

---

# Siguiente documento

En el próximo incremento construiremos **`docs/governance/VISION.md`**, pero quiero introducir una mejora metodológica que considero muy valiosa.

Hasta ahora hemos pensado en documentos individuales. A partir del siguiente documento comenzaremos a crear una **red documental**. Cada archivo incluirá una sección final llamada **"Relaciones"**, por ejemplo:

```markdown
## Relaciones

### Documentos superiores
- PKB-MANIFEST.md

### Documentos relacionados
- MISSION.md
- CORE-PRINCIPLES.md
- ADR-0001-Repository-Architecture.md

### Documentos derivados
- ROADMAP.md
- DOCUMENT-STANDARD.md
```

Con este mecanismo construiremos una **trazabilidad navegable** entre los documentos del PKB. Más adelante, cuando incorporemos scripts y automatizaciones (ahí sí utilizaremos Codex), podremos generar automáticamente mapas de relaciones, índices y un grafo de conocimiento a partir de estos enlaces. Creo que esa será una de las capacidades más valiosas del sistema a largo plazo.
