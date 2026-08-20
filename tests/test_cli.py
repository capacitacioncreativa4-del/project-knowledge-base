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


def test_cli_diagnostics_reports_relationship_metrics(monkeypatch, capsys):
    """Verifica que diagnostics exponga todas las métricas relacionales."""

    class FakeDiagnostics:
        scanned_files = 10
        parsed_files = 9
        registered_objects = 8
        objects_without_identifier = 1
        rejected_files = 1
        objects_with_relationships = 3
        declared_relationships = 5
        valid_relationships = 3

        unresolved_relationships = [
            ("REQ-001", "derived_from", "ADR-999"),
        ]

        duplicate_relationships = [
            ("REQ-002", "related", "ADR-001"),
        ]

        @property
        def unresolved_relationship_count(self):
            return len(self.unresolved_relationships)

        @property
        def duplicate_relationship_count(self):
            return len(self.duplicate_relationships)

    class FakeLoader:
        @staticmethod
        def load_repository_with_diagnostics(_):
            return object(), FakeDiagnostics()

    monkeypatch.setattr(
        "pkb.cli.commands.diagnostics.KnowledgeLoader",
        FakeLoader,
    )

    original_argv = sys.argv

    try:
        sys.argv = ["pkb", "diagnostics"]
        main()
    finally:
        sys.argv = original_argv

    output = capsys.readouterr().out

    expected_metrics = {
        "Archivos escaneados:": "10",
        "Archivos procesados:": "9",
        "Objetos registrados:": "8",
        "Objetos sin identificador:": "1",
        "Archivos rechazados:": "1",
        "Objetos con relaciones:": "3",
        "Relaciones declaradas:": "5",
        "Relaciones válidas:": "3",
        "Relaciones no resueltas:": "1",
        "Relaciones duplicadas:": "1",
    }

    for label, value in expected_metrics.items():
        assert f"{label}" in output
        assert value in output

    assert "REQ-001 - derived_from -> ADR-999" in output
    assert "REQ-002 - related -> ADR-001" in output
