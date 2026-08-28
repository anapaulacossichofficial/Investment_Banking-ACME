```markdown
# Platform Limitations and Scope Boundaries

## Purpose

This document records known boundaries of the proposed DMO-backed hybrid
retrieval architecture and of the current Engineering Lab Runtime.

The documented boundaries prevent overclaiming and provide clear delivery
guidance for the Salesforce implementation.

## Current Limitations

- Data Cloud ingestion, DMO mapping, and Search Index updates can be
  asynchronous. The Engineering Lab Runtime does not simulate data freshness,
  indexing delay, or eventual-consistency behavior.
- Automated recovery from ingestion, mapping, indexing, metadata filtering, or
  retrieval failures is not implemented in the current build.
- The Engineering Lab Runtime validates the hybrid retrieval contract with local
  structured fixtures and approved local documents. The native live DMO-backed
  Data Cloud retrieval is handled separately within the ACME Dev Org on Agentforce.
- The target DMO-backed retriever requires Data Cloud readiness, approved
  document ingestion, mapping, indexing, permissions, and metadata design.
- Account and contact metadata filtering is an explicit target requirement.
  The Engineering Lab Runtime validates scope lock using fixtures, but does not
  prove Salesforce permission enforcement or live Data Cloud filters natively.
- Standard Salesforce citations can resolve to a root Account or record context
  instead of the supporting file, depending on configured retrieval and
  citation behavior.
- Document titles, file identifiers, chunk identifiers, and deep links may not
  be propagated into every Prompt Builder runtime result. Plain-text source
  attribution is emitted only when supported by retrieved evidence.
- Live market data, news, external document repositories, production document
  lifecycle events, and live record updates are outside the current scope.
- The agent prepares a grounded meeting briefing and competitive benchmarking
  analysis only. It does not make commercial, investment, credit, suitability,
  legal, compliance, or transaction decisions.
- Local observability proves event contracts and controlled test behavior. It
  does not replace Salesforce production monitoring, audit operations,
  alerting, incident management, or enterprise security controls.
- MCP and A2A are governed architectural interoperability patterns. While
  scaffolding for External/Named Credentials exists in the ACME Dev Org on
  Agentforce, live external agent-to-agent mesh integration is outside the
  current scope.

## Delivery Position

The **Engineering Lab Runtime** serves as the reliable engineering evidence base
for validating the proposed architecture's logic, contracts, and fallback behaviors.

This baseline has now been successfully transitioned into the **ACME Dev Org on
Agentforce**. The active cloud deployment demonstrates the complete Option B
Meeting Prep runtime path, utilizing native Agentforce routing, Prompt Builder,
live CRM context grounding, semantic guardrails, and secure M2M callout actions.

```
