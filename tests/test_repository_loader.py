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


def test_load_repository_diagnostics_unresolved_relationships():
    registry, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(".")

    expected_unresolved = []

    for obj in registry.all():
        for relationship in obj.typed_relationships:
            if registry.get(relationship.target_id) is None:
                expected_unresolved.append(
                    (
                        obj.identifier,
                        relationship.relation_type,
                        relationship.target_id,
                    )
                )

    assert diagnostics.unresolved_relationships == expected_unresolved
    assert diagnostics.unresolved_relationship_count == len(expected_unresolved)


def test_load_repository_diagnostics_duplicate_relationships():
    registry, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(".")

    expected_duplicates = []

    for obj in registry.all():
        seen = set()

        for relationship in obj.typed_relationships:
            relation_key = (
                relationship.relation_type,
                relationship.target_id,
            )

            if relation_key in seen:
                expected_duplicates.append(
                    (
                        obj.identifier,
                        relationship.relation_type,
                        relationship.target_id,
                    )
                )
                continue

            seen.add(relation_key)

    assert diagnostics.duplicate_relationships == expected_duplicates
    assert diagnostics.duplicate_relationship_count == len(expected_duplicates)


def test_load_repository_diagnostics_valid_relationships():
    registry, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(".")

    expected_valid = 0

    for obj in registry.all():
        seen = set()

        for relationship in obj.typed_relationships:
            relation_key = (
                relationship.relation_type,
                relationship.target_id,
            )

            if relation_key in seen:
                continue

            seen.add(relation_key)

            if registry.get(relationship.target_id) is not None:
                expected_valid += 1

    assert diagnostics.valid_relationships == expected_valid


def test_load_repository_diagnostics_preserves_typed_relationship_identity():
    registry, diagnostics = KnowledgeLoader.load_repository_with_diagnostics(".")

    actual_relationships = (
        diagnostics.unresolved_relationships + diagnostics.duplicate_relationships
    )

    for diagnostic in actual_relationships:
        assert len(diagnostic) == 3
        assert diagnostic[0]
        assert diagnostic[1]
        assert diagnostic[2]


def test_load_repository_remains_backward_compatible():
    registry = KnowledgeLoader.load_repository(".")

    assert registry.count() > 0
