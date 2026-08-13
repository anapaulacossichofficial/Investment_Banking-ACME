# High-Level Architecture: Investment Banking Meeting Prep

```mermaid
flowchart TB
    Banker[Banker / Relationship Manager] --> UX[Salesforce UI / Agentforce Experience]

    subgraph SF[Proposed Salesforce Target Architecture]
        Supervisor[Agentforce Supervisor / Planner]
        MeetingPrep[Meeting Prep Agent]
        Topic[Meeting Preparation Topic]
        Action[Agentforce Action / Flow or Apex-backed action]

        Scope[Account and Contact Scope Resolution]
        CRM[Structured CRM and Data Cloud Entities: Accounts, Contacts, Opportunities, Activities]
        DMO[DMO-Backed Data Cloud Retriever: Approved Documents, Semantic Search, Metadata Filters]
        Evidence[Evidence Context: Structured Facts and Scoped Document Evidence]
        Prompt[Prompt Builder: Grounded Prompt Contract]
        Guardrails[Evidence and Guardrail Validation]
        Trust[Einstein Trust Layer: Trust, Privacy, Masking, Auditability]
        Brief[Grounded Executive Briefing]
        Citations[Citations and Source Attribution]
        Fallback[No-Evidence or Ambiguous-Scope Fallback]
        Observe[Observability and Evidence]

        Supervisor --> MeetingPrep
        MeetingPrep --> Topic
        Topic --> Action
        Action --> Scope

        Scope --> CRM
        Scope --> DMO

        CRM --> Evidence
        DMO --> Evidence

        Evidence --> Prompt
        Prompt --> Guardrails
        Guardrails --> Trust

        Trust --> Brief
        Trust --> Citations
        Guardrails --> Fallback
        Guardrails --> Observe
    end

    UX --> Supervisor
    Brief --> UX
    Citations --> UX
    Fallback --> UX
```

## Architecture Decision

The proposed final architecture is **DMO-backed hybrid retrieval**. Structured
CRM facts are retrieved through deterministic account and contact context.
Approved unstructured documents are retrieved through a DMO-backed Data Cloud
Retriever using semantic search and metadata filtering. Both flows converge in
an Evidence Context before Prompt Builder generates a grounded briefing.

Data Library is a valid faster-start alternative, but it is not the selected
primary target architecture for this metadata-rich Investment Banking use case.
