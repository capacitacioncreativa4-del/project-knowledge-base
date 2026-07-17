from pathlib import Path
from typing import List
from pkb.core.exceptions import RepositoryError

class RepositoryScanner:
    @staticmethod
    def markdown_files(root_path: str) -> List[Path]:
        """
        Escanea recursivamente el directorio raíz buscando archivos Markdown (.md).
        Ignora directorios ocultos (como .git) y entornos virtuales.
        """
        try:
            root = Path(root_path).resolve()
            if not root.exists() or not root.is_dir():
                raise RepositoryError(f"La ruta del repositorio no es válida o no existe: {root_path}")
            
            archivos = []
            # Recorremos de forma iterativa y filtramos carpetas conflictivas
            for path in root.rglob("*.md"):
                # Evitar leer archivos dentro de .git, venv o directorios ocultos
                if any(part.startswith(".") or part in ("venv", "env", "build") for part in path.parts):
                    continue
                archivos.append(path)
                
            return archivos
        except Exception as e:
            if not isinstance(e, RepositoryError):
                raise RepositoryError(f"Fallo inesperado durante el escaneo del repositorio: {str(e)}")
            raise e