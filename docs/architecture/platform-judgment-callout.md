# Platform Judgment Callout

## Decision

The final enterprise version should be positioned as a Salesforce/Agentforce implementation with grounded retrieval, supervisor routing, and prompt-based validation.

## Why this is the right direction

This project already demonstrates the core behavior required for a trusted banking assistant:
- account and contact scoping;
- evidence-grounded response generation;
- citation visibility;
- explicit fallback behavior;
- reusable orchestration patterns.

That makes the Salesforce/Agentforce mapping natural rather than forced.

## Recommended platform posture

Use the current Streamlit build as the local demo runtime and validation harness.

Use Salesforce/Agentforce as the target runtime because it provides:
- agent supervision;
- prompt and topic structure;
- platform-native trust and guardrail concepts;
- enterprise integration patterns for CRM and knowledge;
- a scalable model for reuse across many future capabilities.

## Retrieval strategy

The final design should assume a hybrid grounding model:
- structured data from CRM-backed retrieval;
- unstructured data from a knowledge library or equivalent content retrieval layer.

If the target platform supports a unified retrieval layer, use it. If not, keep the hybrid model explicit and documented.

## Trust strategy

The response layer must always preserve trust signals:
- citations should be visible or recoverable;
- unsupported claims should not be produced;
- missing evidence should trigger fallback;
- prompt contracts should stay narrow and scoped.

## Outcome

This is not just a demo choice. It is the platform direction that best matches the solution’s requirements for grounding, governance, and reuse.