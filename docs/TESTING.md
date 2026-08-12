# Testing and Observability

## Purpose

This document defines the automated validation strategy for the ACME
Investment Banking Working Build.

The test strategy covers:

- Prompt governance contracts.
- Zero-Trust and fallback guardrails.
- Observability KPI calculations.
- Citation and grounding validation.
- Session latency.
- Supervisor route traceability.
- Competitive intelligence components.
- Smoke and regression behavior.
- Test execution performance.
- Machine-readable test reporting.

## Test Layers

### Prompt Contracts

Prompt contract tests validate deterministic behavior for:

- Prompt directory and file presence.
- Fallback safety contract.
- Meeting preparation Zero-Trust contract.

Primary file:

```text
tests/test_prompts_contract.py
```

Current result:

```text
3 passed
```

### Observability Contracts

Observability tests validate deterministic KPI behavior for:

- Grounded Answer Rate.
- Fallback Rate.
- Citation Coverage.
- Session latency.
- Supervisor route traceability.
- Guardrail traceability.

Primary files:

```text
tests/test_observability_contract.py
tests/fixtures/observability_events.jsonl
```

Current result:

```text
8 passed
```

### Full Regression

The repository-wide suite validates end-to-end stability across the working
build.

Generated evidence:

```text
docs/evidence/test_full_suite.log
docs/evidence/test-results.xml
docs/evidence/test_performance_all.log
```

Current result:

```text
31 passed
0 failed
```

## Visual Validation Support

The automated package is complemented by interface screenshots under:

```text
docs/screenshots/
```

These screenshots document:

- Home dashboard.
- Executive briefing.
- Grounding and citation tracing.
- Competitive intelligence scenarios.
- Fallback behavior.
- Adversarial prompt rejection.

Representative examples include:

```text
docs/screenshots/2_executive-briefing.png
docs/screenshots/6_Citations_Groud&Tracing.png
docs/screenshots/7_fallback-orion_missing-account.png
docs/screenshots/8_Hallucination_adversarial-prompt.png
```

## Commands

Run prompt governance tests:

```bash
pytest tests/test_prompts_contract.py -v
```

Run observability tests:

```bash
pytest tests/test_observability_contract.py -v
```

Run the full suite and export JUnit XML:

```bash
pytest -v \
  --durations=10 \
  --durations-min=0.1 \
  --junitxml=docs/evidence/test-results.xml \
  | tee docs/evidence/test_full_suite.log
```

Run a broader performance-oriented execution log:

```bash
pytest -v --durations=0 | tee docs/evidence/test_performance_all.log
```

## Validation Baseline

```text
Prompt contract tests: 3 passed
Observability contract tests: 8 passed
Full regression suite: 31 passed
Failures: 0
```

## Evidence Interpretation

- Screenshots prove local interface behavior.
- Prompt tests prove deterministic prompt governance.
- Observability tests prove KPI and telemetry logic.
- JUnit XML proves machine-readable test reporting.
- Full-suite logs prove repository-wide execution.

## Scope Note

The observability layer is a local simulation aligned with Agentforce Session
Tracing. It does not represent a live Salesforce production telemetry
connection.

Suggested explanation:
>"The interface demonstrates the agent's behavior, but governance does not rely on the UI.
>Automated contracts validate prompts, Zero Trust, fallback, grounding, citation coverage, latency, routing, and guardrails.
>The current test suite has 31 passing tests with zero failures, generating textual evidence and JUnit XML. In the Demo,
>simulate the test execution, noting that this exact same event model connects to Session Tracing and the telemetry
>platform."