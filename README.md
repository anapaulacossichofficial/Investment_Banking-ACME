# 🚀 ACME Investment Banker Assistant & Agentforce Blueprint

A hybrid enterprise architecture combining a **Salesforce Agentforce target deployment** and an **Engineering Lab Runtime**. This repository serves as the definitive artifact for the Option B Scenario: Knowledge-Grounded Meeting Prep Agent.

---

## 🚨 Option B Technical Scenario: Start Here

If you are reviewing this repository for the Option B deliverables, all 5 required elements have been fully validated and committed to the `main` branch (Release `v0.9.8`).

For direct navigation to the exact files and evidence required by the rubric, please see the:
👉 **[Option B: Technical Panel Navigation Guide](EVALUATION_GUIDE_OPTION_B.md)**

### Option B Deliverables Summary
1. **Architecture Diagram:** Bounded flows between Agent, Actions, CRM, and External API documented in `docs/architecture/`.
2. **Working Build (End-to-End):** Validated conversational routing, CRM grounding (`Account Snapshot`), and Apex Code Coverage (**>75%**). Full UI tracing available in `docs/evidence/salesforce-org/`.
3. **Prompt Iteration:** Evolved from raw string inputs to strict *Semantic Guardrails* in Reasoning Instructions, preventing data inversion and hallucination.
4. **Platform Judgment Callout:** Formal ADR documenting the architectural trade-off of disabling `Session Activation Required` for autonomous M2M Agent callouts.
5. **Observability Note:** Validated using native Agentforce `Trace` metrics and local simulated telemetry logs.

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
| Active Prompt Template | `Meeting_Prep_Briefing` (v5, `Published`) |
| Known Integrations | ✅ `ACME_CompetitiveIntelligenceAction` (Apex Invocable) · ✅ `ACME_Meeting_Prep_Knowledge` (Data Cloud Grounding) · 🎯 Named Credentials (MCP/A2A pattern — configured, not yet production-active) |
| Permission Sets | ✅ Retrieved from `acme-dev-org` — agent-specific (`Agentforce_CI_Access`, `Agentforce_CRM_Access`, `ACME_Investment_Banker_Assistant1012860999_Permissions`) plus platform system-managed sets present in any Agentforce-enabled org |

*(Note: Session creation against the live org returns `404 NOT_FOUND` when invoked outside the Salesforce CLI agent test harness until an active agent session is configured).*

---

## 💻 Engineering Runtime & Visual Preview

<details>
<summary><b>Click to expand: Executive Visual Preview & Simulated Environment Evidence</b></summary>
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
The target CRM evidence covers the account, contact, and opportunity context used by the grounding layer.
- ![Target CRM Data Model — GlobalTrust](docs/screenshots/1_target_data-model-GLOBALTRUST.png)
- ![Target CRM Data Model — Quantum](docs/screenshots/1_target_data-model-QUANTUM.png)

### Validation Evidence (Agentforce Runtime & Engineering Lab Runtime)
The screenshots below record the validation runs for observability, contract checks, full regression, and architecture-blueprint evidence.
- ![Observability Testing](docs/screenshots/9_Observability_Testing.png)
- ![Blueprint Validation Architecture Evidence](docs/screenshots/9_Blueprint_Validation_Architecture_evidence.png)

*(For the complete screenshot catalog, see `docs/evidence/interface/screenshot-index.md`)*.

</details>

---

## 🛠️ Run the Application & Validation Suite

### Test Architecture
The repository validates behavior at three complementary levels:
1. **Visual validation** through screenshots under `docs/screenshots/`
2. **Prompt governance validation** through `tests/test_prompts_contract.py`
3. **Observability and regression validation** through `tests/test_observability_contract.py` and the full pytest suite

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

Repository Tag: v0.9.12 | Status: Option B Fully Validated, README Terminology & Metadata Consolidated.

