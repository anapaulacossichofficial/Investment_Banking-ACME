import importlib.util
from pathlib import Path


def test_page_competitive_intelligence_imports_without_app_templates():
    page_path = Path("pages/2_Competitive_Intelligence.py")
    assert page_path.exists()
    text = page_path.read_text(encoding="utf-8")
    assert "app.templates" not in text
    assert "CompetitiveIntelligenceRetriever" in text

    spec = importlib.util.spec_from_file_location("competitive_page", page_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module is not None