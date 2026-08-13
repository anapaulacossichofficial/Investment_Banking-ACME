#!/usr/bin/env bash
set -euo pipefail

echo "1) Validating configuration..."
./scripts/validate_front3_configs.sh

echo "2) Running prompt contract tests..."
pytest -v tests/test_prompts_contract.py

echo "3) Running observability contract tests..."
pytest -v tests/test_observability_contract.py

echo "4) Running full regression suite..."
pytest -v --junitxml=docs/evidence/test-results.xml

echo "Front 3 validation completed successfully."
