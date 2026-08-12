from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

EXCLUDED_PARTS = {
    ".venv",
    "venv",
    ".git",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
    ".mypy_cache",
    "site-packages",
    ".ruff_cache",
}

EXPECTED_FILES = [
    ROOT / "src" / "config" / "agent_profile.yaml",
    ROOT / "src" / "config" / "data_source_strategy.yaml",
    ROOT / "src" / "config" / "retrieval_policy.yaml",
    ROOT / "src" / "config" / "citation_policy.yaml",
    ROOT / "src" / "config" / "guardrail_policy.yaml",
    ROOT / "src" / "config" / "fallback_policy.yaml",
    ROOT / "src" / "config" / "observability_policy.yaml",
    ROOT / "src" / "prompts" / "prompt_versions.yaml",
    ROOT / "tests" / "test_prompts_contract.py",
    ROOT / "tests" / "test_competitive_intelligence_retriever.py",
    ROOT / "tests" / "test_observability_contract.py",
]

CONFIG_REQUIRED_KEYS = {
    "agent_profile.yaml": [
        "solution_name",
        "primary_capability",
        "capabilities",
    ],
    "data_source_strategy.yaml": [
        "runtime_profiles",
    ],
    "retrieval_policy.yaml": [
        "retrieval",
    ],
    "citation_policy.yaml": [
        "citation",
    ],
    "guardrail_policy.yaml": [
        "guardrails",
    ],
    "fallback_policy.yaml": [
        "fallback",
    ],
    "observability_policy.yaml": [
        "observability",
    ],
}

FORBIDDEN_PATTERNS = {
    "ACME_BANKING (use ACME_Banking)": re.compile(r"\bACME_BANKING\b"),
    "get_context() (contrato inexistente)": re.compile(r"\bget_context\s*\("),
    "transactions.csv (fora do schema)": re.compile(r"transactions\.csv"),
    "market_signals.csv (fora do schema)": re.compile(r"market_signals\.csv"),
}

BASE_INSTITUTION = "ACME_Banking"
INSTITUTION_FILES = [
    ROOT / "tests" / "test_competitive_intelligence_retriever.py",
    ROOT / "agents" / "competitive_intelligence_agent.py",
    ROOT / "pages" / "2_Competitive_Intelligence.py",
]

issues: list[str] = []


def ok(msg: str) -> None:
    print(f"[OK]   {msg}")


def err(msg: str) -> None:
    issues.append(msg)
    print(f"[ERR]  {msg}")


def in_scope(path: Path) -> bool:
    if path.resolve() == SELF:
        return False
    return not any(part in EXCLUDED_PARTS for part in path.parts)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def scoped_files(*suffixes: str) -> list[Path]:
    out: list[Path] = []
    for suffix in suffixes:
        out.extend(
            p for p in ROOT.rglob(f"*{suffix}")
            if p.is_file() and in_scope(p)
        )
    return sorted(set(out))


def validate_expected_files() -> None:
    print("\n== 1. Arquivos esperados ==")
    for path in EXPECTED_FILES:
        if path.exists():
            ok(f"exists: {rel(path)}")
        else:
            err(f"missing: {rel(path)}")


def validate_yaml_files() -> None:
    print("\n== 2. YAML parse ==")
    for path in scoped_files(".yml", ".yaml"):
        try:
            with path.open("r", encoding="utf-8") as f:
                yaml.safe_load(f)
            ok(f"yaml valid: {rel(path)}")
        except Exception as e:
            err(f"yaml invalid: {rel(path)} -> {e}")


def validate_config_keys() -> None:
    print("\n== 3. Chaves obrigatorias das policies ==")
    config_dir = ROOT / "src" / "config"
    if not config_dir.exists():
        err(f"missing directory: {rel(config_dir)}")
        return

    for name, keys in CONFIG_REQUIRED_KEYS.items():
        path = config_dir / name
        if not path.exists():
            continue

        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as e:
            err(f"parse error: {rel(path)} -> {e}")
            continue

        if not isinstance(data, dict):
            err(f"top-level nao e mapping: {rel(path)}")
            continue

        for key in keys:
            if key in data:
                ok(f"key '{key}' present in {rel(path)}")
            else:
                err(f"key '{key}' missing in {rel(path)}")


def validate_prompt_versions() -> None:
    print("\n== 4. prompt_versions.yaml ==")
    path = ROOT / "src" / "prompts" / "prompt_versions.yaml"
    if not path.exists():
        err(f"missing: {rel(path)}")
        return

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"parse error: {rel(path)} -> {e}")
        return

    prompts = (data or {}).get("prompts")
    if not isinstance(prompts, dict):
        err(f"'prompts' ausente ou invalido em {rel(path)}")
        return

    required_prompt_entries = [
        "meeting_prep_system",
        "supervisor_router",
        "meeting_prep_user",
    ]

    for name in required_prompt_entries:
        if name not in prompts:
            err(f"entry '{name}' ausente em {rel(path)}")
            continue

        entry = prompts[name]
        if not isinstance(entry, dict):
            err(f"entry '{name}' nao e mapping em {rel(path)}")
            continue

        if "current" in entry:
            ok(f"entry '{name}' possui 'current'")
        elif "current_version" in entry:
            ok(
                f"entry '{name}' possui 'current_version' "
                f"(aceito, mas prefira manter tambem 'current')"
            )
        else:
            err(f"entry '{name}' sem 'current' ou 'current_version'")

        versions = entry.get("versions")
        if isinstance(versions, dict) and versions:
            ok(f"entry '{name}' possui versions")
        else:
            err(f"entry '{name}' sem versions validas")


def scan_forbidden_patterns() -> None:
    print("\n== 5. Tokens proibidos (codigo do projeto) ==")
    found = False
    for path in scoped_files(".py", ".md", ".yml", ".yaml"):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(content):
                err(f"token proibido [{label}] em {rel(path)}")
                found = True

    if not found:
        ok("nenhum token proibido encontrado no codigo do projeto")


def validate_base_institution() -> None:
    print("\n== 6. Nome base da instituicao ==")
    for path in INSTITUTION_FILES:
        if not path.exists():
            continue

        content = path.read_text(encoding="utf-8", errors="ignore")
        if BASE_INSTITUTION in content:
            ok(f"'{BASE_INSTITUTION}' presente em {rel(path)}")
        else:
            err(f"'{BASE_INSTITUTION}' ausente em {rel(path)}")


def main() -> int:
    print(f"Project root: {ROOT}")
    validate_expected_files()
    validate_yaml_files()
    validate_config_keys()
    validate_prompt_versions()
    scan_forbidden_patterns()
    validate_base_institution()

    print("\n" + "=" * 66)
    if not issues:
        print("BLUEPRINT VALIDATION: PASS")
        return 0

    print(f"BLUEPRINT VALIDATION: FAIL -> {len(issues)} issue(s)")
    for i, item in enumerate(issues, 1):
        print(f"  {i:02d}. {item}")
    return 1


if __name__ == "__main__":
    sys.exit(main())