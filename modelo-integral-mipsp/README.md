# Modelo Integral para la Profesionalización de la Seguridad Privada (MIPSP)

## Alcance de esta carpeta

Esta carpeta contiene el desarrollo del **Modelo Integral** (MIPSP): el marco metodológico
conceptual que organiza, relaciona y transforma las obligaciones jurídicas, los procesos
operativos y los estándares de competencia en programas estructurados de formación,
evaluación y desarrollo profesional.

**Esta carpeta es un proyecto hermano, separado de:**
- `capacitacion-guardias-seguridad-privada/` — el Proyecto 1 (kit de 21 cursos), ya
  cerrado. El Modelo Integral se apoya conceptualmente en ese trabajo, pero no lo modifica
  ni depende de él para funcionar.
- El Project Knowledge Base (PKB) institucional, en `projects/mipsp/`.

## Principio de trabajo

Igual que con el Proyecto 1 y el `ROADMAP.md` del PKB, esta carpeta sigue el principio de
**una meta a la vez, con resultado tangible**, evitando repetir la expansión hacia una
colección de 6 tomos de 250-350 páginas que pausó el proyecto originalmente.

## Contenido

- **`MIPSP-Tomo-I-Marco-Metodologico-Ejecutivo.md`** — Versión ejecutiva consolidada del
  marco metodológico: definición, 10 principios rectores, los 9 subsistemas del modelo con
  su estado real de avance (contrastado contra el Proyecto 1), y la arquitectura general
  del conocimiento.

- **`subsistema-1-sistema-juridico/`** — Desarrollo del Subsistema 1 (Sistema Jurídico):
  - `IARF-v1-Capitulo-IX-Ley-Morelos.md` — Inventario Analítico de Requisitos Formativos,
    primera versión, basado en el texto oficial de los Capítulos VII a IX (artículos 38-53)
    de la Ley de Seguridad Privada para el Estado de Morelos. Confirma con cita legal
    exacta que 16 de 18 obligaciones formativas analizadas ya están cubiertas por el kit de
    21 cursos, y resuelve el criterio de decisión de los dos pendientes normativos
    heredados del Proyecto 1 (armamento/tiro y protección a funcionarios).

- **`Manual-Maestro-PNO-v1.md`** — Subsistema 3 (Sistema de Procesos Operativos):
  compilación de los 21 Procedimientos Normalizados de Operación que ya existían en el kit
  de capacitación, organizados por bloque temático (operación diaria, emergencias,
  conducta/situaciones sensibles, documentación y gestión), con mapa de referencias
  cruzadas entre ellos.

- **`Matriz-Riesgo-Formativo-MRF-v1.md`** — Subsistema 6 (Gestión del Riesgo Formativo):
  matriz multicriterio (riesgo operativo, jurídico, reputacional) completa para los 21
  cursos. Hallazgo principal: 8 de 21 cursos cambian de categoría de riesgo frente a la
  clasificación informal usada originalmente; en particular, Derechos Humanos, Uso de la
  Fuerza y Perspectiva de Género se reclasifican como "Muy Alta", lo que abrió una
  decisión (ya tomada: ampliar el Curso 20 a 12 horas anuales).

- **`Catalogo-Maestro-Competencias-v1.md`** — Subsistema 2 (Sistema de Competencias):
  27 competencias nucleares (una o dos por cada uno de los 21 cursos), clasificadas en las
  9 familias del diseño original (Jurídicas, Operativas, Técnicas, Tecnológicas,
  Comunicación, Atención al usuario, Seguridad y emergencias, Gestión documental,
  Desarrollo profesional). Resuelve 14 de las 18 filas "Pendiente" del IARF v1.

- **`Programa-Gobernanza-Mejora-Continua-v1.md`** — Subsistema 9 (Gobernanza y Mejora
  Continua): formaliza el control de cambios (flujo de Git/GitHub ya en uso), el
  versionado de documentos, un ciclo anual de revisión alineado con el Curso 20,
  indicadores ágiles y la bitácora de decisiones estructurales del proyecto. Reemplaza
  deliberadamente el diseño original (SIGD-MIPSP, 4 niveles jerárquicos y RACI completo),
  pensado para una institución con muchos colaboradores, no para un operador único.

- **`MMC-SP-Modelo-Madurez-Competencial-v1.md`** — Subsistema 7 (Madurez Competencial):
  modelo de 4 niveles (Inducido, Operativo Básico, Operativo Consolidado, Senior/Mentor),
  diseñado desde cero (el original nunca se desarrolló más allá del nombre), apoyado en la
  infraestructura ya existente del kit (constancias, evaluaciones de desempeño, refrendo
  anual). Incluye reglas explícitas de regresión de nivel, no solo de progresión.

## Estado actual — MODELO INTEGRAL COMPLETO (versión ágil)

Los 9 subsistemas del Modelo Integral están desarrollados:

| # | Subsistema | Documento | Estado |
|---|---|---|---|
| 1 | Sistema Jurídico | `subsistema-1-sistema-juridico/IARF-v1-Capitulo-IX-Ley-Morelos.md` | ✅ |
| 2 | Sistema de Competencias | `Catalogo-Maestro-Competencias-v1.md` | ✅ |
| 3 | Procesos Operativos | `Manual-Maestro-PNO-v1.md` | ✅ |
| 4 | Diseño Curricular | Kit de 21 cursos (`capacitacion-guardias-seguridad-privada/`) | ✅ |
| 5 | Evaluación | Incluido en cada uno de los 21 paquetes | ✅ |
| 6 | Gestión del Riesgo Formativo | `Matriz-Riesgo-Formativo-MRF-v1.md` | ✅ |
| 7 | Madurez Competencial | `MMC-SP-Modelo-Madurez-Competencial-v1.md` | ✅ |
| 8 | Inteligencia Operativa | `Sistema-Inteligencia-Operativa-v1.md` | ✅ |
| 9 | Gobernanza y Mejora Continua | `Programa-Gobernanza-Mejora-Continua-v1.md` | ✅ |

**El desarrollo conceptual del Modelo Integral, en su versión ágil, está terminado.**

## Pendientes generales (fases de profundización y validación, no diseño)

⏳ Ampliar el IARF al Reglamento estatal, Ley/Reglamento Federal y EC0060.
⏳ Decidir si se desarrolla el "Curso 22 — Especialización en Modalidades Armadas".
⏳ Personalizar el Manual Maestro de PNO con los procedimientos de un sitio/cliente real.
⏳ Actualizar el IARF v1 con la correspondencia de competencias derivadas (ajuste menor).
⏳ Realizar el primer ciclo anual de revisión formal del Subsistema 9.
⏳ Aplicar el MMC-SP con un grupo piloto real.
⏳ Llenar el Tablero de Control del Subsistema 8 con datos reales del piloto.

Todos estos pendientes comparten una misma condición: **requieren la validación práctica
del kit con personal real**, un pendiente que se identificó desde el cierre del Proyecto 1
y que aún no se ha abordado.
