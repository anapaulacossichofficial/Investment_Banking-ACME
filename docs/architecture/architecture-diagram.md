# Architecture Diagram

## Diagram

```mermaid
flowchart TD
    User[Banker] --> UI[Streamlit Application]

    UI --> Supervisor[ACME Supervisor / Orchestrator]

    Supervisor --> MeetingPrep[Meeting Prep Agent]
    Supervisor --> Competitive[Competitive Intelligence Agent]

    MeetingPrep --> Scope[Account and Contact Scoping]
    Scope --> CRM[CRM Retriever]
    Scope --> Knowledge[Knowledge Retriever]

    CRM --> CRMData[(CRM Fixtures)]
    Knowledge --> Docs[(Knowledge Documents)]

    CRMData --> Evidence[Grounding Bundle]
    Docs --> Evidence

    Evidence --> Prompt[Grounded Prompt Contract]
    Prompt --> Validation[Evidence and Guardrail Validation]

    Validation --> Output[Executive Briefing]
    Validation --> Sources[Citations and Source Metadata]
    Validation --> Fallback[No-Evidence Fallback]

    Output --> UI
    Sources --> UI
    Fallback --> UI
```

## Reading the diagram

- The banker starts in the Streamlit interface.
- The supervisor resolves intent and routes the request.
- The meeting prep agent narrows the request to a specific account and contact.
- Structured and unstructured retrieval feed a shared grounding bundle.
- The prompt contract generates the answer only after validation.
- The final response returns citations, source metadata, or fallback behavior when necessary.

## Notes

This diagram should stay simple and readable. It is better as a high-level reference than as a full runtime spec.