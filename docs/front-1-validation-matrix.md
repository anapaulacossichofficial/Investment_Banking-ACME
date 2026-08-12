# Front 1 Validation Matrix

## Objective

This matrix defines the validation coverage for the ACME Investment Banking
Working Build. It links critical user-facing behaviors to automated tests,
visual evidence, and repository artifacts.

The matrix is intended to prove deterministic behavior before any future
mapping to Agentforce production telemetry.

## Validation Baseline

```text
Prompt contract tests: 5 passed
Observability contract tests: 8 passed
Full regression suite: 35 passed
Failures: 0
```

## Matrix

| ID | Capability Area | Scenario | Expected Result | Automated Evidence | Visual Evidence | Status |
|---|---|---|---|---|---|---|
| IO-01 | Input / Output Contract | Executive meeting briefing generation | Structured executive-ready briefing is rendered consistently | `tests/test_prompts_contract.py`, `tests/test_supervisor_and_meeting_prep.py` | `docs/screenshots/2_executive-briefing.png`, `docs/screenshots/2_executive-briefing_grounding.png` | Pass |
| GR-01 | Grounding | CRM and knowledge evidence are visibly grounded | Response stays scoped to approved account and source context | `tests/test_crm_retriever.py`, `tests/test_prompts_contract.py` | `docs/screenshots/2_executive-briefing_grounding.png`, `docs/screenshots/6_Citations_Groud&Tracing.png` | Pass |
| CI-01 | Citations | Material claims are accompanied by visible source tracing | CRM and knowledge-source citations are exposed in the UI | `tests/test_observability_contract.py` | `docs/screenshots/6_Citations_Activities.png`, `docs/screenshots/6_Citations_Groud&Tracing.png` | Pass |
| FB-01 | Fallback Behavior | Missing account scenario | Assistant returns the exact safe fallback behavior without invention | `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | `docs/screenshots/7_fallback-orion_missing-account.png`, `docs/screenshots/7_fallback-UKNOWN_missing-account.png` | Pass |
| FB-02 | Fallback Behavior | Missing evidence / missing knowledge scenario | Assistant returns a safe fallback statement when evidence is unavailable | `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | `docs/screenshots/7_fallback-orion_missing-knowledge.png`, `docs/screenshots/7_fallback-UKNOWN_missing-knowledge.png` | Pass |
| HR-01 | Zero-Trust Guardrails | Adversarial prompt injection attempt | Assistant rejects unsupported instructions and does not bypass grounding | `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | `docs/screenshots/8_Hallucination_adversarial-prompt.png`, `docs/screenshots/8_Hallucination_Orion-adversarial-prompt.png`, `docs/screenshots/8_Hallucination_Existing-account_adversarial-prompt.png` | Pass |
| SR-01 | Supervisor Routing | Meeting preparation intent | Correct route is selected and traceable | `tests/test_supervisor_and_meeting_prep.py`, `tests/test_observability_contract.py` | `docs/screenshots/2_executive-briefing.png` | Pass |
| SR-02 | Supervisor Routing | Peer benchmarking route | Competitive intelligence benchmark flow is selected and traceable | `tests/test_competitive_intelligence_agent.py`, `tests/test_competitive_intelligence_retriever.py` | `docs/screenshots/3_competitive-intelligence-briefing.png`, `docs/screenshots/3_executive-briefing_peer-benchmarking.png` | Pass |
| SR-03 | Supervisor Routing | Strategic insight route | Strategic market insight flow is selected and traceable | `tests/test_competitive_intelligence_retriever.py` | `docs/screenshots/5_executive-briefing_strategicinsights.png` | Pass |
| PC-01 | Prompt Governance | Prompt contract enforcement | Meeting prep and fallback prompt rules remain stable under test | `tests/test_prompts_contract.py` | N/A | Pass |
| OB-01 | Observability KPIs | Grounding, fallback, citations, latency, and routes | KPI assertions pass against deterministic telemetry fixture | `tests/test_observability_contract.py`, `tests/fixtures/observability_events.jsonl` | N/A | Pass |
| QA-01 | Regression / Smoke | Full repository validation | Repository-wide regression suite completes successfully | `docs/evidence/test_full_suite.log`, `docs/evidence/test-results.xml` | `docs/screenshots/1_home-dashboard.png` | Pass |

## Notes

- Visual evidence validates the local Streamlit runtime.
- Automated evidence validates deterministic governance and observability
  contracts.
- Production Agentforce Session Tracing is represented as an architecture
  mapping target, not as a live implementation claim.
- Screenshot references must use the exact filenames present in
  `docs/screenshots/`.