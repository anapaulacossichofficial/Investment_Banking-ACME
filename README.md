# ACME Investment Banking Working Build

A local Streamlit working build for executive meeting preparation, grounded CRM analysis, competitive intelligence workflows, and simulated observability validation.

## Overview

This repository demonstrates a deterministic working build aligned with enterprise coverage workflows.

The solution combines:

- Executive meeting briefing generation
- CRM retrieval and grounding
- Knowledge-source tracing and citations
- Competitive intelligence analysis
- Zero-Trust prompt governance
- Fallback handling for missing data
- Supervisor routing validation
- Simulated observability KPI contracts

## Executive Summary

The ACME working build demonstrates:

- Grounded executive briefing generation from local CRM fixtures and approved knowledge sources
- Account and contact scoping before downstream analysis
- Competitive intelligence, peer benchmarking, strategic insights, and meeting-preparation workflows
- Citation, source-tracing, and no-evidence fallback behavior
- Prompt, observability, regression, and JUnit-based validation evidence

## Architecture at a Glance

| Diagram | Purpose |
|---|---|
| [Solution Flow](docs/architecture/solution-flow.png) | Executive path from user interaction to evidence package |
| [High-Level Architecture](docs/architecture/high-level-architecture.png) | Functional flow across agents, CRM, knowledge grounding, and assurance |
| [Detailed Architecture & Salesforce Target Mapping](docs/architecture/detailed-architecture-salesforce-mapping.png) | Local implementation detail and target-state Salesforce / Agentforce mapping |

<p align="center">
  <img src="docs/architecture/solution-flow.png" alt="Solution Flow" width="900">
</p>

For the complete architecture package, see [docs/architecture/README.md](docs/architecture/README.md).

## Agentforce Dev Working Build

This section documents the Salesforce Agentforce configuration captured during the **14/08/2026 dev build session**. It maps the target-state Agentforce components — prompt builder, data model, and routing — to the local working build contracts validated in this repository.

> **Scope:** These screenshots represent a dev/sandbox Agentforce configuration. They are visual evidence of the intended enterprise target state, complementing the local test contracts.

### Agentforce — CRM Data Model (Target)

The target Salesforce data model maps accounts, contacts, and opportunities for QUANTUM and GlobalTrust entities:

![Target Data Model — GlobalTrust](docs/screenshots/1_target_data-model-GLOBALTRUST.png)

![Target Data Model — QUANTUM Base Object](docs/screenshots/1_target_data-model-QUANTUM.png)

![Target Data Model — QUANTUM Contacts Relationship](docs/screenshots/1_target_data-model-QUANTUM_contacts.png)

![Target Data Model — QUANTUM Opportunities Relationship](docs/screenshots/1_target_data-model-QUANTUM_opps.png)

### Agentforce — Prompt Builder (Target)

The target prompt configuration in Agentforce Builder, aligned with the Zero-Trust prompt governance contracts in `tests/test_prompts_contract.py`:

![Target Prompt Builder Configuration](docs/screenshots/1_target_prompt_builder.png)

![QUANTUM Agent Prompt Preview](docs/screenshots/1_QUANTUM_prompt_PREVIEW.png)

![Prompt Template Configuration](docs/screenshots/1_prompt_template.png)

### Agentforce — Routing Configuration (Target)

The target Agentforce supervisor routing configuration, aligned with the routing validation contracts in `tests/test_supervisor_and_meeting_prep.py`:

![Target Agentforce Routing Configuration](docs/screenshots/1_target_agentforce_routing.png)

### Agentforce — CRM Account Seeding (Target)

Salesforce account records and data seeding validated as part of the 14/08/2026 build session:

![ACME New Account Creation](docs/screenshots/1_ACME_newacc.png)

![ACME Account Record View](docs/screenshots/1_ACMEacc.png)

![Account List — CRM Data Seeding](docs/screenshots/1_AccList.png)

![GlobalTrust Peer Account Record](docs/screenshots/1_Globaltrust_peerAccount.png)

Full mapping of all Agentforce target screenshots is available in [docs/evidence/interface/screenshot-index.md](docs/evidence/interface/screenshot-index.md) (SS-20 to SS-31).

## Enterprise Visual Preview

The application provides an executive banking interface for institutional coverage workflows, grounded meeting preparation, and competitive intelligence analysis.

### Main Intelligence Hub

![ACME Banking Intelligence Hub](docs/screenshots/1_home-dashboard.png)

### Executive Briefing

![Executive Briefing](docs/screenshots/2_executive-briefing.png)

![Grounded Executive Briefing](docs/screenshots/2_executive-briefing_grounding.png)

### Competitive Intelligence

![Competitive Intelligence Briefing](docs/screenshots/3_competitive-intelligence-briefing.png)

![Peer Benchmarking](docs/screenshots/3_executive-briefing_peer-benchmarking.png)

![Strategic Insights](docs/screenshots/5_executive-briefing_strategicinsights.png)

### Citations and Source Tracing

![CRM Activities Citations](docs/screenshots/6_Citations_Activities.png)

![Grounding and Source Tracing](docs/screenshots/6_Citations_Groud&Tracing.png)

### Fallback Validation

![Fallback Orion Missing Account](docs/screenshots/7_fallback-orion_missing-account.png)

![Fallback Orion Missing Knowledge](docs/screenshots/7_fallback-orion_missing-knowledge.png)

### Hallucination Rejection

![Adversarial Prompt Rejection](docs/screenshots/8_Hallucination_adversarial-prompt.png)

## Validation Status

The validation package includes:

- Executive briefing UI evidence
- CRM and knowledge grounding evidence
- Citation and source-tracing evidence
- Competitive intelligence routing evidence
- Missing-account and missing-knowledge fallback evidence
- Adversarial prompt rejection evidence
- Prompt governance contract validation
- Observability KPI contract validation
- Full regression and JUnit XML evidence
- Agentforce target build evidence (prompt builder, data model, routing) — 14/08/2026

Visual evidence is stored under `docs/screenshots/`, and automated evidence is stored under `docs/evidence/`.

## Test Architecture

The repository validates behavior at three complementary levels:

- **Visual validation** through screenshots under `docs/screenshots/`
- **Prompt governance validation** through `tests/test_prompts_contract.py`
- **Observability and regression validation** through `tests/test_observability_contract.py` and the full pytest suite

Generated evidence includes:

```text
docs/evidence/test_prompts_contract.log
docs/evidence/test_observability_contract.log
docs/evidence/test_full_suite.log
docs/evidence/test-results.xml
docs/evidence/test_performance_all.log
```

## Run the Application

```bash
streamlit run streamlit_app.py
```

## Run the Validation Suite

Validate script syntax:

```bash
bash -n scripts/run_validation_suite.sh
```

Make the script executable:

```bash
chmod +x scripts/run_validation_suite.sh
```

Run the complete validation suite:

```bash
./scripts/run_validation_suite.sh
```

The suite executes:

- Prompt contract tests
- Observability contract tests
- Full regression suite
- JUnit XML generation
- Performance logging

Review the generated evidence:

```bash
ls -lh docs/evidence/
tail -n 20 docs/evidence/test_prompts_contract.log
tail -n 20 docs/evidence/test_observability_contract.log
tail -n 20 docs/evidence/test_full_suite.log
tail -n 20 docs/evidence/test_performance_all.log
```

## Observability Scope

The observability layer is a local simulation aligned with Agentforce Session Tracing concepts.

It validates deterministic KPI behavior for:

- Grounded Answer Rate
- Fallback Rate
- Citation Coverage
- Session latency
- Supervisor route traceability
- Guardrail event traceability

This repository does not claim to expose live Salesforce production telemetry. It demonstrates the local measurement contract and its intended mapping to a future enterprise observability integration.

## Repository References

Primary evidence and validation files:

```text
docs/architecture/README.md
docs/evidence/interface/evidence-note.md
docs/evidence/interface/screenshot-index.md
docs/evidence/interface/validation-log.md
docs/front-1-validation-matrix.md
docs/TESTING.md
scripts/run_validation_suite.sh
```

## Prompt Templates

The single source of truth for prompt templates is the `src/prompts/` directory.

Legacy prompt files are archived under `docs/templates/legacy-prompts/`.
