## Validation Status

The current validation package includes:

- Executive briefing UI evidence.
- CRM and knowledge grounding evidence.
- Citation and source tracing evidence.
- Competitive intelligence routing evidence.
- Missing-account and missing-knowledge fallback evidence.
- Adversarial prompt rejection evidence.
- Prompt governance contract validation.
- Observability KPI contract validation.
- Full regression and JUnit XML evidence.

Current automated baseline:

```text
Prompt contract tests: 3 passed
Observability contract tests: 8 passed
Full regression suite: 31 passed
Failures: 0
```

Visual evidence is stored under `docs/screenshots/`, and automated evidence is
stored under `docs/evidence/`.

## Enterprise Visual Preview

The application includes an executive banking interface designed for
institutional coverage workflows, grounded meeting preparation, and
competitive intelligence analysis.

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


## Run the Validation Suite
> To run the full validation package and regenerate the evidence logs, use the
> commands below.

> Note: `chmod +x` and `./scripts/run_validation_suite.sh` must be run in the
> terminal, not inside the script file itself.

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

### Test Execution Complete - Demo presentation

```bash
bash -n scripts/run_validation_suite.sh
chmod +x scripts/run_validation_suite.sh
./scripts/run_validation_suite.sh
ls -lh docs/evidence/
tail -n 20 docs/evidence/test_full_suite.log
```