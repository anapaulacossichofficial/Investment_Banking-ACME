# ADR 001: Platform Judgment Callout - Autonomous Agent Callouts vs. Session Activation

## 1. Context & Business Problem
To deliver the **Competitive Intelligence Capability (Option B)**, the Agentforce orchestration layer must securely invoke an external peer-benchmarking API. The architectural standard is to use Salesforce **External Credentials** mapped to a Permission Set to inject the `x-api-key` header, ensuring zero hardcoded tokens in the Apex code (`ACME_CompetitiveIntelligenceAction`).

## 2. Platform Constraint Identified
During the end-to-end integration phase, the Agentforce autonomous routing failed to authenticate against the external backend. 
*   **The Root Cause:** The assigned Permission Set (`Agentforce_CI_Access`) had **"Session Activation Required"** enabled.
*   **Platform Limitation:** While Session Activation (MFA / Step-up authentication) is a Salesforce best practice for human users operating in the UI, **autonomous Agents and background Apex Callouts (M2M - Machine-to-Machine) do not run in interactive sessions**. Consequently, the platform silently blocked the credential injection, leading to obscure Agent reasoning failures.

## 3. Architecture Trade-off & Decision
To unblock the SI team across the 30+ agent backlog, we must establish a clear boundary between Human identity governance and Machine identity governance.

*   **Decision:** We decoupled the integration security policies. We explicitly disabled *Session Activation Required* for the specific Permission Set bound to the Agent's External Credential, allowing background headless execution.
*   **Trade-off (OOTB vs. Custom):** We traded the out-of-the-box (OOTB) interactive step-up security for functional automation. 
*   **Risk Mitigation:** To offset this trade-off, the Permission Set is strictly scoped (Principle of Least Privilege) granting access *only* to the target External Credential Principal, ensuring that even if the Agent's internal context is compromised, it cannot pivot to other Salesforce resources.

## 4. Guidance for the SI Partner
When building the remaining 30+ agents:
> *"Never reuse human-user Permission Sets for Agentforce External Credential mappings. Always provision dedicated M2M Permission Sets with Session Activation disabled to prevent silent orchestration failures in production."*