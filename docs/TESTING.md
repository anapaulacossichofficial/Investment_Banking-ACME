# Testing and Observability

## Purpose

This document defines the automated validation strategy for the
`ib-agent-demo`.

The test strategy covers:

- Prompt governance contracts.
- Zero-Trust and fallback guardrails.
- Observability KPI calculations.
- Citation and grounding validation.
- Session latency.
- Supervisor route traceability.
- Competitive intelligence components.
- Smoke and regression behavior.
- Test execution performance.
- Machine-readable test reporting.

All commands in this document must be executed from the repository root.

## Test Layout

```text
tests/
├── test_competitive_intelligence_agent.py
├── test_competitive_intelligence_retriever.py
├── test_crm_retriever.py
├── test_observability_contract.py
├── test_page_competitive_intelligence.py
├── test_prompts_contract.py
├── test_smoke.py
├── test_supervisor_and_meeting_prep.py
└── fixtures/
    └── observability_events.jsonl
```

## Focused Prompt Tests

Run the prompt contract tests with:

```bash
pytest tests/test_prompts_contract.py -v
```

These tests validate that:

- The `prompts/` directory exists.
- `fallback_prompt.txt` exists.
- `meeting_prep_prompt.txt` exists.
- The fallback prompt defines a safety guardrail.
- The exact fallback statement is present.
- Strict Zero-Trust constraints are present.
- CRM evidence restrictions are present.
- Mandatory citations are required.
- The required output structure is present.

Expected current result:

```text
3 passed
```

## Focused Observability Tests

Run the observability contract tests with:

```bash
pytest tests/test_observability_contract.py -v
```

These tests validate:

- The telemetry fixture exists.
- Every event contains the required schema.
- Grounded Answer Rate is calculable.
- Fallback Rate is calculable.
- Citation Coverage is calculable.
- Session latency is calculable.
- Supervisor routes are traceable.
- Guardrail events are traceable.

Expected current result:

```text
8 passed
```

## Full Regression Suite

Run the complete test suite with:

```bash
pytest -v
```

Expected current result:

```text
31 passed
0 failed
```

The full suite covers prompt contracts, observability contracts, retrievers,
agents, routing, competitive intelligence, page imports, and smoke behavior.

## Automated Test Execution

Run the full suite with verbose output, duration profiling, JUnit XML report
generation, and a preserved textual log:

```bash
pytest -v \
  --durations=10 \
  --durations-min=0.1 \
  --junitxml=docs/evidence/test-results.xml \
  | tee docs/evidence/test_full_suite.log
```

The command produces:

- Full verbose test output.
- The ten slowest test executions taking at least 0.1 seconds.
- A machine-readable JUnit XML report.
- A preserved textual execution log.
- A complete pass/fail summary.

Pytest supports `--durations` for identifying slow test executions and
`--junitxml` for producing reports consumable by CI and test-reporting
systems. [web:1930][web:2301]

## Inspecting All Test Durations

To inspect every collected test duration:

```bash
pytest -v \
  --durations=0 \
  | tee docs/evidence/test_performance_all.log
```

The duration report is diagnostic evidence. A slow test is not considered a
failure unless it exceeds an agreed project threshold or introduces
unnecessary external I/O.

The current suite completed successfully in approximately 11 seconds:

```text
31 passed in 11.14s
```

The execution time may vary according to the WSL environment, filesystem,
Python version, virtual environment, and machine load.

## Structured JUnit Report

The structured report is generated with:

```bash
pytest -v \
  --junitxml=docs/evidence/test-results.xml
```

The report contains:

- Test suite name.
- Number of collected tests.
- Number of failures.
- Number of errors.
- Number of skipped tests.
- Per-test execution information.
- Execution duration.

The JUnit XML file is generated output and must not be edited manually.

If the test source, fixture, environment, or expected result changes, the XML
file must be regenerated.

## Performance Evidence

Expected evidence files:

```text
docs/evidence/
├── test_full_suite.log
├── test-results.xml
└── test_performance_all.log
```

Optional focused evidence files:

```text
docs/evidence/
├── test_prompts_contract.log
├── test_observability_contract.log
└── test_performance.log
```

Generate focused prompt evidence:

```bash
pytest tests/test_prompts_contract.py -v \
  | tee docs/evidence/test_prompts_contract.log
```

Generate focused observability evidence:

```bash
pytest tests/test_observability_contract.py -v \
  | tee docs/evidence/test_observability_contract.log
```

Generate the top-ten performance report:

```bash
pytest -v \
  --durations=10 \
  --durations-min=0.1 \
  | tee docs/evidence/test_performance.log
```

## Acceptance Criteria

The automated validation is accepted when:

- All collected tests pass.
- No unexpected external network dependency exists.
- Required prompt files exist.
- Prompt Zero-Trust constraints remain present.
- The exact fallback statement remains present.
- Observability KPI tests pass.
- Supervisor route and guardrail events remain traceable.
- Slow tests are identified by name and duration.
- Any optimization is performed only after measurement.
- The JUnit XML report corresponds to the latest execution.
- The textual log corresponds to the same execution where applicable.

## Observability KPIs

The local observability contract uses:

```text
tests/fixtures/observability_events.jsonl
```

The following KPIs are validated deterministically.

### Grounded Answer Rate

```text
Grounded Answer Rate =
grounded eligible responses / eligible non-fallback responses
```

Current fixture expectation:

```text
2/3
```

### Fallback Rate

```text
Fallback Rate =
fallback responses / total responses
```

Current fixture expectation:

```text
1/4
```

### Citation Coverage

```text
Citation Coverage =
cited claims / total claims
```

Current fixture expectation:

```text
7/8
```

### Session Latency

```text
Session Latency =
session_completed.timestamp_ms - session_started.timestamp_ms
```

The fixture validates latency for every recorded session.

### Supervisor Route Traceability

The telemetry events preserve:

- Session identifier.
- Timestamp.
- Source component.
- Target component.
- Routing reason or matched keyword.

### Guardrail Traceability

Guardrail events preserve:

- Session identifier.
- Timestamp.
- Guardrail name.
- Associated response outcome.

## Local Versus Production Observability

The local JSONL fixture validates the telemetry schema and KPI calculations
deterministically. It is a contract test and not a replacement for production
telemetry.

In a production Agentforce environment, session tracing should provide
end-to-end visibility into user turns, reasoning execution, actions, prompt
and gateway inputs and outputs, errors, and final responses. [web:2332][web:2224]

The simulated telemetry design should map these events to:
- Grounded Answer Rate.
- Fallback Rate.
- Citation Coverage.
- Session latency.
- Supervisor transitions.
- Guardrail activations.
- Retrieval failures.
- User feedback and escalations.

Agentforce Session Trace data can also be exported through an OpenTelemetry
interface for analysis in an external observability platform. [web:2222]

## Evidence Preservation

Evidence must be generated from the repository root and preserved under:

```text
docs/evidence/
```

Do not manually alter:

```text
docs/evidence/test-results.xml
docs/evidence/test_full_suite.log
```

If an annotation is needed, create a separate file, for example:

```text
docs/evidence/test-run-notes.md
```

Recommended note contents:

```markdown
# Test Run Notes

- Environment: WSL2
- Python: 3.12.3
- Pytest: 9.1.1
- Result: 31 passed, 0 failed
- Runtime: approximately 11 seconds
- JUnit report: `test-results.xml`
- Full log: `test_full_suite.log`
```

## Banker Presentation

Present the automated evidence after the UI demonstration:

1. Show the executive briefing.
2. Show grounding and source tracing.
3. Show fallback behavior.
4. Show hallucination rejection.
5. Run the prompt contract tests.
6. Run the observability contract tests.
7. Show the `31 passed` full-suite result.
8. Show `test-results.xml` as structured evidence.
9. Explain the local-to-production observability mapping.

Suggested explanation:

> “A interface demonstra o comportamento do agente, mas a governança não
> depende da tela. Os contratos automatizados validam prompts, Zero Trust,
> fallback, grounding, cobertura de citações, latência, roteamento e
> guardrails. A suíte atual possui 31 testes aprovados, sem falhas, e gera
> evidência textual e JUnit XML. Em produção, o mesmo modelo de eventos será
> conectado ao Session Tracing e à plataforma corporativa de telemetria.”