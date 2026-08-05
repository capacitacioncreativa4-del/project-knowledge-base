import sys

from pkb.cli.main import main
from pkb.version import VERSION


def test_version():
    """Verifica que la versión de la plataforma esté correctamente definida."""
    assert VERSION == "0.1.0"


def test_cli_diagnostics_help(capsys):
    """Verifica que el CLI reconozca el subcomando diagnostics."""
    original_argv = sys.argv

    try:
        sys.argv = ["pkb", "diagnostics", "--help"]

        try:
            main()
        except SystemExit as exc:
            assert exc.code == 0

        output = capsys.readouterr().out

        assert "usage: pkb diagnostics" in output
        assert "--help" in output

    finally:
        sys.argv = original_argv
