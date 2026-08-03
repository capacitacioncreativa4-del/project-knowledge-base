from pkb.config import PKB_ROOT
from pkb.query import QueryEngine
from pkb.repository.loader import KnowledgeLoader


def run(args) -> None:
    """Ejecuta consultas sobre el Knowledge Registry."""

    registry = KnowledgeLoader.load_repository(str(PKB_ROOT))
    engine = QueryEngine(registry)

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

    for obj in objetos:
        print(f"{obj.identifier:30}{obj.object_type:18}{obj.domain:18}{obj.status}")
