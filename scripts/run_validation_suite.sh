#!/usr/bin/env bash
set -euo pipefail

mkdir -p docs/evidence

pytest tests/test_prompts_contract.py -v \
  | tee docs/evidence/test_prompts_contract.log

pytest tests/test_observability_contract.py -v \
  | tee docs/evidence/test_observability_contract.log

pytest -v \
  --durations=10 \
  --durations-min=0.1 \
  --junitxml=docs/evidence/test-results.xml \
  | tee docs/evidence/test_full_suite.log

pytest -v --durations=0 \
  | tee docs/evidence/test_performance_all.log