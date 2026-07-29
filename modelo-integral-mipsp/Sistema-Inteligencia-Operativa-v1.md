---
proyecto: MIPSP — Modelo Integral para la Profesionalización de la Seguridad Privada
subsistema: 8 — Inteligencia Operativa
documento: Sistema de Inteligencia Operativa — Versión 1
versión: 1.0
fecha: 2026-07-18
---

# Sistema de Inteligencia Operativa
## Subsistema 8 del Modelo Integral — Inteligencia Operativa

## Nota sobre el origen de este documento

Igual que el Subsistema 7, este tampoco se desarrolló nunca más allá de su definición
original de una línea: *"Analiza indicadores, incidentes y resultados de evaluación para
identificar tendencias y necesidades emergentes de capacitación."* Este documento es un
**diseño nuevo**, construido para reutilizar la información que ya generan los demás
subsistemas, sin crear un sistema de información paralelo ni depender de software
especializado.

## Principio de diseño

El Sistema de Inteligencia Operativa **no recolecta datos nuevos**. Se alimenta
exclusivamente de lo que ya producen los otros ocho subsistemas:

| Fuente | Subsistema | Qué aporta |
|---|---|---|
| Constancias y exámenes de los 21 cursos | 4 y 5 | Tasa de acreditación y reprobación por curso |
| Reportes vía PNO-REPORTES-01, PNO-ETICA-01, PNO-FUERZA-01, PNO-DDHH-01/GENERO-01 | 3 | Incidentes reales, clasificados por tipo |
| Matriz de Riesgo Formativo | 6 | Nivel de criticidad de cada curso |
| Fichas de seguimiento del MMC-SP | 7 | Distribución del personal por nivel de madurez |
| Resultados del Curso 20 (diagnóstico y refrendo) | Gobernanza (9) | Áreas de reforzamiento detectadas cada ciclo |

## Indicadores centrales

| Indicador | Fórmula simple | Qué revela |
|---|---|---|
| Tasa de acreditación por curso | Acreditados ÷ Total de participantes | Cursos con dificultad de comprensión inusual |
| Incidentes por competencia | Conteo de reportes vinculados a una competencia (Subsistema 2) en el periodo | Competencias que fallan en la práctica pese a estar acreditadas |
| Concentración de riesgo | % de incidentes originados en cursos "Muy Alta" (Subsistema 6) | Si el riesgo real coincide con el riesgo formativo estimado |
| Distribución de madurez | % de personal en cada nivel del MMC-SP | Salud general de la plantilla operativa |
| Cumplimiento del refrendo anual | Refrendados a tiempo ÷ Total obligado (Curso 20) | Riesgo de vencimiento de certificaciones |

## Regla de alerta automática (la pieza más valiosa de este subsistema)

> **Si 3 o más incidentes en un periodo de 6 meses se vinculan con la misma competencia
> del Catálogo Maestro (Subsistema 2), se activa automáticamente una revisión del curso
> correspondiente** — sin esperar al ciclo anual completo del Subsistema 9.

Esta regla conecta, por primera vez en el Modelo Integral, la operación real (lo que pasa
en el campo) con el diseño curricular (lo que se enseña), cerrando el ciclo completo:
ley → competencia → curso → evaluación → **incidente real → retroalimentación al curso**.

## Plantilla del Tablero de Control (a llenar con datos reales del piloto)

| Curso | Criticidad (MRF) | Tasa de acreditación | Incidentes del periodo | Competencia más señalada | Estado |
|---|---|---|---|---|---|
| Curso 4 — Control de Accesos | Muy Alta | *(pendiente de datos)* | *(pendiente)* | CO-001 / CO-002 | — |
| Curso 8 — Primeros Auxilios | Muy Alta | *(pendiente)* | *(pendiente)* | CSE-003 | — |
| Curso 3 — Derechos Humanos | Muy Alta | *(pendiente)* | *(pendiente)* | CJ-003 | — |
| Curso 12 — Uso de la Fuerza | Muy Alta | *(pendiente)* | *(pendiente)* | CO-005 / CT-001 | — |
| Curso 14 — Perspectiva de Género | Muy Alta | *(pendiente)* | *(pendiente)* | CJ-004 | — |
| *(resto de los 21 cursos)* | — | *(pendiente)* | *(pendiente)* | — | — |

*(Esta tabla es una plantilla lista para usarse en una hoja de cálculo; se activa en cuanto
exista al menos un ciclo de operación real con personal capacitado. No se requiere software
adicional — la misma ficha de seguimiento del MMC-SP y los reportes vía PNO alimentan estas
columnas directamente.)*

## Formato de Informe Ejecutivo (estructura, no contenido — depende de datos reales)

1. Periodo cubierto.
2. Resumen de acreditaciones y refrendos del periodo.
3. Incidentes relevantes y su vínculo con competencias/cursos.
4. Alertas automáticas activadas (según la regla de 3+ incidentes).
5. Recomendaciones de ajuste al kit de capacitación, si aplica.
6. Vínculo con el ciclo anual del Subsistema 9 (Gobernanza).

## Estado del Subsistema 8 frente al Modelo Integral

✅ Sistema de Inteligencia Operativa v1 diseñado desde cero: indicadores, regla de alerta
automática y plantillas de tablero de control e informe ejecutivo, todo alimentado por la
información que ya generan los demás ocho subsistemas.
⏳ Pendiente: llenar el tablero de control con datos reales, una vez que el kit se aplique
con personal real (mismo pendiente de validación práctica señalado desde el cierre del
Proyecto 1).

---

# Cierre del Modelo Integral — los 9 subsistemas completos

Con este documento, **los 9 subsistemas del Modelo Integral para la Profesionalización de
la Seguridad Privada (MIPSP) quedan desarrollados**, cada uno en una versión ágil, honesta
sobre lo que reutiliza y lo que queda pendiente, y sin repetir el patrón de sobre-alcance
(6 tomos de 250-350 páginas, 175-230 competencias, 4 niveles de gobernanza institucional)
que pausó el proyecto originalmente.

| # | Subsistema | Documento | Estado |
|---|---|---|---|
| 1 | Sistema Jurídico | IARF v1 | ✅ Completo (Cap. IX Ley Morelos) |
| 2 | Sistema de Competencias | Catálogo Maestro v1 | ✅ Completo (27 competencias) |
| 3 | Procesos Operativos | Manual Maestro de PNO v1 | ✅ Completo (21 PNO) |
| 4 | Diseño Curricular | Kit de 21 cursos (Proyecto 1) | ✅ Completo |
| 5 | Evaluación | Incluido en cada PDIC | ✅ Completo |
| 6 | Gestión del Riesgo Formativo | Matriz de Riesgo Formativo v1 | ✅ Completo |
| 7 | Madurez Competencial | Modelo MMC-SP v1 | ✅ Completo |
| 8 | Inteligencia Operativa | Sistema de Inteligencia Operativa v1 | ✅ Completo |
| 9 | Gobernanza y Mejora Continua | Programa de Gobernanza v1 | ✅ Completo |

**El Modelo Integral, en su versión ágil, está terminado.** Lo que sigue —según ya se ha
señalado en cada subsistema— son fases de profundización y validación práctica, no
desarrollo conceptual pendiente.
