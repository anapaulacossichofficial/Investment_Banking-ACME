# 🚀 ACME Investment Banker Assistant & Agentforce Blueprint

A hybrid enterprise architecture combining a **Salesforce Agentforce target deployment** and an **Engineering Lab Runtime**. This repository serves as the definitive artifact for the Option B Scenario: Knowledge-Grounded Meeting Prep Agent.

## 🚨 Option B Technical Scenario: Start Here

If you are reviewing this repository for the Option B deliverables, all 5 required elements have been fully validated and committed to the `main` branch (Release `v0.9.8`).

For direct navigation to the exact files and evidence required by the rubric, please see the:
👉 **[Option B: Technical Navigation Guide](EVALUATION_GUIDE_OPTION_B.md)**

### Option B Deliverables Summary
1. **Architecture Diagram:** Bounded flows between Agent, Actions, CRM, and External API documented in [`docs/architecture/`](docs/architecture/).
2. **Working Build (End-to-End):** Validated conversational routing, CRM grounding (`Account Snapshot`), and Apex Code Coverage (**>75%**). Full UI tracing available in [`docs/evidence/salesforce-org/`](docs/evidence/salesforce-org/).
3. **Prompt Iteration:** Evolved from raw string inputs to strict *Semantic Guardrails* in Reasoning Instructions, preventing data inversion and hallucination. See [`docs/evidence/front3_prompt_contracts.log`](docs/evidence/front3_prompt_contracts.log).
4. **Platform Judgment Callout:** Formal ADR documenting the architectural trade-off of disabling `Session Activation Required` for autonomous M2M Agent callouts. See [`docs/architecture/ADR-001-platform-constraints-m2m.md`](docs/architecture/ADR-001-platform-constraints-m2m.md).
5. **Observability Note:** Validated using native Agentforce `Trace` metrics and local simulated telemetry logs. See [`docs/evidence/test_observability.log`](docs/evidence/test_observability.log).

---

## 🏛️ Executive Summary & Architecture

The ACME working build demonstrates deterministic engineering aligned with enterprise coverage workflows. It implements a disaggregated serving model, bridging Salesforce's conversational AI capabilities with a Python-based Intelligence Backend.

> **🌟 Key Highlight: Beyond Option B — Lab-to-Cloud End-to-End Validation**
> To simulate a realistic enterprise client experience, this solution goes beyond the baseline Meeting Prep requirements. We built an **Engineering Lab Runtime (Streamlit)** that not only fulfills the Option B knowledge-grounding criteria but also introduces an advanced **Competitive Intelligence & Market Benchmarking** workflow comparing industry peers. This exact end-to-end scenario was successfully transitioned from the Engineering Lab Runtime and fully validated natively inside **ACME Dev Org on Agentforce** (complete with test results and proofs). This proves a seamless, end-to-end leap from lab simulation to a production-ready enterprise cloud deployment.

**Key Capabilities:**
- Grounded executive briefing generation from local CRM fixtures and approved knowledge sources.
- Account and contact scoping before downstream analysis.
- Competitive intelligence, peer benchmarking, strategic insights, and meeting-preparation workflows.
- Citation, source-tracing, and no-evidence fallback behavior.
- Zero-Trust prompt governance and observability KPI contracts.

### Architecture at a Glance

| Diagram | Purpose |
|---|---|
| [Solution HLD](docs/architecture/3_ACME_Investment_Bank_HLD_Architecture.png) | High-level design of the proposed solution: banker interaction, Salesforce UX, Agentforce Supervisor, CRM retrieval, and Trust Layer. |
| [Functional Diagram — Option B](docs/architecture/2_acme-optionB-functionaldiagram.png) | Knowledge-grounded Meeting Prep pattern aligned to the Salesforce Architects' Guide. |
| [Solution Flow](docs/architecture/2_acme-flow-diagram-tradeoffs.png) | Executive path from user interaction to evidence package. |
| [Design Trade-offs](docs/architecture/2_acme-agentforce-pattern_Tradeoffs.png) | Consolidated trade-offs view referencing `docs/architecture/design-trade-offs.md`. |
| **Scope Boundaries** | 🛑 Explicitly documented in **[Platform Limitations and Scope Boundaries](docs/architecture/platform-limitations.md)** to ensure realistic delivery guidelines. |

<p align="center">
  <img src="docs/architecture/2_acme-optionB-functionaldiagram.png" alt="Functional Diagram — Option B" width="900">
</p>

For the complete architecture package, see [docs/architecture/README.md](docs/architecture/README.md).

---

## ☁️ ACME Dev Org on Agentforce
This repository is tightly coupled with a Salesforce Agentforce Developer Edition Org to validate native AI orchestration. The Apex Actions, Bots, Prompt Templates, External Credentials, and Named Credentials are located in `acme-agentforce/force-app/main/default/`. Permission Sets retrieved directly from the dev org are tracked in `force-app/main/default/permissionsets/`.

| Item | Value |
|---|---|
| Target Org Alias | `acme-dev-org` |
| Agent | `ACME_Investment_Banker_Assistant` |
+ | Active Prompt Template | [Meeting_Prep_Briefing.genAiPromptTemplate-meta.xml](acme-agentforce/force-app/main/default/genAiPromptTemplates/Meeting_Prep_Briefing.genAiPromptTemplate-meta.xml) (v5, `Published`) |
| Known Integrations | ✅ `ACME_CompetitiveIntelligenceAction` (Apex Invocable) · ✅ `ACME_Meeting_Prep_Knowledge` (Data Cloud Grounding) · 🎯 Named Credentials (MCP/A2A pattern) |
| Permission Sets | ✅ Retrieved from `acme-dev-org` — agent-specific (`Agentforce_CI_Access`, `Agentforce_CRM_Access`, `ACME_Investment_Banker_Assistant1012860999_Permissions`) plus platform system-managed sets present in any Agentforce-enabled org |

*(Note: Session creation against the live org returns `404 NOT_FOUND` when invoked outside the Salesforce CLI agent test harness until an active agent session is configured).*

---

## 📎 Key Governance & Evidence Documents

| Document | Why it matters |
|---|---|
| [`docs/architecture/platform-limitations.md`](docs/architecture/platform-limitations.md) | Governance document defining exactly which steps require manual org configuration (Data Cloud Search Index, Retriever, ingestion) — protects scope boundaries during evaluation. |
+ | [`docs/architecture/platform-judgment-callout.md`](docs/architecture/platform-judgment-callout.md) | Strategic platform decision: custom Python stack vs. native Salesforce Agentforce. |
| [`docs/adr/adr-001-retrieval-strategy.md`](docs/adr/adr-001-retrieval-strategy.md) | Architecture Decision Record explaining why `src/` (Engineering Lab Runtime) and `agents/`/`acme-agentforce/` (Salesforce target) are kept as separate, purpose-specific layers. |
| [`force-app/README.md`](force-app/README.md) | Guide to the original SFDX metadata scaffold and its native Salesforce metadata components. |
| [`acme-agentforce/force-app/main/default/genAiPromptTemplates/Meeting_Prep_Briefing.genAiPromptTemplate-meta.xml`](acme-agentforce/force-app/main/default/genAiPromptTemplates/Meeting_Prep_Briefing.genAiPromptTemplate-meta.xml) | The published Flex Prompt Template (v5) — the core Agentforce artifact fulfilling the Option B knowledge-grounding requirement. |
| [`docs/evidence/test-results.xml`](docs/evidence/test-results.xml) | JUnit-standard machine-readable proof that the automated test suite passed. |

---

## 💻 Engineering Runtime & End-to-End Test Evidence

| Engineering Lab Runtime (Streamlit) | ACME Dev Org on Agentforce |
|---|---|
| ![Home Dashboard](docs/screenshots/1_home-dashboard.png) | ![Agentforce Live Test Response](docs/evidence/salesforce-org/7_AgentforceE2E_LiveTestResponse.png) |

<details>
<summary><b>Click to expand: End-to-End Agentforce Test Tracing (Dev Org)</b></summary>
<br>

### Agentforce End-to-End Test Tracing
The screenshots below trace a complete live agent session inside `acme-dev-org`, from live query through Action routing, competitive-intelligence handoff, guardrail validation, and grounded output.

- **Live Test Query:** ![Live Test Query](docs/evidence/salesforce-org/7_AgentforceE2E_LiveTestQuery.png)
- **Live Test Query Tracing:** ![Live Test Query Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_LiveTestQuery-Tracing.png)
- **Live Test Response:** ![Live Test Response](docs/evidence/salesforce-org/7_AgentforceE2E_LiveTestResponse.png)
- **Actions Tracing:** ![Actions Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_Actions-Tracing.png)
- **Actions Scope Resolver Tracing:** ![Actions Scope Resolver Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_ActionsScopeResolver-Tracing.png)
- **Agent Route Validation Tracing:** ![Agent Route Validation Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_AgentRoute-Validation-Tracing.png)
- **Agent Route Validation Tracing 2:** ![Agent Route Validation Tracing 2](docs/evidence/salesforce-org/7_AgentforceE2E_AgentRoute-Validation-Tracing2.png)
- **Agent Route — Competitive Intelligence Variables:** ![Agent Route Competitive Intelligence Variables](docs/evidence/salesforce-org/7_AgentforceE2E_AgentRoute-CompetIntel_Variables.png)
- **Sub-agent Handoff Tracing:** ![Sub-agent Handoff Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_SubagentHandoff-Tracing.png)
- **Competitive Intelligence Handoff Tracing:** ![Competitive Intelligence Handoff Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_CompetIntel-Handoff_Tracing.png)
- **Competitive Intelligence Action Tracing:** ![Competitive Intelligence Action Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_CompetIntelligence-Action_Tracing.png)
- **Competitive Intelligence Reasoning Tracing:** ![Competitive Intelligence Reasoning Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_CompetIntelligence-Reasoning_Tracing.png)
- **Competitive Intelligence Return:** ![Competitive Intelligence Return](docs/evidence/salesforce-org/7_AgentforceE2E_CompetitiveIntelligence_Return.png)
- **Competitive Intelligence Return Tracing (1-5):** ![Return Tracing 1](docs/evidence/salesforce-org/7_AgentforceE2E_ComIntelligenceReturn_Tracing.png) ![Return Tracing 2](docs/evidence/salesforce-org/7_AgentforceE2E_ComIntelligenceReturn_Tracing2.png) ![Return Tracing 3](docs/evidence/salesforce-org/7_AgentforceE2E_ComIntelligenceReturn_Tracing3.png) ![Return Tracing 4](docs/evidence/salesforce-org/7_AgentforceE2E_ComIntelligenceReturn_Tracing4.png) ![Return Tracing 5](docs/evidence/salesforce-org/7_AgentforceE2E_ComIntelligenceReturn_Tracing5.png)
- **Meeting Prep Briefing Tracing:** ![Meeting Prep Briefing Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_MeetingPrepBriefing-Tracing.png)
- **Output Grounded Tracing:** ![Output Grounded Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_OutputGrounded-Tracing.png)
- **Output Metrics Code Tracing:** ![Output Metrics Code Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_OutputMetricsCode-Tracing.png)
- **Reasoning — Opportunity Citation Tracing (1-2):** ![Reasoning Opp Citation 1](docs/evidence/salesforce-org/7_AgentforceE2E_Reasoning-OppCitation-Tracing.png) ![Reasoning Opp Citation 2](docs/evidence/salesforce-org/7_AgentforceE2E_Reasoning-OppCitation-Tracing2.png)
- **Reasoning — Prompt Response Tracing:** ![Reasoning Prompt Response Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_Reasoning-PromptResponse-Tracing.png)
- **Variable Update Tracing:** ![Variable Update Tracing](docs/evidence/salesforce-org/7_AgentforceE2E_VariableUpdate-Tracing.png)

### Agent Configuration & Prompt Builder Evidence
- **Prompt Builder — Data Model Object (DMO):** ![Prompt Builder DMO](docs/evidence/salesforce-org/1_promptbuilder_DMO.png)
- **Agentforce Summary:** ![Agentforce Summary](docs/evidence/salesforce-org/4_AgentforceSummary.png)
- **Data Library to Agent:** ![Data Library to Agent](docs/evidence/salesforce-org/4_DataLibrarytoAgent.png)
- **Agent Change:** ![Agent Change](docs/evidence/salesforce-org/4_AgentChange.png)
- **Resolved Prompt — Generate Response:** ![Resolved Prompt Generate Response](docs/evidence/salesforce-org/5_ResolvedPrompt_GenerateResponse.png)
- **Agentforce Meeting Preview:** ![Agentforce Meeting Preview](docs/evidence/salesforce-org/6_AgentorceMeetingPreview.png)
- **Meeting Preview Tracing:** ![Meeting Preview Tracing](docs/evidence/salesforce-org/6_MeetingPreviewTracing.png)
- **Meeting Preview Tracing — Code Detailed:** ![Meeting Preview Tracing Code Detailed](docs/evidence/salesforce-org/6_MeetingPreviewTracing-Codedetailed.png)
- **Reasoning Rules & Guardrails:** ![Reasoning Rules and Guardrails](docs/evidence/salesforce-org/6_Reasoning_Rules&Guardrails.png)
- **Agent Router — Competitive Intelligence:** ![Agent Router Competitive Intelligence](docs/evidence/salesforce-org/6_AgentRouter_CompetitiveIntelligence.png)

*(For the complete ACME Dev Org evidence catalog — including permission sets, external credentials, and guardrail tracing variants — browse [`docs/evidence/salesforce-org/`](docs/evidence/salesforce-org/).)*

</details>

<details>
<summary><b>Click to expand: Engineering Lab Runtime — Visual Preview & Simulated Environment Evidence</b></summary>
<br>

The repository includes an Engineering Lab working build (Demo Runtime) using **Streamlit** to simulate the end-to-end experience of the ACME Investment Banker Assistant. The Engineering Lab Runtime is a fully functional simulation of the ACME Dev Org on Agentforce deployment, allowing for testing and validation of the grounding, citation, and fallback behaviors before deploying to the cloud.

### Enterprise Visual Preview
The application provides an executive banking interface for institutional coverage workflows and competitive intelligence analysis.

- **Main Intelligence Hub:** ![ACME Banking Intelligence Hub](docs/screenshots/1_home-dashboard.png)
- **Executive Briefing:** ![Executive Briefing](docs/screenshots/2_executive-briefing.png)
- **Grounded Briefing:** ![Grounded Executive Briefing](docs/screenshots/2_executive-briefing_grounding.png)
- **Peer Benchmarking:** ![Peer Benchmarking](docs/screenshots/3_executive-briefing_peer-benchmarking.png)
- **Strategic Insights:** ![Strategic Insights](docs/screenshots/5_executive-briefing_strategicinsights.png)

### Citations and Fallback Validation
- **CRM Activities Citations:** ![CRM Activities Citations](docs/screenshots/6_Citations_Activities.png)
- **Grounding and Source Tracing:** ![Grounding and Source Tracing](docs/screenshots/6_Citations_Groud&Tracing.png)
- **Fallback (Missing Account):** ![Fallback Orion Missing Account](docs/screenshots/7_fallback-orion_missing-account.png)
- **Adversarial Prompt Rejection:** ![Adversarial Prompt Rejection](docs/screenshots/8_Hallucination_adversarial-prompt.png)

### CRM Data Model and Account Context
- ![Target CRM Data Model — GlobalTrust](docs/screenshots/1_target_data-model-GLOBALTRUST.png)
- ![Target CRM Data Model — Quantum](docs/screenshots/1_target_data-model-QUANTUM.png)

### Validation Evidence (Agentforce Runtime & Engineering Lab Runtime)
- ![Observability Testing](docs/screenshots/9_Observability_Testing.png)
- ![Blueprint Validation Architecture Evidence](docs/screenshots/9_Blueprint_Validation_Architecture_evidence.png)

*(For the complete screenshot catalog, see [`docs/evidence/interface/screenshot-index.md`](docs/evidence/interface/screenshot-index.md) or browse [`docs/screenshots/`](docs/screenshots/) directly.)*

</details>

---

## 📂 Repository Architecture & Governance Map

To enforce strict architectural discipline, this repository is organized by separating runtime execution from policy governance, and initial scaffolding from mature deployment.

**1. Salesforce Metadata (Cloud Deployment Layer)**
*   `acme-agentforce/`: The mature, E2E-tested Salesforce Agentforce implementation. Contains fully covered Apex Actions, Agent configurations, and secure M2M policies (External/Named Credentials).
*   **[`force-app/`](force-app/README.md):** The initial architectural scaffold. Preserved intentionally to document the structural baseline and version system-retrieved metadata (Permission Sets, Flex Prompt Templates) before integration maturity.

**2. Intelligence Backend (Engineering Lab Runtime)**
*   `src/`: The **Policy and Contract Layer**. As prescribed in **[`ADR-001: Retrieval Strategy`](docs/adr/adr-001-retrieval-strategy.md)**, this explicitly isolates execution from governance. Holds YAML policies and JSON schemas to enforce strict Zero-Trust boundaries.
*   `agents/` & `retrieval/`: The **Runtime Execution Layer**. Consumes the contracts from `src/` to execute the local simulation.

---

## 🛠️ Run the Application & Validation Suite

### Test Architecture
The repository validates behavior at three complementary levels:
1. **Visual validation** through screenshots under `docs/screenshots/`
2. **Prompt governance validation** through `tests/test_prompts_contract.py`
3. **Observability and regression validation** through `tests/test_observability_contract.py` and the full pytest suite

Review the generated evidence:
- **Prompt Contracts:** `docs/evidence/test_prompts_contract.log`
- **Observability:** `docs/evidence/test_observability_contract.log`
- **Full Suite Output:** `docs/evidence/test_full_suite.log`
- **JUnit Test Artifact:** [`docs/evidence/test-results.xml`](docs/evidence/test-results.xml)

To spin up the visual interface:
```bash
streamlit run streamlit_app.py
```
To run the local validation suite:
```bash
chmod +x scripts/run_validation_suite.sh
./scripts/run_validation_suite.sh
```
Review the generated evidence:
```bash
ls -lh docs/evidence/
tail -n 20 docs/evidence/test_prompts_contract.log
tail -n 20 docs/evidence/test_observability_contract.log
tail -n 20 docs/evidence/test_full_suite.log
```

### Observability Scope
The observability layer simulates Agentforce Session Tracing concepts. It validates deterministic KPI behavior for:
- Grounded Answer Rate
- Fallback Rate
- Citation Coverage
- Session latency
- Supervisor route traceability
- Guardrail event traceability

+ Repository Tag: v0.9.16 | Status: Option B Fully Validated, Architecture Governance Index Consolidated.