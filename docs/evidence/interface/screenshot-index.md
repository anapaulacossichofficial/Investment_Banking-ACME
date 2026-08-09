# Screenshot Index

## Scope

This index maps the screenshots actually available in
`docs/screenshots/` to the validation scenarios defined in the Front 1
Validation Matrix.

Screenshots provide visual evidence of the local Streamlit experience.
Automated test logs, telemetry contracts, and JUnit reports provide separate
programmatic evidence.

## Collected Screenshots

| ID | Screenshot File | Scenario | Linked Tests / Matrix IDs | Status | Evidence Type |
|---|---|---|---|---|---|
| **SS-01** | `docs/screenshots/1_home-dashboard.png` | Landing page and application overview | `test_smoke.py::test_smoke`, RS-01 | Collected | Visual |
| **SS-02** | `docs/screenshots/2_executive-briefing.png` | Executive meeting briefing | `test_meeting_prep_agent_generates_briefing`, IO-01 | Collected | Visual |
| **SS-03** | `docs/screenshots/2_executive-briefing_grounding.png` | Grounded executive briefing | `test_get_account_bundle_filters_by_account_id`, IO-01, GR-01 | Collected | Visual |
| **SS-04** | `docs/screenshots/3_competitive-intelligence-briefing.png` | Competitive Intelligence briefing | Competitive intelligence agent and retriever tests, SR-02, SR-03 | Collected | Visual |
| **SS-05** | `docs/screenshots/3_executive-briefing_peer-benchmarking.png` | Peer benchmarking | Competitive intelligence retriever tests, SR-02 | Collected | Visual |
| **SS-06** | `docs/screenshots/5_executive-briefing_strategicinsights.png` | Strategic market insights | Competitive intelligence retriever tests, SR-03 | Collected | Visual |
| **SS-07** | `docs/screenshots/6_Citations_Activities.png` | CRM activity citation evidence | CI-01, `test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-08** | `docs/screenshots/6_Citations_Groud&Tracing.png` | CRM and knowledge source tracing | CI-01, `test_observability_contract.py` | Collected | Visual and contract-linked |

## Pending Screenshots

| ID | Expected Screenshot File | Scenario | Linked Tests / Matrix IDs | Status | Evidence Type |
|---|---|---|---|---|---|
| **SS-09** | `docs/screenshots/fallback-orion.png` | Missing account or unavailable evidence fallback | FB-01, FB-02, `test_prompts_contract.py`, `test_observability_contract.py` | Pending capture | Visual |
| **SS-10** | `docs/screenshots/hallucination-rejection.png` | Adversarial prompt rejection | HR-01, `test_prompts_contract.py`, `test_observability_contract.py` | Pending capture | Visual |

## Automated Evidence References

| Evidence File | Purpose | Status |
|---|---|---|
| `docs/evidence/test_prompts_contract.log` | Prompt governance and safety contract | Automated |
| `docs/evidence/test_observability_contract.log` | KPI and telemetry contract | Automated |
| `docs/evidence/test_full_suite.log` | Full regression execution | Automated |
| `docs/evidence/test-results.xml` | Structured JUnit test report | Automated |
| `tests/fixtures/observability_events.jsonl` | Deterministic telemetry fixture | Test fixture |

## Status Definitions

- **Collected:** The screenshot file exists at the referenced path.
- **Pending capture:** The scenario is defined but the screenshot file does not
  yet exist.
- **Automated:** The scenario is covered by executable tests or a structured
  test report.
- **Architecture Mapping:** The item describes the intended production
  integration and is not a local screenshot.

## Validation Baseline

The current automated validation baseline is:

```text
Prompt contract tests: 3 passed
Observability contract tests: 8 passed
Full regression suite: 31 passed
Failures: 0
```

## Production Observability Note

Screenshots do not prove production observability.

The local build validates observability through:

```text
tests/test_observability_contract.py
tests/fixtures/observability_events.jsonl
docs/evidence/test-results.xml
```

Production Agentforce observability requires session-level tracing,
structured events, metrics, and diagnostics. Agentforce Session Tracing
captures agent interactions from start to finish, including turns, reasoning
execution, actions, prompt and gateway inputs and outputs, errors, and final
responses. [web:2332][web:2224]

## Review Checklist

- [x] All eight existing screenshot files are mapped with their real names.
- [x] `.jpg` references were corrected to `.png`.
- [x] Missing fallback screenshot is marked pending.
- [x] Missing hallucination screenshot is marked pending.
- [x] Automated evidence is listed separately from visual evidence.
- [ ] Capture `fallback-orion.png`.
- [ ] Capture `hallucination-rejection.png`.
- [ ] Re-run the index review after both screenshots are captured.