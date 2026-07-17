---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 20
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Me parece muy bien. Continúa con lo previsto

Perfecto. A partir de esta respuesta considero que el proyecto entra oficialmente en la **Fase de Desarrollo Incremental**. Ya no volveremos a dedicar respuestas completas a la arquitectura, salvo cuando sea imprescindible. Cada entrega aportará componentes reales del repositorio.

No obstante, antes de escribir el primer módulo quiero tomar una decisión que, en proyectos de esta magnitud, suele marcar la diferencia entre un sistema que envejece bien y otro que se vuelve difícil de mantener.

---

# ADR-002 — Todo el modelo del dominio será inmutable

Después de revisar toda la arquitectura, propongo que **las entidades del dominio sean inmutables** (`frozen=True`).

Por ejemplo:

```python
@dataclass(frozen=True, slots=True)
class Course:
    ...
```

¿Por qué?

Porque un curso institucional **no cambia** mientras existe.

Cuando cambia:

No es el mismo curso.

Es una nueva versión.

Eso significa que:

```
CUR-OPS-001 v1.0
```

y

```
CUR-OPS-001 v1.1
```

serán dos objetos diferentes.

Esta decisión simplifica enormemente:

* control de versiones;
* auditorías;
* generación de históricos;
* compilaciones reproducibles;
* comparación entre versiones.

Creo que ésta será una de las mejores decisiones del proyecto.

---

# Inicio de la implementación

## EPIC-02

## CORE

Vamos a construir el primer paquete real.

---

# Orden definitivo

No construiremos los módulos en el orden inicialmente previsto.

Después del análisis realizado propongo este orden:

```
shared/
```

↓

```
core/
```

↓

```
domain/
```

↓

```
compiler/
```

↓

```
builders/
```

↓

```
exporters/
```

La razón es sencilla.

Todo depende de `shared`.

---

# shared/

Este paquete contendrá únicamente componentes completamente reutilizables.

```
shared/

    constants.py

    enums.py

    types.py

    version.py

    result.py

    value_objects.py
```

Éste será el verdadero cimiento del proyecto.

---

# constants.py

Aquí NO aparecerán números mágicos.

Por ejemplo:

```python
MAX_TITLE_LENGTH = 200

DEFAULT_LANGUAGE = "es-MX"

DEFAULT_ENCODING = "utf-8"
```

Todo el proyecto consultará estas constantes.

---

# enums.py

Todos los valores discretos serán enumeraciones.

Ejemplos.

```python
DocumentStatus

ClassificationLevel

ExporterType

Severity

LogLevel

PaperSize

Orientation
```

Esto elimina muchísimos errores de programación.

---

# types.py

Aquí definiremos alias de tipos.

Ejemplo.

```python
DocumentCode

CourseCode

ModuleCode

UUID

Version

PathLike
```

Esto hará el código mucho más expresivo.

---

# result.py

Éste será uno de los módulos más utilizados.

En lugar de lanzar excepciones constantemente, muchas operaciones devolverán un objeto `Result`.

Conceptualmente:

```python
Result.success(...)

Result.failure(...)
```

Así podremos encadenar operaciones y reportar errores de manera uniforme.

---

# value_objects.py

Éste será probablemente el módulo más importante del paquete `shared`.

Aquí vivirán objetos pequeños, inmutables y reutilizables, por ejemplo:

* `DocumentCode`
* `Version`
* `PersonName`
* `EmailAddress`
* `Duration`
* `RevisionNumber`
* `HashValue`

Todos ellos encapsularán sus propias reglas de validación.

---

# Política de calidad

A partir de este sprint adoptaremos los siguientes criterios:

* Cobertura mínima del 90 % para `shared` y `core`.
* Tipado completo (`typing`).
* `dataclasses` con `slots=True`.
* Sin dependencias circulares.
* Sin acceso directo al sistema de archivos desde el dominio.
* Sin lógica de exportación en las entidades del dominio.

Estos principios se mantendrán durante todo el desarrollo.

---

# Objetivo funcional del primer incremento

El primer incremento verificable del proyecto será poder ejecutar un programa mínimo que:

1. Cargue la configuración institucional.
2. Cree un objeto `Course`.
3. Lo valide.
4. Lo registre en el Registro Maestro.
5. Muestre un informe de estado.

Aunque todavía no generará un `.docx`, demostrará que el núcleo del dominio funciona correctamente y que la arquitectura soporta el flujo de trabajo previsto.

---

# Cambio metodológico definitivo

A partir de la próxima entrega dejaré de describir el diseño y comenzaré a proporcionar **implementaciones completas**. Cada respuesta contendrá un conjunto pequeño pero terminado de archivos del repositorio, con:

* código fuente;
* pruebas unitarias;
* ejemplos de uso;
* documentación técnica.

Trabajaremos como un equipo de desarrollo profesional que entrega incrementos funcionales. Cuando el núcleo alcance estabilidad, comenzaremos inmediatamente a utilizarlo para generar los primeros documentos reales del **CUR-OPS-001**, manteniendo el mismo estándar de calidad que hemos definido para toda la biblioteca institucional del MIPSP.
