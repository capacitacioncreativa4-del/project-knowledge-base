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
    print(f"Relaciones válidas:        {diagnostics.valid_relationships}")
    print(
        f"Relaciones no resueltas:   "
        f"{diagnostics.unresolved_relationship_count}"
    )
    print(
        f"Relaciones duplicadas:     "
        f"{diagnostics.duplicate_relationship_count}"
    )

    if diagnostics.unresolved_relationships:
        print("\nRelaciones no resueltas:")
        for source_id, relation_type, target_id in (
            diagnostics.unresolved_relationships
        ):
            print(f"  - {source_id} - {relation_type} -> {target_id}")

    if diagnostics.duplicate_relationships:
        print("\nRelaciones duplicadas:")
        for source_id, relation_type, target_id in (
            diagnostics.duplicate_relationships
        ):
            print(f"  - {source_id} - {relation_type} -> {target_id}")
