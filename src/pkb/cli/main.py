import argparse
import sys
from pathlib import Path
from pkb.version import VERSION
from pkb.knowledge.loader import KnowledgeLoader
from pkb.knowledge.catalog import KnowledgeCatalog
from pkb.validators.rules import ValidationEngine
from pkb.reporting.markdown_report import MarkdownInventoryReport

def cmd_validate(args):
    print("==================================================")
    print(f"PKB Platform v{VERSION} - Domain-Driven Architecture")
    print("==================================================\n")
    
    from pkb.repository.scanner import RepositoryScanner
    from pkb.metadata.parser import MetadataParser
    
    archivos = RepositoryScanner.markdown_files(".")
    print(f"🔍 Escaneando {len(archivos)} archivos Markdown...\n")
    
    total_errores = 0
    archivos_con_fallas = 0
    
    for archivo in archivos:
        try:
            metadata_cruda, _ = MetadataParser.parse_file(str(archivo))
            resultado = ValidationEngine.validate_metadata(metadata_cruda)
            if not resultado.success:
                archivos_con_fallas += 1
                print(f"❌ {archivo}:")
                for err in resultado.errors:
                    print(f"   - {err}")
                    total_errores += 1
        except Exception as e:
            archivos_con_fallas += 1
            print(f"❌ {archivo}: Error crítico de lectura: {str(e)}")
            total_errores += 1
                
    print("\n--------------------------------------------------")
    if total_errores == 0:
        print("🟢 ¡VALIDACIÓN EXITOSA! Todos los objetos de conocimiento cumplen los estándares.")
        sys.exit(0)
    else:
        print(f"🔴 VALIDACIÓN FALLIDA: {total_errores} error(es) en {archivos_con_fallas} documento(s).")
        sys.exit(1)

def cmd_inventory(args):
    print("==================================================")
    print(f"PKB Platform v{VERSION} - Repository Inventory")
    print("==================================================\n")
    
    # 1. Cargar el repositorio en memoria usando el motor
    registry = KnowledgeLoader.load_repository(".")
    catalog = KnowledgeCatalog(registry)
    
    # 2. Imprimir resumen por consola con formato alineado
    print(f"Total Objects ............. {registry.count()}")
    
    por_tipo = catalog.by_type()
    for tipo, cantidad in por_tipo.most_common():
        # Ajustamos el espaciado para que se vea limpio en la terminal
        puntos = "." * (23 - len(tipo))
        print(f"{tipo} {puntos} {cantidad}")
        
    # 3. Generar y exportar automáticamente el reporte Markdown a disco
    try:
        reporte_md = MarkdownInventoryReport.generate(catalog)
        carpeta_reportes = Path("reports")
        carpeta_reportes.mkdir(exist_ok=True)
        
        ruta_archivo = carpeta_reportes / "repository-inventory.md"
        ruta_archivo.write_text(reporte_md, encoding="utf-8")
        print(f"\n💾 Reporte guardado con éxito en: {ruta_archivo}")
    except Exception as e:
        print(f"\n⚠️ No se pudo guardar el archivo de reporte: {str(e)}")

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
    
    # Comando pkb validate
    validate = sub.add_parser(
        "validate",
        help="Ejecuta la auditoría integral basada en objetos de dominio en memoria"
    )
    validate.set_defaults(func=cmd_validate)
    
    # Nuevo comando pkb inventory
    inventory = sub.add_parser(
        "inventory",
        help="Genera un inventario estadístico completo de los objetos de conocimiento"
    )
    inventory.set_defaults(func=cmd_inventory)
    
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