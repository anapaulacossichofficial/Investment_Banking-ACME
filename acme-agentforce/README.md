# Salesforce Metadata Scaffold — Advanced Implementation

This directory contains the more advanced, independently maintained
Salesforce Agentforce implementation, with completed Apex classes,
`externalCredentials/`, `namedCredentials/`, and the published
`Meeting_Prep_Briefing` Prompt Template (v5).

## Status

This directory holds **real, committed Salesforce metadata** validated
against the `acme-dev-org` Developer Edition org. It is the canonical,
tested implementation referenced from the root README's "ACME Dev Org
on Agentforce" section.

## Relationship to `force-app/`

The original scaffold — kept for historical reference of the migration
path described in `docs/adr/adr-001-retrieval-strategy.md` — lives in
[`force-app/`](../force-app/main/default/). That directory holds the 10
Permission Sets retrieved directly from `acme-dev-org` via
`sf project retrieve start --metadata PermissionSet` (agent-specific sets
plus platform system-managed sets present in any Agentforce-enabled org).

## What is included in this directory

- [`force-app/main/default/classes/`](force-app/main/default/classes/) — completed Apex classes, including
  `ACME_CompetitiveIntelligenceAction` (Apex Invocable).
- [`force-app/main/default/genAiPromptTemplates/`](force-app/main/default/genAiPromptTemplates/) — the published
  `Meeting_Prep_Briefing` Flex Prompt Template (v5).
- [`force-app/main/default/externalCredentials/`](force-app/main/default/externalCredentials/) and
  [`force-app/main/default/namedCredentials/`](force-app/main/default/namedCredentials/) —
  credential metadata supporting the MCP/A2A integration pattern.
- [`force-app/main/default/permissionsets/`](force-app/main/default/permissionsets/) — a single manually authored
  set, `ACME_Agentforce_Integration_User.permissionset-meta.xml`, granting
  the agent's integration user Apex class access and read-only
  Account/Contact/Opportunity access. This set was **hand-written**, not
  retrieved from the org. The 10 sets retrieved directly from `acme-dev-org`
  are a separate collection, tracked at the repository root in
  [`force-app/main/default/permissionsets/`](../force-app/main/default/permissionsets/)
  (see "Relationship to `force-app/`" above).

## What is NOT included yet

- Agent Script / Agentforce Agent Builder authoring bundle.
- Data Cloud DMOs, Account-to-File relationships, and Hybrid Search Index
  configuration (these require org-level provisioning and cannot be fully
  captured as deployable metadata alone).
- Apex unit tests and Code Analyzer validation beyond current coverage.

## Prerequisites

- **Salesforce CLI** — Download from [developer.salesforce.com/tools/salesforcecli](https://developer.salesforce.com/tools/salesforcecli).
- **A development org** — sign up for a free Developer Edition org [here](https://developer.salesforce.com/signup).

## Common Salesforce CLI Commands

- `sf org login web`: Authorize an org
- `sf project deploy start`: Deploy metadata to your org
- `sf project retrieve start`: Retrieve metadata from your org

## Deployment

```bash
sf org login web --alias acme-dev-org
sf project deploy start --source-dir acme-agentforce/force-app --target-org acme-dev-org
```

Deploying this metadata alone does not reproduce the complete runtime.
Data Cloud ingestion, Search Index activation, and Agent Script
publication/activation are separate lifecycle steps, consistent with the
platform limitations already documented in
+[`docs/architecture/platform-limitations.md`](../docs/architecture/platform-limitations.md).
