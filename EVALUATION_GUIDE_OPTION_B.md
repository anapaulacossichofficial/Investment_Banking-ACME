# 🧭 Option B: Technical Panel Navigation Guide

Welcome. If you are reviewing this repository for the **Partner Technical Architect (Agentforce)** panel, this guide maps the exact locations of the 5 requested deliverables within the codebase. 

Because this repository also contains a full Engineering Lab Runtime test-harness (Python/Pytest), this map ensures you can bypass the lab simulation and jump straight into the **ACME Dev Org on Agentforce** evidence.

| Option B Deliverable | Where to find it in this Repository |
| :--- | :--- |
| **1. Architecture Diagram** | 📂 `docs/architecture/`<br>*(Contains the HLD and Functional Diagrams mapping the Agent → Actions → External API flow).* |
| **2. Working Build (End-to-End)** | 📂 `docs/evidence/salesforce-org/`<br>*(Contains the >75% Apex Code Coverage log and the `7_AgentforceE2E_*.png` tracing screenshots proving CRM grounding and routing).* |
| **3. Prompt Templates & Iteration** | 📂 `docs/evidence/front3_prompt_contracts.log`<br>*(Documents the evolution from parsing brittle String IDs to robust `Account Snapshot` SObjects, including strict Semantic Guardrails).* |
| **4. Platform Judgment Callout** | 📄 `docs/architecture/ADR-001-platform-constraints-m2m.md`<br>*(Documents the critical trade-off regarding M2M Callouts and Session Activation limitations).* |
| **5. Observability Note** | 📄 `docs/evidence/test_observability.log` & `docs/evidence/salesforce-org/`<br>*(Showcases how Agentforce native Trace metrics were used alongside Execute Anonymous Apex to debug the payload).* |

### Notes on the Architecture
The Salesforce source code for **ACME Dev Org on Agentforce** — Apex Actions, Bots, the published `Meeting_Prep_Briefing` Prompt Template, External Credentials, and Named Credentials — is located in `acme-agentforce/force-app/main/default/`. Permission Sets retrieved directly from the dev org — including agent-specific access (`Agentforce_CI_Access`, `Agentforce_CRM_Access`, `ACME_Investment_Banker_Assistant1012860999_Permissions`) — are tracked in `force-app/main/default/permissionsets/`. The solution is fully deployable to any scratch or dev org, though Data Cloud ingestion, Search Index activation, and Agent Script publication remain separate manual lifecycle steps (see `docs/architecture/platform-limitations.md`).