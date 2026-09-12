# AI Governance Resource Hub

> A practitioner-first, vendor-neutral field guide for governing AI systems and AI agents—from first inventory to production assurance.

[![Link check](https://github.com/francoisarthanas/AI-Governance-Resource-Hub/actions/workflows/links.yml/badge.svg)](https://github.com/francoisarthanas/AI-Governance-Resource-Hub/actions/workflows/links.yml)
[![Catalog validation](https://github.com/francoisarthanas/AI-Governance-Resource-Hub/actions/workflows/validate.yml/badge.svg)](https://github.com/francoisarthanas/AI-Governance-Resource-Hub/actions/workflows/validate.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](LICENSE)

**Last verified:** 29 July 2026 · **Scope:** enterprise and public-sector AI governance, including generative and agentic AI · **No sponsored links**

This is not a directory of everything ever written about responsible AI. It is the smaller set of resources, controls, tools, and working documents that a governance lead can use at work.

## Start here

If you have one hour:

1. Read the [Start Here guide](docs/START-HERE.md).
2. Copy the [AI inventory](templates/ai-inventory.csv) and record every known use case, model, vendor feature, and agent.
3. Run the [AI use-case intake](templates/ai-use-case-intake.md) on one live use case.
4. For an agent, also complete the [agentic risk assessment](templates/agentic-risk-assessment.md) and [access matrix](templates/agent-access-matrix.csv).
5. Do not approve production until the [go-live checklist](templates/go-live-checklist.md) has an accountable sign-off and linked evidence.

If you are building a program, follow the [90-day implementation playbook](docs/IMPLEMENTATION-PLAYBOOK.md). If an agent can call tools or change state, begin with the [Agentic AI Governance guide](docs/AGENTIC-AI-GOVERNANCE.md).

## The essential shelf

Read these before buying a governance platform or inventing a framework.

| Resource | Use it for | Do this next |
|---|---|---|
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) + [Playbook](https://airc.nist.gov/airmf-resources/playbook/) | The program backbone: Govern, Map, Measure, Manage | Select outcomes that fit your risk and context; do not turn the whole playbook into a checklist |
| [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) | GenAI risks and actions | Add the relevant actions to design review, testing, incident response, and supplier review |
| [ISO/IEC 42001](https://www.iso.org/standard/81230.html) | Auditable AI management system | Use when you need management-system rigor or certification; the standard text is paid |
| [ISO/IEC 42005](https://www.iso.org/standard/42005) | Repeatable AI system impact assessments | Use alongside—not instead of—your legal, privacy, security, and human-rights assessments |
| [OECD AI Principles](https://oecd.ai/en/principles) + [classification framework](https://oecd.ai/en/p/classification) | Common vocabulary and system classification | Use its dimensions to make your inventory and risk tiers consistent |
| [EU AI Act official text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) + [official Service Desk](https://ai-act-service-desk.ec.europa.eu/en) | EU obligations and implementation tools | Determine role, scope, and risk category with counsel; use the official checker as orientation, not legal advice |
| [CSA AI Controls Matrix v1.1](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) | A detailed, vendor-neutral cloud AI control catalog | Map existing cloud/security controls before creating new ones |
| [NCSC/CISA secure AI development guidelines](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) | Secure design, development, deployment, and operations | Put the guidance into your SDLC and supplier requirements |
| [Singapore Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) | The agent governance foundation | Apply its four dimensions to responsibility, technical controls, lifecycle activity, and end-user responsibility |
| [Joint guidance: Careful Adoption of Agentic AI Services](https://www.cyber.gc.ca/en/news-events/joint-guidance-careful-adoption-agentic-artificial-intelligence-services) | Security baseline for agent adoption | Start small, constrain privileges, monitor actions, and plan containment before connecting real systems |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Agent threat modeling and testing | Map each applicable threat to a preventive control, test, signal, and response owner |
| [Australian Government Agentic AI Addendum](https://www.digital.gov.au/policy/ai/agentic-ai-addendum-introduction) | An unusually concrete lifecycle control set | Reuse the criteria for memory, orchestration, evaluation, observability, shutdown, and accountability |

## What good looks like

A functioning program can answer these questions with evidence—not slides:

- What AI do we use, who owns it, what can it affect, and where does its data go?
- Which uses are prohibited, which need review, and who has authority to accept residual risk?
- What changed since the last approval: model, prompt, data, tool, permission, workflow, or law?
- How was the system tested for its real users, context, failure modes, misuse, and adversarial behavior?
- What do we monitor, who responds, and how can we stop, revoke, roll back, notify, and recover?
- For every agent: whose authority is it exercising, with which identity, credentials, tools, memory, budgets, and human approval gates?

The operating loop is:

```text
Discover -> Triage -> Assess -> Decide -> Build controls -> Verify -> Release -> Monitor -> Respond/Change/Retire
```

Every gate should produce durable evidence. See [Operating Model](docs/OPERATING-MODEL.md), [Evidence & Metrics](docs/EVIDENCE-AND-METRICS.md), and the [control baseline](catalog/control-baseline.csv).

## Pick your path

| You are… | Begin with… | Then use… |
|---|---|---|
| Establishing governance | [Start Here](docs/START-HERE.md) | [90-day playbook](docs/IMPLEMENTATION-PLAYBOOK.md), [operating model](docs/OPERATING-MODEL.md) |
| Governing agents | [Agentic AI Governance](docs/AGENTIC-AI-GOVERNANCE.md) | [agentic assessment](templates/agentic-risk-assessment.md), [access matrix](templates/agent-access-matrix.csv), [agent evaluation plan](templates/agent-evaluation-plan.md) |
| Reviewing a use case | [Use-case intake](templates/ai-use-case-intake.md) | [impact assessment](templates/ai-impact-assessment.md), [system card](templates/ai-system-card.md), [go-live checklist](templates/go-live-checklist.md) |
| Buying AI | [Procurement & Third Parties](docs/PROCUREMENT.md) | [vendor questionnaire](templates/vendor-due-diligence.md), [contract checklist](templates/contract-clauses-checklist.md) |
| Testing or red teaming | [Tools & Test Stack](docs/TOOLS-AND-TESTING.md) | [evaluation plan](templates/evaluation-plan.md), [incident report](templates/ai-incident-report.md) |
| Tracking rules | [Regulatory Map](docs/REGULATORY-MAP.md) | Official sources and qualified counsel in every applicable jurisdiction |
| Learning the field | [Learning Path](docs/LEARNING-PATH.md) | [Curated Library](docs/CURATED-LIBRARY.md) |
| Auditing a program | [Evidence & Metrics](docs/EVIDENCE-AND-METRICS.md) | [IIA AI Auditing Framework](https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework), [GAO accountability framework](https://www.gao.gov/products/gao-21-519sp) |

## Repository map

```text
docs/                  Opinionated practitioner guides
templates/             Editable intake, assessment, approval, and response artifacts
catalog/resources.json Machine-readable curated resource catalog
catalog/control-baseline.csv  Minimum control objectives and evidence
scripts/validate.py    Dependency-free structural and catalog checks
.github/workflows/     Automated catalog and link checking
```

## Curation standard

A resource is included only when it has a clear owner, direct practitioner value, and a reason to be used. Primary sources beat summaries. Maintained resources beat abandoned projects. Free and open material is preferred; paid standards are labeled. Vendor resources are included only when they are concrete enough to reuse or inspect, and never as proof that the vendor's own product is safe.

Each catalog entry states **why it matters** and **what to do with it**. See the full [curation policy](CONTRIBUTING.md#curation-policy) and [machine-readable catalog](catalog/resources.json).

## Important limits

This repository is educational and operational guidance, not legal, audit, certification, cybersecurity, or procurement advice. Laws, standards, and tools change. Validate applicability and current versions with the responsible experts. A framework mapping is an aid to reuse evidence; it is not a statement of compliance or equivalence.

## Contribute

Corrections and high-signal additions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md). A proposed link without a use case, authoritative owner, and concrete practitioner action will not be accepted.

Licensed under [CC BY 4.0](LICENSE). External resources retain their own licenses and terms.
