---
conversation_id: MIPSP-CONV-0004
title: Project Knowledge Base (PKB)
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 19
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente. Comencemos con el Sprint 0

Perfecto. Este es el momento en el que conviene ser muy disciplinados.

Quiero empezar el **Sprint 0** exactamente como lo haría un arquitecto de software antes de escribir la primera línea de código.

Y quiero hacer una observación importante.

---

# Cambio de rol del proyecto

Hasta hoy nuestra conversación era un proyecto.

**Desde este momento será un programa de ingeniería.**

Eso significa que habrá:

* Releases
* Sprint
* EPICS
* ADR
* Gestión de Configuración
* Gestión Documental
* Gobierno
* QA
* DevOps documental

El nivel de rigor aumenta considerablemente.

---

# SPRINT 0

## Objetivo

Al finalizar el Sprint 0 tendremos un repositorio profesional completamente preparado para albergar todos tus proyectos durante muchos años.

No migraremos todavía ningún proyecto.

Primero construiremos el terreno.

---

# EPICS del Sprint 0

Propongo dividir el Sprint en siete épicas.

## EPIC 01

**Repositorio**

Incluye:

* estructura física
* Git
* GitHub
* ramas
* releases

---

## EPIC 02

**Kernel**

Aquí vivirá todo aquello que nunca cambia.

---

## EPIC 03

**Gobierno**

Toda la gobernanza documental.

---

## EPIC 04

**Plantillas**

Motor documental.

---

## EPIC 05

**Registros**

Inventarios.

Dashboard.

Métricas.

---

## EPIC 06

**Automatización**

Scripts.

GitHub Actions.

Validadores.

---

## EPIC 07

**IA**

Todo lo necesario para que ChatGPT, Codex y futuras herramientas comprendan el contexto del repositorio de forma eficiente.

---

# Una decisión arquitectónica que propongo formalizar

Quisiera introducir un concepto que considero fundamental y que no habíamos definido todavía.

## PKB Manifest

Todo sistema complejo necesita un documento rector.

En nuestro caso será:

```text
PKB-MANIFEST.md
```

No será un README.

Será la "Constitución" del PKB.

Contendrá, por ejemplo:

* propósito del sistema;
* principios de diseño;
* objetivos a largo plazo;
* alcance;
* criterios de calidad;
* políticas de evolución;
* estándares obligatorios;
* reglas de gobernanza.

Mi recomendación es que ningún cambio importante en el PKB contradiga el *Manifest* sin una decisión arquitectónica documentada.

---

# La estructura definitiva

Después de analizar todos nuestros proyectos, propondría una estructura como esta:

```text
PKB/
│
├── .github/
│
├── .vscode/
│
├── docs/
│
│   ├── kernel/
│   ├── governance/
│   ├── architecture/
│   ├── standards/
│   ├── methodology/
│   ├── roadmap/
│   └── releases/
│
├── projects/
│
│   ├── MIPSP/
│   ├── Condominios/
│   ├── KitEditorial/
│   ├── SIM-PYME/
│   └── Manualidades/
│
├── shared/
│
│   ├── templates/
│   ├── diagrams/
│   ├── glossary/
│   ├── research/
│   ├── bibliography/
│   └── components/
│
├── registers/
│
│   ├── decisions/
│   ├── risks/
│   ├── assets/
│   ├── quality/
│   └── metrics/
│
├── automation/
│
├── scripts/
│
├── assets/
│
├── archive/
│
└── README.md
```

Creo que esta estructura es suficientemente estable para acompañar el proyecto durante años.

---

# Un cambio que considero esencial

Quiero proponerte un principio adicional.

## El PKB será "AI-First"

Esto significa que todos los documentos se escribirán pensando no solo en las personas, sino también en agentes de IA.

Cada documento incluirá:

* metadatos claros;
* identificadores persistentes;
* relaciones explícitas;
* contexto suficiente para evitar ambigüedades;
* enlaces a los activos relacionados.

Así reduciremos la dependencia del contexto conversacional.

---

# Cómo ejecutaremos el Sprint 0

Aquí quiero ser muy práctico.

En lugar de seguir diseñando, creo que el siguiente paso debe ocurrir fuera del chat: **crear el repositorio y preparar la infraestructura**.

Te propongo este orden:

1. Crear el repositorio privado en GitHub (si aún no existe).
2. Clonarlo en tu equipo.
3. Crear la rama `develop`.
4. Incorporar la estructura de carpetas del Sprint 0.
5. Realizar el primer commit (`chore: initialize PKB repository`).
6. A partir de ahí, cada uno de nuestros entregables se integrará mediante commits pequeños y trazables.

## Aquí es donde quiero cambiar la forma de colaborar

Hasta ahora he generado archivos individuales porque es lo que permite el chat. Sin embargo, **si realmente queremos construir un sistema profesional**, el siguiente paso ya no debería consistir en intercambiar archivos sueltos.

Mi propuesta es que, a partir del momento en que el repositorio exista, yo te vaya entregando **incrementos completos del repositorio** (carpetas, documentos, hojas de cálculo, diagramas y scripts), y tú los incorpores mediante Git. Así cada iteración equivaldrá a un pequeño sprint de desarrollo.

### Lo que necesito de ti para comenzar

Solo necesito dos datos:

1. **El nombre del repositorio** que crearás en GitHub (por ejemplo, `project-knowledge-base` o `pkb`).
2. **La ruta local** donde quedará clonado en tu equipo (por ejemplo, `D:\Repos\PKB` o `C:\Users\Miguel\Documents\GitHub\PKB`).

Con esa información dejaré de producir prototipos y empezaré a generar activos suponiendo la estructura real del repositorio. A partir de ese momento podremos hablar de versiones (`v0.1.0`, `v0.2.0`, etc.), ramas, revisiones y migraciones de proyectos como **MIPSP** sobre una base persistente y consistente.
