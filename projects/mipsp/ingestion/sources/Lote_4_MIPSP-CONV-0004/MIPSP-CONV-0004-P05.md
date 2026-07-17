---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 5
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Genial. Continuemos

Perfecto. A partir de este punto empezamos a construir el **PKB** como si estuviéramos diseñando el sistema documental de una empresa de desarrollo de software o de una consultora tecnológica. La prioridad deja de ser producir documentos aislados; pasamos a construir un **ecosistema de conocimiento**.

# FASE 2 – Arquitectura Documental

## Objetivo

Diseñar una arquitectura documental que:

* escale durante años;
* sea independiente de cualquier proyecto particular;
* facilite la búsqueda de información;
* permita trabajar simultáneamente con ChatGPT, Codex y Git;
* preserve la trazabilidad entre documentos.

Esta fase definirá la "columna vertebral" del PKB.

---

# Entregable 2.1 – Arquitectura lógica

La arquitectura se organiza en cuatro niveles.

```text
PKB
│
├── Nivel 1. Gobierno
│
├── Nivel 2. Proyectos
│
├── Nivel 3. Componentes reutilizables
│
└── Nivel 4. Histórico
```

Cada nivel tiene una responsabilidad claramente delimitada.

---

## Nivel 1 – Gobierno

Contiene las normas que rigen todo el repositorio.

```text
00_Gobierno
```

Incluye, entre otros:

```text
Vision

Metodologia

Taxonomia

Plantillas

Convenciones

ADR

Politicas

Glosario
```

Nunca contendrá información específica de un proyecto.

---

## Nivel 2 – Proyectos

Aquí vive el conocimiento funcional.

```text
01_Proyectos
```

Ejemplo:

```text
MIPSP

KitEditorial

SIM-PYME

Condominios

Manualidades

TransformacionDigital
```

Cada proyecto es completamente autónomo.

---

## Nivel 3 – Biblioteca reutilizable

Aquí almacenaremos componentes comunes.

Ejemplos:

```text
Patrones

Diagramas

Plantillas

Prompts

Snippets

Bibliografía

Normatividad

Iconografía

Estilos
```

Esto evitará duplicar contenido entre proyectos.

---

## Nivel 4 – Histórico

Todo aquello que ya no es vigente pero que deseamos conservar:

```text
Versiones anteriores

Decisiones descartadas

Ideas

Prototipos

Chats resumidos
```

---

# Entregable 2.2 – Arquitectura interna de un proyecto

Todos los proyectos seguirán exactamente la misma estructura.

Por ejemplo:

```text
Proyecto

00_Gobierno

01_Contexto

02_Vision

03_Objetivos

04_Requisitos

05_ReglasNegocio

06_ModeloDominio

07_Arquitectura

08_ModeloDatos

09_APIs

10_UI

11_EPICS

12_CasosUso

13_Pruebas

14_Manuales

15_Planeacion

16_Roadmap

17_Riesgos

18_Historico
```

Observa que no depende del lenguaje de programación ni de la tecnología empleada.

---

# Entregable 2.3 – Clasificación del conocimiento

No toda la información tiene el mismo nivel de estabilidad. Propongo clasificarla así:

| Nivel          | Tipo                     | Frecuencia de cambio |
| -------------- | ------------------------ | -------------------- |
| Estratégico    | Visión, objetivos        | Muy baja             |
| Arquitectónico | Arquitectura, dominio    | Baja                 |
| Funcional      | Requisitos, casos de uso | Media                |
| Técnico        | APIs, BD, UI             | Alta                 |
| Operativo      | Manuales, procedimientos | Media                |
| Histórico      | Actas, versiones         | Nula                 |

Esta clasificación nos ayudará a priorizar revisiones.

---

# Entregable 2.4 – Relaciones entre documentos

El PKB funcionará como un grafo de conocimiento.

Por ejemplo:

```text
Visión
   │
   ▼
Objetivos
   │
   ▼
Requisitos
   │
   ▼
EPICS
   │
   ▼
Casos de Uso
   │
   ├────────► UI
   │
   ├────────► API
   │
   ├────────► Base de Datos
   │
   └────────► Pruebas
```

La trazabilidad será explícita.

---

# Entregable 2.5 – Índices

Cada carpeta tendrá su propio índice (`INDEX.md`) con enlaces a los documentos que contiene.

Ejemplo para `04_Requisitos`:

| ID      | Documento     | Estado      | Versión |
| ------- | ------------- | ----------- | ------- |
| REQ-001 | Autenticación | Aprobado    | 1.2     |
| REQ-002 | Usuarios      | En revisión | 0.9     |
| REQ-003 | Editor        | Borrador    | 0.4     |

Además, el repositorio tendrá un índice maestro para localizar rápidamente cualquier documento.

---

# Entregable 2.6 – Convención de enlaces

Todos los documentos incluirán una sección de relaciones:

```text
## Relacionado con

REQ-001

EPIC-001

CU-004

API-002

UI-003

ADR-001
```

Esto permitirá navegar el conocimiento sin depender de búsquedas de texto.

---

# Entregable 2.7 – Estado de madurez

Cada documento llevará un indicador de madurez.

| Estado     | Significado                            |
| ---------- | -------------------------------------- |
| Draft      | Primer borrador                        |
| Review     | En revisión técnica                    |
| Approved   | Validado y aceptado                    |
| Published  | Publicado como referencia              |
| Deprecated | Obsoleto                               |
| Archived   | Conservado solo por motivos históricos |

---

# Entregable 2.8 – Sistema de identificación

Propongo un identificador persistente que no cambie aunque el documento se renombre:

```text
PKB-MIPSP-REQ-001

PKB-MIPSP-CU-014

PKB-MIPSP-API-009

PKB-MIPSP-ADR-003
```

Esto facilita referencias cruzadas y evita romper enlaces.

---

# Un refinamiento que considero especialmente valioso

Dado que uno de nuestros objetivos es colaborar con herramientas de IA, añadiría una carpeta específica dentro de cada proyecto:

```text
90_AI_Context/
```

Contendría, por ejemplo:

* `PROJECT_SUMMARY.md`: resumen ejecutivo del proyecto.
* `ARCHITECTURE_CONTEXT.md`: visión general de la arquitectura.
* `DOMAIN_GLOSSARY.md`: terminología del dominio.
* `CURRENT_STATUS.md`: estado actual del desarrollo.
* `NEXT_ACTIONS.md`: prioridades inmediatas.
* `DECISIONS.md`: decisiones arquitectónicas vigentes.

Estos documentos estarán pensados para proporcionar contexto rápidamente a un asistente de IA o a un nuevo colaborador, reduciendo la necesidad de recorrer decenas de archivos para entender el proyecto.

## Próximo paso: Fase 3 – Inventario y migración

Con la arquitectura documental definida, el siguiente paso será construir un **Inventario Maestro de Activos**. Ahí registraremos todas las conversaciones y entregables existentes, identificaremos qué conocimiento contienen y decidiremos en qué documentos del PKB debe consolidarse. Esa fase será el puente entre los chats y la base de conocimiento versionada. Por el volumen de material que ya hemos generado, ese inventario será el elemento que nos permitirá migrar de forma ordenada y sin perder información.
