# Observability & Evaluation Note: Agentforce Meeting Prep Architecture

## 1. Executive Summary
To ensure enterprise trust, compliance, and predictable behavior for the Knowledge-Grounded Meeting Prep Agent (Option B), ACME implements a multi-layered observability framework. This framework monitors runtime latency, retrieval grounding size, citation coverage, and fallback rates across both local simulation and Salesforce Agentforce production environments.

### A. Lab ACME Build
The local Engineering Lab implements and validates the following:
- Selected capability
- Resolved account and contact
- Retrieved source identifiers
- Citation metadata
- Fallback activation
- Execution errors
- Response latency
- Routing outcome

## 2. Observability Pillars & Metrics

### A. Tracing (Execution Flow)
* **Request Tracing:** Every incoming banker request is stamped with a unique `trace_id` (UUID) to track its lifecycle across layers.
* **Agent Handoffs:** Tracks transitions from the `SupervisorAgent` to capability agents (`MeetingPrepAgent`, `CompetitiveIntelligenceAgent`).
* **Retrieval & Grounding Events:** Captures exact query payloads, filtering criteria, and chunks retrieved from structured (CRM) and unstructured (Knowledge) sources.
* **Citation Generation:** Logs the binding process between generated text claims and underlying source metadata IDs.

### B. Core KPIs & Thresholds
| Metric Name | Target Threshold | Action on Breach |
| :--- | :--- | :--- |
| **Retrieval Latency** | < 1,500ms | Log warning; trigger fallback if timeout exceeds 3s. |
| **Citation Coverage Rate** | 100% of material claims | Reject output or suppress uncited claims via citation policy. |
| **Fallback Rate** | < 20% of total requests | Flag for prompt/retrieval review if threshold is breached. |
| **Hallucination Rejection Rate** | 0 tolerance for ungrounded facts | Guardrail triggers immediate abstention response. |

### C. Primary Metrics & Diagnostic Indicators
* **Primary Metrics:** Grounded answer rate, citation coverage, unsupported claim rate, fallback rate, supervisor routing accuracy, account resolution accuracy, median and p95 latency.
* **Diagnostic Indicators:**
  * Increase in fallback rate indicates missing knowledge or retrieval failure.
  * Increase in unsupported claims indicates prompt regression or scoping issue.
  * Increase in latency indicates excessive retrieval breadth or over-orchestration.

## 3. Salesforce Target Mapping
A Salesforce implementation should monitor:
- Agent sessions
- Topic and action execution
- Retriever activity
- Citation coverage
- Fallback rate
- Unsupported claim rate
- Latency
- User corrections
- Escalations

## 4. Evaluation and Testing Hooks
* **Automated Regression (`pytest`):** Contract schemas (`tool_contract.schema.json`, `handoff_contract.schema.json`) and core policies are validated locally prior to environment promotion.
* **Fixture-Driven Validation:** Standardized test fixtures (`crm_accounts.json`, `relationship_notes.json`) test edge cases such as missing account scopes and cross-account isolation.

## 5. Platform Alignment (Salesforce Integration)
In the Proposed Salesforce deployment, application-level tracing is natively augmented by the **Einstein Trust Layer Audit Trail**, ensuring real-time masking metrics, toxic language rejection logs, and immutable feedback loops for administrative review.