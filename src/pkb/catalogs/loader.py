from pathlib import Path

import yaml

from pkb.config import PKB_ROOT


class CatalogLoader:
    """Carga catálogos institucionales desde archivos YAML."""

    @staticmethod
    def load_catalog(name: str) -> set[str]:
        catalog_path = (
            PKB_ROOT / "src" / "pkb" / "schemas" / "catalogs" / f"{name}.yaml"
        )

        with open(catalog_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return {item.upper().strip() for item in data.get(name, [])}
