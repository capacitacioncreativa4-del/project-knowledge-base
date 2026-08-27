"""Comando para mostrar la versión instalada del PKB."""

from pkb import __version__


def run() -> None:
    print(f"PKB {__version__}")
