from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

DOCUMENTS = [
    ROOT / "README.md",
    ROOT / "docs" / "architecture" / "README.md",
    ROOT / "docs" / "TESTING.md",
    ROOT / "docs" / "front-3-validation-matrix.md",
    ROOT / "docs" / "observability-note.md",
    ROOT / "docs" / "prompt_evolution.md",
]

PATH_PATTERN = re.compile(
    r"(?<![\w./-])"
    r"((?:docs|src|tests|scripts)/[\w./&@+=:,\- ]+"
    r"\.(?:md|txt|yaml|yml|jsonl|json|xml|log|png|pdf|py|sh))"
)

def normalize(value: str) -> str:
    return value.strip().rstrip(".,;:)]}`")

def check_document(doc: Path) -> list[tuple[str, str]]:
    if not doc.exists():
        return [(str(doc.relative_to(ROOT)), "document missing")]

    issues = []
    text = doc.read_text(encoding="utf-8", errors="replace")
    for raw in PATH_PATTERN.findall(text):
        rel = normalize(raw)
        if not (ROOT / rel).exists():
            issues.append((rel, f"referenced by {doc.relative_to(ROOT)}"))
    return issues

def main() -> int:
    missing = []
    for doc in DOCUMENTS:
        missing.extend(check_document(doc))

    if missing:
        print("DOCUMENTATION PATH VALIDATION FAILED")
        for path, source in missing:
            print(f"MISSING: {path} ({source})")
        return 1

    print("DOCUMENTATION PATH VALIDATION PASSED")
    return 0

if __name__ == "__main__":
    sys.exit(main())
