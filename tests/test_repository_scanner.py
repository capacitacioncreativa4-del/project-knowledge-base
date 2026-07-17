import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SRC_PATH = str(RAIZ / "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import pytest
from pkb.repository.scanner import RepositoryScanner
from pkb.core.exceptions import RepositoryError

def test_scanner_returns_list():
    """Verifica que el escáner devuelva una lista al pasar la raíz."""
    base_dir = Path(__file__).resolve().parents[1]
    resultado = RepositoryScanner.markdown_files(str(base_dir))
    assert isinstance(resultado, list)

def test_scanner_invalid_path():
    """Verifica que lanzar una ruta inexistente levante la excepción institucional."""
    with pytest.raises(RepositoryError):
        RepositoryScanner.markdown_files("C:/Ruta/Que/No/Existe/Jamas")