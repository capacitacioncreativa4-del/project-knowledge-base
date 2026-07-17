# PKB General Architecture — Especificación del Producto (v0.1.0)

## 1. Visión del Sistema
El Project Knowledge Base (PKB) no es un gestor documental ni una biblioteca de archivos estáticos. Es una **plataforma de ingeniería del conocimiento** diseñada para capturar, modelar, gobernar, versionar, validar y reutilizar conocimiento técnico estructurado en proyectos complejos.

## 2. Modelo de 7 Capas del Núcleo
El sistema organiza sus componentes de forma modular en las siguientes capas instrumentales y normativas:

1. **/schemas**: Contratos sintácticos rígidos en formato YAML que validan la estructura de los objetos.
2. **/ontology**: Definición semántica, alcance conceptual y significado del metamodelo.
3. **/registry**: Registro maestro de entidades, políticas de identificadores únicos y prefijos globales.
4. **/templates**: Plantillas oficiales instanciables para la creación de nuevos objetos.
5. **/validation**: Motores de reglas en Python y Quality Gates encargados de hacer cumplir los contratos.
6. **/ingestion**: Componentes orientados a transformar fuentes primarias (conversaciones) en paquetes lógicos.
7. **/graph**: Infraestructura de almacenamiento y enlace que compone el Knowledge Graph final.