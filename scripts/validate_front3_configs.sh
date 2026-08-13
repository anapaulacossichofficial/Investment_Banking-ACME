#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "============================================================"
echo "Front 3 — Structural Configuration Validation"
echo "============================================================"

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 was not found in PATH."
  exit 1
fi

if ! python3 -c "import yaml" >/dev/null 2>&1; then
  echo "ERROR: PyYAML is not installed."
  echo "Run: python3 -m pip install pyyaml"
  exit 1
fi

required_files=(
  "src/config/observability_policy.yaml"
  "src/config/agent_profile.yaml"
  "src/contracts/meeting_prep_contract.yaml"
  "src/contracts/competitive_intelligence_contract.yaml"
  "src/prompts/supervisor_routing.md"
  "src/prompts/prompt_versions.yaml"
  "docs/front-3-validation-matrix.md"
  "scripts/audit_front3_alignment.py"
)

echo
echo "1) Checking required files..."

missing_files=0

for file_name in "${required_files[@]}"; do
  if [[ -f "$file_name" ]]; then
    echo "PASS: $file_name"
  else
    echo "FAIL: Missing required file: $file_name"
    missing_files=1
  fi
done

if [[ "$missing_files" -ne 0 ]]; then
  echo
  echo "Validation stopped: one or more required files are missing."
  exit 1
fi

echo
echo "2) Validating YAML syntax..."

python3 - <<'PY'
from pathlib import Path
import sys
import yaml

files = [
    "src/config/observability_policy.yaml",
    "src/config/agent_profile.yaml",
    "src/contracts/meeting_prep_contract.yaml",
    "src/contracts/competitive_intelligence_contract.yaml",
    "src/prompts/prompt_versions.yaml",
]

failed = False

for file_name in files:
    path = Path(file_name)
    try:
        with path.open(encoding="utf-8") as handle:
            content = yaml.safe_load(handle)

        if not isinstance(content, dict):
            raise ValueError("The YAML root must be a mapping/object.")

        print(f"PASS: Valid YAML — {file_name}")

    except Exception as error:
        failed = True
        print(f"FAIL: Invalid YAML — {file_name}: {error}")

if failed:
    sys.exit(1)
PY

echo
echo "3) Running Front 3 alignment audit..."

python3 scripts/audit_front3_alignment.py

echo
echo "============================================================"
echo "PASS: Front 3 structural validation completed successfully."
echo "Next step: ./scripts/run_front3_validation.sh"
echo "============================================================"