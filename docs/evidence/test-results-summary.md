# Test Results Summary

Consolidated, human-readable summary of all automated test runs and validation evidence stored under `docs/evidence/`. Last reviewed: 2026-08-31.

## Latest Full Regression Run (Authoritative)

Source: [`test-results.xml`](./test-results.xml) (JUnit XML) · [`test_full_suite.log`](./test_full_suite.log) · [`test-report.html`](./test-report.html) (interactive report)

| Metric | Value |
|---|---|
| Total tests | 39 |
| Passed | 39 |
| Failures / Errors / Skipped | 0 / 0 / 0 |
| Execution time | 0.825s (XML run) / 0.83s (log run) |
| Last run timestamp | 2026-08-26T12:55:29 (-03:00), re-verified 2026-08-31 13:17:06 |
| Host | BOOK-D9KDUVEQSD (WSL2, Python 3.12.3, pytest 9.1.1) |

### Coverage by Test Module

| Test module | Tests | What it validates |
|---|---|---|
| `test_competitive_intelligence_agent` | 2 | Module imports and exposes a usable Competitive Intelligence agent |
| `test_competitive_intelligence_retriever` | 10 | Retriever init, real data loaders (institutions, peers, metrics, insights, sources), option resolution, metric-to-source mapping |
| `test_crm_retriever` | 2 | CRM account bundle retrieval and filtering by account ID |
| `test_handoff_contract` | 1 | Sub-agent handoff contract generation |
| `test_observability_contract` | 8 | Fixture existence, event schema, grounded answer rate, fallback rate, citation coverage, session latency, supervisor route trace, guardrail traceability |
| `test_page_competitive_intelligence` | 1 | Streamlit page imports without app template dependencies |
| `test_prompts_contract` | 5 | Prompt directory/files, Meeting Prep zero-trust contract, non-empty user prompts, supervisor router prompt contract, prompt version registry |
| `test_scope_resolver` | 3 | Account scope locking, unknown-account handling, cross-account boundary blocking |
| `test_smoke` | 1 | Baseline smoke test |
| `test_supervisor_and_meeting_prep` | 2 | Supervisor intent routing, hybrid grounded briefing generation |
| `test_tool_contract_schema` | 1 | Tool contract schema validity |

## Historical / Segmented Runs (Earlier Environment)

These logs were captured on a prior machine path (`/mnt/c/4_SalesForce/...`) during incremental development. They are superseded by the full 39-test run above but are kept as an audit trail of module-by-module validation.

| Log file | Tests | Result | Scope |
|---|---|---|---|
| [`performance_competitive_intelligence.log`](./performance_competitive_intelligence.log) | 14 | 14 passed | Competitive Intelligence agent + retriever |
| [`performance_observability.log`](./performance_observability.log) | 8 | 8 passed | Observability contract (early version, pre-supervisor-route-trace addition) |
| [`performance_prompts.log`](./performance_prompts.log) | 3 | 3 passed | Prompt directory, fallback safety, zero-trust contract |
| [`performance_agents_smoke.log`](./performance_agents_smoke.log) | 3 | 3 passed | Supervisor routing, meeting prep briefing, smoke test |
| [`routing_audit.log`](./routing_audit.log) / [`test_routing_evidence.log`](./test_routing_evidence.log) | 2 | 2 passed | Supervisor intent routing + meeting prep briefing generation |
| [`test_prompts_contract.log`](./test_prompts_contract.log) | 3 | 3 passed | Prompt contract (early naming, pre-`active_` prefix refactor) |
| [`test_observability_contract.log`](./test_observability_contract.log) / [`test_observability.log`](./test_observability.log) | — | Passed | Observability contract, duplicate captures |
| [`test_routing_and_governance.log`](./test_routing_and_governance.log) | — | Passed | Combined routing + governance checks |
| [`test_performance.log`](./test_performance.log) / [`test_performance_all.log`](./test_performance_all.log) | — | Passed | Broader performance/regression captures |
| [`hybrid_retrieval_scope_tests.log`](./hybrid_retrieval_scope_tests.log) | — | Passed | Hybrid retrieval + scope resolver checks |
| [`test_evidence_run.log`](./test_evidence_run.log) | — | Passed | General evidence capture run |
| [`test_execution_report.log`](./test_execution_report.log) | — | Passed | Short-form execution summary |

## Structural & Blueprint Validation

Source: [`blueprint_validation.log`](./blueprint_validation.log)

| Check | Result |
|---|---|
| Expected config/prompt/test files exist | PASS (11/11) |
| YAML files parse correctly | PASS (9/9) |
| Required policy keys present (agent profile, retrieval, citation, guardrail, fallback, observability) | PASS |
| `prompt_versions.yaml` entries have `current_version` + versions | PASS (3/3 prompts) |
| No forbidden tokens in project code | PASS |
| Base institution name (`ACME_Banking`) consistently referenced | PASS |
| **Overall** | **BLUEPRINT VALIDATION: PASS** |

Related structural logs: [`front3_structural_validation.log`](./front3_structural_validation.log), [`front3_alignment_audit.log`](./front3_alignment_audit.log), [`front3_observability_contracts.log`](./front3_observability_contracts.log), [`front3_prompt_contracts.log`](./front3_prompt_contracts.log) — all aligned with the same PASS outcome for structure, observability, and prompt governance checks.

## UI / Interface Validation

Source: [`interface/validation-log.md`](./interface/validation-log.md), [`interface/evidence-note.md`](./interface/evidence-note.md), [`interface/screenshot-index.md`](./interface/screenshot-index.md)

- Validated 2026-08-10 against `docs/front-1-validation-matrix.md`, covering I/O stability, CRM grounding, citations, fallback behavior, supervisor routing, hallucination rejection, UI structure, prompt governance, and observability KPIs.
- All checks marked **[PASS]**: executive briefing, CRM scoping, citation tracing, meeting-prep routing, peer benchmarking, strategic insight routing, missing-account fallback, missing-knowledge fallback, adversarial prompt rejection.
- Screenshot inventory cross-checked against real filenames under `docs/screenshots/` (corrected `.png` extension mismatches).
- Explicit reviewer note: the local Streamlit app must **not** be presented as a live production Agentforce telemetry implementation — that mapping is a planned integration target, not a current claim.

## Platform-Native Evidence (Salesforce / Agentforce)

Source: [`salesforce-org/`](./salesforce-org/) (70+ files)

- **Apex/deploy evidence:** `2026-08-26_apex-test-coverage.json`, `2026-08-26_deploy-dry-run_api67.json`, `2026-08-26_deploy-real_api67.json`, `2026-08-26_globaltrust-target-account.json`, `target-account.json`.
- **Agent Builder & routing screenshots:** agent creation, naming, routing config, subagent summary (`4_Agent*.png`).
- **Data Cloud / Prompt Builder screenshots:** DMO setup, resolved prompt previews, data library wiring (`1_promptbuilder_*.png`, `4_DataCloud*.png`, `5_ACME_PromptBuilder.png`).
- **Guardrails & Zero-Trust tracing:** `6_EinsteinGuardrails.png`, `6_RestrictedGuardrailsTracing*.png`, `6_Zero-Trust_Tracing_EinsteinGuardrails*.png`.
- **End-to-end Agentforce tracing (18 screenshots):** live test query/response, action tracing, scope resolver tracing, competitive intelligence handoff and return, meeting prep briefing tracing, reasoning/citation tracing, variable updates (`7_AgentforceE2E_*.png`).
- **Functional test log:** `competitive_action_test_result.log`.

This is the evidence set that demonstrates native Agentforce/Data Cloud behavior, complementing the local pytest suite above.

## Architecture Reference Scope

Source: [`target-vs-demo-runtime.md`](./target-vs-demo-runtime.md)

- `docs/architecture/option-b-architecture.md` is a **target/reference architecture**, explicitly not part of the live demo.
- The demo is supported only by `docs/architecture/architecture-diagram.md` and `docs/architecture/solution-blueprint.md`, which must describe only capabilities observable in the working build.
- Any future-state or conceptual integration must be labeled as non-runtime reference material.

## Overall Status

| Evidence category | Status |
|---|---|
| Automated unit/contract tests (latest full suite) | 39/39 PASS |
| Blueprint/structural validation | PASS |
| UI/interface validation | PASS (all scenarios) |
| Salesforce/Agentforce platform tracing | Captured (screenshots + JSON deploy evidence) |
| Architecture scope discipline | Documented and enforced |

No open failures, errors, or unresolved gaps were found across the reviewed evidence set as of this update.
