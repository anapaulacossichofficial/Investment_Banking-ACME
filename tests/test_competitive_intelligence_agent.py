from importlib import import_module


def test_competitive_intelligence_agent_module_imports():
    module = import_module("agents.competitive_intelligence_agent")
    assert module is not None


def test_competitive_intelligence_agent_exposes_something_usable():
    module = import_module("agents.competitive_intelligence_agent")
    public = [name for name in dir(module) if not name.startswith("_")]
    assert public

    candidates = [
        getattr(module, name)
        for name in public
        if callable(getattr(module, name, None)) or isinstance(getattr(module, name, None), type)
    ]
    assert candidates