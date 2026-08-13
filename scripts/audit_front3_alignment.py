#!/usr/bin/env python3
"""
Audita a aderência estrutural da Frente 3 ao blueprint local.

Uso:
    python3 scripts/audit_front3_alignment.py
    python3 scripts/audit_front3_alignment.py --strict
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_YAML_FILES = {
    "src/config/observability_policy.yaml": [
        "observability.tracing",
        "observability.metrics",
        "observability.logging",
        "observability.alerts",
        "observability.evidence",
        "observability.alignment",
    ],
    "src/config/agent_profile.yaml": [
        "solution_name",
        "primary_capability",
        "supervisor.enabled",
        "supervisor.role",
        "capabilities.meeting_prep",
        "capabilities.competitive_intelligence",
        "architectural_alignment.salesforce_target_runtime",
        "architectural_alignment.trust_layer_position",
        "architectural_alignment.interoperability_support",
    ],
    "src/contracts/meeting_prep_contract.yaml": [
        "capability",
        "input_contract.required",
        "sources",
        "output_contract.required_sections",
        "output_contract.rules",
        "fallback_behavior",
    ],
    "src/contracts/competitive_intelligence_contract.yaml": [
        "capability",
        "input_contract.required",
        "sources",
        "output_contract.required_sections",
        "output_contract.rules",
        "fallback_behavior",
    ],
    "src/prompts/prompt_versions.yaml": [
        "prompts.meeting_prep_system",
        "prompts.supervisor_router",
    ],
}

REQUIRED_TEXT_FILES = {
    "src/prompts/supervisor_routing.md": [
        "Supervisor Router",
        "intent classification",
        "scope validation",
        "capability routing",
        "meeting_prep_agent",
        "competitive_intelligence_agent",
        "Agentforce",
    ],
    "docs/front-3-validation-matrix.md": [
        "Front 3 Validation Matrix",
        "Observability",
        "Supervisor Behavior",
        "Target Runtime Alignment",
    ],
}

EXPECTED_COMPETITIVE_FIXTURES = {
    "institutions.csv",
    "peers.csv",
    "metrics.csv",
    "insights.csv",
}

FORBIDDEN_COMPETITIVE_METHODS = {
    "get_context",
}

EXPECTED_COMPETITIVE_METHODS = {
    "get_institution_options",
    "get_peer_options",
    "get_metrics",
    "get_insight",
    "get_sources",
}


@dataclass
class Finding:
    status: str
    area: str
    message: str


findings: list[Finding] = []


def add(status: str, area: str, message: str) -> None:
    findings.append(Finding(status, area, message))


def get_nested_value(payload: dict[str, Any], dotted_key: str) -> Any:
    current: Any = payload
    for key in dotted_key.split("."):
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def load_yaml(path: Path) -> dict[str, Any] | None:
    try:
        import yaml
    except ModuleNotFoundError:
        add(
            "FAIL",
            "dependencies",
            "PyYAML não está instalado. Execute: python3 -m pip install pyyaml",
        )
        return None

    try:
        with path.open(encoding="utf-8") as file:
            payload = yaml.safe_load(file)
    except Exception as error:
        add("FAIL", str(path.relative_to(ROOT)), f"YAML inválido: {error}")
        return None

    if not isinstance(payload, dict):
        add(
            "FAIL",
            str(path.relative_to(ROOT)),
            "O YAML deve conter um objeto/mapeamento na raiz.",
        )
        return None

    return payload


def validate_yaml_files() -> None:
    for relative_path, required_keys in REQUIRED_YAML_FILES.items():
        path = ROOT / relative_path

        if not path.exists():
            add("FAIL", relative_path, "Arquivo obrigatório ausente.")
            continue

        payload = load_yaml(path)
        if payload is None:
            continue

        missing = [
            key
            for key in required_keys
            if get_nested_value(payload, key) is None
        ]

        if missing:
            add(
                "FAIL",
                relative_path,
                f"Campos obrigatórios ausentes: {', '.join(missing)}",
            )
        else:
            add("PASS", relative_path, "YAML válido e campos mínimos presentes.")


def validate_text_files() -> None:
    for relative_path, expected_terms in REQUIRED_TEXT_FILES.items():
        path = ROOT / relative_path

        if not path.exists():
            add("FAIL", relative_path, "Arquivo obrigatório ausente.")
            continue

        content = path.read_text(encoding="utf-8").lower()
        missing_terms = [
            term for term in expected_terms if term.lower() not in content
        ]

        if missing_terms:
            add(
                "WARN",
                relative_path,
                "Termos recomendados não encontrados: "
                + ", ".join(missing_terms),
            )
        else:
            add(
                "PASS",
                relative_path,
                "Arquivo presente com conteúdo mínimo esperado.",
            )


def validate_competitive_contract() -> None:
    relative_path = "src/contracts/competitive_intelligence_contract.yaml"
    path = ROOT / relative_path

    if not path.exists():
        return

    payload = load_yaml(path)
    if payload is None:
        return

    declared_sources = payload.get("sources", {}).get("fixtures", [])
    declared_sources = set(declared_sources) if isinstance(declared_sources, list) else set()

    missing_fixtures = EXPECTED_COMPETITIVE_FIXTURES - declared_sources
    if missing_fixtures:
        add(
            "WARN",
            relative_path,
            "Fixtures esperadas ausentes do contrato: "
            + ", ".join(sorted(missing_fixtures)),
        )
    else:
        add(
            "PASS",
            relative_path,
            "Contrato competitivo declara os fixtures aprovados.",
        )

    methods = payload.get("runtime_methods_allowed", [])
    methods = set(methods) if isinstance(methods, list) else set()

    missing_methods = EXPECTED_COMPETITIVE_METHODS - methods
    if missing_methods:
        add(
            "WARN",
            relative_path,
            "Métodos de runtime esperados não declarados: "
            + ", ".join(sorted(missing_methods)),
        )
    else:
        add(
            "PASS",
            relative_path,
            "Métodos de runtime competitivo esperados estão declarados.",
        )

    forbidden_methods = methods & FORBIDDEN_COMPETITIVE_METHODS
    if forbidden_methods:
        add(
            "FAIL",
            relative_path,
            "Método proibido declarado no contrato: "
            + ", ".join(sorted(forbidden_methods)),
        )
    else:
        add(
            "PASS",
            relative_path,
            "Nenhum método competitivo proibido foi declarado.",
        )


def validate_test_suite() -> None:
    expected_tests = [
        "tests/test_prompts_contract.py",
        "tests/test_observability_contract.py",
    ]

    for relative_path in expected_tests:
        path = ROOT / relative_path
        if path.exists():
            add("PASS", relative_path, "Teste de evidência encontrado.")
        else:
            add(
                "WARN",
                relative_path,
                "Teste esperado não encontrado; ajuste o runner ou crie o teste.",
            )


def validate_python_dependencies() -> None:
    if importlib.util.find_spec("yaml") is None:
        add(
            "FAIL",
            "dependencies",
            "Dependência ausente: PyYAML. Execute: python3 -m pip install pyyaml",
        )
    else:
        add("PASS", "dependencies", "PyYAML disponível.")


def print_report() -> int:
    status_order = {"FAIL": 0, "WARN": 1, "PASS": 2}
    ordered_findings = sorted(
        findings,
        key=lambda item: (status_order[item.status], item.area, item.message),
    )

    print("\nFront 3 Alignment Audit")
    print("=" * 72)

    for finding in ordered_findings:
        print(f"[{finding.status}] {finding.area}: {finding.message}")

    totals = {
        status: sum(1 for item in findings if item.status == status)
        for status in ("PASS", "WARN", "FAIL")
    }

    print("-" * 72)
    print(
        f"Resultado: {totals['PASS']} PASS | "
        f"{totals['WARN']} WARN | {totals['FAIL']} FAIL"
    )

    if totals["FAIL"]:
        print("Status final: FAIL — corrija os itens críticos antes da regressão.")
        return 1

    if totals["WARN"]:
        print("Status final: WARN — estrutura válida, mas há ajustes recomendados.")
        return 0

    print("Status final: PASS — estrutura alinhada ao baseline da Frente 3.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audita a aderência estrutural da Frente 3."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Trata WARN como falha de validação.",
    )
    args = parser.parse_args()

    print("Auditando aderência da Frente 3 ao blueprint local...")
    print(f"Raiz do projeto: {ROOT}")

    validate_python_dependencies()
    validate_yaml_files()
    validate_text_files()
    validate_competitive_contract()
    validate_test_suite()

    exit_code = print_report()

    if args.strict and any(item.status == "WARN" for item in findings):
        print("Modo strict: WARN tratado como falha.")
        return 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main())