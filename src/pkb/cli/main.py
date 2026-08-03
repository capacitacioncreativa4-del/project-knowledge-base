import argparse
import sys
from pathlib import Path
from pkb.cli.commands.query import run as run_query

# Asegurar que el path reconozca la estructura de paquetes internos
sys.path.append(str(Path(__file__).resolve().parents[2]))

from pkb.cli.commands.ingest import run as run_ingestion
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

    elif args.command == "ingest":
        run_ingestion(args.lot)

    elif args.command == "query":
        run_query(args)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
