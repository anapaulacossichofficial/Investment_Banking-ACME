# ACME Investment Banking Working Build

A local Streamlit working build for executive meeting preparation, CRM grounding, competitive intelligence workflows, and validation evidence.

## Overview

This repository demonstrates a deterministic, enterprise-aligned working build for grounded meeting prep and competitive intelligence within an investment banking coverage context.

The solution combines:
- executive meeting briefing generation;
- CRM retrieval and grounding;
- knowledge-source tracing and citations;
- Supervisor routing validation;
- fallback handling for missing data;
- competitive intelligence analysis;
- Zero-Trust prompt governance;
- simulated observability KPI contracts.

## Validation Status

The current validation package includes:
- executive briefing UI evidence;
- CRM and knowledge grounding evidence;
- citation and source tracing evidence;
- competitive intelligence routing evidence;
- missing-account and missing-knowledge fallback evidence;
- adversarial prompt rejection evidence;
- prompt governance contract validation;
- observability KPI contract validation;
- full regression and JUnit XML evidence.

Current automated baseline:

```text
Prompt contract tests: 3 passed
Observability contract tests: 8 passed
Full regression suite: 31 passed
Failures: 0
```
Visual evidence is stored under `docs/screenshots/`, and automated evidence is stored under `docs/evidence/`.

## Enterprise Visual Preview

The application includes an executive banking interface designed for institutional coverage workflows, grounded meeting preparation, and competitive intelligence analysis.

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

## Test Architecture

The repository validates behavior at three complementary levels:
- visual validation, through screenshots under `docs/screenshots/`;
- prompt governance validation, through `tests/test_prompts_contract.py`;
- observability and regression validation, through `tests/test_observability_contract.py` and the full pytest suite.

Generated evidence includes:

```text
docs/evidence/test_prompts_contract.log
docs/evidence/test_observability_contract.log
docs/evidence/test_full_suite.log
docs/evidence/test-results.xml
docs/evidence/test_performance_all.log
```

## Validation Commands

To regenerate the evidence package, run the following commands in order.

### 1. Validate the script syntax

```bash
bash -n scripts/run_validation_suite.sh
```

### 2. Make the script executable

```bash
chmod +x scripts/run_validation_suite.sh
```

### 3. Run the full validation suite

```bash
./scripts/run_validation_suite.sh
```

This script executes:

- prompt contract tests;
- observability contract tests;
- the full regression suite;
- JUnit XML generation;
- performance logging.

### 4. Verify generated evidence

```bash
ls -lh docs/evidence/
```

Expected generated artifacts:

```text
docs/evidence/test_prompts_contract.log
docs/evidence/test_observability_contract.log
docs/evidence/test_full_suite.log
docs/evidence/test-results.xml
docs/evidence/test_performance_all.log
```

### 5. Review the latest results

```bash
tail -n 20 docs/evidence/test_prompts_contract.log
tail -n 20 docs/evidence/test_observability_contract.log
tail -n 20 docs/evidence/test_full_suite.log
tail -n 20 docs/evidence/test_performance_all.log
```

## Observability Scope

The observability layer in this repository is a local simulation aligned with Agentforce Session Tracing concepts.

It validates deterministic KPI behavior for:

- Grounded Answer Rate;
- Fallback Rate;
- Citation Coverage;
- Session latency;
- Supervisor route traceability;
- guardrail event traceability.

This repository does not claim to expose live Salesforce production telemetry. It demonstrates the local measurement contract and its intended mapping to future enterprise observability integration.

## Repository Evidence

Primary evidence and validation files:

```text
docs/evidence/interface/evidence-note.md
docs/evidence/interface/screenshot-index.md
docs/evidence/interface/validation-log.md
docs/front-1-validation-matrix.md
docs/TESTING.md
scripts/run_validation_suite.sh
```


### Demo Verification Commands

Use the commands below during a live walkthrough or presentation:
```bash
bash -n scripts/run_validation_suite.sh
chmod +x scripts/run_validation_suite.sh
./scripts/run_validation_suite.sh
ls -lh docs/evidence/
tail -n 20 docs/evidence/test_full_suite.log
```
