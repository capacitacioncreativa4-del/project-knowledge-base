class PKBException(Exception):
    """Excepción base para todos los errores de la plataforma PKB."""
    pass

class RepositoryError(PKBException):
    """Se levanta cuando ocurre un error al escanear o leer el repositorio."""
    pass

class MetadataError(PKBException):
    """Se levanta cuando el parseo o la estructura del Front Matter falla."""
    pass