---
conversation_id: MIPSP-CONV-0003
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 19
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Excelente decisión. Adelante con lo que sigue.

Perfecto. A partir de esta respuesta considero que debemos cumplir el compromiso que adquirimos: **dejar de describir el software y comenzar a construirlo**.

Voy a modificar ligeramente la estrategia de implementación porque, tras revisar toda la arquitectura que hemos diseñado, veo una oportunidad de hacer el sistema todavía más sólido.

---

# Decisión Técnica DT-001

## Adoptaremos un enfoque "API First"

En lugar de comenzar escribiendo clases aisladas, primero definiremos **los contratos internos** del sistema.

En ingeniería de software esto reduce enormemente el retrabajo.

Es decir, antes de implementar:

```text
Course
```

primero definiremos qué operaciones puede realizar un curso.

Lo mismo ocurrirá con:

* Document
* Exporter
* Registry
* Builder
* Validator

Una vez definidos los contratos, las implementaciones serán mucho más sencillas.

---

# SPRINT 02

## CORE

### Objetivo

Construir el primer paquete completamente estable.

```text
src/

    mipsp/

        core/
```

Contendrá únicamente componentes reutilizables.

---

# Módulo 1

## identifiers.py

Después de analizar todo el MIPSP creo que la codificación merece un servicio específico.

No utilizaremos cadenas de texto.

Crearemos objetos.

Por ejemplo:

```python
DocumentIdentifier

CourseIdentifier

ModuleIdentifier

SessionIdentifier

CompetencyIdentifier
```

Todos heredarán de una clase base.

```text
Identifier
```

Ventajas.

* Validación inmediata.

* Comparaciones seguras.

* Sin errores tipográficos.

* Conversión automática.

* Serialización.

---

## Ejemplo

En lugar de escribir

```python
"CUR-OPS-001"
```

escribiremos

```python
CourseIdentifier(
    area="OPS",
    number=1
)
```

El propio objeto producirá

```text
CUR-OPS-001
```

y comprobará que el código sea válido.

---

# Módulo 2

## configuration.py

Aquí quiero introducir otra mejora.

La configuración será inmutable.

Una vez iniciado el sistema:

No podrá cambiar.

Usaremos

```python
frozen=True
```

en todas las configuraciones.

Esto evita errores extremadamente difíciles de localizar.

---

# Módulo 3

## metadata.py

Aquí construiremos una verdadera Ficha Técnica Editorial.

No solamente:

Autor

Versión

Fecha

Sino también:

```text
UUID

Hash SHA256

Estado documental

Nivel de revisión

Firma

Idioma

Zona horaria

Clasificación

Propietario

Repositorio

URL de origen

Licencia
```

Esto permitirá administrar miles de documentos.

---

# Módulo 4

## registry.py

Creo que aquí podemos mejorar mucho.

No quiero que sea un diccionario.

Quiero que sea un verdadero servicio.

```text
Registry
```

Con operaciones como

```python
register()

remove()

find()

exists()

dependencies()

dependents()
```

Es decir,

el Registro Maestro Documental será un objeto del dominio.

---

# Módulo 5

## validation.py

Después de pensarlo bastante,

propongo dividir la validación.

```text
Syntax Validation

↓

Semantic Validation

↓

Editorial Validation

↓

Publication Validation
```

Cada nivel comprobará aspectos distintos.

---

# Módulo 6

## logging.py

Desde el primer Sprint incorporaremos trazabilidad.

No utilizaremos

```python
print()
```

Nunca.

Todo pasará por un servicio.

```text
Logger
```

Con niveles.

```text
DEBUG

INFO

WARNING

ERROR

CRITICAL
```

Además cada compilación generará un log propio.

---

# Organización del código

Quiero adoptar una regla muy estricta.

## Un archivo = una responsabilidad.

Nunca tendremos archivos de 3000 líneas.

Ejemplo.

```text
domain/

course.py

module.py

session.py

competency.py
```

No:

```text
domain.py
```

Esto facilitará muchísimo el mantenimiento.

---

# Pruebas

Desde este Sprint aparecerá una carpeta gemela.

```text
src/

tests/
```

Cada archivo tendrá su prueba.

Ejemplo.

```text
course.py

↓

test_course.py
```

Es una disciplina que reducirá defectos conforme el proyecto crezca.

---

# Objetivo del Sprint 02

Al finalizar este Sprint deberíamos ser capaces de ejecutar algo como:

```bash
mipsp doctor
```

Y obtener una salida similar a:

```text
MIPSP Editor v1.0

Configuration ............. OK

Registry .................. OK

Metadata .................. OK

Identifiers ............... OK

Validation ................ OK

Exporters ................. Not installed

Overall Status ............ READY
```

Este será el primer ejecutable real del sistema.

---

# Cambio importante para las siguientes entregas

A partir de la próxima respuesta dejaré de describir módulos y comenzaré a entregar **código fuente completo**, siguiendo una disciplina de desarrollo incremental.

Cada entrega contendrá aproximadamente entre **600 y 1 000 líneas de código** distribuidas en varios archivos del repositorio, incluyendo:

* implementación;
* pruebas unitarias;
* ejemplos de uso;
* documentación técnica;
* registro de cambios.

De esta forma, tras varias iteraciones dispondremos de un repositorio Python completo, coherente y ejecutable, capaz de generar progresivamente toda la biblioteca documental del MIPSP. Creo que éste es el punto en el que el proyecto empieza a transformarse en un producto de software real, y a partir de aquí el mayor valor estará en la construcción sistemática del código y no en seguir ampliando el diseño.
