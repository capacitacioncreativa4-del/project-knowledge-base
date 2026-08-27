"""
Configuración central del Project Knowledge Base.
"""

from pathlib import Path

# ---------------------------------------------------------------------
# Directorio raíz del repositorio
# ---------------------------------------------------------------------

PKB_ROOT = Path(__file__).resolve().parents[2]

# ---------------------------------------------------------------------
# Directorios principales
# ---------------------------------------------------------------------

PROJECTS_DIR = PKB_ROOT / "projects"

MIPSP_DIR = PROJECTS_DIR / "mipsp"

REPOSITORY_DIR = MIPSP_DIR / "repository"

INGESTION_DIR = MIPSP_DIR / "ingestion" / "sources"

PACKAGES_DIR = REPOSITORY_DIR / "packages"

SCHEMAS_DIR = PKB_ROOT / "src" / "pkb" / "schemas"

TEMPLATES_DIR = PKB_ROOT / "src" / "pkb" / "templates"

DOCS_DIR = PKB_ROOT / "docs"

# ---------------------------------------------------------------------
# Configuración global
# ---------------------------------------------------------------------

DEFAULT_ENCODING = "utf-8"

SUPPORTED_MARKDOWN_EXTENSIONS = (".md",)

VERSION = "0.1.0"
