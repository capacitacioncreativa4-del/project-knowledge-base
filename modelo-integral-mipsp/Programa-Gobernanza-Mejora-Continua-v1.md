---
proyecto: MIPSP — Modelo Integral para la Profesionalización de la Seguridad Privada
subsistema: 9 — Gobernanza y Mejora Continua
documento: Programa de Gobernanza y Mejora Continua — Versión 1
versión: 1.0
fecha: 2026-07-18
---

# Programa de Gobernanza y Mejora Continua
## Subsistema 9 del Modelo Integral — Gobernanza y Mejora Continua

## Decisión metodológica: por qué esta versión es distinta al diseño original

El diseño original (`MIPSP-CONV-0002-P01.md`, Lote 2) proponía un **Sistema Institucional
de Gobernanza Documental (SIGD-MIPSP)**: 4 niveles jerárquicos de gobierno (estratégico,
táctico, operativo, ejecución), una matriz RACI completa, y hasta 10 roles distintos por
cada documento del sistema — incluso para la guía de un solo instructor de un solo curso.
Inmediatamente después de proponerlo, el propio documento anunciaba "la siguiente
evolución": un sistema aún mayor (SICA-MIPSP).

Ese diseño está pensado para una institución con decenas de colaboradores en distintas
áreas. **La realidad operativa de este proyecto es un operador único**, trabajando desde
su propio repositorio de GitHub. Replicar esa estructura no aportaría gobierno real —
sería, de nuevo, teoría desconectada de quien realmente usa el sistema.

Esta versión formaliza, en cambio, **lo que ya está funcionando en la práctica** desde que
se cerró el Proyecto 1, y le da nombre y continuidad como Subsistema 9.

---

## 1. Principio rector (ya vigente desde el `ROADMAP.md`)

Una sola meta activa a la vez, con resultado tangible, antes de abrir la siguiente. Ningún
subsistema se inicia sin que el anterior haya cerrado con un entregable verificable.

## 2. Control de cambios (ya vigente desde el Proyecto 1)

Todo cambio a cualquier documento del kit o del Modelo Integral sigue el mismo
procedimiento, sin excepción:

1. Se crea una rama nueva a partir de `develop`.
2. Se aplica el cambio.
3. Se revisa con `git status` antes de confirmar.
4. Se abre un Pull Request **con base `develop`** (verificar siempre este campo).
5. Se revisan los archivos modificados antes de fusionar.
6. Se fusiona y se elimina la rama.

Este control de cambios **ya es, en la práctica, el equivalente funcional** del "Flujo de
Aprobación Documental" del diseño original — solo que ejecutado por una sola persona, con
una herramienta (Git/GitHub) en vez de una matriz RACI de cuatro niveles.

## 3. Versionado de documentos

Cada documento del Modelo Integral lleva en su encabezado un campo `versión` (v1.0, v1.1,
v2.0, etc.). Se incrementa la versión menor (v1.0 → v1.1) ante correcciones o ampliaciones
parciales, y la versión mayor (v1 → v2) ante un rediseño sustancial — como ya ocurrió con
el Curso 20 (v1 → v2, tras la Matriz de Riesgo Formativo).

## 4. Ciclo anual de revisión

Se establece un ciclo anual, alineado con el Curso 20 (Actualización Anual), que revisa:

| Elemento a revisar | Pregunta guía |
|---|---|
| IARF (Subsistema 1) | ¿Hubo reformas a la Ley o Reglamento de Morelos, la Ley Federal o el EC0060 en el periodo? |
| Catálogo de Competencias (Subsistema 2) | ¿Algún curso cambió lo suficiente como para requerir una nueva competencia? |
| Manual Maestro de PNO (Subsistema 3) | ¿Algún procedimiento dejó de reflejar la práctica real? |
| Matriz de Riesgo Formativo (Subsistema 6) | ¿Cambió el nivel de riesgo de algún curso por incidentes reales del periodo? |
| ROADMAP del PKB | ¿Se completó la meta activa? ¿Cuál es la siguiente? |

## 5. Indicadores de gobernanza (versión ágil)

En vez de los 5 indicadores institucionales originales (pensados para medir cumplimiento
de una burocracia de RACI), se proponen 4 indicadores simples y verificables directamente
en GitHub:

| Indicador | Meta | Cómo se verifica |
|---|---|---|
| Documentos con campo `versión` en su encabezado | 100% | Revisión visual del encabezado |
| Pull Requests fusionados con base `develop` (no `main` por error) | 100% | Historial de Pull Requests en GitHub |
| Subsistemas con al menos un entregable tangible | Aumenta cada ciclo | Este mismo documento y el README de `modelo-integral-mipsp/` |
| Meta activa única en el `ROADMAP.md` | Siempre 1, nunca 0 ni varias | Lectura directa del archivo |

## 6. Historial de decisiones de gobernanza (bitácora)

| Fecha | Decisión | Documento relacionado |
|---|---|---|
| 2026-07-16 | Cierre formal del Proyecto 1 con definición de entregable mínimo | `DEFINICION-ENTREGABLE-MINIMO-Proyecto-1.md` |
| 2026-07-16 | Adopción del principio "una meta a la vez" para el PKB | `ROADMAP.md` |
| 2026-07-16 | Separación de "Relaciones Humanas" como Curso 21 independiente | `Curso-21-Relaciones-Humanas-Paquete-Completo.md` |
| 2026-07-17 | Reclasificación de 8 cursos según Matriz de Riesgo Formativo | `Matriz-Riesgo-Formativo-MRF-v1.md` |
| 2026-07-17 | Ampliación del Curso 20 de 8 a 12 horas anuales | `Curso-20-Actualizacion-Anual-Paquete-Completo.md` (v2) |
| 2026-07-18 | Definición de 27 competencias nucleares en vez de 175-230 | `Catalogo-Maestro-Competencias-v1.md` |
| 2026-07-18 | Adopción de gobernanza ágil (este documento) en vez del SIGD-MIPSP de 4 niveles | `Programa-Gobernanza-Mejora-Continua-v1.md` |

*Esta tabla se actualiza cada vez que se tome una decisión estructural relevante — no cada
cambio menor de redacción.*

---

## Estado del Subsistema 9 frente al Modelo Integral

✅ Programa de Gobernanza y Mejora Continua v1 completo, formalizando el control de
cambios, versionado, ciclo anual de revisión, indicadores y bitácora de decisiones que ya
estaban en uso de facto.
⏳ Pendiente: aplicar el primer ciclo anual de revisión formal (correspondería, de forma
natural, junto con la primera aplicación real del Curso 20 ampliado).
