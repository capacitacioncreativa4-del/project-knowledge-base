# Especificación de Entidad: Requirement

## 1. Propósito
La entidad `Requirement` modela cualquier declaración funcional, técnica u organizativa extraída de las sesiones de diseño de la suite MIPSP.

## 2. Atributos Estructurales
* **id:** Identificador único alfanumérico inmutable (ej. REQ-EXT-0001).
* **entity:** Constante fija que debe ser exactamente "Requirement".
* **title:** Nombre corto descriptivo del requerimiento.
* **type:** Categorización funcional o no funcional (FUNCTIONAL / NON_FUNCTIONAL).
* **status:** Estado actual dentro del Object Lifecycle (DRAFT, REVIEW, etc.).
* **relationships:** Mapa de enlaces semánticos direccionales hacia sistemas (`implements`) o estándares (`governed_by`).