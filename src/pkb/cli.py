import argparse
import sys
from pkb.version import VERSION
from pkb.repository.scanner import RepositoryScanner
from pkb.metadata.parser import MetadataParser
from pkb.validators.rules import ValidationEngine

def cmd_validate(args):
    print("==================================================")
    print(f"PKB Platform v{VERSION} - Domain-Driven Architecture")
    print("==================================================\n")
    
    ruta_raiz = "."
    print(f"🔍 Escaneando repositorio en: {ruta_raiz}...")
    
    try:
        archivos = RepositoryScanner.markdown_files(ruta_raiz)
        print(f"📂 Se encontraron {len(archivos)} objetos de conocimiento para auditoría.\n")
        
        total_errores = 0
        archivos_con_fallas = 0
        
        for archivo in archivos:
            try:
                # El parser ahora retorna una instancia formal de KnowledgeObject
                knowledge_object, _ = MetadataParser.parse_file(str(archivo))
                
                # El motor audita el objeto de dominio y devuelve un ValidationResult estructurado
                resultado = ValidationEngine.validate_metadata(knowledge_object)
                
                if not resultado.success:
                    archivos_con_fallas += 1
                    print(f"❌ {resultado.document}:")
                    for err in resultado.errors:
                        print(f"   - {err}")
                        total_errores += 1
            except Exception as e:
                archivos_con_fallas += 1
                print(f"💥 {archivo.name}: Error crítico en el pipeline -> {str(e)}")
                total_errores += 1
                
        print("\n--------------------------------------------------")
        if total_errores == 0:
            print("🟢 ¡VALIDACIÓN EXITOSA! Todos los objetos de conocimiento cumplen los estándares.")
            sys.exit(0)
        else:
            print(f"🔴 VALIDACIÓN FALLIDA: {total_errores} error(es) en {archivos_con_fallas} documento(s).")
            sys.exit(1)
            
    except Exception as e:
        print(f"🔴 Error general del sistema: {str(e)}")
        sys.exit(1)

def cmd_version(args):
    print(VERSION)

def build_parser():
    parser = argparse.ArgumentParser(
        prog="pkb",
        description="Project Knowledge Base Platform"
    )
    parser.add_argument(
        "--version",
        action="store_true"
    )
    
    sub = parser.add_subparsers(dest="command")
    
    validate = sub.add_parser(
        "validate",
        help="Ejecuta la auditoría integral basada en objetos de dominio"
    )
    validate.set_defaults(func=cmd_validate)
    
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    
    if args.version:
        cmd_version(args)
        return
        
    if hasattr(args, "func"):
        args.func(args)
        return
        
    parser.print_help()