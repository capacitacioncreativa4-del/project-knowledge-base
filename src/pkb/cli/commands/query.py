from pkb.config import PKB_ROOT
from pkb.query import QueryEngine
from pkb.repository.loader import KnowledgeLoader
from pkb.reporting import QueryExporter


def run(args) -> None:
    """Ejecuta consultas sobre el Knowledge Registry."""

    registry = KnowledgeLoader.load_repository(str(PKB_ROOT))
    engine = QueryEngine(registry)

    if args.format == "table":
    print(f"\nObjetos cargados: {registry.count()}")

    if args.domain:
        objetos = engine.by_domain(args.domain)

    elif args.object_type:
        objetos = engine.by_type(args.object_type)

    elif args.status:
        objetos = engine.by_status(args.status)

    elif args.owner:
        objetos = engine.by_owner(args.owner)

    else:
        objetos = engine.all()

    if args.format == "table":
        QueryExporter.table(objetos)

    elif args.format == "json":
        QueryExporter.json(objetos)

    elif args.format == "yaml":
        QueryExporter.yaml(objetos)
