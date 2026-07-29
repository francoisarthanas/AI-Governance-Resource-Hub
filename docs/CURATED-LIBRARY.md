# Curated Library

This library is ranked by actionability. **Essential** means most governance programs should use it. **Core** means use it when the scope applies. **Deep dive** is for specialist or mature work. “Official page” is preferred over a copied PDF so updates are visible.

The machine-readable version, with tags and access notes, is [`catalog/resources.json`](../catalog/resources.json).

## Essential: program foundation

| Resource | Why it is here | Use it now |
|---|---|---|
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | Best free cross-sector program backbone; connects governance to context, measurement, and treatment | Tailor Govern, Map, Measure, Manage outcomes to your organization |
| [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) | Concrete actions and documentation suggestions in PDF/CSV/XLSX/JSON | Filter to your role/risk; make chosen actions owned and evidenced |
| [NIST GenAI Profile](https://doi.org/10.6028/NIST.AI.600-1) | Authoritative generative-AI risk profile and action set | Add relevant risks/actions to assessments, tests, monitoring, and incidents |
| [NIST AI Resource Center](https://airc.nist.gov/) | Implementation, profiles, use cases, and TEVV resources | Use as the maintained NIST entry point |
| [ISO/IEC 42001](https://www.iso.org/standard/81230.html) | Requirements for an auditable AI management system | Use for formal management-system discipline or certification; paid text |
| [ISO/IEC 23894](https://www.iso.org/standard/77304.html) | AI-specific risk management guidance | Use with enterprise risk management; paid text |
| [ISO/IEC 42005](https://www.iso.org/standard/42005) | Lifecycle AI system impact assessment guidance | Establish a repeatable assessment process; paid text |
| [OECD AI Principles](https://oecd.ai/en/principles) | Widely adopted, updated international principles and definitions | Align vocabulary and policy objectives |
| [OECD AI Classification Framework](https://oecd.ai/en/p/classification) | Practical dimensions for differentiating systems and impacts | Use in inventory, scoping, and tiering |
| [CSA AI Controls Matrix v1.1](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) | 247 vendor-neutral cloud AI control objectives with mappings and guidance | Reuse existing control ownership; tailor, do not implement blindly |
| [NCSC/CISA Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) | International secure-by-design guidance across the lifecycle | Add to engineering standards and supplier requirements |
| [GAO AI Accountability Framework](https://www.gao.gov/products/gao-21-519sp) | Governance, data, performance, and monitoring questions plus audit procedures | Use for management self-assessment or independent review |

## Essential: agentic AI

| Resource | Why it is here | Use it now |
|---|---|---|
| [Singapore Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) | First national framework focused on reliable and safe agent deployment | Structure agent responsibility, controls, lifecycle, and user responsibility |
| [Australian Government Agentic AI Addendum](https://www.digital.gov.au/policy/ai/agentic-ai-addendum-introduction) | Detailed criteria for memory, orchestration, evals, monitoring, and shutdown | Reuse criteria as engineering and go-live requirements |
| [Careful Adoption of Agentic AI Services](https://www.cyber.gc.ca/en/news-events/joint-guidance-careful-adoption-agentic-artificial-intelligence-services) | Joint Australia/Canada/New Zealand/UK/US security guidance | Start low risk, enforce least privilege, layered defense, visibility, and containment |
| [NIST AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure) | Authoritative place to track emerging US agent standards work | Track deliverables; do not claim standards that have not been published |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Peer-reviewed agent-specific threat baseline | Convert each applicable risk to controls and test cases |
| [NSA MCP Security Design Considerations](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/) | Government security guidance for MCP deployments | Use in MCP architecture, authorization, gateway, monitoring, and supplier review |
| [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) | Maintained protocol-specific threat and implementation guidance | Enforce audience validation; prevent token passthrough and confused-deputy attacks |
| [A2A Protocol specification](https://a2a-protocol.org/latest/specification/) | Current agent-to-agent interoperability and security requirements | Apply transport, identity, input, capability, privacy, and audit controls |
| [Google SAIF—Agents](https://saif.google/focus-on-agents) | Visual risk/control map for agent components | Threat-model data, model, orchestration, tools, memory, and actions |
| [Anthropic: Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Concrete long-horizon evaluation methods and grader choices | Build trajectory, outcome, state, and human evaluation |
| [OpenAI: Practical Guide to Building Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | Practical scoping, architecture, tool safeguards, guardrails, and human handoff | Use the patterns, then add independent authorization and assurance |

## Core: law, regulation, and public policy

| Resource | Scope | Practitioner use |
|---|---|---|
| [EU AI Act—official text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | Binding EU regulation with phased application | Source of truth; determine role, scope, classification, and dates with counsel |
| [EU AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en) | Official explorer, beta compliance checker, and help desk | Navigate obligations; checker output is informational, not legal advice |
| [EU GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) | Voluntary compliance route for GPAI provider obligations | Use transparency, copyright, safety/security measures where role applies |
| [Council of Europe Framework Convention on AI](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence) | International treaty on human rights, democracy, and rule of law | Check ratification/application and integrate rights-based governance |
| [Council of Europe HUDERIA](https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems) | Context-based rights, democracy, and rule-of-law assessment | Add structured rights impact analysis and mitigation |
| [UNESCO Recommendation on AI Ethics](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence) | Global normative framework adopted by 193 member states | Use as a rights, inclusion, environment, and public-interest lens |
| [UNESCO Ethical Impact Assessment](https://www.unesco.org/en/articles/ethical-impact-assessment-tool-recommendation-ethics-artificial-intelligence) | Practical ethical impact assessment | Challenge appropriateness, stakeholders, and lifecycle safeguards |
| [US OMB M-25-21](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf) | US federal agency use of AI | Current federal governance baseline for covered agencies and useful public-sector reference |
| [US OMB M-25-22](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf) | US federal AI acquisition | Procurement responsibilities, competition, portability, data, performance, and risk |
| [Canada Algorithmic Impact Assessment](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html) | Mandatory Canadian federal tool under its directive | Strong public, interactive impact-assessment pattern |
| [UK ICO AI and Data Protection Risk Toolkit](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/ai-and-data-protection-risk-toolkit/) | UK data protection | Identify and mitigate AI privacy/data-protection risks |
| [Australian Government AI Technical Standard](https://www.digital.gov.au/policy/ai/AI-technical-standard) | Government lifecycle technical requirements/guidance | Highly reusable requirements even outside government |
| [Japan AI Guidelines for Business](https://www.meti.go.jp/english/press/2024/0419_002.html) | Japanese government guidance for developers/providers/users | Role-based, lifecycle governance reference |
| [Singapore AI governance resources](https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence) | Traditional, generative, and agentic AI frameworks | Compare maturity-specific guidance and testing tools |
| [OECD AI Policy Observatory](https://oecd.ai/en/) | Global policies, tools, metrics, and incidents | Monitor jurisdictions and find official national sources |

## Core: security and resilience

- [MITRE ATLAS](https://atlas.mitre.org/) — AI attack tactics, techniques, mitigations, and case studies; filter for predictive, generative, or agentic AI.
- [NIST AI 100-2e2025](https://doi.org/10.6028/NIST.AI.100-2e2025) — adversarial ML terminology, attacks, mitigation approaches, and limitations.
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) — application security baseline for LLM systems.
- [NSA/CISA joint AI data security guidance](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4192332/nsas-aisc-releases-joint-guidance-on-the-risks-and-best-practices-in-ai-data-se/) — provenance, integrity, trusted infrastructure, and protection of data used to train/operate AI.
- [CISA JCDC AI Cybersecurity Collaboration Playbook](https://www.cisa.gov/news-events/alerts/2025/01/14/cisa-releases-jcdc-ai-cybersecurity-collaboration-playbook-and-fact-sheet) — AI cyber incident information sharing and coordination.
- [Coalition for Secure AI](https://www.coalitionforsecureai.org/) — open work on risk/controls, agentic design patterns, software supply chain, and threat-informed defense; verify deliverable maturity.
- [C2PA specifications](https://spec.c2pa.org/) — tamper-evident content provenance and authenticity; provenance is context, not proof that content is true.
- [CycloneDX AI/ML-BOM](https://www.cyclonedx.org/capabilities/mlbom/) — model/dataset/dependency inventory for AI supply chains.

## Core: evaluation, assurance, and audit

- [Inspect](https://inspect.aisi.org.uk/) — open model and agent evaluation framework from the UK AI Security Institute.
- [NIST Dioptra](https://pages.nist.gov/dioptra/) — reproducible, traceable AI test platform.
- [Microsoft PyRIT](https://github.com/microsoft/PyRIT) — GenAI red-team orchestration.
- [NVIDIA garak](https://github.com/NVIDIA/garak) — LLM vulnerability scanner.
- [Project Moonshot](https://aiverifyfoundation.sg/project-moonshot/) — open LLM benchmark/red-team toolkit.
- [AI Verify](https://aiverifyfoundation.sg/what-is-ai-verify/toolkit/) — governance testing framework/toolkit for traditional AI.
- [MLCommons AILuminate safety resources](https://mlcommons.org/ailuminate/safety-resources/) — standardized LLM risk/reliability benchmark materials.
- [Fairlearn](https://fairlearn.org/) — fairness assessment/mitigation for ML; metrics are not a substitute for contextual judgment.
- [IIA AI Auditing Framework](https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework) — public practical guidance and checklist for internal audit.
- [ISO/IEC 38507](https://www.iso.org/standard/56641.html) — governing-body implications of organizational AI use; paid text.

## Core: incidents, transparency, and documentation

- [OECD AI Incidents and Hazards Monitor](https://oecd.ai/en/incidents) — real-time incident/hazard evidence for risk assessment.
- [OECD common incident reporting framework](https://oecd.ai/en/ai-publications/towards-a-common-reporting-framework-for-ai-incidents) — 29 criteria for consistent incident reports.
- [AI Incident Database](https://partnershiponai.org/workstream/ai-incidents-database/) — searchable crowdsourced real-world AI failures.
- [OECD Hiroshima AI Process Reporting Framework](https://oecd.ai/en/transparency/overview) — voluntary governance/risk transparency structure for advanced AI value-chain actors.
- [EU GPAI training-content summary template](https://digital-strategy.ec.europa.eu/en/faqs/template-general-purpose-ai-model-providers-summarise-their-training-content) — current official public-summary baseline for covered GPAI providers.
- [Data Cards Playbook](https://sites.research.google/datacardsplaybook/) — dataset documentation method and templates.
- [OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/) — current system cards and evaluation disclosures; useful examples, not independent assurance.
- [Anthropic Transparency Hub](https://www.anthropic.com/transparency) — model reports and governance disclosures; useful examples, not independent assurance.

## Deep dive: frontier and systemic risk

- [EU GPAI provider guidance](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers) — official scope and submission guidance for GPAI obligations.
- [EU GPAI Safety and Security Code chapter](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) — concrete practices for models with systemic risk.
- [Google DeepMind Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/) — capability thresholds, early-warning evaluations, and mitigations; lab-authored and voluntary.
- [Anthropic Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) — capability thresholds, safeguards, governance, and transparency; lab-authored and voluntary.
- [MLCommons AILuminate Agentic](https://mlcommons.org/ailuminate/agentic/) — emerging agent reliability benchmark maturity model.

## Sector entry points

| Sector | Start here |
|---|---|
| Banking | [US interagency Revised Guidance on Model Risk Management (SR 26-2)](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm); map AI governance into established model-risk and third-party processes |
| Insurance | [NAIC Model Bulletin on AI Systems](https://content.naic.org/article/naic-members-approve-model-bulletin-use-ai-insurers); confirm adoption and state-specific requirements |
| Medical devices | [FDA Digital Health Guidance list](https://www.fda.gov/medical-devices/digital-health-center-excellence/guidances-digital-health-content) and [Good Machine Learning Practice principles](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles) |
| Employment | [EEOC Employment Tests and Selection Procedures](https://www.eeoc.gov/laws/guidance/employment-tests-and-selection-procedures); also check state/local and EU rules |
| Government | [Canada AIA](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html), [GAO framework](https://www.gao.gov/products/gao-21-519sp), and [Australian AI standard](https://www.digital.gov.au/policy/ai/AI-technical-standard) |

Sector pages are entry points, not complete legal inventories.
