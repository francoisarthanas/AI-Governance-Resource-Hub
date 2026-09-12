# 90-Day AI Governance Implementation Playbook

The goal is not to “finish governance” in 90 days. It is to create a working control loop, prove it on real systems, and establish an improvement backlog.

## Outcomes by day 90

- A governed inventory with owners and a discovery process.
- A risk taxonomy and intake with fast and enhanced review lanes.
- Clear decision authority, escalation, exception, and emergency-stop rules.
- A minimum control baseline embedded in delivery and procurement.
- At least two use cases taken through assessment, test, decision, and monitoring.
- Agent-specific identity, authorization, memory, tool, observability, and containment controls.
- Board/management and operational metrics based on evidence.
- A prioritized roadmap for regulatory, assurance, and tooling gaps.

## Days 0–15: establish authority and visibility

### Executive mandate

Approve a one-page charter that states scope, sponsor, governance lead, risk appetite, decision rights, budget, and how existing risk functions participate. Include AI acquired in SaaS, embedded features, employee use, APIs, models, and agents.

### Interim rules

Publish a short acceptable-use standard while the fuller program is built:

- approved tools and accounts;
- allowed and prohibited data;
- human verification expectations;
- prohibited or restricted uses;
- no unapproved tool/action integrations or agent credentials;
- IP, confidentiality, records, disclosure, and incident rules;
- a simple intake and help route.

### Inventory sprint

Seed the inventory from multiple sources:

- application/SaaS and procurement records;
- identity provider, CASB/SSE, browser, API gateway, cloud, expense, and network data;
- repositories, model registries, data-science platforms, and CI/CD;
- enterprise architecture and privacy records;
- team attestations, surveys, and interviews;
- agents, tool registries, service accounts, MCP servers, plugins, and automations.

Do not promise completeness. Record coverage, confidence, last attestation, and gaps.

### Select pathfinders

Choose one low-risk use that can demonstrate the fast lane and one material use that exercises multidisciplinary review. If agents are in scope, make one pathfinder a tightly bounded, read-only agent.

### Deliverables

- Charter and interim acceptable-use standard.
- Initial inventory and discovery backlog.
- Named pathfinders and accountable owners.
- Initial risk appetite and prohibited-use statement.
- Communication and training plan.

## Days 16–30: build the common decision process

### Risk classification

Define contextual risk factors:

- rights, safety, vulnerability, essential service, and decision impact;
- users, affected groups, scale, geography, and sector;
- data sensitivity, provenance, and privacy;
- model capability, opacity, and misuse potential;
- autonomy, tool access, delegation, memory, speed, and reversibility;
- external dependency, resilience, lock-in, and supply-chain risk;
- legal/regulatory role and classification.

Create three or four tiers and state decision authority, minimum controls, independent-review needs, and reassessment frequency for each.

### Intake and gates

Adopt a single intake that routes to existing experts. Define the artifacts at each lifecycle gate in [Operating Model](OPERATING-MODEL.md). Establish response targets and an exception process with expiry.

### Baseline controls

Tailor [`catalog/control-baseline.csv`](../catalog/control-baseline.csv). Map controls to existing enterprise control owners before assigning new owners.

### Deliverables

- Risk taxonomy and review lanes.
- Intake, impact assessment, and decision record.
- RACI/decision authority and service-level targets.
- Tailored minimum control baseline.
- Legal and regulatory applicability workflow.

## Days 31–60: prove the lifecycle on live systems

### Assess

For each pathfinder, complete:

- system/context map and AI system card;
- impact and privacy assessment as triggered;
- security/abuse threat model;
- supplier and contract review;
- evaluation and monitoring plan;
- agentic risk assessment and access matrix if applicable.

Use incidents from [OECD AIM](https://oecd.ai/en/incidents) and the [AI Incident Database](https://partnershiponai.org/workstream/ai-incidents-database/) to challenge assumptions with analogous failures.

### Verify

Test the complete system, not only a model endpoint. Include:

- task quality and failure behavior in representative contexts;
- disaggregated performance where people can be differently affected;
- privacy, security, abuse, and prompt-injection tests;
- tool and action authorization, idempotency, confirmation, and rollback;
- long-horizon, stateful, multi-turn, memory, and delegation tests for agents;
- operator workload, human override, appeal, fallback, and recovery drills;
- latency, availability, cost, rate, and resource exhaustion.

Record dataset/version, system configuration, seed or sampling method, evaluator, thresholds, results, failures, limitations, and decision.

### Decide and release

The decision record should say approved, conditionally approved, deferred, or rejected. It should name the owner, residual risks, conditions, expiry/review date, monitoring thresholds, and emergency authority.

### Deliverables

- Completed pathfinder evidence packs.
- Test results and resolved/accepted findings.
- Production monitoring and response routes.
- First formal decisions and lessons learned.

## Days 61–90: operationalize and assure

### Integrate into ordinary work

- Add AI questions and evidence to procurement, privacy, architecture, security, change, and release processes.
- Synchronize inventory with authoritative platforms where possible.
- Add policy and evaluation checks to delivery pipelines.
- Establish model/prompt/data/tool/version tracking and material-change triggers.
- Add AI and agent scenarios to incident response, business continuity, access review, and disaster recovery.

### Train by role

Give everyone basic permitted-use, data, verification, disclosure, and incident training. Add scenario-based training for owners, reviewers, builders, operators, procurement, executives, and incident responders. Test competence, not attendance alone.

### Measure and challenge

Report both enablement and risk:

- inventory coverage and unowned systems;
- review time by tier and rework rate;
- conditions/exceptions overdue;
- high-risk systems without current independent validation;
- agent permissions, dormant credentials, and unapproved tools;
- eval pass rates, significant regressions, incidents, near misses, complaints, and overrides;
- mean time to detect, contain, revoke, recover, and notify;
- realized value compared with the approved business case.

Run an independent design review using the [IIA AI Auditing Framework](https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework) or [GAO AI Accountability Framework](https://www.gao.gov/products/gao-21-519sp).

### Deliverables

- Embedded lifecycle and procurement changes.
- Role-based training and support.
- Management dashboard and operational measures.
- Independent review findings.
- 6–12 month prioritized roadmap with owners and funding.

## A practical evidence pack

For each material system, store a versioned evidence index linking to:

1. inventory and owner;
2. use-case intake and alternatives considered;
3. applicable obligations and risk classification;
4. system/context/data-flow diagram;
5. impact, privacy, security, safety, and supplier assessments;
6. system/model/data cards and AI/ML bill of materials;
7. requirements and controls, with owners and implementation evidence;
8. evaluation plan, datasets, runs, results, findings, and approvals;
9. deployment configuration, access, monitoring, and runbooks;
10. user/operator notices, instructions, fallback, and contest routes;
11. decision record, residual risk, conditions, and expiry;
12. changes, incidents, complaints, overrides, reviews, and retirement evidence.

Evidence should be reproducible enough for a qualified reviewer to understand what was approved and why.

## Tooling sequence

Do not lead with a platform procurement. First define the operating model, minimum data, owners, integrations, and evidence. Then automate the highest-friction or highest-risk gaps:

1. discovery and inventory synchronization;
2. intake, workflow, and evidence indexing;
3. model/prompt/data/tool versioning;
4. automated evals and release thresholds;
5. runtime policy, identity, authorization, and approval;
6. observability, anomaly detection, incident response, and reporting;
7. regulatory/control mapping and assurance reporting.

Avoid one-vendor claims of “continuous compliance” when the product cannot observe business context, human impacts, or decisions outside its integration boundary.
