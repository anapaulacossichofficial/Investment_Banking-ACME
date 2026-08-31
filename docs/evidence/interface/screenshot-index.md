# Screenshot Index

> **Navigation note:** This file indexes UI/interface evidence only. For the current, authoritative architecture documentation, see [`docs/architecture/README.md`](../../architecture/README.md).


## Scope

This index maps the screenshots available in `docs/screenshots/` to the
validation scenarios defined in the Front 1 Validation Matrix.

Screenshots provide visual evidence of the local Streamlit experience.
Automated test logs, telemetry contracts, and JUnit reports provide separate
programmatic evidence.

## Collected Screenshots

| ID | Screenshot File | Scenario | Linked Tests / Matrix IDs | Status | Evidence Type |
|---|---|---|---|---|---|
| **SS-01** | `docs/screenshots/1_home-dashboard.png` | Landing page and application overview | `test_smoke.py::test_smoke`, QA-01 | Collected | Visual |
| **SS-02** | `docs/screenshots/2_executive-briefing.png` | Executive meeting briefing | `test_meeting_prep_agent_generates_briefing`, IO-01, SR-01 | Collected | Visual |
| **SS-03** | `docs/screenshots/2_executive-briefing_grounding.png` | Grounded executive briefing | `test_get_account_bundle_filters_by_account_id`, IO-01, GR-01 | Collected | Visual |
| **SS-04** | `docs/screenshots/3_competitive-intelligence-briefing.png` | Competitive intelligence briefing | Competitive intelligence agent and retriever tests, SR-02 | Collected | Visual |
| **SS-05** | `docs/screenshots/3_executive-briefing_peer-benchmarking.png` | Peer benchmarking | Competitive intelligence retriever tests, SR-02 | Collected | Visual |
| **SS-06** | `docs/screenshots/5_executive-briefing_strategicinsights.png` | Strategic market insights | Competitive intelligence retriever tests, SR-03 | Collected | Visual |
| **SS-07** | `docs/screenshots/6_Citations_Activities.png` | CRM activity citation evidence | CI-01, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-08** | `docs/screenshots/6_Citations_Groud&Tracing.png` | CRM and knowledge source tracing | CI-01, GR-01, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-09** | `docs/screenshots/7_fallback-orion_missing-account.png` | Missing account fallback for Orion scenario | FB-01, `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-10** | `docs/screenshots/7_fallback-orion_missing-knowledge.png` | Missing knowledge fallback for Orion scenario | FB-02, `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-11** | `docs/screenshots/7_fallback-UKNOWN_missing-account.png` | Missing account fallback for unknown account scenario | FB-01, `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-12** | `docs/screenshots/7_fallback-UKNOWN_missing-knowledge.png` | Missing knowledge fallback for unknown account scenario | FB-02, `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-13** | `docs/screenshots/8_Hallucination_adversarial-prompt.png` | Generic adversarial prompt rejection | HR-01, `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-14** | `docs/screenshots/8_Hallucination_Orion-adversarial-prompt.png` | Orion adversarial prompt rejection | HR-01, `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-15** | `docs/screenshots/8_Hallucination_Existing-account_adversarial-prompt.png` | Existing-account adversarial prompt rejection | HR-01, `tests/test_prompts_contract.py`, `tests/test_observability_contract.py` | Collected | Visual and contract-linked |
| **SS-16** | `docs/screenshots/9_Observability_Testing.png` | Agentforce observability test run overview | OBS-01, `tests/test_observability_contract.py` | Collected — 14/08/2026 | Visual and contract-linked |
| **SS-17** | `docs/screenshots/9_Observability_Contract_Testing.png` | Observability contract test execution | OBS-01, `tests/test_observability_contract.py` | Collected — 14/08/2026 | Visual and contract-linked |
| **SS-18** | `docs/screenshots/9_Full_suite_Testing.png` | Full test suite execution evidence | QA-01, all test modules | Collected — 14/08/2026 | Visual and contract-linked |
| **SS-19** | `docs/screenshots/9_Blueprint_Validation_Architecture_evidence.png` | Architecture blueprint validation | ARCH-01, `tests/test_supervisor_and_meeting_prep.py` | Collected — 14/08/2026 | Visual |
| **SS-20** | `docs/screenshots/1_ACME_newacc.png` | ACME new account creation in Salesforce | DS-01, CRM-01 | Collected — 14/08/2026 | Visual |
| **SS-21** | `docs/screenshots/1_ACMEacc.png` | ACME account record view | DS-01, CRM-01 | Collected — 14/08/2026 | Visual |
| **SS-22** | `docs/screenshots/1_AccList.png` | Account list — CRM data seeding validation | DS-01, CRM-01 | Collected — 14/08/2026 | Visual |
| **SS-23** | `docs/screenshots/1_Globaltrust_peerAccount.png` | GlobalTrust peer account record | DS-01, CRM-02 | Collected — 14/08/2026 | Visual |
| **SS-24** | `docs/screenshots/1_target_data-model-GLOBALTRUST.png` | Target data model — GlobalTrust object mapping | DM-01, DS-02 | Collected — 14/08/2026 | Visual |
| **SS-25** | `docs/screenshots/1_target_data-model-QUANTUM.png` | Target data model — QUANTUM base object | DM-01, DS-02 | Collected — 14/08/2026 | Visual |
| **SS-26** | `docs/screenshots/1_target_data-model-QUANTUM_contacts.png` | Target data model — QUANTUM Contacts relationship | DM-01, DS-02 | Collected — 14/08/2026 | Visual |
| **SS-27** | `docs/screenshots/1_target_data-model-QUANTUM_opps.png` | Target data model — QUANTUM Opportunities relationship | DM-01, DS-02 | Collected — 14/08/2026 | Visual |
| **SS-28** | `docs/screenshots/1_target_prompt_builder.png` | Agentforce target prompt builder configuration | PB-01, `tests/test_prompts_contract.py` | Collected — 14/08/2026 | Visual and contract-linked |
| **SS-29** | `docs/screenshots/1_target_agentforce_routing.png` | Agentforce target routing configuration | SR-01, `tests/test_supervisor_and_meeting_prep.py` | Collected — 14/08/2026 | Visual and contract-linked |
| **SS-30** | `docs/screenshots/1_QUANTUM_prompt_PREVIEW.png` | QUANTUM agent prompt preview in Agentforce builder | PB-01, `tests/test_prompts_contract.py` | Collected — 14/08/2026 | Visual and contract-linked |
| **SS-31** | `docs/screenshots/1_prompt_template.png` | Prompt template configuration in Agentforce builder | PB-01, `tests/test_prompts_contract.py` | Collected — 14/08/2026 | Visual and contract-linked |

## Automated Evidence References

| Evidence File | Purpose | Status |
|---|---|---|
| `docs/evidence/test_prompts_contract.log` | Prompt governance and safety contract | Automated |
| `docs/evidence/test_observability_contract.log` | KPI and telemetry contract | Automated |
| `docs/evidence/test_full_suite.log` | Full regression execution | Automated |
| `docs/evidence/test-results.xml` | Structured JUnit test report | Automated |
| `docs/evidence/test_performance_all.log` | Performance and duration evidence — updated 14/08/2026 | Automated |
| `data/crm/activities_fixed.csv` | CRM activity seed data — fixed dataset 14/08/2026 | Data fixture |
| `tests/fixtures/observability_events.jsonl` | Deterministic telemetry fixture | Test fixture |

## Status Definitions

- **Collected:** The screenshot file exists at the referenced path and the
  scenario was validated.
- **Automated:** The scenario is covered by executable tests or a structured
  test report.
- **Architecture Mapping:** The item describes the intended production
  integration and is not a local screenshot.

## Validation Baseline

The current automated validation baseline is:

```text
Prompt contract tests: 3 passed
Observability contract tests: 8 passed
Full regression suite: 39 passed
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
structured events, metrics, and diagnostics. The local repository documents a
simulation of these contracts, not a live Salesforce production trace.

## Review Checklist

- [x] All existing screenshot files are mapped with their real names.
- [x] Fallback screenshots are marked collected.
- [x] Hallucination rejection screenshots are marked collected.
- [x] Observability and full-suite test screenshots from 14/08/2026 added (SS-16..SS-19).
- [x] Agentforce target build screenshots from 14/08/2026 added (SS-20..SS-31).
- [x] Automated evidence updated: test_performance_all.log and activities_fixed.csv.
- [x] Screenshot references use `.png` filenames that match the repository.
- [x] Validation baseline reflects the current automated test results.