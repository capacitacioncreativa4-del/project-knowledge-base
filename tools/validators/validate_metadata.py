"""
PKB Metadata Validator
Version: 1.0.0
Valida los encabezados YAML de todos los documentos Markdown del repositorio.
"""
import sys
import re
from pathlib import Path
import yaml

# Configuración de rutas relativas basadas en la arquitectura del repositorio
ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "tools" / "config" / "metadata_schema.yaml"
REPORT_PATH = ROOT / "tools" / "reports" / "metadata_validation_report.md"

def load_schema():
    """Carga las reglas de validación desde el esquema centralizado."""
    if not SCHEMA_PATH.exists():
        print(f"❌ Error: No se encontró el esquema en {SCHEMA_PATH}")
        sys.exit(1)
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)

def extract_front_matter(file_path):
    """Extrae el bloque Front Matter (YAML) entre los delimitadores '---'."""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
        
        # Expresión regular para capturar el primer bloque delimitado por ---
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if match:
            return yaml.safe_load(match.group(1)), None
        return None, "Falta el bloque Front Matter (---) al inicio del documento."
    except yaml.YAMLError as e:
        return None, f"Sintaxis YAML inválida: {e}"
    except Exception as e:
        return None, f"Error al leer el archivo: {e}"

def validate_document(metadata, schema):
    """Evalúa los metadatos de un documento individual contra el esquema."""
    errors = []
    if not metadata or not isinstance(metadata, dict):
        return ["El documento no contiene un diccionario de metadatos válido."]

    # 1. Validar campos obligatorios
    for field in schema.get("required", []):
        if field not in metadata or metadata[field] is None:
            errors.append(f"Campo obligatorio ausente o vacío: '{field}'")

    # 2. Validar valores restringidos para el estado (status)
    if "status" in metadata and "status" in schema:
        if metadata["status"] not in schema["status"]:
            errors.append(f"Estado inválido: '{metadata['status']}'. Permitidos: {schema['status']}")

    # 3. Validar patrón de versión por expresión regular
    if "version" in metadata and "version_pattern" in schema:
        version_str = str(metadata["version"])
        if not re.match(schema["version_pattern"], version_str):
            errors.append(f"Formato de versión inválido: '{version_str}'. Debe cumplir la regex {schema['version_pattern']}")

    return errors

def generate_markdown_report(results):
    """Genera un reporte analítico estructurado en la carpeta de reportes."""
    total_files = len(results)
    failed_files = [r for r in results if r["errors"]]
    
    markdown = "# Reporte de Validación de Metadatos (QA)\n\n"
    markdown += f"- **Estado general:** {'❌ RECHAZADO' if failed_files else '✅ APROBADO'}\n"
    markdown += f"- **Archivos evaluados:** {total_files}\n"
    markdown += f"- **Archivos con defectos:** {len(failed_files)}\n\n"
    
    if not failed_files:
        markdown += "## ✅ Conclusiones\nTodos los documentos analizados cumplen estrictamente las directrices del esquema de metadatos institucional.\n"
    else:
        markdown += "## ❌ Defectos detectados\nSe requiere corregir los siguientes archivos antes de realizar la integración:\n\n"
        for item in failed_files:
            markdown += f"### 📄 `{item['relative_path']}`\n"
            for err in item["errors"]:
                markdown += f"- {err}\n"
            markdown += "\n"
            
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(markdown)
    return len(failed_files) > 0

def main():
    print("🚀 Ejecutando el Motor de Validación de Metadatos del PKB...")
    schema = load_schema()
    results = []
    
    # Escaneo recursivo del repositorio excluyendo directorios técnicos
    for path in ROOT.rglob("*.md"):
        # Ignorar herramientas de validación, reportes y directorios ocultos de Git
        if "tools" in path.parts or ".git" in path.parts:
            continue
            
        relative_path = path.relative_to(ROOT)
        metadata, err = extract_front_matter(path)
        
        if err:
            results.append({"relative_path": relative_path, "errors": [err]})
        else:
            errors = validate_document(metadata, schema)
            results.append({"relative_path": relative_path, "errors": errors})
            
    # Generar el reporte físico
    has_errors = generate_markdown_report(results)
    print(f"📊 Análisis finalizado. Reporte guardado en: {REPORT_PATH.relative_to(ROOT)}")
    
    # Código de salida dinámico: 1 si hay fallos (rompe la build de CI), 0 si todo está limpio
    if has_errors:
        print("❌ Control de calidad rechazado. Se encontraron defectos documentales.")
        sys.exit(1)
    else:
        print("✅ Control de calidad exitoso. Repositorio en estado saludable.")
        sys.exit(0)

if __name__ == "__main__":
    main()