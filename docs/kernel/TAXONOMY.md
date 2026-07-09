---
id: PKB-KERNEL-TAXONOMY-001
title: Repository Taxonomy
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: KERNEL
domain: PKB
parent: PKB-KERNEL-MANIFEST-001
tags:
  - kernel
  - taxonomy
  - structure
---

# Taxonomía Institucional de la Base de Conocimiento

## Propósito
Definir la arquitectura de carpetas, categorías de indexación y dominios de conocimiento oficiales del Project Knowledge Base (PKB). Esta taxonomía garantiza una organización lógica que previene la fragmentación de activos y optimiza el consumo semántico para búsquedas manuales o automatizaciones con inteligencia artificial.

---

# Estructura de Directorios del Ecosistema

El repositorio se organiza de manera formal bajo el siguiente árbol de directorios raíz, constituyendo el estándar taxonómico obligatorio:

```text
project-knowledge-base/
├── docs/                   # Documentación conceptual, técnica y estratégica
│   ├── kernel/             # Modelos fundamentales (Metadata, Taxonomy, Identity)
│   ├── governance/         # Políticas, Visión, Misión y directrices macro
│   ├── architecture/       # ADRs y lineamientos técnicos de sistemas
│   ├── standards/          # Estándares operativos y de codificación
│   └── templates/          # Plantillas oficiales reutilizables (TMP)
├── registers/              # Registros dinámicos de control técnico
│   ├── decisions/          # Historial extendido de decisiones arquitectónicas
│   ├── risks/              # Matrices y registros de mitigación de riesgos
│   └── metrics/            # Indicadores de calidad y salud del sistema
├── automation/             # Scripts, configuraciones CI/CD y flujos de IA
└── projects/               # Directorios asignados a los dominios de aplicación
    ├── mipsp/              # Marco Institucional de Procesos
    ├── sim-pyme/           # Plataforma SIM-PYME
    ├── condominios/        # Sistema de Gestión de Condominios
    └── manualidades/       # Repositorio de Manualidades y proyectos compartidos