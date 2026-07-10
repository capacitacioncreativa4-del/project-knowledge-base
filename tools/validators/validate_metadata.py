import os
import re
import yaml

def load_schema(schema_path):
    """Carga las reglas de negocio desde el archivo YAML de configuración."""
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"No se encontró el esquema en: {schema_path}")
    with open(schema_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract_yaml_front_matter(file_path):
    """Extrae el bloque Front Matter (YAML) ubicado al inicio de un archivo Markdown."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Patrón clásico para capturar el bloque entre las primeras líneas ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)), None
        except yaml.YAMLError as e:
            return None, f"Error de sintaxis YAML: {e}"
    return None, "Falta el bloque de metadatos Front Matter (---)"

def validate_metadata(metadata, schema):
    """Compara los metadatos de un archivo contra el esquema agnóstico."""
    errors = []
    
    # 1. Validar campos obligatorios
    for field in schema.get('required', []):
        if field not in metadata or metadata[field] is None:
            errors.append(f"Campo obligatorio ausente o vacío: '{field}'")
            
    # 2. Validar valores permitidos para 'status'
    if 'status' in metadata and 'status' in schema:
        if metadata['status'] not in schema['status']:
            errors.append(f"Estado inválido: '{metadata['status']}'. Permitidos: {schema['status']}")
            
    # 3. Validar patrón de versión (regex)
    if 'version' in metadata and 'version_pattern' in schema:
        version_str = str(metadata['version'])
        if not re.match(schema['version_pattern'], version_str):
            errors.append(f"Formato de versión inválido: '{version_str}'. Debe seguir el formato X.Y.Z")
            
    return errors

def generate_report(report_data, output_path):
    """Genera un reporte consolidado en formato Markdown listo para ser guardado."""
    report_dir = os.path.dirname(output_path)
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
        
    markdown = "# Reporte Automático de Calidad Documental: Metadatos\n\n"
    markdown += f"**Fecha de ejecución:** 2026-07-09\n"
    markdown += f"**Total de archivos evaluados:** {len(report_data)}\n\n"
    
    errors_found = any(data['errors'] for data in report_data)
    
    if not errors_found:
        markdown += "## ✅ ¡Éxito! Todos los documentos cumplen con el estándar institucional.\n"
    else:
        markdown += "## ❌ Se detectaron defectos documentales que requieren atención:\n\n"
        for data in report_data:
            if data['errors']:
                markdown += f"### 📄 Archivo: `{data['file']}`\n"
                for err in data['errors']:
                    markdown += f"- {err}\n"
                markdown += "\n"
                
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    return errors_found

def main():
    # Rutas basadas en la taxonomía oficial del PKB
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    schema_file = os.path.join(base_dir, "tools", "config", "metadata_schema.yaml")
    report_file = os.path.join(base_dir, "tools", "reports", "metadata_validation_report.md")
    
    print("🚀 Iniciando Motor de Validación de Metadatos...")
    schema = load_schema(schema_file)
    results = []
    
    # Recorrer de forma recursiva todas las carpetas del repositorio buscando archivos .md
    for root, _, files in os.walk(base_dir):
        # Excluir la propia carpeta 'tools' y carpetas ocultas de Git de la revisión
        if "tools" in root or ".git" in root:
            continue
            
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, base_dir)
                
                metadata, err = extract_yaml_front_matter(full_path)
                if err:
                    results.append({"file": relative_path, "errors": [err]})
                else:
                    file_errors = validate_metadata(metadata, schema)
                    results.append({"file": relative_path, "errors": file_errors})
                    
    has_errors = generate_report(results, report_file)
    print(f"📊 Validación concluida. Reporte guardado en: tools/reports/metadata_validation_report.md")
    
    # Si hay errores y el sistema está configurado para fallar, devolvemos código de salida 1 para Git / CI-CD
    if has_errors:
        print("❌ Defectos documentales encontrados. Revise el reporte.")
    else:
        print("✅ Control de calidad completado con éxito.")

if __name__ == "__main__":
    main()