import argparse
import sys
from pathlib import Path

# Asegurar que el path reconozca la estructura de paquetes internos
sys.path.append(str(Path(__file__).resolve().parents[2]))

from pkb.cli.commands.diagnostics import run as run_diagnostics
from pkb.cli.commands.ingest import run as run_ingestion
from pkb.cli.commands.query import run as run_query
from pkb.cli.commands.validate import run as run_validation
from pkb.cli.commands.version import run as run_version


def main():
    parser = argparse.ArgumentParser(
        description="PKB Command Line Interface — Sistema de Control y Automatización"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Comandos disponibles",
    )

    subparsers.add_parser(
        "validate",
        help="Valida la estructura sintáctica de los esquemas y archivos YAML",
    )

    subparsers.add_parser(
        "version",
        help="Muestra la versión instalada del PKB",
    )

    subparsers.add_parser(
        "diagnostics",
        help="Muestra diagnósticos de carga del Knowledge Registry",
    )

    query_parser = subparsers.add_parser(
        "query",
        help="Consulta el Knowledge Registry",
    )

    query_parser.add_argument(
        "--domain",
        help="Filtra por dominio",
    )

    query_parser.add_argument(
        "--type",
        dest="object_type",
        help="Filtra por tipo",
    )

    query_parser.add_argument(
        "--status",
        help="Filtra por estado",
    )

    query_parser.add_argument(
        "--owner",
        help="Filtra por propietario",
    )

    query_parser.add_argument(
        "--related",
        help="Consulta los objetos relacionados directamente con un identificador",
    )

    query_parser.add_argument(
        "--referenced-by",
        dest="referenced_by",
        help="Consulta los objetos que referencian directamente a un identificador",
    )

    query_parser.add_argument(
        "--format",
        choices=["table", "json", "yaml"],
        default="table",
        help="Formato de salida",
    )

    ingest_parser = subparsers.add_parser(
        "ingest",
        help="Procesa e ingiere lotes históricos de conversaciones",
    )

    ingest_parser.add_argument(
        "--lot",
        type=int,
        required=True,
        help="Número del lote a procesar (1 al 4)",
    )

    args = parser.parse_args()

    if args.command == "validate":
        run_validation()

    elif args.command == "version":
        run_version()

    elif args.command == "diagnostics":
        run_diagnostics()

    elif args.command == "ingest":
        run_ingestion(args.lot)

    elif args.command == "query":
        run_query(args)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
