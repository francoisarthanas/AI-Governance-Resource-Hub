# AI Procurement and Third-Party Governance

Buying a model, agent, copilot, or embedded AI feature transfers implementation—not accountability. Evaluate the complete service and shared-responsibility boundary.

## Start with the use case, not the vendor demo

Document:

- the decision or workflow, intended users, affected parties, measurable benefit, and safer alternatives;
- required data, actions, integrations, autonomy, scale, availability, and jurisdictions;
- prohibited uses and non-negotiable controls;
- the evidence needed before pilot, production, expansion, and renewal;
- exit, portability, continuity, and manual fallback requirements.

Do not let a generic “enterprise-grade” claim substitute for system-specific evidence.

## Due-diligence domains

Use [`templates/vendor-due-diligence.md`](../templates/vendor-due-diligence.md) and require evidence for material claims.

| Domain | What to establish |
|---|---|
| Roles and scope | Provider/deployer roles, subcontractors, locations, support model, intended and prohibited use |
| System transparency | Model/provider/version, architecture, system and data flows, limitations, known failures, change history |
| Data governance | Sources and provenance; IP rights; customer data, prompt, output, telemetry, and feedback use; retention, deletion, residency, isolation |
| Security | Secure SDLC, threat model, independent testing, vulnerability disclosure, incident history, encryption, secrets, tenant isolation, supply chain |
| Identity and agents | Agent identity, per-tool scopes, delegated authority, short-lived credentials, approvals, protocol security, non-human identity lifecycle |
| Safety and quality | Context-relevant evals, subgroup analysis, red teaming, abuse prevention, human oversight, fallback, accessibility |
| Operations | Availability, rate/cost limits, monitoring, logging, evidence export, versioning, change notice, rollback, recovery |
| Compliance and assurance | Applicable laws/standards, audit reports/certifications and scope, regulator support, documentation, customer audit rights |
| Incidents | Definitions, notification window, cooperation, evidence preservation, root cause, remediation, downstream notification |
| Exit | Data/model/artifact return and deletion, configuration/eval export, transition help, continuity if provider/model/tool disappears |

## Evidence hierarchy

Prefer, in order:

1. system-specific technical artifacts and reproducible test results;
2. recent independent assessment with relevant scope and exceptions;
3. contractual commitments and customer-verifiable controls;
4. documented process and named control owner;
5. public policy or marketing statement.

A SOC 2 or ISO 27001 certificate can support assurance over its stated scope. It does not prove the AI use case is fair, lawful, safe, accurate, robust, or fit for your context. ISO/IEC 42001 certification similarly does not certify every system outcome.

## Agent-specific questions

- Does every agent/sub-agent use a unique identity attributable to a principal and task?
- Can customers restrict individual tools, actions, fields, resources, recipients, destinations, amounts, and environments?
- Are credentials short-lived, audience-bound, revocable, and hidden from model context?
- Can untrusted content change instructions, discover tools, or trigger state-changing calls?
- How are MCP servers, A2A peers, plugins, skills, tool descriptions, models, and dependencies approved, pinned, verified, and monitored?
- Can customers impose step, time, cost, retry, recursion, delegation, and transaction limits independently of prompts?
- Which actions support preview, confirmation, idempotency, soft deletion, compensation, and rollback?
- What telemetry reconstructs tool calls, approvals, state changes, sub-agent handoffs, and policy decisions?
- How quickly can the customer pause all execution and revoke every credential and scheduled task?
- Which agentic threats and recovery paths were independently tested, in what configuration, and with what unresolved findings?

## Pilot design

Run the pilot in a contained environment with representative but minimized data. Use read-only access first. Define success, safety, cost, exit, and stop criteria before the pilot starts. Do not quietly convert a proof of concept into production.

The pilot should test:

- the customer's actual configuration, integrations, prompts, tools, and workload;
- normal, boundary, out-of-scope, ambiguous, malicious, and failure cases;
- monitoring, human review, support, incident, revocation, rollback, data deletion, and export;
- version changes and the provider's notification/rollback process;
- total cost at expected and adversarial load.

## Contract checklist

Use [`templates/contract-clauses-checklist.md`](../templates/contract-clauses-checklist.md). High-priority terms usually include:

- permitted purpose and prohibited secondary use of customer data, prompts, outputs, telemetry, and feedback;
- no training or improvement use unless explicitly authorized;
- ownership, license, infringement process, and provenance disclosures;
- subprocessor and location transparency, change/objection rights, retention, return, and verified deletion;
- system/model/tool change notice, release notes, backward compatibility, revalidation support, and rollback;
- security and AI incident definitions, rapid notice, cooperation, evidence, root-cause, and corrective-action duties;
- audit/evidence access, regulator support, and ongoing documentation;
- performance, availability, safety, support, continuity, and recovery commitments;
- indemnity, liability, insurance, suspension, termination, and exit/portability proportionate to risk.

Qualified counsel should tailor terms to the jurisdiction, sector, roles, and facts.

## Continuous supplier governance

At least on renewal and after material change or incident:

- confirm inventory, owner, business value, user population, and current risk tier;
- review new models, features, agents, tools, subprocessors, data uses, incidents, vulnerabilities, limitations, and certifications;
- rerun context-specific evals and access/containment tests;
- review usage, exceptions, complaints, overrides, costs, and exit feasibility;
- accept, condition, reduce, suspend, replace, or retire.

## Useful external baselines

- [OMB M-25-22: Driving Efficient Acquisition of Artificial Intelligence in Government](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf)
- [Australian Government guidance on AI procurement](https://www.digital.gov.au/ai/ai-in-government-policy/preparedness-and-operations)
- [CSA AI Controls Matrix v1.1](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1)
- [NCSC Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development)
- [CycloneDX AI/ML Bill of Materials](https://www.cyclonedx.org/capabilities/mlbom/)
- [OECD Hiroshima AI Process Reporting Framework](https://oecd.ai/en/transparency/overview)
