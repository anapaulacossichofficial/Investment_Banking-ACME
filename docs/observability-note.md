# Observability Note

## Local ACME Build
The local implementation records or validates:
- Selected capability
- Resolved account and contact
- Retrieved source identifiers
- Citation metadata
- Fallback activation
- Execution errors
- Response latency
- Routing outcome

## Salesforce Target Mapping
A Salesforce implementation should monitor:
- Agent sessions
- Topic and action execution
- Retriever activity
- Citation coverage
- Fallback rate
- Unsupported claim rate
- Latency
- User corrections
- Escalations

## Primary Metrics
- Grounded answer rate
- Citation coverage
- Unsupported claim rate
- Fallback rate
- Supervisor routing accuracy
- Account resolution accuracy
- Median and p95 latency

## Operational Response
- Increase in fallback rate indicates missing knowledge or retrieval failure.
- Increase in unsupported claims indicates prompt regression or scoping issue.
- Increase in latency indicates excessive retrieval breadth or over-orchestration.