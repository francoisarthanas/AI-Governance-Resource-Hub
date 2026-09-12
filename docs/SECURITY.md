# AI and agent security

[← Resource hub](../README.md) · [Start here](START-HERE.md)

Use these references to identify threats, design controls, test assumptions, and translate security findings into governance decisions.

**8 selected resources · Catalog reviewed 2026-09-12.**

<!-- Generated from catalog/resources.json. Edit the catalog, then run python scripts/generate_catalog.py. -->

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

**Why it earns a place:** Lifecycle guidance for privilege, configuration, behaviour, structural and accountability risks, including prerequisites for deploying agents.

**Use it to:** Compare a proposed deployment with its design, development, deployment and operations recommendations; identify gaps before rollout.

**Version / status:** April 2026; CISA release 1 May 2026  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official joint-government PDF reviewed for scope, authoring agencies, risk categories and lifecycle recommendations. The shared publication is hosted by the U.S. Department of Defense.

</details>

<a id="owasp-agentic-top10"></a>

### [OWASP Top 10 for Agentic Applications 2026](<https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>)

**Publisher:** OWASP GenAI Security Project  
**Format:** Threat and mitigation guide · **Access:** Free  
**For:** Security, GRC, developers

**Why it earns a place:** A compact security baseline specifically for autonomous agents, covering threats beyond the single prompt-response interaction.

**Use it to:** Seed an agent threat register and security review; turn relevant risks into concrete test cases and control evidence.

**Version / status:** 2026 edition; published 9 December 2025  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Inspected official resource page and download link. Community security guidance, not a legal compliance standard. Distinct from OWASP GenAI LLM Top 10 2026.

</details>

<a id="mitre-atlas"></a>

### [MITRE ATLAS](<https://atlas.mitre.org/>)

**Publisher:** MITRE  
**Format:** Threat knowledge base / case studies / Navigator · **Access:** Free  
**For:** Threat modeling, cybersecurity, red teams

**Why it earns a place:** Connects AI attack techniques to documented cases and mitigations, giving security reviews a shared vocabulary and evidence base.

**Use it to:** Map a short, relevant attack path for an agent and prioritize the controls and tests that interrupt it.

**Version / status:** Living knowledge base; monthly content updates  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official MITRE ATLAS source repository and releases reviewed for techniques, cases, mitigations and Navigator exports. This is a living knowledge base; use the current definitions when building a threat model.

</details>

<a id="maestro"></a>

### [Agentic AI Threat Modeling Framework: MAESTRO](<https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro>)

**Publisher:** Ken Huang / Cloud Security Alliance  
**Format:** Threat-modeling method / article · **Access:** Free  
**For:** Security architects, threat modelers

**Why it earns a place:** A structured way to examine risks across agent architecture layers and the dependencies between them.

**Use it to:** Decompose an agent system before reviewing model, data, execution, monitoring, security and ecosystem threats.

**Version / status:** Original method article, 6 February 2025  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Inspected original CSA article including seven-layer architecture. A proposed practitioner method, not a formal consensus standard. Prefer original method over vendor summaries or AI-generated threat reports.

</details>

<a id="mcp-security"></a>

### [MCP Security Best Practices](<https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices>)

**Publisher:** Model Context Protocol project  
**Format:** Protocol security documentation · **Access:** Free  
**For:** Security, IAM, architects, developers

**Why it earns a place:** Concrete controls for tool-connected agents, including consent, token audiences, confused-deputy risks and unsafe proxy behaviour.

**Use it to:** Review MCP authorization and trust boundaries with engineering; require evidence that server and client controls match the deployed protocol version.

**Version / status:** Versioned documentation: 2025-11-25; draft documentation also exists  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Read versioned official page and separate draft. Old /specification/.../basic/security_best_practices URLs redirect to /docs/.../tutorials/security/. Draft has changed state handling, so do not silently mix protocol generations or describe draft behaviour as a deployed requirement.

</details>

<a id="lethal-trifecta"></a>

### [The lethal trifecta for AI agents: private data, untrusted content, and external communication](<https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/>)

**Publisher:** Simon Willison  
**Format:** Technical explainer · **Access:** Free  
**For:** Beginner–intermediate; governance, security and architecture teams

**Why it earns a place:** Provides a memorable way to recognize when prompt injection could turn an agent's legitimate capabilities into a data-exfiltration path.

**Use it to:** Map each of the three capabilities to the agent's tools and data flows; require controls wherever they intersect.

**Version / status:** 2025-06-16; architectural risk explanation  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Opened author's original article. A threat-model heuristic, not an exhaustive checklist or proof that eliminating one path makes an agent secure.

</details>

<a id="owasp-llm-top10"></a>

### [OWASP GenAI LLM Top 10 2026](<https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/>)

**Publisher:** OWASP GenAI Security Project  
**Format:** Security guide · **Access:** Free  
**For:** Security teams, application owners and governance reviewers

**Why it earns a place:** A practical baseline for LLM application security, with attack scenarios and mitigations that complement agent-specific risks.

**Use it to:** Use the applicable risks to review an LLM application's data flows and controls, then extend the review with the Agentic Top 10 when it can take actions.

**Version / status:** 2026 edition; official resource page dated 3 August 2026.  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official 2026 resource page and download link inspected. Distinct from the 2025 LLM edition and from the Agentic Applications Top 10; community guidance, not certification.

</details>

<a id="secure-ai-development"></a>

### [Guidelines for Secure AI System Development](<https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development>)

**Publisher:** UK NCSC, CISA and international partner agencies  
**Format:** Lifecycle security guidelines · **Access:** Free  
**For:** Security leaders, suppliers and AI system owners

**Why it earns a place:** Covers secure design, development, deployment, operation and maintenance across the AI system lifecycle.

**Use it to:** Add the relevant supply-chain, documentation, release and monitoring questions to a design or supplier review.

**Version / status:** Version 1.0, 27 November 2023.  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official NCSC collection and publication metadata inspected. Baseline government guidance predating current agent-specific guidance; use both where appropriate.

</details>
