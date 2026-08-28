# 🚀 ACME Investment Banker Assistant & Agentforce Blueprint

A hybrid enterprise architecture combining a local engineering runtime and a **Salesforce Agentforce target deployment** validated against the Option B architectural deliverables.

---

## 🏆 Option B Deliverables (Agentforce Target Build)

This repository serves as the definitive artifact for the Agentforce Option B Technical Panel (Release `v0.9.6`). The target Agentforce build is fully validated for autonomous routing, CRM grounding, and secure M2M callouts.

| Option B Deliverable | Implementation Evidence (Repo Location) | Status |
| :--- | :--- | :--- |
| **1. Architecture Diagram** | [View System Diagrams & Interoperability Design](docs/architecture/) | **PASS** |
| **2. Working Build (E2E)** | [View Apex Test Coverage (>75%) & E2E Trace Logs](docs/evidence/salesforce-org/) | **PASS** |
| **3. Prompt Iterations** | [View Semantic Guardrails & Prompt Contracts](docs/evidence/front3_prompt_contracts.log) | **PASS** |
| **4. Platform Judgment** | Trade-off: Disabled *Session Activation Required* for autonomous Agent callouts. | **PASS** |
| **5. Observability Note** | Traced payload routing via native Agentforce Trace metrics. | **PASS** |

### 🛠️ Quick Start (Agentforce Deployment)
Deploy the validated actions, security policies, and AI metadata to your Dev Org:
\`\`\`bash
sf project deploy start --source-dir acme-agentforce/force-app/main/default/ --target-org acme-dev-org
\`\`\`
*(For instructions on spinning up the external benchmarking backend, see the Architecture section).*

---

## 🏛️ Hybrid Architecture Overview

This project implements a disaggregated serving model, bridging Salesforce's conversational AI capabilities with a Python-based Intelligence Backend.

| Diagram | Purpose |
|---|---|
| [Solution HLD](docs/architecture/3_ACME_Investment_Bank_HLD_Architecture.png) | High-level design: Agentforce Supervisor, CRM retrieval, and Trust Layer. |
| [Functional Diagram](docs/architecture/2_acme-optionB-functionaldiagram.png) | Knowledge-grounded Meeting Prep pattern aligned to Salesforce standards. |

<p align="center">
  <img src="docs/architecture/2_acme-optionB-functionaldiagram.png" alt="Functional Diagram — Option B" width="800">
</p>

---

## 📂 Engineering Runtime & Local Validation (Streamlit)

<details>
<summary><b>Click to expand: Executive Visual Preview & Simulated Environment Evidence</b></summary>
<br>

The ACME working build demonstrates deterministic engineering aligned with enterprise coverage workflows, validated locally via Streamlit before cloud deployment.

### Executive Briefing & Competitive Intelligence
The application provides an executive banking interface for institutional coverage workflows, grounded meeting preparation, and competitive intelligence analysis.

- **Main Intelligence Hub:** `docs/screenshots/1_home-dashboard.png`
- **Executive Briefing:** `docs/screenshots/2_executive-briefing.png`
- **Peer Benchmarking:** `docs/screenshots/3_executive-briefing_peer-benchmarking.png`

### CRM Data Model and Account Context
The target CRM evidence covers the account, contact, and opportunity context used by the grounding layer.

![Target CRM Data Model — GlobalTrust](docs/screenshots/1_target_data-model-GLOBALTRUST.png)
![Target CRM Data Model — Quantum](docs/screenshots/1_target_data-model-QUANTUM.png)

### Citations and Fallback Validation
- **CRM Citations:** `docs/screenshots/6_Citations_Activities.png`
- **Fallback (Missing Account):** `docs/screenshots/7_fallback-orion_missing-account.png`
- **Adversarial Prompt Rejection:** `docs/screenshots/8_Hallucination_adversarial-prompt.png`

### Test Architecture
The repository validates behavior at three complementary levels:
1. **Visual validation** through screenshots under `docs/screenshots/`
2. **Prompt governance validation** through `tests/test_prompts_contract.py`
3. **Observability and regression validation** through `tests/test_observability_contract.py`

Run the validation suite locally:
\`\`\`bash
chmod +x scripts/run_validation_suite.sh
./scripts/run_validation_suite.sh
\`\`\`
Generated evidence includes `test-results.xml`, `test_full_suite.log`, and `front3_prompt_contracts.log`.

### Observability Scope
The local observability layer simulates Agentforce Session Tracing concepts, tracking KPIs like Grounded Answer Rate, Citation Coverage, and Fallback Rate.

</details>

---

## 🌐 Agentforce Dev Org — Active Environment

This repository is tightly coupled with a Salesforce Agentforce Developer Edition Org to validate native AI orchestration.

| Item | Value |
|---|---|
| Target Org Alias | `acme-dev-org` |
| Agent | `ACME_Investment_Banker_Assistant` |
| Active Prompt Template | `Meeting_Prep_Briefing` (Published) |
| Known Integrations | Apex Invocables (`ACME_CompetitiveIntelligenceAction`), Data Cloud Grounding, Named Credentials (MCP/A2A patterns) |

*(Note: Session creation against the live org returns `404 NOT_FOUND` when invoked outside the Salesforce CLI agent test harness until an active agent session is configured).*