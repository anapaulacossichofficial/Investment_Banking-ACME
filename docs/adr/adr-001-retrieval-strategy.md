# ADR-001 — Retrieval Strategy for Meeting Prep Agent

## Status
Proposed

## Context
Option B requires the Meeting Prep Agent to answer banker-facing meeting preparation questions using grounded evidence from:
- structured CRM data;
- unstructured knowledge sources such as relationship notes, research documents, and pitch materials.

The solution must demonstrate:
- correct account and contact scoping;
- blending of structured and unstructured evidence;
- source attribution and citations;
- safe fallback behavior when evidence is insufficient;
- a credible path from local demo implementation to enterprise target architecture.

Two retrieval approaches are evaluated:
1. a controlled grounding layer optimized for local demo stability;
2. a DMO-backed Data Cloud Retriever as the target enterprise retrieval architecture.

## Decision
The recommended target retrieval architecture is a DMO-backed Data Cloud Retriever.

For the local demo build, the implementation may continue to use a controlled grounding layer as a runtime-compatible execution mode, provided that:
- the architecture decision is documented explicitly;
- the retrieval contracts remain consistent with the target state;
- citations, scoping, guardrails, and fallback behavior remain enforced.

## Rationale
The DMO-backed Data Cloud Retriever is preferred as the target architecture because it provides:
- stronger support for hybrid retrieval across dense financial content;
- richer metadata filtering and scoping controls;
- better extensibility for future multi-agent reuse;
- stronger architecture judgment for enterprise investment banking scenarios.

The controlled grounding layer remains acceptable for the demo because it provides:
- lower setup complexity;
- more deterministic panel behavior;
- easier inspection of grounding and source attribution during the demo.

## Consequences
### Positive
- Aligns the solution with an enterprise-ready retrieval model.
- Preserves demo stability while documenting the intended production path.
- Makes scoping, citations, and fallback behavior easier to reason about through explicit contracts.

### Negative
- Introduces a temporary split between demo runtime mode and target architecture.
- Requires clear documentation to avoid overstating what is already implemented.
- Adds configuration and policy management overhead.

## Implementation Notes
The repository should externalize retrieval decisions into configuration and prompt files, including:
- `src/config/data_source_strategy.yaml`
- `src/config/retrieval_policy.yaml`
- `src/config/citation_policy.yaml`
- `src/config/guardrail_policy.yaml`
- `src/config/fallback_policy.yaml`
- `src/config/observability_policy.yaml`
- `src/prompts/meeting_prep_system.md`
- `src/prompts/prompt_versions.yaml`

## Review Trigger
This ADR should be reviewed when:
- the local demo is replaced by a production-integrated build;
- Data Cloud retrieval becomes available end-to-end;
- new agents need to reuse the same retrieval contracts;
- governance or observability requirements materially change.