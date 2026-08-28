# 🧭 Option B: Technical Panel Navigation Guide

Welcome. If you are reviewing this repository for the **Partner Technical Architect (Agentforce)** panel, this guide maps the exact locations of the 5 requested deliverables within the codebase. 

Because this repository also contains a full local engineering test-harness (Python/Pytest), this map ensures you can bypass the local simulation and jump straight into the **Salesforce Target Deployment** evidence.

| Option B Deliverable | Where to find it in this Repository |
| :--- | :--- |
| **1. Architecture Diagram** | 📂 `docs/architecture/`<br>*(Contains the HLD and Functional Diagrams mapping the Agent → Actions → External API flow).* |
| **2. Working Build (End-to-End)** | 📂 `docs/evidence/salesforce-org/`<br>*(Contains the >75% Apex Code Coverage log and the `7_AgentforceE2E_*.png` tracing screenshots proving CRM grounding and routing).* |
| **3. Prompt Templates & Iteration** | 📂 `docs/evidence/front3_prompt_contracts.log`<br>*(Documents the evolution from parsing brittle String IDs to robust `Account Snapshot` SObjects, including strict Semantic Guardrails).* |
| **4. Platform Judgment Callout** | 📄 `docs/architecture/ADR-001-platform-constraints-m2m.md`<br>*(Documents the critical trade-off regarding M2M Callouts and Session Activation limitations).* |
| **5. Observability Note** | 📄 `docs/evidence/test_observability.log` & `docs/evidence/salesforce-org/`<br>*(Showcases how Agentforce native Trace metrics were used alongside Execute Anonymous Apex to debug the payload).* |

### Notes on the Architecture
The Salesforce source code (Apex Actions, Bots, Permission Sets, External Credentials) is located in the `acme-agentforce/force-app/main/default/` directory. The solution is fully deployable to any scratch or dev org.