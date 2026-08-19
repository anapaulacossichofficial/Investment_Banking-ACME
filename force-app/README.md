# Salesforce Metadata Scaffold

This directory contains an initial SFDX metadata scaffold aligned with the
Account resolution and grounding contracts validated in the local Streamlit
working build (`src/`, `retrieval/`, `tests/`).

## Status

This is a **scaffold, not a complete deployable capability**. It exists to:

- Provide a starting point for migrating validated Python logic (supervisor
  routing, Account scoping, fallback handling) into native Apex/Agent Script.
- Make explicit which pieces still require org-level configuration.

## What is included

- `sfdx-project.json` — minimal SFDX project descriptor.
- `classes/ClientResolver.cls` — scaffold mirroring the local Account
  resolution contract.

## What is NOT included yet

- Agent Script / Agentforce Agent Builder authoring bundle.
- Flex Prompt Template metadata for grounded briefing generation.
- Data Cloud DMOs, Account-to-File relationships, and Hybrid Search Index
  configuration (these require org-level provisioning and cannot be fully
  captured as deployable metadata alone).
- Apex unit tests and Code Analyzer validation for the scaffolded class.

## Deployment

```bash
sf org login web --alias ACMEOrg
sf project deploy start --source-dir force-app --target-org ACMEOrg
```

Deploying this metadata alone does not reproduce the complete runtime.
Data Cloud ingestion, Search Index activation, and Agent Script
publication/activation are separate lifecycle steps, consistent with the
platform limitations already documented in
`docs/architecture/platform-limitations.md`.
