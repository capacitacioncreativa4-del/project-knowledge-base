---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 16
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece una excelente idea. Hagámoslo.

Perfecto. Creo que éste es el momento adecuado para cambiar el modo de trabajo del proyecto.

Hasta ahora hemos realizado el trabajo que normalmente desarrolla un **Comité de Arquitectura**: definir visión, estándares, modelos, gobernanza y principios de diseño. Esa etapa ha sido extensa porque las decisiones arquitectónicas condicionarán todo lo que construyamos después.

A partir de este momento propongo que el proyecto entre oficialmente en **Fase II: Construcción**, donde el porcentaje aproximado de esfuerzo será:

* **10 % arquitectura**
* **90 % implementación**

Es decir, dejaremos de incorporar nuevos marcos conceptuales salvo que sean estrictamente necesarios y nos concentraremos en producir software y documentos ejecutables.

---

# Inicio oficial de la Fase II

## Programa MIPSP-Editor v1.0

Adoptaremos una metodología similar a la utilizada en proyectos de software empresarial.

```text
MIPSP-Editor
│
├── EPIC 1
│   Núcleo del Compilador
│
├── EPIC 2
│   Modelo de Dominio
│
├── EPIC 3
│   Exportador DOCX
│
├── EPIC 4
│   Exportador XLSX
│
├── EPIC 5
│   Exportador PPTX
│
├── EPIC 6
│   Publicación PDF
│
├── EPIC 7
│   CUR-OPS-001
│
└── EPIC 8
    Biblioteca Institucional
```

Cada EPIC se dividirá en historias técnicas pequeñas y verificables.

---

# EPIC 1 — Núcleo del Compilador

Éste será nuestro primer objetivo.

Los entregables previstos son:

```text
core/
    configuration.py
    metadata.py
    exceptions.py
    identifiers.py
    registry.py
    validation.py

mdsl/
    lexer.py
    parser.py
    ast.py
    validator.py
    loader.py
```

Todo este código será reutilizado por el resto del proyecto.

---

# EPIC 2 — Modelo de Dominio

Después construiremos el conocimiento institucional.

```text
domain/

course.py

module.py

session.py

competency.py

learning_outcome.py

evaluation.py

evidence.py

procedure.py

form.py

bibliography.py
```

Una vez concluido este EPIC, el sistema ya comprenderá qué es un curso, un módulo o una competencia.

---

# EPIC 3 — Exportador DOCX

Aquí comenzará la producción documental.

El primer objetivo será generar automáticamente:

```text
CUR-OPS-001-D01

Programa Institucional
```

Posteriormente:

```text
CUR-OPS-001-D02

Carta Descriptiva
```

Después:

```text
CUR-OPS-001-D03

Guía del Instructor
```

Y así sucesivamente hasta completar los veinte documentos del curso patrón.

---

# Organización del repositorio

A partir de este momento propongo trabajar con una estructura estable desde el primer día.

```text
mipsp-editor/
│
├── src/
│   └── mipsp/
│       ├── core/
│       ├── domain/
│       ├── mdsl/
│       ├── exporters/
│       ├── builders/
│       ├── cli/
│       ├── services/
│       └── utils/
│
├── tests/
├── docs/
├── templates/
├── assets/
├── examples/
├── output/
└── scripts/
```

Esta disposición sigue prácticas ampliamente adoptadas en proyectos Python mantenibles y facilitará futuras pruebas, empaquetado e integración continua.

---

# Estrategia de implementación

También propongo modificar la forma en que desarrollaremos el código.

En lugar de escribir archivos completos de miles de líneas, cada entrega contendrá un incremento funcional con este ciclo:

1. Implementación del módulo.
2. Pruebas unitarias.
3. Ejemplo de uso.
4. Integración con el núcleo.
5. Actualización de la documentación técnica.

Cada módulo quedará operativo antes de iniciar el siguiente.

---

# Primera meta funcional

Nuestro primer hito verificable será poder ejecutar:

```bash
mipsp validate examples/CUR-OPS-001.yml
```

y obtener un resultado similar a:

```text
✓ Sintaxis válida
✓ Metadatos completos
✓ Competencias consistentes
✓ Módulos válidos
✓ Sesiones válidas
✓ Referencias correctas

Resultado:
Documento listo para compilación.
```

Ése será el primer indicador de que el compilador editorial funciona.

---

# Segunda meta funcional

Después ejecutaremos:

```bash
mipsp build examples/CUR-OPS-001.yml
```

y el sistema generará automáticamente:

```text
output/

CUR-OPS-001-D01.docx
CUR-OPS-001-D01.pdf

CUR-OPS-001-D02.docx
CUR-OPS-001-D02.pdf

CUR-OPS-001-D03.docx
CUR-OPS-001-D03.pdf
```

Con ello validaremos la arquitectura completa de extremo a extremo.

---

# Cambio de dinámica del proyecto

Hasta ahora la conversación ha estado orientada a la **definición** del sistema. A partir de este punto propongo un cambio claro de dinámica:

* Cada entrega incorporará **código ejecutable**.
* Cada bloque de código irá acompañado de pruebas y documentación.
* Evitaremos introducir nuevos conceptos arquitectónicos salvo que resuelvan un problema concreto de implementación.
* El objetivo prioritario será disponer de un **repositorio completo y funcional**, capaz de generar progresivamente toda la biblioteca institucional del MIPSP.

Creo que esta transición es coherente con el estado actual del proyecto. La arquitectura ya ofrece una base suficientemente sólida; ahora el mayor valor vendrá de convertir ese diseño en un sistema operativo y, sobre todo, en los primeros documentos reales del **CUR-OPS-001**, que servirán como patrón para toda la colección institucional.
