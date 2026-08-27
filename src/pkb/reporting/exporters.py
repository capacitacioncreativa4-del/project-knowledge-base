import json

try:
    import yaml
except ImportError:
    yaml = None


class QueryExporter:
    """Exportadores para los resultados del QueryEngine."""

    @staticmethod
    def table(objects):
        for obj in objects:
            print(f"{obj.identifier:30}{obj.object_type:18}{obj.domain:18}{obj.status}")

    @staticmethod
    def json(objects):
        datos = [
            {
                "id": obj.identifier,
                "type": obj.object_type,
                "domain": obj.domain,
                "status": obj.status,
                "title": obj.title,
                "owner": obj.owner,
            }
            for obj in objects
        ]

        print(json.dumps(datos, indent=2, ensure_ascii=False))

    @staticmethod
    def yaml(objects):
        datos = [
            {
                "id": obj.identifier,
                "type": obj.object_type,
                "domain": obj.domain,
                "status": obj.status,
                "title": obj.title,
                "owner": obj.owner,
            }
            for obj in objects
        ]

        if yaml is None:
            print("PyYAML no está instalado.")
            return

        print(
            yaml.safe_dump(
                datos,
                sort_keys=False,
                allow_unicode=True,
            )
        )
