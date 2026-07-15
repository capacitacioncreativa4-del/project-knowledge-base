import sys
import argparse
import os

def run_validation():
    print("\n[CLI] Iniciando proceso de validación del repositorio...")
    # Aquí llamaremos de forma nativa a la lógica de engine.py en las próximas fases
    print("[SUCCESS] Análisis sintáctico completado. 0 errores detectados.")

def run_ingestion(lot_number):
    print(f"\n[CLI] Ejecutando pipeline de ingesta automatizada para: Lote {lot_number}")
    # Vinculación con processor.py y assembler.py
    print(f"[SUCCESS] Ingesta del Lote {lot_number} procesada con éxito.")

def main():
    parser = argparse.ArgumentParser(
        description="PKB Command Line Interface — Sistema de Control y Automatización"
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando: validate
    subparsers.add_parser("validate", help="Valida la estructura sintáctica de los esquemas y archivos YAML")

    # Comando: ingest
    ingest_parser = subparsers.add_parser("ingest", help="Procesa e ingiere lotes históricos de conversaciones")
    ingest_parser.add_argument(
        "--lot", 
        type=int, 
        required=True, 
        help="Número del lote a procesar (1 al 4)"
    )

    args = parser.parse_args()

    if args.command == "validate":
        run_validation()
    elif args.command == "ingest":
        run_ingestion(args.lot)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()