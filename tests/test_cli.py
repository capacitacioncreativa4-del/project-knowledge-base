from pkb.version import VERSION

def test_version():
    """Verifica que la versión de la plataforma esté correctamente definida."""
    assert VERSION == "0.1.0"