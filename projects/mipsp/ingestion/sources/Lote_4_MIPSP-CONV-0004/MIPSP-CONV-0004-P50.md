---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 50
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente el gran avance que registra el proyecto. Sigamos adelante

Excelente. Después de revisar la evolución completa del proyecto, considero que estamos en un momento donde conviene cambiar la forma de trabajar para acelerar el desarrollo sin perder calidad.

Hasta ahora hemos trabajado principalmente con una secuencia de **arquitectura → diseño → implementación**. Esa etapa era necesaria porque estábamos definiendo los fundamentos del PKB.

A partir de este punto propongo entrar en lo que llamaría la **Fase de Industrialización**.

No cambiaremos la visión del proyecto; cambiaremos la forma de construirlo.

---

# FASE 7 — Industrialización del PKB

El objetivo de esta fase es transformar el PKB en una plataforma que pueda crecer durante años sin perder consistencia.

Para ello propongo dividir el desarrollo en cinco corrientes de trabajo permanentes.

```text
                    PKB PROGRAM
                         │
 ┌──────────┬────────────┼────────────┬────────────┐
 │          │            │            │            │
 ▼          ▼            ▼            ▼            ▼
Platform  Knowledge   Projects   Automation   Quality
```

Cada una evolucionará de forma independiente, pero sincronizada mediante versiones.

---

# Corriente 1 — PKB Platform

Aquí vive el software.

Objetivo para la versión **0.4.0**:

```text
CLI

Repository Scanner

Metadata Engine

Knowledge Registry

Validation Engine

Reporting Engine

Plugin Framework
```

Esta corriente tendrá ciclos de liberación propios.

---

# Corriente 2 — Knowledge Library

Aquí vive el conocimiento institucional.

```text
Knowledge

├── Standards

├── ADR

├── Templates

├── Research

├── Governance

├── Architecture

└── References
```

Esta biblioteca será reutilizada por todos los proyectos.

---

# Corriente 3 — Projects

Aquí viven los proyectos reales.

```text
Projects

MIPSP

SIM-PYME

Condominios

Kit Editorial

Manualidades
```

Cada proyecto será tratado como un **dominio independiente**, con su propio manifiesto, métricas y ciclo de evolución.

---

# Corriente 4 — Automation

La automatización dejará de limitarse a GitHub Actions.

Propondría organizarla así:

```text
automation/

ci/

quality/

release/

migration/

ingestion/

reporting/
```

Esto facilitará incorporar nuevos procesos sin afectar al núcleo.

---

# Corriente 5 — Quality Engineering

Ésta es probablemente la más importante para el futuro.

Propongo crear un subsistema específico para calidad.

```text
quality/

lint/

validation/

testing/

coverage/

metrics/

performance/
```

Su objetivo será garantizar que cualquier cambio preserve la estabilidad del PKB.

---

# EPIC S6-001 — Plugin Framework

Quiero proponer una evolución que permitirá mantener el núcleo pequeño.

En lugar de que todas las funcionalidades formen parte del core, construiremos una arquitectura basada en extensiones.

```text
PKB Core

│

├── Repository

├── Metadata

├── Registry

├── Validation

└── Plugins

        │

        ▼

+------------------------+

Inventory Plugin

Doctor Plugin

Graph Plugin

Metrics Plugin

Excel Plugin

Codex Plugin

GitHub Plugin

MIPSP Plugin

+------------------------+
```

Esto permitirá añadir nuevas capacidades sin modificar el núcleo de la plataforma.

---

# Interfaz de un plugin

Propongo un contrato simple:

```python
from abc import ABC, abstractmethod

class PKBPlugin(ABC):
    """Contrato base para todos los plugins del PKB."""

    name: str
    version: str

    @abstractmethod
    def register(self, application) -> None:
        """Registra comandos, servicios o validadores."""
        raise NotImplementedError
```

Los plugins podrán registrar:

* comandos CLI;
* validadores;
* generadores de informes;
* importadores;
* exportadores;
* integraciones externas.

---

# EPIC S6-002 — Event Bus

En lugar de que los componentes se llamen directamente entre sí, propongo introducir un bus de eventos.

```text
Repository Loaded

↓

Metadata Parsed

↓

Knowledge Registered

↓

Validation Finished

↓

Inventory Generated

↓

Report Generated
```

Los componentes reaccionarán a eventos.

Esto reducirá el acoplamiento y facilitará añadir nuevas capacidades.

---

# EPIC S6-003 — Domain SDK

Creo que debemos empezar a pensar en el PKB como una plataforma reutilizable.

Propongo organizar el SDK así:

```text
pkb.sdk

repository

metadata

knowledge

validation

reporting

automation

graph
```

Los proyectos podrán importar directamente:

```python
from pkb.sdk.validation import ValidationEngine

from pkb.sdk.repository import RepositoryScanner
```

sin depender de la CLI.

---

# EPIC S6-004 — Data Exchange

Todos los componentes deberán poder intercambiar información mediante formatos estándar.

```text
Knowledge Object

↓

JSON

↓

YAML

↓

Markdown

↓

GraphML

↓

CSV

↓

Excel

↓

RDF
```

Esto permitirá integrar el PKB con otras herramientas sin cambios profundos.

---

# ADR-0018 — Núcleo pequeño, capacidades extensibles

Propongo registrar la siguiente decisión:

> **El núcleo del PKB deberá permanecer deliberadamente pequeño. Las nuevas capacidades se implementarán preferentemente como plugins o servicios desacoplados, evitando aumentar innecesariamente la complejidad del core.**

Este principio tiene varias ventajas:

* facilita el mantenimiento;
* reduce el riesgo de regresiones;
* permite desarrollar nuevas funcionalidades de manera independiente;
* simplifica la incorporación de integraciones futuras.

---

# Cambio metodológico para nuestro desarrollo

Hasta ahora hemos producido una gran cantidad de diseño arquitectónico, y era necesario.

A partir del próximo ciclo propongo un cambio muy concreto:

## Cada incremento contendrá exactamente seis entregables

1. **Código ejecutable** (Python).
2. **Pruebas automatizadas** (`pytest`).
3. **Documentación técnica** (`.md`).
4. **ADR**, cuando aplique.
5. **Ejemplo funcional** o datos de prueba.
6. **Script de integración** (CLI, CI o automatización).

Con esta disciplina, cada sesión de trabajo dejará un incremento completo, integrable y verificable.

## El siguiente gran hito

Considero que ya es el momento de abandonar definitivamente los ejemplos sintéticos y comenzar a trabajar sobre **MIPSP** como proyecto piloto. Mi propuesta es dedicar el siguiente ciclo a construir el **Project Ingestion Framework v1**, cuyo objetivo será importar un proyecto existente al PKB de forma reproducible.

Ese marco incluirá:

* descubrimiento de documentos;
* clasificación automática por tipo;
* validación de metadatos;
* generación del manifiesto del proyecto;
* construcción del inventario inicial;
* creación de un informe de ingestión.

Con ese hito lograremos algo muy importante: el PKB dejará de ser una plataforma diseñada para gestionar proyectos y comenzará a gestionar uno de tus proyectos reales. A partir de ahí, el desarrollo estará impulsado por necesidades concretas, lo que fortalecerá tanto la plataforma como los estándares que hemos definido.
