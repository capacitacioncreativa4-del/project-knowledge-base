---
conversation_id: MIPSP-CONV-0001
title: Revisión normativa capacitación
project: MIPSP
source: ChatGPT
status: Original
created_by: Miguel Angel
ingestion_status: Pending
part: 38
---
# Conversación original
(Contenido del chat correspondiente a esta parte)

Adelante. Continúa con el proyecto

Perfecto. Considero que estamos entrando en la fase más importante del proyecto. Si mantenemos el nivel metodológico alcanzado, esta obra dejará de ser un manual de capacitación y se convertirá en un **Modelo Integral de Profesionalización para Empresas de Seguridad Privada**, susceptible de utilizarse como referencia institucional, para procesos de autorización, auditoría interna, certificación y mejora continua.

Después de haber estudiado nuevamente las cinco fuentes normativas, encuentro una oportunidad de gran valor: **incorporar el enfoque de procesos**. Las normas regulan obligaciones; el EC0060 define competencias; pero ninguna de las fuentes modela cómo fluye el trabajo operativo de principio a fin. Ese vacío lo llenaremos nosotros.

A partir de este momento, cada competencia operativa estará integrada por cinco niveles de análisis:

1. **Nivel jurídico** (qué exige la norma).
2. **Nivel competencial** (qué debe saber hacer el elemento).
3. **Nivel de proceso** (cómo se ejecuta el trabajo).
4. **Nivel de riesgo** (qué puede fallar y cómo prevenirlo).
5. **Nivel didáctico** (cómo enseñar y evaluar la competencia).

Este será el sello distintivo de la obra.

---

# TOMO III

# CATÁLOGO MAESTRO DE COMPETENCIAS (CMC)

## COMPETENCIA OPERATIVA FUNDAMENTAL

# COMP-OPS-010

# CONTROL DE ACCESOS

## Capítulo II

# Arquitectura Funcional del Proceso

---

# 2.1 Visión sistémica

El control de accesos no debe entenderse como una sucesión de tareas independientes. Constituye un **proceso operativo integrado**, en el que cada decisión condiciona la eficacia de la siguiente etapa.

Un error en la identificación puede invalidar el registro.

Un registro incompleto puede impedir la trazabilidad.

Una autorización incorrecta puede comprometer la seguridad de toda la instalación.

Desde la perspectiva de la gestión por procesos, el control de accesos es un sistema con entradas, transformaciones, controles y salidas.

---

## Entradas

### Personas

* Empleados.
* Visitantes.
* Proveedores.
* Contratistas.
* Autoridades.
* Clientes.
* Personal de mantenimiento.
* Servicios de emergencia.

### Bienes

* Herramientas.
* Equipos.
* Materiales.
* Paquetería.
* Documentación.
* Activos propiedad del cliente.

### Información

* Listas de autorización.
* Consignas.
* Credenciales.
* Órdenes de trabajo.
* Programación de visitas.
* Protocolos especiales.

---

## Recursos

* Personal operativo.
* Supervisor.
* Barreras físicas.
* Sistemas electrónicos de control de acceso.
* CCTV.
* Radios.
* Bitácoras.
* Formatos.
* Manual operativo.
* Procedimientos Normalizados de Operación (PNO).

---

## Salidas

* Acceso autorizado.
* Acceso restringido.
* Acceso condicionado.
* Incidencia reportada.
* Registro documental.
* Evidencia para auditoría.

---

# 2.2 Modelo Operativo Integrado (MOI)

```text
SOLICITUD DE INGRESO
          │
          ▼
RECEPCIÓN
          │
          ▼
IDENTIFICACIÓN
          │
          ▼
AUTENTICACIÓN
          │
          ▼
VALIDACIÓN DE AUTORIZACIÓN
          │
          ▼
EVALUACIÓN DEL RIESGO
          │
     ┌────┼────┐
     │    │    │
     ▼    ▼    ▼
AUTORIZAR RESTRINGIR ESCALAR
     │    │    │
     └────┼────┘
          ▼
REGISTRO
          ▼
MONITOREO
          ▼
SALIDA
          ▼
CIERRE DEL EVENTO
```

Este modelo será común para todas las modalidades de control de accesos, adaptándose únicamente las reglas de decisión según el tipo de servicio.

---

# 2.3 Puntos Críticos de Control (PCC)

Se identifican los siguientes PCC:

| PCC    | Etapa          | Riesgo principal                   | Medida de control                                         |
| ------ | -------------- | ---------------------------------- | --------------------------------------------------------- |
| PCC-01 | Recepción      | Omisión del procedimiento inicial  | Confirmar tipo de usuario y motivo del acceso             |
| PCC-02 | Identificación | Suplantación de identidad          | Verificación de credenciales y documentos autorizados     |
| PCC-03 | Autorización   | Ingreso no autorizado              | Confirmación con listas, sistemas o responsable designado |
| PCC-04 | Registro       | Pérdida de trazabilidad            | Registro completo y legible de la información requerida   |
| PCC-05 | Monitoreo      | Permanencia indebida               | Seguimiento de tiempos y áreas autorizadas                |
| PCC-06 | Salida         | Extracción no autorizada de bienes | Verificación conforme a los procedimientos establecidos   |

---

# 2.4 Modos de Falla Operativa (MFO)

Inspirado en metodologías de análisis de fallos, se propone identificar los principales modos de falla que pueden presentarse durante el proceso.

| Código | Modo de falla                          | Consecuencia                            |
| ------ | -------------------------------------- | --------------------------------------- |
| MFO-01 | No solicitar identificación            | Acceso de persona no autorizada         |
| MFO-02 | Verificación incompleta                | Suplantación de identidad               |
| MFO-03 | Registro parcial                       | Pérdida de trazabilidad                 |
| MFO-04 | Interpretación incorrecta de consignas | Decisiones inconsistentes               |
| MFO-05 | Falta de comunicación con supervisión  | Retraso en la respuesta ante incidentes |
| MFO-06 | Omisión del control de salida          | Pérdida o extracción indebida de bienes |

---

# 2.5 Controles Preventivos, Detectivos y Correctivos

## Controles preventivos

* Capacitación inicial y periódica.
* Actualización de consignas.
* Revisión diaria del puesto de control.
* Verificación del funcionamiento del equipo.
* Simulaciones de escenarios críticos.

## Controles detectivos

* Supervisión en sitio.
* Revisión de bitácoras.
* Auditorías documentales.
* Análisis de grabaciones de CCTV.
* Indicadores de desempeño.

## Controles correctivos

* Retroalimentación individual.
* Reentrenamiento focalizado.
* Actualización de procedimientos.
* Investigación de incidentes.
* Implementación de acciones correctivas y preventivas (CAPA).

---

# 2.6 Indicadores Clave de Desempeño (KPI)

Para evaluar la eficacia del proceso se propone el siguiente conjunto inicial de indicadores:

| Código    | Indicador                                | Fórmula                                                                            | Meta                     |
| --------- | ---------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------ |
| KPI-CA-01 | Cumplimiento del procedimiento de acceso | Procedimientos ejecutados correctamente / Total de procedimientos observados × 100 | ≥ 98 %                   |
| KPI-CA-02 | Exactitud de los registros               | Registros sin errores / Total de registros × 100                                   | ≥ 99 %                   |
| KPI-CA-03 | Incidentes por acceso no autorizado      | Total de incidentes                                                                | 0                        |
| KPI-CA-04 | Tiempo promedio de atención              | Tiempo total / Número de accesos                                                   | Definido por el servicio |
| KPI-CA-05 | Cumplimiento de consignas                | Observaciones conformes / Observaciones totales × 100                              | ≥ 95 %                   |

---

# 2.7 Diseño instruccional de la competencia

La capacitación no debe limitarse a la explicación del procedimiento. Se propone una secuencia didáctica basada en el aprendizaje progresivo:

### Fase 1. Comprensión conceptual

* Marco jurídico.
* Finalidad del control de accesos.
* Tipología de usuarios.
* Gestión del riesgo.

### Fase 2. Demostración

* Ejecución del procedimiento por un instructor.
* Explicación de decisiones críticas.
* Identificación de errores frecuentes.

### Fase 3. Práctica guiada

* Simulaciones con retroalimentación inmediata.
* Escenarios de dificultad creciente.
* Rotación de roles.

### Fase 4. Práctica autónoma

* Ejecución individual.
* Resolución de incidencias.
* Registro documental completo.

### Fase 5. Evaluación de competencia

* Observación estructurada.
* Caso integrador.
* Evaluación escrita.
* Entrevista técnica.
* Retroalimentación final.

---

# 2.8 Matriz de trazabilidad normativa

Una de las innovaciones metodológicas de esta obra será la incorporación de una matriz que vincule cada competencia con sus fundamentos jurídicos y curriculares.

| Elemento                  | Referencia                                                                                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Obligación legal          | Ley Federal de Seguridad Privada, Reglamento Federal, Ley de Seguridad Privada para el Estado de Morelos y su Reglamento (disposiciones aplicables sobre capacitación, manuales operativos, actuación del personal y prestación del servicio)     |
| Competencia laboral       | EC0060 (desempeños, conocimientos, productos, actitudes y valores)                                                                                                                                                                                |
| Ficha FARF relacionada    | FARF-0001 a FARF-0009                                                                                                                                                                                                                             |
| Procedimiento Normalizado | PNO-CA-001 Control de Accesos                                                                                                                                                                                                                     |
| Curso asociado            | CUR-OPS-001 Control de Accesos                                                                                                                                                                                                                    |
| Instrumento de evaluación | IE-CA-001 Lista de cotejo y guía de observación                                                                                                                                                                                                   |

---

# Propuesta de evolución del proyecto

A partir de este punto propongo que la obra evolucione hacia una estructura documental comparable con la utilizada en sistemas de gestión de alta confiabilidad. Para ello incorporaremos tres componentes adicionales:

1. **Procedimientos Normalizados de Operación (PNO):** cada competencia tendrá un procedimiento operativo completo, con objetivo, alcance, responsabilidades, desarrollo, registros y criterios de control.

2. **Escenarios de simulación y banco de casos:** cada competencia incluirá situaciones reales, graduales y evaluables, alineadas con el EC0060 y con las obligaciones normativas identificadas.

3. **Matriz de correspondencia normativa:** al final de la obra habrá una matriz donde cualquier artículo de las leyes o reglamentos pueda localizarse inmediatamente en los cursos, competencias, PNO, formatos, indicadores e instrumentos de evaluación que lo desarrollan.

Con estos elementos, el proyecto trascenderá el formato tradicional de un manual de capacitación y se convertirá en un **Sistema Integral de Profesionalización**, con plena trazabilidad entre la norma, la operación y el aprendizaje. Ese enfoque permitirá utilizar la obra como base para programas de capacitación, auditorías internas, supervisión operativa y procesos de mejora continua en empresas de seguridad privada.
