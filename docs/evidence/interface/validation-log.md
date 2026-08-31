# UI Validation Log

> **Navigation note:** This log validates UI/interface behavior only. For the current, authoritative architecture documentation, see [`docs/architecture/README.md`](../../architecture/README.md). For the consolidated automated test summary, see [`docs/evidence/test-results-summary.md`](../test-results-summary.md).


## Environment

- **Application:** Investment Bank ACME
- **Entry point:** `streamlit_app.py`
- **Validation date:** 2026-08-10
- **Runtime:** Local Streamlit application under WSL
- **Validation scope:** UI behavior, grounding, citations, fallback,
  hallucination rejection, routing, and evidence capture

## Source Matrix

This log is aligned with:

```text
docs/front-1-validation-matrix.md
```

The validation matrix defines the critical cases for:

- Input and output stability.
- CRM grounding.
- Source citations.
- Fallback behavior.
- Supervisor routing.
- Hallucination rejection.
- UI structure.
- Prompt governance.
- Observability KPIs.

## Storage

- **Screenshots:** `docs/screenshots/`
- **Interface evidence:** `docs/evidence/interface/`
- **Prompt contract evidence:** `docs/evidence/test_prompts_contract.log`
- **Observability contract evidence:** `docs/evidence/test_observability_contract.log`
- **Full regression evidence:** `docs/evidence/test_full_suite.log`
- **Structured test report:** `docs/evidence/test-results.xml`
- **Telemetry fixture:** `tests/fixtures/observability_events.jsonl`

## Screenshot Inventory

The following screenshots were confirmed in the repository:

- `1_home-dashboard.png`
- `2_executive-briefing.png`
- `2_executive-briefing_grounding.png`
- `3_competitive-intelligence-briefing.png`
- `3_executive-briefing_peer-benchmarking.png`
- `5_executive-briefing_strategicinsights.png`
- `6_Citations_Activities.png`
- `6_Citations_Groud&Tracing.png`
- `7_fallback-UKNOWN_missing-account.png`
- `7_fallback-UKNOWN_missing-knowledge.png`
- `7_fallback-orion_missing-account.png`
- `7_fallback-orion_missing-knowledge.png`
- `8_Hallucination_Existing-account_adversarial-prompt.png`
- `8_Hallucination_Orion-adversarial-prompt.png`
- `8_Hallucination_adversarial-prompt.png`

## Execution Log

- **[PASS] IO-01:** Executive briefing scenario is represented by the
  collected executive briefing screenshots.
  Evidence: `SS-02` and `SS-03`.
- **[PASS] GR-01:** CRM account scoping and opportunity filtering are covered
  by the retriever tests and grounded briefing evidence.
  Evidence: `SS-03` and `SS-08`.
- **[PASS] CI-01:** CRM activity and source tracing evidence is available.
  Evidence: `SS-07` and `SS-08`.
- **[PASS] SR-01:** Meeting preparation routing is covered by the Supervisor
  tests.
  Evidence: `SS-02`.
- **[PASS] SR-02:** Peer benchmarking scenario is represented by the collected
  peer benchmarking screenshot.
  Evidence: `SS-04` and `SS-05`.
- **[PASS] SR-03:** Strategic insight and competitive intelligence scenarios
  are represented by the collected screenshots.
  Evidence: `SS-06`.
- **[PASS] FB-01:** Missing-account fallback behavior is visually documented.
  Evidence: `SS-09` and `SS-11`.
- **[PASS] FB-02:** Missing-knowledge fallback behavior is visually documented.
  Evidence: `SS-10` and `SS-12`.
- **[PASS] HR-01:** Adversarial prompt rejection is visually documented.
  Evidence: `SS-13`, `SS-14`, and `SS-15`.
- **[PASS] PC-01:** Prompt governance contract passed.
  Evidence: 3 prompt contract tests passed.
- **[PASS] OB-01:** Local observability contract passed.
  Evidence: 8 observability contract tests passed.
- **[PASS] QA-01:** Full regression suite passed.
  Evidence: 39 tests passed with zero failures.

## Automated Validation Baseline

```text
Prompt contract: 3 passed
Observability contract: 8 passed
Full regression suite: 39 passed
Failures: 0
```

## Evidence Classification

- **Visual evidence:** Screenshots under `docs/screenshots/`.
- **Automated evidence:** Pytest logs and JUnit XML.
- **Telemetry contract evidence:** JSONL fixture and KPI assertions.
- **Production architecture evidence:** Planned mapping to Agentforce
  Session Tracing and OpenTelemetry.

The local Streamlit application must not be described as a live production
Agentforce telemetry implementation.

## Corrected File References

The following actual files use `.png` extensions:

```text
docs/screenshots/1_home-dashboard.png
docs/screenshots/6_Citations_Groud&Tracing.png
docs/screenshots/7_fallback-orion_missing-account.png
docs/screenshots/8_Hallucination_adversarial-prompt.png
```

Repository references must use the exact filenames present under
`docs/screenshots/`.

## Exit Status

Current status:

- [x] Automated tests pass: 39/39.
- [x] Prompt governance contract passes: 3/3.
- [x] Observability contract passes: 8/8.
- [x] Core Supervisor intents are covered.
- [x] Existing screenshots are indexed using real filenames.
- [x] Missing-account fallback screenshots captured.
- [x] Missing-knowledge fallback screenshots captured.
- [x] Hallucination rejection screenshots captured.
- [x] Final visual evidence package completed.

## Reviewer Notes

The automated and visual validation package is complete.

The current evidence set includes:

1. Executive briefing and grounding.
2. Citation tracing.
3. Competitive intelligence routing.
4. Fallback behavior.
5. Adversarial prompt rejection.
6. Structured automated evidence and JUnit output.

Production Agentforce observability remains an integration target, not a claim
about the local Streamlit runtime.