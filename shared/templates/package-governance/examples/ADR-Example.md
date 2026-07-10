---
id: PKB-ADR-0008
title: "ADR-0008: Arquitectura de Grafo de Conocimiento sobre Git y Markdown"
version: 1.0.0
status: Approved
owner: Architecture
created: 2026-07-09
updated: 2026-07-09
type: ADR
domain: PKB
tags:
  - architecture
  - adr
  - knowledge-graph
---

# ADR-0008: Arquitectura de Grafo de Conocimiento sobre Git y Markdown

## Estado
Approved[cite: 2]

---

# Contexto
El Project Knowledge Base (PKB) está creciendo en volumen de documentos y requiere capacidades avanzadas de indexación, consistencia relacional y consumo inteligente por parte de agentes de IA, evitando que la información quede aislada en simples árboles de carpetas estáticas[cite: 2].

---

# Problema
¿Cómo estructurar un Grafo de Conocimiento (Knowledge Graph) interoperable y navegable sin introducir bases de datos orientadas a grafos complejas que rompan la portabilidad, simplicidad y el control de versiones nativo de Git y Markdown?[cite: 2]

---

# Decisión
Diseñar el PKB como un grafo de conocimiento lógico, preservando el almacenamiento físico en archivos Markdown dentro de un repositorio Git convencional[cite: 2]. 

La capa semántica se construirá exclusivamente mediante la combinación obligatoria de dos elementos[cite: 2]:
1. Identificadores persistentes unívocos definidos en los metadatos YAML[cite: 1, 2].
2. Enlaces relacionales explícitos tipificados dentro del cuerpo del texto mediante rutas relativas[cite: 2].

Esto nos permitirá exportar el grafo lógico a formatos estándar de la industria (RDF, JSON-LD o GraphML) en el futuro mediante scripts de automatización, sin alterar el contenido original de los documentos[cite: 2].

---

# Alternativas consideradas

## Alternativa A: Base de datos de Grafos dedicada (Neo4j)
- **Pros**: Consultas nativas inmediatas en lenguaje Cypher.
- **Contras**: Requiere infraestructura adicional, rompe el principio de descentralización en texto plano y complica el versionado por Pull Requests.

## Alternativa B: Sistema Wiki Tradicional (Confluence)
- **Pros**: Curva de aprendizaje baja.
- **Contras**: Cero capacidades semánticas nativas para agentes de IA y dependencia total de software propietario.

---

# Consecuencias

## Beneficios
- **Cero Infraestructura**: Portabilidad absoluta en cualquier máquina local con editores de texto básicos[cite: 2].
- **Preparación para IA**: Permite a los agentes inteligentes recorrer relaciones, localizar dependencias cruzadas de forma exacta y realizar análisis de impacto automáticos[cite: 2].
- **Evolución Flexible**: El repositorio documental se convierte en una plataforma interoperable sin necesidad de rehacer su arquitectura[cite: 2].

## Riesgos
- **Rigidez Sintáctica**: Requiere validación estricta de metadatos y enlaces para prevenir referencias rotas que actúen como defectos documentales[cite: 2].

---

# Relaciones

## Documento superior
- PKB-KERNEL-KOM-001[cite: 2]

## Relacionados
- [TRACEABILITY-MODEL.md](../../../../docs/kernel/TRACEABILITY-MODEL.md)[cite: 2]
- [IDENTIFIER-SCHEME.md](../../../../docs/kernel/IDENTIFIER-SCHEME.md)[cite: 2]

---

# Historial
| Versión | Fecha | Descripción |
|---------|-------|-------------|
| 1.0.0   | 2026-07-09 | Aprobación inicial de la estrategia de grafos semánticos.[cite: 2] |