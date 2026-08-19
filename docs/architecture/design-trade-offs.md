# Architecture Design Trade-offs

This document records the key architectural trade-offs made while building the ACME Investment Banking Meeting Prep and Competitive Intelligence agents, following the same trade-off discipline used in Salesforce Agentforce reference implementations.

Each trade-off states what was gained, what was given up, and what the migration path to full Agentforce/Data Cloud production looks like.

## 1. Streamlit local runtime vs. native Agentforce runtime

**Decision:** Validate supervisor routing, retrieval, grounding, and guardrail logic in a local Streamlit application before completing full Data Cloud provisioning.

- **Gained:** Fast, deterministic iteration on prompt contracts and fallback behavior; full pytest coverage (38+ tests) without depending on asynchronous Data Cloud ingestion cycles; no risk of breaking a shared dev org during rapid iteration.
- **Given up:** No proof that the same logic executes natively inside Agent Script, Prompt Builder, or the Einstein Trust Layer end to end; local behavior is not a substitute for Agentforce session tracing evidence.
- **Migration path:** Port the supervisor router to Agent Script topics/actions, replace the local retriever with a Data Cloud Retriever bound to DMOs, and re-validate the same test contracts against the Agentforce Employee Agent.

## 2. Local fixture CRM vs. Salesforce Data Cloud (DMOs)

**Decision:** Use fictional local CRM fixtures (Account, Contact, Opportunity, Activity) instead of provisioning full Data Cloud ingestion for the demo.

- **Gained:** Isolation for repeatable testing; no dependency on Data Cloud connector setup, Content Bundle ingestion, or Hybrid Search Index activation, which are asynchronous and org-configuration-heavy.
- **Given up:** No evidence of real Account-to-File relationship mapping, DMO-backed retrieval, or Data Cloud citation resolution — a known platform constraint even in native implementations (citations can resolve to the root Account rather than the specific File).
- **Migration path:** Map fixtures 1:1 to Account/Content Document/Content Document Version DMOs and re-run the same retrieval test suite against an Account-rooted Hybrid Search Index.

## 3. Custom Python retriever vs. Data Cloud native Retriever

**Decision:** Implement a custom scoped retriever in Python rather than the native Data Cloud Retriever/Prompt Builder combination for the demo layer.

- **Gained:** Full control over scoping logic, fallback triggers, and citation formatting during rapid prompt iteration (see prompt v1 vs. final version evolution).
- **Given up:** Native semantic search (E5 Large V2 embeddings), Retriever Playground validation, and Prompt Builder Preview — tools that give reviewers direct, tool-native evidence of grounding behavior.
- **Migration path:** Recreate the same Individual Retriever pattern (Account-ID filtered, document-content source) inside Data Cloud and swap the custom retriever module for the native one behind the same interface contract.

## 4. Account-scoped retrieval vs. broader cross-object search

**Decision:** Restrict all knowledge retrieval to a single confirmed Account, resolved before any downstream retrieval executes.

- **Gained:** Eliminates cross-account data bleed by design; simplifies guardrail testing and citation trust.
- **Given up:** Cannot answer independent queries that start from a Contact, Opportunity, or Task without first resolving an Account — a deliberate scope limitation, not an oversight.

## 5. Second capability (Competitive Intelligence) vs. single-capability depth

**Decision:** Build a second capability (Competitive Intelligence Agent) in addition to Meeting Prep, rather than concentrating all effort on deepening a single capability.

- **Gained:** Demonstrates the bonus "second capability" deliverable and validates that the supervisor routing pattern generalizes beyond one workflow.
- **Given up:** Less depth of native Agentforce evidence (Apex tests, Code Analyzer runs, Session Tracing) per capability compared to a single-capability implementation with full native stack depth.

## Summary

The trade-offs above consistently favor **fast, testable validation of behavior and contracts** over **native platform proof** at this stage. The explicit migration path for each trade-off is intended to close that gap without discarding the validated logic.

## Related Documentation

- [Solution Blueprint](solution-blueprint.md) — full architecture narrative these trade-offs support.
- [Option B Functional Diagram](2_acme-optionB-functionaldiagram.png) — visual pattern reflecting the retrieval and grounding trade-offs above.
- [Trade-offs Diagram](2_acme-agentforce-pattern_Tradeoffs.png) — consolidated visual summary of this document.
- [Platform Limitations](platform-limitations.md) — related platform-level constraints referenced in Trade-off 2.
