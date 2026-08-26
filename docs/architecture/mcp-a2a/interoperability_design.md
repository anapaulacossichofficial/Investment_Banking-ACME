# External Interoperability: MCP & A2A

## Architectural Boundary
This design establishes the boundary for the `ACME_Investment_Banker_Assistant` to securely invoke external enterprise tools using the **Model Context Protocol (MCP)** and delegate tasks to specialized external agents (A2A).

## Components
1. **External Credential (`MCP_Auth_Provider`)**: Manages the OAuth 2.0 / Bearer token exchange required to securely authenticate against external agent platforms.
2. **Named Credential (`MCP_External_Agent_Gateway`)**: Defines the unified callout endpoint. Agentforce Custom Actions (via Apex Invocable methods) will reference this Named Credential to issue governed API calls to external tools without hardcoding endpoints or secrets.
