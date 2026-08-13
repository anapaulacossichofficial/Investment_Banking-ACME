from src.orchestration.scope_resolver import ScopeResolver


def test_scope_resolver_locks_known_account_scope():
    resolver = ScopeResolver()

    result = resolver.resolve_scope("Quantum", "Jane Doe")

    assert result["scope_status"] == "locked"
    assert result["account_id"] == "ACC-QUANTUM-001"
    assert result["account_name"] == "Quantum"
    assert result["contact_name"] == "Jane Doe"
    assert result["scope_level"] == "account_contact"
    assert result["cross_account_leakage_prevented"] is True


def test_scope_resolver_returns_not_found_for_unknown_account():
    resolver = ScopeResolver()

    result = resolver.resolve_scope("Unknown Bank")

    assert result["scope_status"] == "not_found"
    assert result["account_id"] is None
    assert result["scope_level"] == "unresolved"
    assert result["cross_account_leakage_prevented"] is True


def test_scope_resolver_blocks_cross_account_boundary():
    resolver = ScopeResolver()

    assert resolver.validate_boundary("ACC-QUANTUM-001", "ACC-QUANTUM-001") is True
    assert resolver.validate_boundary("ACC-ORION-001", "ACC-QUANTUM-001") is False
    assert resolver.validate_boundary("ACC-ORION-001", "") is False
