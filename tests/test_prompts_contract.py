"""
Prompt Contract Unit Tests (ib-agent-demo)
Validates the structural presence and safety guardrails of prompt templates.
"""

from pathlib import Path

# Resolve the prompts directory relative to the test file location
PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"
FALLBACK_FILE = PROMPTS_DIR / "fallback_prompt.txt"
MEETING_PREP_FILE = PROMPTS_DIR / "meeting_prep_prompt.txt"


def test_prompt_directory_and_files_exist():
    """Validates that the prompts directory and required prompt files exist."""
    assert PROMPTS_DIR.exists(), "The 'prompts/' directory must exist in the root."
    assert FALLBACK_FILE.exists(), "fallback_prompt.txt is missing from the prompts directory."
    assert MEETING_PREP_FILE.exists(), "meeting_prep_prompt.txt is missing from the prompts directory."


def test_fallback_prompt_safety_contract():
    """Validates that the fallback prompt contains strict safety directives."""
    content = FALLBACK_FILE.read_text(encoding="utf-8")

    # Assert critical safety rules are embedded
    assert "Safety Guardrail" in content, "Fallback prompt must define a safety guardrail role."
    assert "Data not available in current institutional records" in content, (
        "Fallback prompt must specify the exact mandatory safe statement."
    )

# Assert Zero-Trust constraints and output structure rules
def test_meeting_prep_prompt_zero_trust_contract():
    """Validates that the meeting prep prompt enforces Zero-Trust and citations."""
    content = MEETING_PREP_FILE.read_text(encoding="utf-8")

    assert "STRICT ZERO-TRUST CONSTRAINTS" in content, (
        "Meeting prep prompt must outline strict Zero-Trust constraints."
    )
    assert "Rely exclusively on the provided CRM" in content, (
        "Prompt must restrict the LLM to provided fixtures only."
    )
    assert "Mandatory Citations" in content, "Prompt must enforce source/citation mapping."
    assert "REQUIRED OUTPUT STRUCTURE" in content, (
        "Prompt must enforce a predictable executive output schema."
    )