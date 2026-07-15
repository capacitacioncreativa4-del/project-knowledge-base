---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 21
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente decisión. Continúa con lo que sigue.

Perfecto. A partir de este punto voy a cambiar deliberadamente el nivel de detalle de las entregas. Hemos dedicado suficiente tiempo al diseño y ahora conviene trabajar como lo haría un equipo de desarrollo profesional: **cada sprint debe dejar el repositorio en un estado ejecutable**.

También quiero introducir una última decisión metodológica antes de comenzar la implementación del código.

---

# ADR-003 — Desarrollo basado en Vertical Slices

En lugar de desarrollar primero todos los módulos (`core`, `domain`, `compiler`, `exporters`) y al final comprobar si funcionan juntos, construiremos **incrementos funcionales completos**.

Cada incremento atravesará todas las capas de la aplicación.

Por ejemplo, el primer incremento será:

```text
MDSL
   │
   ▼
Parser
   │
   ▼
Domain
   │
   ▼
Builder
   │
   ▼
DOCX
```

Aunque inicialmente genere un documento muy sencillo, validará toda la arquitectura de extremo a extremo.

Esta estrategia reduce significativamente el riesgo de integración.

---

# Backlog Reestructurado

## Incremento 1

**Objetivo**

Compilar un curso mínimo.

Entradas:

```text
CUR-OPS-001.yml
```

Salida:

```text
CUR-OPS-001-D01.docx
```

Aunque el contenido sea reducido, el flujo completo quedará probado.

---

## Incremento 2

Agregar:

* portada;
* metadatos;
* índice;
* encabezados;
* pies de página.

---

## Incremento 3

Agregar:

* tablas;
* listas;
* figuras;
* anexos.

---

## Incremento 4

Agregar:

* referencias cruzadas;
* numeración automática;
* bibliografía.

---

## Incremento 5

Agregar:

* PDF;
* XLSX;
* PPTX.

---

# Repositorio inicial

El repositorio comenzará con los siguientes archivos fundamentales:

```text
mipsp-editor/
├── pyproject.toml
├── README.md
├── src/
│   └── mipsp/
│       ├── __init__.py
│       ├── cli.py
│       ├── compiler.py
│       ├── builder.py
│       ├── exporter.py
│       ├── models.py
│       └── config.py
├── tests/
└── examples/
```

En iteraciones posteriores estos módulos se dividirán conforme el sistema crezca.

---

# Definición del Primer Caso de Uso

Todo el proyecto girará alrededor de un caso de uso concreto.

**CU-001 — Compilar Curso**

```text
Usuario
    │
    ▼
Selecciona CUR-OPS-001.yml
    │
    ▼
Parser
    │
    ▼
Validador
    │
    ▼
Modelo del dominio
    │
    ▼
Builder
    │
    ▼
Exportador DOCX
    │
    ▼
Documento generado
```

Si este caso de uso funciona, el resto de la plataforma será una extensión del mismo patrón.

---

# Modelo mínimo del dominio

Para evitar sobreingeniería, el primer incremento utilizará únicamente las entidades imprescindibles:

```text
Course
├── Metadata
├── Modules
└── Sections
```

Posteriormente se incorporarán:

* competencias;
* resultados de aprendizaje;
* ETS;
* evaluaciones;
* indicadores;
* evidencias.

Así reducimos la complejidad inicial.

---

# Primer archivo MDSL

El primer curso se describirá de forma muy simple:

```yaml
course:
  code: CUR-OPS-001
  title: Control de Accesos
  version: "1.0"

modules:
  - code: MOD-01
    title: Introducción al Control de Accesos
```

El compilador sólo necesitará interpretar esta estructura para producir el primer documento.

---

# Primer documento generado

La primera versión del **CUR-OPS-001-D01** contendrá únicamente:

1. Portada.
2. Metadatos.
3. Objetivo del curso.
4. Estructura modular.

Una vez validado el flujo de generación, iremos enriqueciendo el contenido hasta alcanzar la versión editorial definitiva.

---

# Hito de aceptación

Consideraré completado el primer incremento cuando podamos ejecutar:

```bash
mipsp build examples/CUR-OPS-001.yml
```

y el sistema produzca un documento `.docx` válido sin intervención manual.

A partir de ese momento comenzará la verdadera productividad del proyecto: cada nueva funcionalidad se reflejará inmediatamente en documentos institucionales reales.

## Propuesta de trabajo para las siguientes entregas

En lugar de seguir describiendo la implementación, las próximas respuestas estarán dedicadas a **entregar código fuente**. Cada entrega contendrá un conjunto coherente de archivos (por ejemplo, `pyproject.toml`, `config.py`, `models.py` y sus pruebas), listos para incorporarse a un repositorio Git.

Ese enfoque nos permitirá avanzar de manera tangible hasta disponer del **MIPSP-Editor** plenamente funcional y utilizarlo para generar toda la biblioteca documental del **CUR-OPS-001** y, posteriormente, del resto del catálogo institucional.
