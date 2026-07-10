# Reporte de Validación de Metadatos (QA)

- **Estado general:** ❌ RECHAZADO
- **Archivos evaluados:** 34
- **Archivos con defectos:** 23

## ❌ Defectos detectados
Se requiere corregir los siguientes archivos antes de realizar la integración:

### 📄 `CHANGELOG.md`
- Falta el bloque Front Matter (---) al inicio del documento.

### 📄 `CONTRIBUTING.md`
- Campo obligatorio ausente o vacío: 'title'
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'
- Estado inválido: 'draft'. Permitidos: ['Draft', 'Review', 'Approved', 'Published', 'Deprecated', 'Archived']
- Formato de versión inválido: '0.1.0-alpha'. Debe cumplir la regex ^[0-9]+\.[0-9]+\.[0-9]+$

### 📄 `CORE-PRINCIPLES.md`
- Campo obligatorio ausente o vacío: 'title'
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'
- Estado inválido: 'draft'. Permitidos: ['Draft', 'Review', 'Approved', 'Published', 'Deprecated', 'Archived']
- Formato de versión inválido: '0.1.0-alpha'. Debe cumplir la regex ^[0-9]+\.[0-9]+\.[0-9]+$

### 📄 `MISSION.md`
- Campo obligatorio ausente o vacío: 'title'
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'
- Estado inválido: 'draft'. Permitidos: ['Draft', 'Review', 'Approved', 'Published', 'Deprecated', 'Archived']
- Formato de versión inválido: '0.1.0-alpha'. Debe cumplir la regex ^[0-9]+\.[0-9]+\.[0-9]+$

### 📄 `README.md`
- Falta el bloque Front Matter (---) al inicio del documento.

### 📄 `ROADMAP.md`
- Falta el bloque Front Matter (---) al inicio del documento.

### 📄 `VISION.md`
- Campo obligatorio ausente o vacío: 'title'
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'
- Estado inválido: 'draft'. Permitidos: ['Draft', 'Review', 'Approved', 'Published', 'Deprecated', 'Archived']
- Formato de versión inválido: '0.1.0-alpha'. Debe cumplir la regex ^[0-9]+\.[0-9]+\.[0-9]+$

### 📄 `shared\templates\package-governance\ADR-TEMPLATE.md`
- Campo obligatorio ausente o vacío: 'id'
- Campo obligatorio ausente o vacío: 'title'
- Campo obligatorio ausente o vacío: 'owner'
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `shared\templates\package-governance\CHANGELOG-TEMPLATE.md`
- Falta el bloque Front Matter (---) al inicio del documento.

### 📄 `shared\templates\package-governance\CHECKLIST.md`
- Falta el bloque Front Matter (---) al inicio del documento.

### 📄 `shared\templates\package-governance\COMODIN.md`
- Falta el bloque Front Matter (---) al inicio del documento.

### 📄 `shared\templates\package-governance\GOVERNANCE-TEMPLATE.md`
- Campo obligatorio ausente o vacío: 'id'
- Campo obligatorio ausente o vacío: 'title'
- Campo obligatorio ausente o vacío: 'version'
- Campo obligatorio ausente o vacío: 'status'
- Campo obligatorio ausente o vacío: 'owner'
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'
- Estado inválido: 'None'. Permitidos: ['Draft', 'Review', 'Approved', 'Published', 'Deprecated', 'Archived']
- Formato de versión inválido: 'None'. Debe cumplir la regex ^[0-9]+\.[0-9]+\.[0-9]+$

### 📄 `shared\templates\package-governance\POLICY-TEMPLATE.md`
- Campo obligatorio ausente o vacío: 'id'
- Campo obligatorio ausente o vacío: 'title'
- Campo obligatorio ausente o vacío: 'version'
- Campo obligatorio ausente o vacío: 'status'
- Campo obligatorio ausente o vacío: 'owner'
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'
- Estado inválido: 'None'. Permitidos: ['Draft', 'Review', 'Approved', 'Published', 'Deprecated', 'Archived']
- Formato de versión inválido: 'None'. Debe cumplir la regex ^[0-9]+\.[0-9]+\.[0-9]+$

### 📄 `shared\templates\package-governance\README.md`
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `docs\architecture\ADR-0001-Project-Knowledge-Base.md`
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'
- Estado inválido: 'Accepted'. Permitidos: ['Draft', 'Review', 'Approved', 'Published', 'Deprecated', 'Archived']

### 📄 `docs\governance\CORE-PRINCIPLES.md`
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `docs\governance\MISSION.md`
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `docs\governance\VISION.md`
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `docs\kernel\IDENTIFIER-STANDARD.md`
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `docs\kernel\KNOWLEDGE-OBJECT-MODEL.md`
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `docs\kernel\METADATA-MODEL.md`
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `docs\kernel\PKB-MANIFEST.md`
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'

### 📄 `docs\standards\standards.md`
- Campo obligatorio ausente o vacío: 'title'
- Campo obligatorio ausente o vacío: 'created'
- Campo obligatorio ausente o vacío: 'updated'
- Campo obligatorio ausente o vacío: 'domain'
- Campo obligatorio ausente o vacío: 'tags'
- Estado inválido: 'draft'. Permitidos: ['Draft', 'Review', 'Approved', 'Published', 'Deprecated', 'Archived']
- Formato de versión inválido: '0.1.0-alpha'. Debe cumplir la regex ^[0-9]+\.[0-9]+\.[0-9]+$

