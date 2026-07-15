# ADR-000006: Reglas de Validación Semántica y Restricciones del Metamodelo

## Estado
PROPUESTO

## Contexto
El análisis del proyecto piloto MIPSP demostró que los requerimientos aislados tienden a perder la traza de qué estándar los gobierna y en qué sistema se aplican, provocando inconsistencias en el diseño organizativo.

## Decisión
Admitir un conjunto rígido y unificado de relaciones semánticas en todos los manifiestos JSON/YAML, prohibiendo de manera estricta relaciones personalizadas o no documentadas en `PKB-SPEC-003`.

## Consecuencias
* **Positivas:** Permite que los validadores sintácticos y el futuro motor del grafo de conocimiento (Knowledge Graph) identifiquen de inmediato enlaces rotos o huérfanos.
* **Negativas:** Exige un esfuerzo de estandarización mayor al procesar y codificar el histórico de conversaciones.