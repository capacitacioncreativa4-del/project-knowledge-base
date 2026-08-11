from pkb.repository.loader import KnowledgeLoader


def test_load_repository_with_diagnostics():
    registry, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(".")

    assert registry.count() == diagnostics.registered_objects
    assert diagnostics.scanned_files >= diagnostics.parsed_files
    assert diagnostics.parsed_files >= diagnostics.registered_objects


def test_load_repository_diagnostics_relationship_counts():
    registry, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(".")

    objects_with_relationships = sum(bool(obj.relationships) for obj in registry.all())

    declared_relationships = sum(len(obj.relationships) for obj in registry.all())

    assert diagnostics.objects_with_relationships == objects_with_relationships
    assert diagnostics.declared_relationships == declared_relationships


def test_load_repository_diagnostics_typed_relationship_counts():
    registry, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(".")

    typed_relationships = sum(len(obj.typed_relationships) for obj in registry.all())

    assert diagnostics.typed_relationships == typed_relationships


def test_load_repository_diagnostics_unresolved_relationships():
    registry, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(".")

    expected_unresolved = []

    for obj in registry.all():
        for related_id in obj.relationships:
            if registry.get(related_id) is None:
                expected_unresolved.append(related_id)

    assert diagnostics.unresolved_relationships == expected_unresolved
    assert diagnostics.unresolved_relationship_count == len(expected_unresolved)


def test_load_repository_remains_backward_compatible():
    registry = KnowledgeLoader.load_repository(".")

    assert registry.count() > 0
