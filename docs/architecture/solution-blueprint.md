# Enterprise Solution Blueprint: Agentforce Investment Banking

## 1. Executive Summary

This blueprint defines the proposed target architecture for the ACME Investment Banking Meeting Prep capability and maps the current local working build to the Salesforce target runtime.

The local application is the **Demo Runtime**. It validates capability logic, hybrid-retrieval contracts, approved-source usage, fallback behavior, testability, and engineering governance in a controlled environment.

The proposed enterprise implementation is the **Salesforce Target Runtime**: an Agentforce capability using Prompt Builder, Salesforce CRM context, DMO-backed Data Cloud retrieval, and Einstein Trust Layer controls.

This positioning is intentional:

- The business capability demonstrated is Meeting Prep
- The ACME Dev Org represents the ACME Investment Banking running on Agentforce Dev Working-build to validate the Meeting Prep capability
- The Demo Runtime is the engineering environment used to validate contracts, prompts, retrieval, fallback, source attribution, observability, and regression

## 2. Capability in Scope

### Primary capability

**Knowledge-Grounded Meeting Prep Agent**

The capability prepares an executive briefing before a banker meeting. It combines deterministic relationship context with approved knowledge sources and produces a concise, grounded, executive-ready briefing.

The briefing may include:

- Client and relationship context
- Opportunity and pipeline context
- Recent activity or meeting context
- Knowledge-grounded account or market background
- Suggested talking points, risks, and follow-up angles
- Citations and source-aware evidence where available

## 3. Runtime Mapping

| Demo Runtime (Local ACME Build) | Salesforce Target Runtime | Architectural Role |
|---|---|---|
| Local supervisor and orchestration logic | Agentforce Supervisor / Planner and Meeting Prep Agent | Intent handling, orchestration, capability execution |
| Meeting Prep capability implementation | Meeting Preparation topic and action(s) | Business capability for briefing generation |
| Local prompt and policy logic | Prompt Builder prompt template(s) | Prompt composition, instruction control, grounded response generation |
| Local structured fixtures and CRM retrieval | Salesforce CRM context and Data Cloud business entities | Deterministic customer, relationship, pipeline, and activity facts |
| Local approved-document retrieval | DMO-backed Data Cloud Retriever | Unstructured document grounding through semantic search and metadata filters |
| Local fallback and approved-source behavior | Agent configuration, retrieval scoping, Prompt Builder rules, and platform controls | Guardrails and controlled output shaping |
| Local observability and tests | Salesforce-side traces and logging plus local engineering validation | Traceability, QA, reproducibility, and risk reduction |

This mapping is role-based. It does not claim that every local object has a one-to-one managed Salesforce component.

## 4. Architectural Layers

### A. Demo Runtime

The Demo Runtime is the current local working build. It validates the capability pattern quickly and repeatedly, verifies scoped retrieval and fallback behavior, and provides regression protection through fixtures, contracts, and automated tests.

It implements a controlled version of the hybrid retrieval contract through:

- Local structured CRM fixtures
- Approved local knowledge documents
- Account and contact scope lock
- Source attribution rules
- Citation and fallback behavior
- Prompt and observability contracts
- Regression evidence through pytest and JUnit XML

The Demo Runtime is engineering evidence for the target architecture. It does not claim live DMO/Data Cloud ingestion, indexing, or retrieval execution.

### B. Salesforce Target Runtime

The proposed Salesforce runtime contains:

- Agentforce Supervisor / Planner
- Agentforce Meeting Prep Agent
- Meeting Preparation topic
- Agentforce actions backed by Flow or Apex where required
- Prompt Builder template(s)
- Salesforce CRM and Data Cloud business entities
- DMO-backed Data Cloud Retriever
- Einstein Trust Layer
- Grounded executive briefing with citations and fallback

The target architecture is designed for native enterprise workflow execution, governed retrieval, trustworthy generation, and scale beyond a single capability.

### C. Enterprise Interoperability

The target architecture supports governed integrations through approved Salesforce actions, APIs, and enterprise integration controls.

MCP and A2A are architectural interoperability patterns under evaluation where they fit the approved operating model. They are not presented as live platform features in the current local build.

## 5. Einstein Trust Layer Positioning

The Einstein Trust Layer is a cross-cutting trust and governance layer, not the central orchestrator.

- Agentforce handles orchestration and capability execution
- Prompt Builder manages prompt-template structure
- CRM and retrieval components supply structured and unstructured grounding
- Einstein Trust Layer supports trustworthy generative operation, including privacy-sensitive handling, policy controls, masking where configured, and auditability

## 6. Retrieval Strategy

### 6.1 Architecture Decision: DMO-Backed Hybrid Retrieval

The proposed final architecture uses a **DMO-backed Data Cloud Retriever** as the primary enterprise retrieval pattern for Investment Banking Meeting Prep.

| Evidence Type | Target Retrieval Path | Purpose |
|---|---|---|
| Structured relationship and financial facts | Salesforce CRM context and Data Cloud business entities where required | Account, contact, opportunity, activity, relationship, owner, stage, date, and financial facts |
| Unstructured relationship and market knowledge | DMO-backed Data Cloud retrieval over approved and indexed documents | Pitch decks, relationship notes, research documents, meeting notes, and internal briefs |
| Retrieval controls | Semantic search plus metadata filters | Account, contact, document type, approval status, permissions, recency, and relationship scope |
| Response generation | Agentforce topic, action(s), and Prompt Builder | Grounded executive briefing generated only from the approved Evidence Context |
| Trust and governance | Einstein Trust Layer | Privacy-sensitive handling, policy controls, masking where configured, and auditability |

The retrieval sequence is explicit:

1. Resolve account and contact scope
2. Retrieve structured CRM facts
3. Retrieve approved unstructured knowledge under the same scope where metadata is available
4. Assemble the Evidence Context
5. Validate sources and guardrails
6. Generate a cited briefing or return a safe fallback

Data Library is a valid out-of-the-box alternative for faster setup and lightweight knowledge grounding. It is not the chosen primary target pattern for metadata-rich Investment Banking retrieval.

The local Demo Runtime implements the same hybrid-retrieval contract through controlled grounding: local structured fixtures, approved local documents, scope lock, source attribution, fallback behavior, and automated regression tests.

### 6.2 Architecture Trade-offs

| Option | Strengths | Trade-offs | Decision |
|---|---|---|---|
| Data Library | Faster setup, simpler out-of-the-box knowledge grounding, suitable for lightweight text content | Less suitable as the primary pattern for metadata-rich, account/contact-scoped financial document retrieval | Alternative, not target architecture |
| Controlled grounding layer | Deterministic local behavior, low integration risk, stable citations, repeatable tests | Does not prove live Data Cloud ingestion, indexing, or metadata filtering | Demo Runtime implementation |
| DMO-backed Data Cloud Retriever | Semantic search with metadata filters, scope enforcement, document segmentation control, governance, enterprise-scale reuse | Higher ingestion, mapping, indexing, and operating complexity | Approved final architecture |

## 7. Guardrails and Fallback

The solution emphasizes controlled behavior over breadth.

- Use only approved context for briefing generation
- Keep output scoped to the resolved relationship and meeting purpose
- Do not infer unsupported facts or financial values
- Preserve separation between structured CRM facts and recommendations
- Cite knowledge-backed statements when evidence is available
- Prefer clarification, constrained output, or no-evidence fallback when context is missing, weak, or ambiguous

## 8. Observability and Validation

The Demo Runtime demonstrates engineering validation through schema alignment, retrieval testing, fixture-based checks, prompt contracts, citation coverage, fallback behavior, routing traces, guardrail traces, and regression tests.

The validated local evidence includes:

- ScopeResolver tests for known-account scope, unknown-account behavior, and cross-account boundary blocking
- Meeting Prep tests for CRM Snapshot, Evidence Context, approved knowledge-source visibility, and Validation Guardrail
- Prompt contract tests
- Observability contract tests
- Full regression output recorded in JUnit XML and evidence logs

The target operating model should provide prompt and action execution visibility, retrieval traceability, fallback visibility, source-aware validation, and reproducibility of major configuration changes.

## 9. Reusable Pattern for Scale

Scale comes from shared patterns rather than duplicated prompts and agents:

- Standard prompt-template structure
- Approved source-metadata contract
- Scoped retrieval contract
- Shared fallback policy
- Reusable evaluation and regression suite
- Consistent trace and event schema
- Governed action catalog
- Versioning and release discipline

## 10. Implementation Status

### Implemented in the current local environment

- Local ACME working build
- Controlled grounding with structured fixtures and approved documents
- Scope lock and cross-account boundary validation
- Source-aware Meeting Prep evidence handling
- Prompt, citation, fallback, and observability contracts
- Automated validation and regression tests
- Evidence outputs in `docs/evidence/`

### Proposed Salesforce target implementation

- Agentforce Meeting Prep capability
- Prompt Builder template
- Meeting topic and action path
- CRM-context-driven briefing
- DMO-backed Data Cloud Retriever
- Einstein Trust Layer controls
- Business-facing Salesforce walkthrough

### Architecturally supported but not demonstrated live today

- Data Cloud DMO ingestion, mapping, indexing, and runtime retrieval
- Data Library runtime behavior
- Broader enterprise interoperability
- Governed integrations with enterprise systems and additional agent endpoints

## 11. Engineering Lab and Agentforce runtime Statement

> We built Meeting Prep as a reusable, grounded pattern. The final architecture uses DMO-backed hybrid retrieval: deterministic CRM facts plus approved, metadata-filtered document retrieval converge in an Evidence Context before response generation. The local ACME environment is the reliable engineering runtime used to validate that contract through prompts, retrieval behavior, citations, fallback rules, observability, and regression safety. Salesforce is the target business runtime for enterprise operation.

## 12. Platform Limitations

Known implementation, retrieval, citation, observability, and scope boundaries are documented in [Platform Limitations](platform-limitations.md).

## Related Trade-off Documentation

The architectural trade-offs underlying this blueprint — Streamlit local runtime vs. native Agentforce runtime, local CRM fixtures vs. Data Cloud DMOs, and second-capability breadth vs. single-capability depth — are documented in detail in [docs/architecture/design-trade-offs.md](design-trade-offs.md). See also the consolidated visual summary in [2_acme-agentforce-pattern_Tradeoffs.png](2_acme-agentforce-pattern_Tradeoffs.png) and the Option B functional pattern in [2_acme-optionB-functionaldiagram.png](2_acme-optionB-functionaldiagram.png).
