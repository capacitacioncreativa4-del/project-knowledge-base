# Reglas de Integridad Automatizadas (v1.0.0)

El sistema de gestión de conocimiento aplica estas reglas de manera determinista antes de compilar cada Knowledge Package[cite: 12]:

* **INT-001:** Ningún objeto de conocimiento puede ser registrado sin un identificador único (UID) global[cite: 12].
* **INT-002:** Ningún objeto puede existir sin una fuente primaria explícita que lo respalde[cite: 12].
* **INT-003:** Todo ADR debe originar al menos un objeto derivado o, en su defecto, justificarse de forma explícita como una decisión independiente[cite: 12].
* **INT-004:** Todo objeto de tipo Documento Editorial (DOC) debe implementar al menos un Requisito (REQ)[cite: 12].
* **INT-005:** Integridad Referencial Estricta. Ninguna relación o arista puede apuntar a un identificador inexistente en el repositorio[cite: 12].
* **INT-006:** Todo Knowledge Package (KP) debe contener de manera obligatoria al menos una fuente primaria y una sesión de ingeniería asociada[cite: 12].