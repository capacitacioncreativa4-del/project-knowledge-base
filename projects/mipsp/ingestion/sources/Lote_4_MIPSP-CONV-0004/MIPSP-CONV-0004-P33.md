---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 33
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente avance. Continuemos con el proyecto

Excelente. El Kernel comienza a tomar forma. Quiero hacer una observación arquitectónica antes de continuar.

Con los documentos que ya hemos construido, hemos respondido dos preguntas fundamentales:

* **¿Qué es un Objeto de Conocimiento?** → `KNOWLEDGE-OBJECT-MODEL.md`
* **¿Qué información mínima debe tener?** → `METADATA-MODEL.md`

Ahora debemos responder una tercera pregunta:

> **¿Cómo identificamos un objeto de manera única durante toda su vida?**

Esta decisión es crítica. Un mal esquema de identificadores puede generar colisiones, duplicados y referencias rotas cuando el PKB alcance cientos o miles de activos.

Por ello, el siguiente documento será uno de los pilares técnicos del Kernel.

---

# Sprint 0 – Incremento 3

## Documento 3 de 6

**Ruta**

```text
docs/kernel/IDENTIFIER-SCHEME.md
```

---

````markdown
---
id: PKB-KERNEL-IDSCHEME-001
title: Identifier Scheme
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: STD
domain: PKB
parent: PKB-KERNEL-KOM-001
tags:
  - identifiers
  - kernel
  - standard
---

# Esquema Institucional de Identificadores

## Propósito

Definir el sistema oficial de identificadores únicos y persistentes para todos los Objetos de Conocimiento del Project Knowledge Base (PKB).

Un identificador constituye la identidad permanente de un objeto y no deberá modificarse durante todo su ciclo de vida.

---

# Objetivos

El esquema debe garantizar:

- unicidad;
- estabilidad;
- legibilidad;
- escalabilidad;
- interoperabilidad;
- trazabilidad.

---

# Principios

## Permanencia

Una vez asignado, un identificador nunca cambia.

---

## Unicidad

No podrán existir dos objetos con el mismo identificador.

---

## Independencia

El identificador no dependerá de la ubicación física del archivo.

Mover un documento entre carpetas no modifica su identidad.

---

## Legibilidad

Los identificadores deberán poder interpretarse fácilmente por personas y herramientas.

---

## Escalabilidad

El esquema deberá soportar decenas de miles de objetos.

---

# Estructura General

```text
<DOMINIO>-<TIPO>-<SECUENCIA>
```

Ejemplo:

```text
PKB-ADR-0001
PKB-GOV-0003
PKB-STD-0012
MIPSP-REQ-0125
SIMPYME-DES-0048
CONDO-RSK-0009
```

---

# Componentes

## Dominio

Identifica el ámbito al que pertenece el objeto.

Ejemplos:

- PKB
- MIPSP
- SIMPYME
- CONDO
- EDITORIAL
- SHARED

---

## Tipo

Representa la naturaleza del objeto.

Catálogo inicial:

| Código | Tipo |
|---------|------|
| ADR | Architecture Decision Record |
| GOV | Governance |
| STD | Standard |
| TMP | Template |
| KNO | Knowledge Object |
| EPIC | Epic |
| REQ | Requirement |
| DES | Design |
| PROC | Procedure |
| REG | Register |
| RSK | Risk |
| MET | Metric |
| RES | Research |
| REF | Reference |

---

## Secuencia

Número correlativo de cuatro dígitos.

Ejemplos:

```text
0001
0002
0003
...
9999
```

Cuando sea necesario se ampliará la longitud sin alterar la estructura.

---

# Ejemplos

| Objeto | Identificador |
|----------|----------------|
| Manifest | PKB-GOV-0001 |
| Vision | PKB-GOV-0002 |
| Mission | PKB-GOV-0003 |
| Core Principles | PKB-GOV-0004 |
| Metadata Model | PKB-STD-0001 |
| Traceability Model | PKB-STD-0002 |
| ADR Inicial | PKB-ADR-0001 |
| Epic del proyecto MIPSP | MIPSP-EPIC-0001 |

---

# Reglas

1. El identificador será único.
2. Nunca se reutilizará un identificador.
3. Los identificadores archivados permanecerán reservados.
4. No se permitirán cambios retroactivos.
5. El identificador será independiente del nombre del archivo.

---

# Casos Especiales

## Plantillas

Las plantillas utilizarán el prefijo TMP.

Ejemplo:

```text
PKB-TMP-0003
```

---

## Investigación

```text
PKB-RES-0010
```

---

## Riesgos

```text
PKB-RSK-0007
```

---

## Proyectos

Cada proyecto mantendrá su propia secuencia interna.

Ejemplo:

```text
MIPSP-REQ-0001
MIPSP-REQ-0002
SIMPYME-REQ-0001
```

No existe conflicto porque pertenecen a dominios distintos.

---

# Validaciones

Todo identificador deberá cumplir:

- Dominio válido.
- Tipo válido.
- Secuencia numérica.
- Longitud correcta.
- Unicidad.

---

# Relaciones

## Documento superior

- KNOWLEDGE-OBJECT-MODEL.md

## Relacionados

- METADATA-MODEL.md
- TRACEABILITY-MODEL.md
- IDENTIFIER-REGISTRY.md

## Derivados

- VALIDATION-RULES.md
- AUTOMATED-ID-CHECKER.md

---

# Historial de Cambios

| Versión | Fecha | Descripción |
|----------|------------|-----------------------------|
|1.0.0|2026-07-09|Versión inicial institucional.|
````

---

# Justificación arquitectónica

Este estándar desacopla la **identidad lógica** del **archivo físico**. Esa separación es una práctica consolidada en gestión documental, arquitectura empresarial y sistemas de configuración. Gracias a ello podremos reorganizar carpetas, renombrar archivos o refactorizar la estructura del repositorio sin romper las referencias entre los objetos de conocimiento.

---

# Commit recomendado

```bash
docs(kernel): establish institutional identifier scheme
```

---

# Checklist de aceptación

* [ ] Guardado en `docs/kernel/IDENTIFIER-SCHEME.md`.
* [ ] Sintaxis institucional definida.
* [ ] Catálogo inicial de tipos incorporado.
* [ ] Reglas de unicidad y permanencia documentadas.
* [ ] Relaciones e historial de cambios incluidos.

---

# Revisión arquitectónica: una mejora para el PKB

Mientras redactaba este documento detecté una oportunidad de mejora respecto a lo que hemos construido hasta ahora.

En los primeros documentos utilizamos identificadores como:

```text
PKB-GOV-VISION-001
PKB-KERNEL-MANIFEST-001
```

Ahora estamos definiendo un esquema institucional normalizado como:

```text
PKB-GOV-0002
PKB-STD-0001
PKB-ADR-0001
```

**Mi recomendación es adoptar definitivamente este segundo esquema**. Es más simple, más consistente y mucho más fácil de automatizar. El nombre descriptivo seguirá estando en el campo `title` y en el nombre del archivo, mientras que el identificador se limitará a proporcionar una identidad estable y única.

Como consecuencia, en un incremento posterior realizaremos una **normalización del Sprint 0**, actualizando los identificadores de los documentos ya creados para que todos sigan el mismo estándar. Será un único commit de refactorización documental que dejará el Kernel completamente consistente antes de empezar a migrar proyectos reales. Esta pequeña inversión ahora evitará inconsistencias durante toda la vida del PKB.
