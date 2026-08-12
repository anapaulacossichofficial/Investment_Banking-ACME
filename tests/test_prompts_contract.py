"""
Prompt Contract Unit Tests (ib-agent-demo)

Validates:
- canonical prompt directory presence in src/prompts;
- required prompt templates for the current blueprint;
- minimum zero-trust and routing guardrail language;
- archived legacy prompt location.
"""

from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT_DIR / "src" / "prompts"
LEGACY_DIR = ROOT_DIR / "docs" / "templates" / "legacy-prompts"

MEETING_PREP_SYSTEM_FILE = PROMPTS_DIR / "meeting_prep_system.md"
MEETING_PREP_USER_FILE = PROMPTS_DIR / "meeting_prep_user.md"
SUPERVISOR_ROUTER_FILE = PROMPTS_DIR / "supervisor_router.md"


def test_prompt_directory_and_files_exist():
    """Validate that the canonical prompt directory and required files exist."""
    assert PROMPTS_DIR.exists(), "The 'src/prompts/' directory must exist."
    assert MEETING_PREP_SYSTEM_FILE.exists(), "meeting_prep_system.md is missing."
    assert MEETING_PREP_USER_FILE.exists(), "meeting_prep_user.md is missing."
    assert SUPERVISOR_ROUTER_FILE.exists(), "supervisor_router.md is missing."


def test_legacy_prompt_archive_directory_exists():
    """Validate that legacy prompt files were archived in the documentation area."""
    assert LEGACY_DIR.exists(), "The legacy prompt archive directory must exist."


def test_meeting_prep_system_zero_trust_contract():
    """Validate that the system prompt contains grounded-behavior constraints."""
    content = MEETING_PREP_SYSTEM_FILE.read_text(encoding="utf-8")

    expected_markers = [
        "zero-trust",
        "citation",
        "scope",
        "ground",
    ]

    lowered = content.lower()
    for marker in expected_markers:
        assert marker in lowered, (
            f"meeting_prep_system.md must contain guidance related to '{marker}'."
        )


def test_meeting_prep_user_scoped_request_contract():
    """Validate that the user prompt describes a scoped meeting-prep request."""
    content = MEETING_PREP_USER_FILE.read_text(encoding="utf-8")
    lowered = content.lower()

    assert "account" in lowered, "meeting_prep_user.md must reference account scope."
    assert (
        "contact" in lowered or "contact scope" in lowered
    ), "meeting_prep_user.md should support optional contact scope."
    assert (
        "briefing" in lowered or "meeting prep" in lowered
    ), "meeting_prep_user.md must describe the expected output."


def test_supervisor_router_prompt_contract():
    """Validate that the supervisor router prompt contains routing behavior."""
    content = SUPERVISOR_ROUTER_FILE.read_text(encoding="utf-8")
    lowered = content.lower()

    expected_markers = [
        "intent",
        "route",
        "scope",
        "meeting_prep",
    ]

    for marker in expected_markers:
        assert marker in lowered, (
            f"supervisor_router.md must contain routing guidance related to '{marker}'."
        )