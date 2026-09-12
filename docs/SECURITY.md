# AI and agent security

[← Resource hub](../README.md) · [Start here](START-HERE.md)

Use these references to identify threats, design controls, test assumptions, and translate security findings into governance decisions.

**8 selected resources**

- [Careful Adoption of Agentic AI Services](#careful-agent-adoption)
- [OWASP Top 10 for Agentic Applications 2026](#owasp-agentic-top10)
- [MITRE ATLAS](#mitre-atlas)
- [Agentic AI Threat Modeling Framework: MAESTRO](#maestro)
- [MCP Security Best Practices](#mcp-security)
- [The lethal trifecta for AI agents: private data, untrusted content, and external communication](#lethal-trifecta)
- [OWASP GenAI LLM Top 10 2026](#owasp-llm-top10)
- [Guidelines for Secure AI System Development](#secure-ai-development)

<a id="careful-agent-adoption"></a>

### [Careful Adoption of Agentic AI Services](<https://media.defense.gov/2026/Apr/30/2003922823/-1/-1/0/CAREFULADOPTIONOFAGENTICAISERVICES_FINAL.PDF>)

**Publisher:** ASD ACSC, CISA, NSA, Canadian Centre for Cyber Security, NCSC-NZ and NCSC-UK  
**Format:** Joint government guidance / PDF · **Access:** Free  
**For:** Security, enterprise operators, government and critical infrastructure

**Why it matters:** Lifecycle guidance for privilege, configuration, behaviour, structural and accountability risks, including prerequisites for deploying agents.

**Put it into practice:** Compare a proposed deployment with its design, development, deployment and operations recommendations; identify gaps before rollout.

<a id="owasp-agentic-top10"></a>

### [OWASP Top 10 for Agentic Applications 2026](<https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>)

**Publisher:** OWASP GenAI Security Project  
**Format:** Threat and mitigation guide · **Access:** Free  
**For:** Security, GRC, developers

**Why it matters:** A compact security baseline specifically for autonomous agents, covering threats beyond the single prompt-response interaction.

**Put it into practice:** Seed an agent threat register and security review; turn relevant risks into concrete test cases and control evidence.

<a id="mitre-atlas"></a>

### [MITRE ATLAS](<https://atlas.mitre.org/>)

**Publisher:** MITRE  
**Format:** Threat knowledge base / case studies / Navigator · **Access:** Free  
**For:** Threat modeling, cybersecurity, red teams

**Why it matters:** Connects AI attack techniques to documented cases and mitigations, giving security reviews a shared vocabulary and evidence base.

**Put it into practice:** Map a short, relevant attack path for an agent and prioritize the controls and tests that interrupt it.

<a id="maestro"></a>

### [Agentic AI Threat Modeling Framework: MAESTRO](<https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro>)

**Publisher:** Ken Huang / Cloud Security Alliance  
**Format:** Practitioner threat-modeling method · **Access:** Free  
**For:** Security architects, threat modelers

**Why it matters:** A structured way to examine risks across agent architecture layers and the dependencies between them.

**Put it into practice:** Decompose an agent system before reviewing model, data, execution, monitoring, security and ecosystem threats.

<a id="mcp-security"></a>

### [MCP Security Best Practices](<https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices>)

**Publisher:** Model Context Protocol project  
**Format:** Protocol security documentation · **Access:** Free  
**For:** Security, IAM, architects, developers

**Why it matters:** Concrete controls for tool-connected agents, including consent, token audiences, confused-deputy risks and unsafe proxy behaviour.

**Put it into practice:** Review MCP authorization and trust boundaries with engineering; require evidence that server and client controls match the deployed protocol version.

<a id="lethal-trifecta"></a>

### [The lethal trifecta for AI agents: private data, untrusted content, and external communication](<https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/>)

**Publisher:** Simon Willison  
**Format:** Technical explainer · **Access:** Free  
**For:** Beginner–intermediate; governance, security and architecture teams

**Why it matters:** Provides a memorable way to recognize when prompt injection could turn an agent's legitimate capabilities into a data-exfiltration path.

**Put it into practice:** Map each of the three capabilities to the agent's tools and data flows; require controls wherever they intersect.

<a id="owasp-llm-top10"></a>

### [OWASP GenAI LLM Top 10 2026](<https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/>)

**Publisher:** OWASP GenAI Security Project  
**Format:** Security guide · **Access:** Free  
**For:** Security teams, application owners and governance reviewers

**Why it matters:** A practical baseline for LLM application security, with attack scenarios and mitigations that complement agent-specific risks.

**Put it into practice:** Use the applicable risks to review an LLM application's data flows and controls, then extend the review with the Agentic Top 10 when it can take actions.

<a id="secure-ai-development"></a>

### [Guidelines for Secure AI System Development](<https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development>)

**Publisher:** UK NCSC, CISA and international partner agencies  
**Format:** Lifecycle security guidelines · **Access:** Free  
**For:** Security leaders, suppliers and AI system owners

**Why it matters:** Covers secure design, development, deployment, operation and maintenance across the AI system lifecycle.

**Put it into practice:** Add the relevant supply-chain, documentation, release and monitoring questions to a design or supplier review.
