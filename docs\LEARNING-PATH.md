# Learning Path: From Newcomer to Practitioner

The fastest route is to learn against one real use case. Reading without producing an inventory record, assessment, control, test, and decision creates familiarity—not capability.

## Level 1 — Essentials (one working day)

### Learn

1. Watch the [NIST AI RMF explainer](https://www.nist.gov/video/introduction-nist-ai-risk-management-framework-ai-rmf-10-explainer-video).
2. Read the [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) executive material and Core.
3. Browse the [NIST Playbook](https://airc.nist.gov/airmf-resources/playbook/) by role.
4. Read the [OECD AI Principles](https://oecd.ai/en/principles) and [classification framework](https://oecd.ai/en/p/classification).
5. Read [Start Here](START-HERE.md).

### Produce

- One use-case inventory record.
- One completed intake.
- A list of affected people, foreseeable harms, controls, evidence, and owners.

### You are ready to move on when

You can explain why risk is contextual, distinguish model from AI system/use case, and name who decides, who is affected, how the system fails, and what evidence would support release.

## Level 2 — Program operator (two weeks alongside work)

### Learn

- NIST [Govern](https://airc.nist.gov/airmf-resources/playbook/) and [GenAI Profile](https://doi.org/10.6028/NIST.AI.600-1).
- [ISO's overview of AI management systems](https://www.iso.org/artificial-intelligence/ai-management-systems); obtain ISO/IEC 42001 if certification or contractual scope requires it.
- [GAO AI Accountability Framework](https://www.gao.gov/products/gao-21-519sp).
- [IIA AI Auditing Framework](https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework).
- Your organization's actual privacy, cyber, legal, model-risk, product, procurement, incident, change, and audit processes.

### Produce

- A charter, decision rights, risk tiers, and fast/enhanced review lanes.
- A tailored control baseline.
- A completed impact assessment and evidence-indexed decision.
- A management metric set and improvement backlog.

### Optional professional baseline

The [IAPP AIGP Body of Knowledge and exam blueprint](https://iapp.org/certify/aigp) is a useful free map of the profession. Certification and training are paid and not required to use this repository.

## Level 3 — Agentic governance specialist

### Learn in this order

1. [Singapore Agentic AI Governance Framework](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf).
2. [Joint guidance on careful agent adoption](https://www.cyber.gc.ca/en/news-events/joint-guidance-careful-adoption-agentic-artificial-intelligence-services).
3. [Australian Agentic AI Addendum](https://www.digital.gov.au/policy/ai/agentic-ai-addendum-introduction).
4. [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) and [MITRE ATLAS](https://atlas.mitre.org/).
5. [NSA MCP security guidance](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/) and current [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices).
6. [Anthropic agent eval guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) and [Inspect](https://inspect.aisi.org.uk/).
7. This repository's [Agentic AI Governance guide](AGENTIC-AI-GOVERNANCE.md).

### Watch/build

- [OpenAI Academy: Designing Reliable Agent Architectures](https://academy.openai.com/public/clubs/builders-etkn1/videos/ai-techniques-production-designing-reliable-agent-architectures-2025-12-11)
- [OpenAI Academy: Skill Lab—Build Your First Workspace Agent](https://academy.openai.com/public/events/skill-lab-build-your-first-workspace-agent-nnjoi6bjce)
- [AI Verify tutorials and Project Moonshot resources](https://aiverifyfoundation.sg/resources/)

### Produce

- An agent system/context/data flow with trust boundaries.
- Per-agent identity and per-tool authorization matrix.
- Action risk levels, human gates, execution budgets, and memory policy.
- Threat model and agent trajectory evaluation suite.
- Observability specification and a tested shutdown/recovery drill.

## Level 4 — Assurance and deep specialization

Choose the path that matches your role:

- **Legal/regulatory:** [Regulatory Map](REGULATORY-MAP.md), official text/guidance, role analysis, obligation-to-control-to-evidence matrix.
- **Security:** NIST AI 100-2e2025, OWASP, MITRE ATLAS, NCSC/CISA, SAIF, MCP/A2A, PyRIT/garak/Inspect.
- **Audit:** IIA/GAO, ISO/IEC 42001 and 42005, control design/operating-effectiveness sampling, evidence integrity.
- **Testing:** Inspect, Dioptra, MLCommons, Moonshot, protected eval design, human factors, statistical validity.
- **Privacy/human rights:** ICO, UNESCO EIA, Council of Europe HUDERIA, stakeholder engagement and remedy.
- **Model/frontier risk:** EU GPAI Code, OECD HAIP reports, model/system cards, capability-threshold frameworks, independent testing.
- **Sector:** authoritative regulator and standards entry points in the [Curated Library](CURATED-LIBRARY.md).

## A 12-week practice sequence

| Week | Practice output |
|---|---|
| 1 | Inventory and context map |
| 2 | Risk tier and applicable-obligations memo |
| 3 | Impact/privacy/threat assessments |
| 4 | Control and evidence plan |
| 5 | Supplier and contract review |
| 6 | Evaluation requirements and dataset |
| 7 | Functional/context/subgroup tests |
| 8 | Security/abuse/agent tests |
| 9 | Monitoring and incident runbook |
| 10 | Release decision and user/operator instructions |
| 11 | Production sampling or tabletop exercise |
| 12 | Independent review and remediation roadmap |

## How to judge a course or certification

Prefer material that is current, sourced, scenario-based, and requires working artifacts. Ask whether it covers:

- system context rather than ethics principles alone;
- law and standards without pretending that a crosswalk equals compliance;
- product, security, privacy, human impact, testing, operations, incidents, and procurement;
- agents, identity, delegated authority, tool use, memory, observability, and containment;
- exercises using real evidence and decisions.

Avoid expensive credentials as a substitute for supervised practice.
