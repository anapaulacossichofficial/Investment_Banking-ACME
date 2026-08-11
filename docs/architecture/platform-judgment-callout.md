# Platform Judgment Callout: Salesforce Agentforce vs. Custom LLM Stacks

## 1. Executive Summary
For the Knowledge-Grounded Meeting Prep Agent, ACME evaluated two paths: a custom Python orchestration stack or a native Salesforce platform approach using Agentforce, Data Cloud, and the Einstein Trust Layer. The recommended target state is Salesforce-native.

## 2. Evaluation Criteria
The decision was evaluated against four enterprise pillars:
- Security, governance, and data privacy.
- Data grounding and hybrid retrieval at scale.
- Operational complexity and total cost of ownership.
- Extensibility for multi-agent enterprise scaling.

## 3. Comparative Analysis
| Dimension | Custom Python Stack | Salesforce Agentforce Native Architecture |
| :--- | :--- | :--- |
| Data residency and security | Requires custom masking, RBAC, and audit implementation. | Native trust controls and platform security boundaries reduce custom compliance work. |
| CRM data blending | Requires custom ETL, connectors, and synchronization logic. | Data Cloud provides a platform-native path for harmonized CRM grounding. |
| Scope enforcement | Depends on application-layer rules and prompt engineering. | Guardrails and orchestration can be enforced at the platform layer. |
| Multi-agent scalability | Routing, contracts, and observability must be built and maintained manually. | Shared platform primitives support reuse across many agent capabilities. |

## 4. Platform Judgment
Decision: adopt Salesforce Agentforce as the primary enterprise target state.

### Rationale
- It reduces custom glue code and integration drift.
- It aligns better with banking governance and trust requirements.
- It provides a more scalable foundation for future agents.

## 5. Role of the Local Reference Lab
The local Python/VSCode lab remains important as a reference implementation for:
- contract testing;
- prompt versioning;
- policy validation;
- fast iteration before Org promotion.

The lab is not the target architecture; it is the executable specification used to prepare the Salesforce Org configuration.