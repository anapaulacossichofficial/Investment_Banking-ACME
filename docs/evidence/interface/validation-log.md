# UI Validation Log

## Environment

- **Application:** Investment Bank ACME
- **Entry point:** `streamlit_app.py`
- **Validation date:** 2026-08-09
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

The following screenshots were confirmed in the repository on 2026-08-09:

- `1_home-dashboard.png`
- `2_executive-briefing.png`
- `2_executive-briefing_grounding.png`
- `3_competitive-intelligence-briefing.png`
- `3_executive-briefing_peer-benchmarking.png`
- `5_executive-briefing_strategicinsights.png`
- `6_Citations_Activities.png`
- `6_Citations_Groud&Tracing.png`

The following validation screenshots remain to be captured:

- `fallback-orion.png`
- `hallucination-rejection.png`

## Execution Log

- **[PASS] IO-01:** Executive briefing scenario is represented by the
  collected executive briefing screenshots.
  Evidence: `SS-02` and `SS-03`.
- **[PASS] GR-01:** CRM account scoping and opportunity filtering are covered
  by the retriever tests and grounded briefing evidence.
  Evidence: `SS-03`.
- **[PASS] CI-01:** CRM activity and source tracing evidence is available.
  Evidence: `SS-07` and `SS-08`.
- **[PASS] SR-01:** Meeting preparation routing is covered by the Supervisor
  tests.
  Evidence: `test_supervisor_routes_intents`.
- **[PASS] SR-02:** Peer benchmarking scenario is represented by the collected
  peer benchmarking screenshot.
  Evidence: `SS-05`.
- **[PASS] SR-03:** Strategic insight and competitive intelligence scenarios
  are represented by the collected screenshots.
  Evidence: `SS-04` and `SS-06`.
- **[PASS] PC-01:** Prompt governance contract passed.
  Evidence: 3 prompt contract tests passed.
- **[PASS] OB-01:** Local observability contract passed.
  Evidence: 8 observability contract tests passed.
- **[PASS] QA-01:** Full regression suite passed.
  Evidence: 31 tests passed with zero failures.
- **[PENDING] FB-01:** Capture the missing-account fallback screenshot.
  Expected file: `docs/screenshots/fallback-orion.png`.
- **[PENDING] FB-02:** Capture the missing-evidence fallback screenshot and
  verify the exact fallback statement.
  Expected file: `docs/screenshots/fallback-orion.png`.
- **[PENDING] HR-01:** Capture the adversarial prompt rejection screenshot.
  Expected file: `docs/screenshots/hallucination-rejection.png`.

## Automated Validation Baseline

```text
Prompt contract: 3 passed
Observability contract: 8 passed
Full regression suite: 31 passed
Failures: 0
```

The local observability contract validates:

- Grounded Answer Rate.
- Fallback Rate.
- Citation Coverage.
- Session latency.
- Supervisor route traceability.
- Guardrail event traceability.

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
```

The validation matrix must not reference:

```text
docs/screenshots/1_home-dashboard.jpg
docs/screenshots/6_Citations_Groud&Tracing.jpg
```

## Exit Status

Current status:

- [x] Automated tests pass: 31/31.
- [x] Prompt governance contract passes: 3/3.
- [x] Observability contract passes: 8/8.
- [x] Core Supervisor intents are covered.
- [x] Existing screenshots are indexed using real filenames.
- [ ] Missing-account fallback screenshot captured.
- [ ] Hallucination rejection screenshot captured.
- [ ] Final visual evidence package completed.

## Reviewer Notes

The automated validation is complete. The remaining work is limited to
capturing the two missing visual scenarios:

1. Missing-account or missing-evidence fallback.
2. Adversarial prompt rejection.

After those files are captured, update the screenshot index from
`Pending capture` to `Collected` and change the corresponding validation log
items from `[PENDING]` to `[PASS]`.