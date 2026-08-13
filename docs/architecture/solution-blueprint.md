# Enterprise Solution Blueprint: Agentforce Investment Banking

## 1. Executive Summary

This blueprint defines the proposed target architecture for the ACME Investment
Banking Meeting Prep capability and maps the current local working build to the
Salesforce target runtime.

The local application is the **Demo Runtime**. It validates capability logic,
retrieval patterns, approved-source usage, fallback behavior, testability, and
engineering governance in a controlled environment. The proposed enterprise
implementation is the **Salesforce Target Runtime**: an Agentforce capability
using Prompt Builder, CRM context, DMO-backed Data Cloud retrieval, and
platform trust controls.

This positioning is intentional:
- the business capability demonstrated is Meeting Prep;
- the target runtime for panel defense is Salesforce;
- the local laboratory is the engineering environment used to validate
  contracts, prompts, retrieval, fallback, source attribution, and regression.

## 2. Capability in Scope

### Primary capability

**Knowledge-Grounded Meeting Prep Agent**

The capability prepares an executive briefing before a banker meeting. It
combines structured relationship context with approved knowledge sources and
produces a concise, grounded, executive-ready briefing.

The briefing may include:
- client and relationship context;
- opportunity and pipeline context;
- recent activity or meeting context;
- knowledge-grounded account or market background;
- suggested talking points, risks, and follow-up angles.

## 3. Runtime Mapping

| Demo Runtime (Local ACME Build) | Salesforce Target Runtime | Architectural Role |
|---|---|---|
| Local supervisor and orchestration logic | Agentforce Supervisor / Planner and Meeting Prep Agent | Intent handling, orchestration, capability execution |
| Meeting Prep capability implementation | Meeting Preparation topic and action(s) | Business capability for briefing generation |
| Local prompt and policy logic | Prompt Builder prompt template(s) | Prompt composition, instruction control, grounded response generation |
| Local structured fixtures and CRM retrieval | Salesforce CRM context and Data Cloud business entities | Deterministic customer, relationship, pipeline, and activity facts |
| Local approved-document retrieval | DMO-backed Data Cloud Retriever | Unstructured document grounding through semantic search and metadata filters |
| Local fallback and approved-source behavior | Agent configuration, retrieval scoping, Prompt Builder rules, and platform controls | Guardrails and controlled output shaping |
| Local observability and tests | Salesforce-side traces/logging plus local engineering validation | Traceability, QA, reproducibility, and risk reduction |

This mapping is role-based. It does not claim that every local object has a
one-to-one managed Salesforce component.

## 4. Architectural Layers

### A. Demo Runtime

The Demo Runtime is the current local working build. It validates the
capability pattern quickly and repeatedly, verifies scoped retrieval and
fallback behavior, and provides regression protection through fixtures,
contracts, and automated tests.

The local runtime is the reliable engineering evidence base for the final
solution. It implements a controlled grounding version of the hybrid retrieval
contract using local structured fixtures, approved local documents, scope lock,
citation rules, fallback behavior, and observability events.

### B. Salesforce Target Runtime

The proposed Salesforce runtime contains:
- Agentforce Supervisor / Planner;
- Agentforce Meeting Prep Agent;
- Meeting Preparation topic;
- Agentforce action backed by Flow or Apex where required;
- Prompt Builder template;
- Salesforce CRM and Data Cloud business entities;
- DMO-backed Data Cloud Retriever;
- Einstein Trust Layer;
- grounded executive briefing with citations and fallback.

The target architecture is designed for native enterprise workflow execution,
governed retrieval, trustworthy generation, and scale beyond one capability.

### C. Enterprise Interoperability

The target architecture supports governed integrations through approved
Salesforce actions, APIs, and enterprise integration controls. MCP and A2A are
architectural interoperability patterns under evaluation where they fit the
approved operating model; they are not presented as live platform features in
the current local build.

## 5. Einstein Trust Layer Positioning

The Einstein Trust Layer is a cross-cutting trust and governance layer, not the
central orchestrator.

- Agentforce handles orchestration and capability execution.
- Prompt Builder manages prompt-template structure.
- CRM and retrieval components supply structured and unstructured grounding.
- Einstein Trust Layer supports trustworthy generative operation, including
  privacy-sensitive handling, policy controls, masking where configured, and
  auditability.

## 6. Retrieval Strategy

### 6.1 Architecture Decision: DMO-Backed Hybrid Retrieval

The proposed final architecture uses a **DMO-backed Data Cloud Retriever** as
the primary enterprise retrieval pattern for Investment Banking Meeting Prep.

| Evidence Type | Target Retrieval Path | Purpose |
|---|---|---|
| Structured relationship and financial facts | Salesforce CRM context and Data Cloud business entities where required | Account, contact, opportunity, activity, relationship, owner, stage, date, and financial facts |
| Unstructured relationship and market knowledge | DMO-backed Data Cloud retrieval over approved and indexed documents | Pitch decks, relationship notes, research documents, meeting notes, and internal briefs |
| Retrieval controls | Semantic search plus metadata filters | Account, contact, document type, approval status, permissions, recency, and relationship scope |
| Response generation | Agentforce topic, action(s), and Prompt Builder | Grounded executive briefing generated only from the approved evidence context |
| Trust and governance | Einstein Trust Layer | Privacy-sensitive handling, policy controls, masking where configured, and auditability |

The retrieval sequence is explicit:
1. Resolve account and contact scope.
2. Retrieve structured CRM facts.
3. Retrieve approved unstructured knowledge under the same scope where metadata is available.
4. Assemble evidence context.
5. Validate sources and guardrails.
6. Generate a cited briefing or return a safe fallback.

Data Library is a valid out-of-the-box alternative for faster setup and
lightweight knowledge grounding. It is not the chosen primary target pattern
for metadata-rich Investment Banking retrieval.

The local Demo Runtime implements the same hybrid retrieval contract through a
controlled grounding layer: local structured fixtures, approved local documents,
scope lock, source attribution, fallback behavior, and automated regression
tests.

### 6.2 Architecture Trade-offs

| Option | Strengths | Trade-offs | Decision |
|---|---|---|---|
| Data Library | Faster setup, simpler out-of-the-box knowledge grounding, suitable for lightweight text content | Less suitable as the primary pattern for metadata-rich, account/contact-scoped financial document retrieval | Alternative, not target architecture |
| Controlled grounding layer | Deterministic local behavior, low integration risk, stable citations, repeatable tests | Does not prove live Data Cloud ingestion, indexing, or metadata filtering | Demo Runtime implementation |
| DMO-backed Data Cloud Retriever | Semantic search with metadata filters, scope enforcement, document segmentation control, governance, enterprise-scale reuse | Higher ingestion, mapping, indexing, and operating complexity | Approved final architecture |

## 7. Guardrails and Fallback

The solution emphasizes controlled behavior over breadth.

- Use only approved context for briefing generation.
- Keep output scoped to the resolved relationship and meeting purpose.
- Do not infer unsupported facts or financial values.
- Prefer clarification, constrained output, or no-evidence fallback when
  context is missing, weak, or ambiguous.
- Preserve separation between structured CRM facts and inferred
  recommendations.
- Cite every knowledge-backed statement when evidence is available.

## 8. Observability and Validation

The Demo Runtime demonstrates engineering validation through schema alignment,
retrieval testing, fixture-based checks, prompt contracts, fallback behavior,
citation coverage, routing traces, guardrail traces, and regression tests.

The target operating model should provide prompt/action execution visibility,
retrieval traceability, fallback visibility, source-aware behavior validation,
and reproducibility of major configuration changes.

## 9. Reusable Pattern for Scale

Scale comes from shared patterns rather than duplicated prompts and agents:

- standard prompt-template structure;
- approved source-metadata contract;
- scoped retrieval contract;
- shared fallback policy;
- reusable evaluation and regression suite;
- consistent trace and event schema;
- governed action catalog;
- versioning and release discipline.

## 10. What Is Implemented vs Supported

### Implemented in the current local environment

- local ACME working build;
- controlled grounding with structured fixtures and approved documents;
- source-aware competitive and contextual evidence handling;
- prompt, citation, fallback, and observability contracts;
- automated validation and regression tests.

### Proposed Salesforce target implementation

- Agentforce Meeting Prep capability;
- Prompt Builder template;
- meeting topic and action path;
- CRM-context-driven briefing;
- DMO-backed Data Cloud Retriever;
- Einstein Trust Layer controls;
- business-facing Salesforce walkthrough.

### Architecturally supported but not demonstrated live today

- Data Cloud DMO ingestion, mapping, indexing, and runtime retrieval;
- Data Library runtime behavior;
- broader enterprise interoperability;
- governed integrations with enterprise systems and additional agent endpoints.

## 11. Panel Positioning Statement

> We built Meeting Prep as a reusable, grounded pattern. The final architecture
> uses DMO-backed hybrid retrieval: deterministic CRM facts plus approved,
> metadata-filtered document retrieval converge in an evidence context before
> response generation. The local ACME environment is the reliable engineering
> runtime used to validate that contract through prompts, retrieval behavior,
> citations, fallback rules, observability, and regression safety. Salesforce
> is the target business runtime for enterprise operation.

## 12. Platform Limitations

Known implementation, retrieval, citation, observability, and scope boundaries
are documented in [Platform Limitations](platform-limitations.md).
