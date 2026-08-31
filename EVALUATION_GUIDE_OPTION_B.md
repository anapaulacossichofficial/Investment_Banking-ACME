# 🧭 Option B Navigation Guide: Knowledge-Grounded Meeting Prep Agent

Welcome. This guide maps the exact locations of the 5 deliverables for the
**Option B Scenario: Knowledge-Grounded Meeting Prep Agent**, as described
in the technical exercise brief, within this codebase.

Because this repository also contains a full Engineering Lab Runtime
(Python/Pytest), this map lets you bypass the lab simulation and jump
straight into the **ACME Dev Org on Agentforce** evidence. The structure
is intentionally kept generic so this repository can serve as a reusable
reference artifact for similar knowledge-grounding agent use cases beyond
this specific scenario.

| Option B Deliverable | Where to find it in this Repository |
| :--- | :--- |
| **1. Architecture Diagram** | 📂 [`docs/architecture/`](docs/architecture/)<br>*(Contains the HLD and Functional Diagrams mapping the Agent → Actions → External API flow).* |
| **2. Working Build (End-to-End)** | 📂 [`docs/evidence/salesforce-org/`](docs/evidence/salesforce-org/)<br>*(Contains the >75% Apex Code Coverage log and the `7_AgentforceE2E_*.png` tracing screenshots proving CRM grounding and routing).* |
| **3. Prompt Templates & Iteration** | 📄 [`docs/evidence/front3_prompt_contracts.log`](docs/evidence/front3_prompt_contracts.log)<br>*(Documents the evolution from parsing brittle String IDs to robust `Account Snapshot` SObjects, including strict Semantic Guardrails).* |
| **4. Platform Judgment Callout** | 📄 [`docs/architecture/ADR-001-platform-constraints-m2m.md`](docs/architecture/ADR-001-platform-constraints-m2m.md)<br>*(Documents the critical trade-off regarding M2M Callouts and Session Activation limitations).* |
| **5. Observability Note** | 📄 [`docs/evidence/test_observability.log`](docs/evidence/test_observability.log) & 📂 [`docs/evidence/salesforce-org/`](docs/evidence/salesforce-org/)<br>*(Showcases how Agentforce native Trace metrics were used alongside Execute Anonymous Apex to debug the payload).* |

### Notes on the Architecture

The Salesforce source code (Apex Actions, External/Named Credentials) is
located in the [`acme-agentforce/force-app/main/default/`](acme-agentforce/force-app/main/default/) directory.
Metadata retrieved from the dev org — including agent-specific access
(`Agentforce_CI_Access`, `Agentforce_CRM_Access`), Bots, and Prompt
Templates — are tracked in [`force-app/main/default/`](force-app/main/default/). The solution is
fully deployable to any scratch or dev org.