from pkb.config import PKB_ROOT
from pkb.query import QueryEngine
from pkb.repository.loader import KnowledgeLoader
from pkb.reporting import QueryExporter


def run(args) -> None:
    """Ejecuta consultas sobre el Knowledge Registry."""

    registry = KnowledgeLoader.load_repository(str(PKB_ROOT))
    engine = QueryEngine(registry)

    if args.related:
        objetos = engine.related(args.related)

    elif args.referenced_by:
        objetos = engine.referenced_by(args.referenced_by)

    elif any(
        [
            args.domain,
            args.object_type,
            args.status,
            args.owner,
        ]
    ):
        objetos = engine.filter(
            domain=args.domain,
            object_type=args.object_type,
            status=args.status,
            owner=args.owner,
        )

    else:
        objetos = engine.all()

    if args.format == "table":
        print(f"\nObjetos en Registry: {registry.count()}")
        print(f"Resultados: {len(objetos)}")
        QueryExporter.table(objetos)

    elif args.format == "json":
        QueryExporter.json(objetos)

    elif args.format == "yaml":
        QueryExporter.yaml(objetos)
