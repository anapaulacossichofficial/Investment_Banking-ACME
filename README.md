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
| [Detailed Architecture & Salesforce Target Mapping](docs/architecture/detailed-architecture-salesforce-mapping.png) | Engineering Demo runtime detail and Agentforce working Build |

<p align="center">
  <img src="docs/architecture/solution-flow.png" alt="Solution Flow" width="900">
</p>

For the complete architecture package, see [docs/architecture/README.md](docs/architecture/README.md).

## Agentforce Dev Working Build

> **Scope:** These screenshots document the **target-state Agentforce sandbox configuration** — Prompt Builder templates, CRM Data Model, and Agent routing — as evidence of the dev working build. They complement the local Streamlit validation layer and demonstrate alignment between the local simulation contracts and the Salesforce platform target.

### Prompt Builder (Target)

The Prompt Builder screenshots capture the configured prompt templates used by the Agentforce agents for executive briefing and competitive intelligence tasks.

![Target Prompt Builder](docs/screenshots/11_target_prompt_builder.png)

### CRM Data Model (Target)

The data model screenshot shows the target Salesforce object schema — Accounts, Contacts, and Opportunities — as configured in the dev sandbox, aligned with the CRM grounding layer of the working build.

![Target CRM Data Model](docs/screenshots/12_target_data_model.png)

### Agentforce Routing Configuration (Target)

The routing screenshot captures the Agentforce supervisor routing configuration, demonstrating how inbound requests are dispatched to the correct specialist agents in the target environment.

![Target Agentforce Routing](docs/screenshots/13_target_agentforce_routing.png)

For the full interface screenshot index (SS-01 through SS-31), see [docs/evidence/interface/screenshot-index.md](docs/evidence/interface/screenshot-index.md).

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
- **Agentforce target build evidence** — Prompt Builder, CRM Data Model, and routing configuration (SS-29 to SS-31, `docs/screenshots/11_*` through `13_*`)

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
