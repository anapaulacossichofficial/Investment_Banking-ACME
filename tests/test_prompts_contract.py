"""
Prompt Contract Unit Tests (ib-agent-demo)

Validates the structural presence and safety guardrails
of the active prompt templates.
"""

from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT_DIR / "src" / "prompts"

MEETING_PREP_SYSTEM_FILE = PROMPTS_DIR / "meeting_prep_system.md"
MEETING_PREP_USER_FILE = PROMPTS_DIR / "meeting_prep_user.md"
SUPERVISOR_ROUTER_FILE = PROMPTS_DIR / "supervisor_router.md"
PROMPT_VERSIONS_FILE = PROMPTS_DIR / "prompt_versions.yaml"


def test_active_prompt_directory_and_files_exist():
    """Validates the active prompt directory and required templates."""
    assert PROMPTS_DIR.exists(), (
        "The active 'src/prompts/' directory must exist in the repository."
    )
    assert MEETING_PREP_SYSTEM_FILE.exists(), (
        "meeting_prep_system.md is missing from src/prompts/."
    )
    assert MEETING_PREP_USER_FILE.exists(), (
        "meeting_prep_user.md is missing from src/prompts/."
    )
    assert SUPERVISOR_ROUTER_FILE.exists(), (
        "supervisor_router.md is missing from src/prompts/."
    )
    assert PROMPT_VERSIONS_FILE.exists(), (
        "prompt_versions.yaml is missing from src/prompts/."
    )


def test_meeting_prep_system_prompt_zero_trust_contract():
    """Validates Zero-Trust, grounding, safety, and citation directives."""
    content = MEETING_PREP_SYSTEM_FILE.read_text(encoding="utf-8")

    required_concepts = (
        "ZERO-TRUST",
        "CRM",
        "citation",
        "evidence",
    )

    missing = [
        concept
        for concept in required_concepts
        if concept.lower() not in content.lower()
    ]

    assert not missing, (
        "meeting_prep_system.md is missing required prompt-contract concepts: "
        f"{', '.join(missing)}"
    )


def test_meeting_prep_user_prompt_exists_and_is_nonempty():
    """Validates that the user-facing meeting-prep prompt is usable."""
    content = MEETING_PREP_USER_FILE.read_text(encoding="utf-8").strip()

    assert content, "meeting_prep_user.md must not be empty."


def test_supervisor_router_prompt_contract():
    """Validates that the supervisor routing prompt remains available."""
    content = SUPERVISOR_ROUTER_FILE.read_text(encoding="utf-8").strip()

    assert content, "supervisor_router.md must not be empty."


def test_prompt_version_registry_exists_and_is_nonempty():
    """Validates that active prompt versions remain tracked."""
    content = PROMPT_VERSIONS_FILE.read_text(encoding="utf-8").strip()

    assert content, "prompt_versions.yaml must not be empty."