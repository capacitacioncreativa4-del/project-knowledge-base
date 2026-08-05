from pkb.config import PKB_ROOT
from pkb.repository.loader import KnowledgeLoader


def run() -> None:
    """Muestra los diagnósticos de carga del Knowledge Registry."""

    _, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(str(PKB_ROOT))

    print("\nDiagnósticos del Knowledge Registry")
    print("-----------------------------------")
    print(f"Archivos escaneados:       {diagnostics.scanned_files}")
    print(f"Archivos procesados:       {diagnostics.parsed_files}")
    print(f"Objetos registrados:       {diagnostics.registered_objects}")
    print(f"Objetos sin identificador: {diagnostics.objects_without_identifier}")
    print(f"Archivos rechazados:       {diagnostics.rejected_files}")
    print(f"Objetos con relaciones:    {diagnostics.objects_with_relationships}")
    print(f"Relaciones declaradas:     {diagnostics.declared_relationships}")
    print(f"Relaciones no resueltas:   {diagnostics.unresolved_relationship_count}")
