# Start Here: From Zero to a Governed AI Use Case

This is the shortest credible path. It creates control without making every experiment wait for a committee.

## The first 60 minutes

### 1. Name one accountable owner

Choose the person who owns the business outcome and can accept, reduce, or reject risk. A project manager, vendor, model, or “the AI team” is not an accountable owner.

### 2. Put the system in the inventory

Copy [`templates/ai-inventory.csv`](../templates/ai-inventory.csv). Record the use case, owner, users, affected people, deployment status, model/provider, data classes, decision impact, geography, and whether it can act.

Inventory at the **use-case/system** level, not only the model level. One model can power many differently risky uses. Also capture embedded vendor AI, employee tools, retrieval systems, fine-tunes, APIs, automations, and agents.

### 3. Decide whether AI is appropriate

Complete [`templates/ai-use-case-intake.md`](../templates/ai-use-case-intake.md). Ask:

- What measurable problem are we solving?
- Could a deterministic rule, ordinary automation, or process change solve it more safely?
- Who benefits, who can be harmed, and who can contest the result?
- What happens when it is wrong, unavailable, manipulated, or misused?
- Is the proposed human review timely, informed, empowered, and realistic at expected volume?

### 4. Triage the risk

Escalate the use case when any answer is “yes”:

- It affects rights, access, eligibility, employment, credit, insurance, healthcare, education, law enforcement, essential services, safety, or critical infrastructure.
- It uses sensitive, confidential, regulated, biometric, children's, or third-party data.
- It profiles people, infers sensitive traits, or produces consequential recommendations.
- It is public-facing at scale or can create convincing content in a high-impact context.
- It is hard to reverse, explain, contest, or correct.
- It can call tools, spend money, send communications, change records, write code, operate equipment, create sub-agents, or delegate work.
- The provider, data provenance, model behavior, or supply chain is insufficiently transparent.

High risk is not automatically “no.” It means stronger expertise, evidence, approvals, safeguards, testing, monitoring, and sometimes a legal prohibition.

### 5. Set the release conditions

For a low-risk pilot, require at least:

- a named owner and approved users;
- an explicit purpose and prohibited-use boundary;
- approved data classes and retention rules;
- a non-production or contained environment;
- representative acceptance tests and recorded results;
- a feedback and incident route;
- a stop date or review date;
- no unreviewed consequential or irreversible actions.

For anything higher risk, complete the impact assessment and obtain the relevant legal, privacy, security, safety, accessibility, records, procurement, domain, and affected-stakeholder reviews.

## If the system is an agent

Treat it as an active workload and a delegated identity—not as a chatbot with a longer prompt.

Before it touches a real system:

1. Give it a unique identity; do not share a human or blanket service account.
2. Allow only named tools and the smallest task-specific scopes.
3. Use short-lived, audience-bound credentials; never place secrets in prompts or memory.
4. Default to read-only. Put human approval before external, privileged, financial, destructive, legal, safety, or irreversible actions.
5. Cap steps, runtime, retries, recursion, spend, tokens, calls, and delegation depth.
6. Isolate execution and constrain network/file access.
7. Validate tool inputs and outputs independently of the model.
8. Log the request, model/version, policy decision, tool calls, approvals, state changes, and outcome. Do not rely on hidden chain-of-thought.
9. Test prompt injection, poisoned context, tool spoofing, memory poisoning, privilege escalation, runaway loops, and failure recovery.
10. Prove that operators can pause, revoke, roll back, contain, and recover.

Use the full [Agentic AI Governance guide](AGENTIC-AI-GOVERNANCE.md).

## The first week

- Appoint an executive sponsor and day-to-day governance lead.
- Publish one intake path and one temporary acceptable-use standard.
- Start an inventory campaign across procurement, SSO/CASB logs, expense data, engineering, data science, SaaS owners, and staff declarations.
- Define three or four risk tiers with service-level targets and decision authority.
- Select a program backbone: usually NIST AI RMF; add ISO/IEC 42001 if a management system or certification is a goal.
- Reuse privacy, cyber, model risk, product safety, legal, procurement, records, and internal-audit processes instead of building a parallel universe.
- Select two live use cases: one low-risk pathfinder and one meaningful higher-risk case.

## Avoid these common failures

- **A principles-only program:** values without gates, owners, tests, and evidence do not control anything.
- **A model-only inventory:** risk depends on context, users, data, integrations, and decisions.
- **“Human in the loop” as a label:** reviewers need time, competence, information, authority, and a workable override path.
- **One-time approval:** model, data, prompt, tool, provider, permission, and context changes can invalidate the decision.
- **Prompt-only guardrails:** agents require independent authorization, isolation, validation, observability, and containment.
- **Compliance by crosswalk:** mappings help reuse controls; they do not prove legal conformity or standard certification.
- **A giant board for every use:** low-risk experiments need a fast lane; high-risk systems need real multidisciplinary challenge.

## Your minimum outputs

At the end of initial review, you should have:

- one inventory record;
- a completed intake and risk tier;
- a system card and impact assessment proportional to risk;
- documented approval, conditions, and residual risk owner;
- test plan and results tied to real requirements;
- monitoring, incident, change, and retirement triggers;
- supplier evidence and contract protections where applicable;
- agent access, action, memory, budget, and shutdown evidence where applicable.

Continue with the [90-day implementation playbook](IMPLEMENTATION-PLAYBOOK.md).
