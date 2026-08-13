# Platform Limitations and Scope Boundaries

## Purpose

This document records known boundaries of the proposed DMO-backed hybrid
retrieval architecture and of the current Demo Runtime.

The documented boundaries prevent overclaiming and provide clear delivery
guidance for the Salesforce implementation.

## Current Limitations

- Data Cloud ingestion, DMO mapping, and Search Index updates can be
  asynchronous. The local Demo Runtime does not simulate data freshness,
  indexing delay, or eventual-consistency behavior.
- Automated recovery from ingestion, mapping, indexing, metadata filtering, or
  retrieval failures is not implemented in the current build.
- The Demo Runtime validates the hybrid retrieval contract with local structured
  fixtures and approved local documents. It does not prove live DMO-backed
  Data Cloud retrieval, Data Library behavior, or Developer Org configuration.
- The target DMO-backed retriever requires Data Cloud readiness, approved
  document ingestion, mapping, indexing, permissions, and metadata design.
- Account and contact metadata filtering is an explicit target requirement.
  The local Demo Runtime validates scope lock using fixtures, but does not
  prove Salesforce permission enforcement or live Data Cloud filters.
- Standard Salesforce citations can resolve to a root Account or record context
  instead of the supporting file, depending on configured retrieval and
  citation behavior.
- Document titles, file identifiers, chunk identifiers, and deep links may not
  be propagated into every Prompt Builder runtime result. Plain-text source
  attribution is emitted only when supported by retrieved evidence.
- Live market data, news, external document repositories, production document
  lifecycle events, and live record updates are outside the current scope.
- The agent prepares a grounded meeting briefing only. It does not make
  commercial, investment, credit, suitability, legal, compliance, or
  transaction decisions.
- Local observability proves event contracts and controlled test behavior. It
  does not replace Salesforce production monitoring, audit operations,
  alerting, incident management, or enterprise security controls.
- MCP and A2A are governed architectural interoperability patterns, not
  demonstrated live integrations in the current build.

## Delivery Position

The Demo Runtime is the reliable engineering evidence base for the proposed
architecture. The next platform milestone is a minimal Salesforce Developer Org
implementation that demonstrates a Meeting Prep runtime path, Prompt Builder,
CRM context, approved retrieval, and grounded output.
