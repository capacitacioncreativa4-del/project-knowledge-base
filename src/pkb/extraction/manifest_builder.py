import os
import re

# Definición de la estructura de directorios del espacio de ejecución (Runtime)
RUNTIME_DIRS = {
    "manifests": "runtime/manifests",
    "workspace": "runtime/workspace",
    "packages": "runtime/packages",
    "cache": "runtime/cache",
    "exports": "runtime/exports"
}

# Patrones de expresiones regulares para identificar entidades dentro del Markdown de conversaciones
REGEX_PATTERNS = {
    "conversation_id": re.compile(r"(?:CONV|MIPSP-CONV)-(\d+)"),
    "knowledge_package": re.compile(r"KP-(\d+)"),
    "sessions": re.compile(r"SES-(\d+)"),
    "adr": re.compile(r"ADR-(\d+)"),
    "requirement": re.compile(r"REQ-[A-Z0-9-]+"),
    "standard": re.compile(r"STD-[A-Z0-9-]+"),
    "document": re.compile(r"DOC-[A-Z0-9-]+")
}

def initialize_runtime_environment():
    """
    Crea la estructura física de carpetas para el entorno de ejecución (Runtime)
    si no existen en el espacio de trabajo actual.
    """
    print("[INFO] Inicializando entorno de ejecución (Runtime)...")
    for name, path in RUNTIME_DIRS.items():
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"  -> Directorio creado: '{path}' ({name})")
        else:
            print(f"  -> Directorio existente: '{path}'")
    print("[INFO] Entorno Runtime inicializado con éxito.\n")


class ManifestBuilder:
    """
    Clase encargada de escanear archivos Markdown de conversaciones 
    y estructurar su correspondiente manifiesto YAML/JSON.
    """
    def __init__(self, source_filepath):
        self.source_filepath = source_filepath
        self.metadata = {
            "conversation_id": "CONV-UNKNOWN",
            "knowledge_package": "KP-UNKNOWN",
            "sessions": [],
            "objects": {
                "adr": [],
                "requirement": [],
                "standard": [],
                "document": []
            }
        }

    def parse(self):
        """Lee el archivo Markdown y extrae todas las entidades que coincidan con los patrones."""
        if not os.path.exists(self.source_filepath):
            raise FileNotFoundError(f"El archivo fuente no existe: {self.source_filepath}")

        print(f"[PARSER] Procesando archivo origen: {self.source_filepath}")
        
        with open(self.source_filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Extraer Identificador de Conversación (con fallback al nombre de archivo)
        conv_match = REGEX_PATTERNS["conversation_id"].search(content)
        if conv_match:
            self.metadata["conversation_id"] = f"CONV-{conv_match.group(1).zfill(6)}"
        else:
            # Fallback: intentar buscar el ID en el propio nombre del archivo físico
            filename = os.path.basename(self.source_filepath)
            conv_file_match = REGEX_PATTERNS["conversation_id"].search(filename)
            if conv_file_match:
                self.metadata["conversation_id"] = f"CONV-{conv_file_match.group(1).zfill(6)}"

        # Extraer Identificador de Paquete de Conocimiento
        kp_match = REGEX_PATTERNS["knowledge_package"].search(content)
        if kp_match:
            self.metadata["knowledge_package"] = f"KP-{kp_match.group(1).zfill(6)}"

        # Extraer Listas de Entidades Coincidentes (eliminando duplicados y ordenando)
        self.metadata["sessions"] = sorted(list(set(
            f"SES-{m.zfill(6)}" for m in REGEX_PATTERNS["sessions"].findall(content)
        )))
        
        self.metadata["objects"]["adr"] = sorted(list(set(
            f"ADR-{m.zfill(6)}" for m in REGEX_PATTERNS["adr"].findall(content)
        )))

        self.metadata["objects"]["requirement"] = sorted(list(set(
            REGEX_PATTERNS["requirement"].findall(content)
        )))

        self.metadata["objects"]["standard"] = sorted(list(set(
            REGEX_PATTERNS["standard"].findall(content)
        )))

        self.metadata["objects"]["document"] = sorted(list(set(
            REGEX_PATTERNS["document"].findall(content)
        )))

        print("[PARSER] Escaneo completado. Entidades encontradas.")

    def save_as_yaml(self):
        """
        Exporta los metadatos recopilados en formato YAML legible 
        dentro de la carpeta runtime/manifests.
        """
        output_filename = f"{self.metadata['conversation_id'].lower()}_manifest.yaml"
        output_filepath = os.path.join(RUNTIME_DIRS["manifests"], output_filename)

        print(f"[EXPORT] Escribiendo manifiesto estructurado en: {output_filepath}")

        # Generador de YAML personalizado para evitar dependencias externas en entornos limpios
        yaml_lines = [
            f"conversation_id: {self.metadata['conversation_id']}",
            f"knowledge_package: {self.metadata['knowledge_package']}",
            "sessions:"
        ]
        
        if self.metadata["sessions"]:
            for session in self.metadata["sessions"]:
                yaml_lines.append(f"  - {session}")
        else:
            yaml_lines.append("  []")

        yaml_lines.append("objects:")
        
        for obj_type, items in self.metadata["objects"].items():
            yaml_lines.append(f"  {obj_type}:")
            if items:
                for item in items:
                    yaml_lines.append(f"    - {item}")
            else:
                yaml_lines.append("      []")

        with open(output_filepath, 'w', encoding='utf-8') as out_file:
            out_file.write("\n".join(yaml_lines) + "\n")

        print(f"[SUCCESS] Manifiesto guardado correctamente.\n")
        return output_filepath


def create_demo_conversation():
    """Genera una conversación de prueba si el usuario no tiene una a mano."""
    demo_path = "projects/mipsp/ingestion/sources/MIPSP-CONV-0003-P01.md"
    os.makedirs(os.path.dirname(demo_path), exist_ok=True)
    
    demo_content = """# Minuta de Alineación MIPSP - Sesión 20 y 21
Este documento recopila las decisiones de la sesión SES-20 y SES-21 para el paquete KP-3.
Durante la sesión se acordó implementar el requerimiento REQ-EXT-0001 (Sincronización de Copropietarios)
bajo el estándar legal de condominios STD-CONDOMINIUM-LAW-MORELOS.

También se aprobó la resolución del conflicto de bases de datos mediante el registro ADR-11.
Toda la documentación final se consolidará en el documento oficial DOC-MIPSP-CORE-01.
"""
    with open(demo_path, 'w', encoding='utf-8') as f:
        f.write(demo_content)
    print(f"[DEMO] Conversación de prueba creada en: {demo_path}")
    return demo_path


if __name__ == "__main__":
    # 1. Configurar carpetas
    initialize_runtime_environment()

    # 2. Asegurar existencia de una conversación de prueba
    demo_file = create_demo_conversation()

    # 3. Ejecutar el constructor de manifiestos
    builder = ManifestBuilder(demo_file)
    builder.parse()
    builder.save_as_yaml()