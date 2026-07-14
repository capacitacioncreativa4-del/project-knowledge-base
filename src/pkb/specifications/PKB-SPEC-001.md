# PKB-SPEC-001: Project Knowledge Base Specification (v1.0)

## 1. Introducción y Propósito
Este documento constituye la norma técnica fundamental del Project Knowledge Base (PKB)[cite: 6]. Define los requerimientos arquitectónicos, sintácticos y relacionales que todo cliente u herramienta de IA debe respetar para operar sobre el grafo de conocimiento[cite: 6].

## 2. El Metamodelo de Entidades
La plataforma reconoce exclusivamente las siguientes entidades nucleares, identificadas unívocamente mediante un ID de 6 dígitos con su respectivo prefijo de tres letras[cite: 3, 6]:

* **CONV**: Conversation (Fuentes primarias de origen)
* **KP**: Knowledge Package (Contenedores lógicos de distribución)
* **SES**: Engineering Session (Diseño y análisis)
* **ADR**: Architecture Decision Record (Puntos de inflexión técnica)
* **REQ**: Requirement (Obligaciones operativas)
* **STD**: Standard (Reglas y directrices de ingeniería)
* **ART**: Conceptual Artifact (Modelos y marcos abstractos)
* **DOC**: Editorial Document (Productos listos para publicación)
* **SYS**: Institutional System (Sistemas de software integrados)