> **Historical snapshot (v0.7.1):** This file is preserved as engineering record and does not reflect the current architecture. For the live, authoritative version, see [`docs/architecture/README.md`](../../architecture/README.md).

---

cat << 'EOF' > docs/architecture/solution-blueprint.md
# Enterprise Solution Blueprint: Agentforce Investment Banking

## 1. Executive Summary

This blueprint defines the target architecture for the ACME Investment Banking Meeting Prep capability and maps the current local working build to the target Salesforce runtime.

The current ACME local application is the **Demo Runtime**: it validates capability logic, retrieval patterns, fallback behavior, approved-source usage, testability, and engineering governance in a controlled environment. The target enterprise implementation is the **Salesforce Target Runtime**: a native Agentforce-based capability using Prompt Builder, CRM context, grounded retrieval, and platform trust controls.

This positioning is intentional:
- the **business capability demonstrated** is Meeting Prep;
- the **target runtime for panel defense** is Salesforce;
- the **local laboratory** is the engineering environment used to validate contracts, prompts, fallback, source attribution, and regression before or alongside platform implementation.

---

## 2. Capability in Scope

### Primary capability
**Knowledge-Grounded Meeting Prep Agent**

Purpose:
- prepare an executive briefing before a banker meeting;
- combine structured relationship context with approved knowledge sources;
- produce a concise, grounded, executive-ready briefing;
- reduce hallucination risk through scoped retrieval, controlled prompting, fallback behavior, and source-aware outputs.

### Capability outcome
The user receives a grounded meeting-preparation briefing that may include:
- client and relationship context;
- opportunity and pipeline context;
- recent activity or meeting context;
- knowledge-grounded market or account-relevant background;
- suggested talking points, risks, and follow-up angles.

---

## 3. Runtime Mapping

| Demo Runtime (Local ACME Build) | Salesforce Target Runtime | Architectural Role |
|---|---|---|
| Local supervisor / orchestration logic | Agentforce Meeting Prep Agent | Intent handling, orchestration, capability execution |
| Meeting Prep capability implementation | Meeting Preparation topic and action(s) | Business capability for meeting briefing generation |
| Local prompt and policy logic | Prompt Builder prompt template(s) | Prompt composition, instruction control, grounded response generation |
| CRM-oriented retrievers and local relationship context | Salesforce record context, actions, Flow/Apex-backed retrieval | Structured customer and pipeline context |
| Local knowledge retrieval pattern | Knowledge / Data Library / Data Cloud retrieval pattern, subject to org capability | Unstructured grounding for account and meeting context |
| Local fallback and approved-source behavior | Agent configuration, prompt rules, retrieval scoping, and platform controls | Guardrails, controlled behavior, trust-oriented output shaping |
| Local observability and tests | Salesforce-side traces/logging plus local engineering validation evidence | Traceability, QA, reproducibility, and risk reduction |

This mapping is deliberately **role-based**, not a claim that every local object has a 1:1 managed Salesforce component.

---

## 4. Architectural Layers

### A. Demo Runtime
This is the current local ACME working build.

Purpose:
- validate the capability pattern quickly and repeatedly;
- test prompt behavior before wider rollout;
- prove grounded retrieval behavior;
- validate fallback and no-evidence behavior;
- maintain regression safety across iterations;
- support engineering rigor through fixtures, contracts, and automated tests.

What it proves:
- the Meeting Prep pattern is implementable;
- retrieval and synthesis behavior can be tested;
- output structure and fallback can be stabilized;
- supporting capabilities can reuse shared governance patterns.

### B. Salesforce Target Runtime
This is the runtime that should be demonstrated to the panel.

Core target components:
- **Agentforce Meeting Prep Agent**
- **Meeting Preparation topic**
- **Prompt Builder template**
- **CRM record context and retrieval**
- **Knowledge-grounded retrieval pattern**
- **Einstein Trust Layer**
- **Grounded executive briefing output**

What it proves:
- the capability can run natively in Salesforce;
- the banker can invoke the capability from the enterprise workflow context;
- prompts, retrieval, and output can be governed inside the target platform;
- the design is aligned to Salesforce-native operating patterns.

### C. Enterprise Interoperability
The target architecture supports governed integration with enterprise systems
and external agent capabilities through approved Salesforce actions, APIs and
enterprise integration controls.

The current working build demonstrates the Meeting Prep capability end to end.
The Demo Runtime validates reusable contracts for routing, retrieval, fallback,
policy enforcement and traceability. Expansion to additional ACME capabilities
will reuse this pattern, subject to enterprise security, identity, API and
operating-model decisions.

MCP and A2A are architectural interoperability patterns under evaluation where
they fit the approved enterprise integration model. They are not presented as
implemented platform features in the current working build.

## 5. Einstein Trust Layer Positioning

The Einstein Trust Layer is part of the target Salesforce architecture and should be represented as a **cross-cutting trust and governance layer**, not as the central orchestrator.

In this solution, it is positioned as the platform trust layer associated with generative execution and enterprise-safe output handling, including areas such as:
- privacy-sensitive handling of enterprise data;
- policy-aligned generative execution;
- safe prompt-response processing;
- trustworthy output controls within the Salesforce runtime.

Important clarification:
- **Agentforce / agent runtime** handles orchestration and capability execution;
- **Prompt Builder** handles prompt template management and generative instruction structure;
- **retrieval components** supply structured and unstructured grounding;
- **Einstein Trust Layer** supports trustworthy generative operation as a platform trust control.

This distinction is essential for panel defense.

---

## 6. Retrieval Strategy

### Structured context
Structured retrieval should come from Salesforce business context such as:
- account;
- contact;
- opportunity;
- related activity or meeting records;
- relationship context available in the record scope.

### Unstructured context
Unstructured grounding should come from the enterprise-approved knowledge source available in the target org, such as:
- Knowledge;
- Data Library;
- Data Cloud-connected retrieval pattern;
- other approved repository pattern available in the environment.

### Practical recommendation
For the panel and the MVP:
- start with the **minimum grounded path that actually works in the org**;
- prioritize **record-context + prompt template + action** first;
- add broader knowledge grounding only if the org capability is available and testable in time.

This avoids overcommitting to a retrieval pattern that the current developer org may not support.

---

## 7. Guardrails and Fallback

The solution must emphasize controlled behavior over breadth.

### Guardrail principles
- use only approved context for briefing generation;
- keep the output scoped to the current relationship and meeting purpose;
- do not imply unsupported facts;
- prefer clarification or no-evidence fallback when context is insufficient;
- preserve separation between structured CRM facts and inferred recommendations.

### Fallback behavior
If evidence is missing, weak, or ambiguous, the capability should prefer one of the following:
- state that supporting evidence is unavailable;
- request clarification;
- constrain the answer to the verified CRM context;
- avoid fabricated market or relationship claims.

This is consistent with the engineering patterns already reinforced in the local demo runtime.

---

## 8. Observability and Validation

The local environment already demonstrates the value of engineering validation through schema alignment, retrieval testing, fixture-based checks, and UI/runtime stabilization. The project history shows concrete examples of aligning retriever behavior, institution naming, and page logic to the actual data contract rather than invented interfaces.

In the target operating model, observability should cover:
- prompt and action execution visibility;
- retrieval traceability;
- fallback visibility;
- source-aware behavior validation;
- reproducibility of major prompt and configuration changes.

For the panel, the observability point should be framed as:
- **local lab = engineering validation and regression discipline**;
- **Salesforce runtime = business-facing capability execution**.

---

## 9. Reusable Pattern for Scale

The panel may ask how this scales beyond a single capability.

The answer is:
- not by duplicating ad hoc prompts and agents;
- but by reusing a shared pattern for retrieval, prompt governance, fallback, source attribution, and observability.

Reusable pattern components:
- standard prompt template structure;
- approved source metadata contract;
- scoped retrieval contract;
- shared fallback policy;
- reusable evaluation and regression suite;
- consistent trace/event schema;
- governed action catalog;
- versioning and release discipline.

This is how the architecture supports expansion to multiple capabilities without presenting uncontrolled sprawl.

---

## 10. What Is Implemented vs Supported

### Implemented in the current local environment
- local ACME working build;
- tested retrieval patterns;
- source-aware competitive and contextual evidence handling;
- local engineering validation patterns;
- UI and workflow demonstrations in the controlled demo environment.

### Must be implemented or demonstrated in the Salesforce target runtime
- a minimum viable Meeting Prep capability in the developer org;
- prompt template in Prompt Builder;
- topic/action or equivalent native runtime path;
- CRM-context-driven briefing execution;
- business-facing demonstration in Salesforce.

### Architecturally supported but not required as fully implemented today
- broader enterprise interoperability;
- expansion to multiple specialized capabilities;
- governed integrations with enterprise systems and additional agent endpoints.

---

## 11. Panel Positioning Statement

Recommended positioning statement:

> We built the Meeting Prep capability as a reusable, grounded pattern.  
> The Salesforce runtime is the target business runtime for demonstration and enterprise operation.  
> The local ACME environment is the engineering runtime used to validate prompts, retrieval behavior, fallback rules, source attribution, and regression safety.  
> The same pattern is designed to expand into a governed enterprise capability layer without confusing architectural support with functionality already implemented today.

---

## 12. Now / Target / Enterprise Summary Table

| Layer | What it is | What we show now |
|---|---|---|
| **Demo Runtime** | Local ACME engineering runtime for validation, tests, retrieval behavior, fallback, and regression safety | Local working build and engineering discipline |
| **Salesforce Target Runtime** | Native business runtime for Meeting Prep in Salesforce using Agentforce, Prompt Builder, CRM context, grounded retrieval, and Trust Layer | The minimum viable Meeting Prep capability in the developer org |
| **Enterprise Interoperability Layer** | Governed expansion path for additional capabilities, enterprise systems, and broader integration patterns | Architectural support and scale narrative, not necessarily full implementation today |
EOF