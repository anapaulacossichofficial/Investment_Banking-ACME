# Solution Blueprint: Knowledge-Grounded Meeting Prep Agent

## 1. Problem Statement
Investment bankers spend excessive time manually collating data from structured CRM records and unstructured documents such as pitch decks and relationship notes to prepare for client meetings. This process is slow, error-prone, and difficult to audit, creating risk around missed signals, cross-account leakage, and weak evidence traceability.

## 2. Business Outcome
Deploy an Agentforce-powered Meeting Prep Agent that securely synthesizes hybrid data into a banker-ready executive briefing, reducing prep time while preserving account isolation, evidence traceability, and trust.

## 3. Scope Definition
- Supported Intents: Account briefing, relationship context summary, recent activity extraction.
- Unsupported Intents: General financial advice, cross-account comparisons, unsupported speculative scenarios.

## 4. Architecture Overview
The solution orchestrates four layers:
1. Supervisor Router: Evaluates intent and enforces the required scope.
2. Meeting Prep Agent: Receives the locked scope, runs retrieval, and generates the briefing.
3. Hybrid Retrieval Engine: Combines structured CRM data with unstructured knowledge content.
4. Trust and Guardrail Layer: Enforces citations, handles fallback, and blocks unsupported claims.

## 5. Retrieval Strategy
The architecture uses a blended retrieval model:
- Structured Data: Accounts, Contacts, Opportunities, and recent activity.
- Unstructured Data: Meeting notes, research, and pitch materials.
- Scope Rule: Unstructured retrieval must always be pre-filtered by the locked Account ID to prevent cross-pollination.

## 6. Citation and Source Attribution
The agent operates under a strict “No Evidence, No Claim” contract.
- Every material claim must be traceable to a source.
- The response must expose citations or equivalent source metadata.
- Outputs lacking traceable grounding are suppressed by the citation policy.

## 7. Guardrails and Scope Control
- Scope Lock: The supervisor requires a valid Account ID before retrieval.
- Anti-Hallucination: Prompts must separate confirmed facts from inference.
- Policy Enforcement: Unsupported or out-of-scope requests are refused.

## 8. Fallback Behavior
- Missing Evidence: The agent abstains and states that sufficient information is not available.
- Missing Scope: The supervisor requests the target Account before proceeding.

## 9. Reusability Pattern
This design decouples retrieval contracts and guardrail policies from agent-specific instructions. By standardizing the handoff contract and using configuration-driven policies, ACME can scale this architecture to 30+ agents with a shared trust and retrieval foundation.