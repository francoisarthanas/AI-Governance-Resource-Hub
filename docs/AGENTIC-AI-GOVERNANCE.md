# Agentic AI Governance: Production Control Guide

An agent is not governed because its base model passed a benchmark. Risk emerges from the complete system: goals, orchestration, tools, credentials, memory, data, environment, other agents, human oversight, and the real-world consequences of actions.

Use this guide for any system that autonomously plans or executes multiple steps, selects tools, changes state, delegates, maintains memory, or acts on behalf of a person or organization.

## The control model

```text
Human authority
  -> delegated task and limits
    -> agent identity and policy decision
      -> bounded plan/orchestration
        -> approved tool + scoped credential
          -> validated action + approval when required
            -> observable result + evidence
              -> feedback, incident, change, or shutdown
```

Every transition is a trust boundary.

## 1. Purpose, ownership, and autonomy

- Name the business owner, technical owner, risk owner, and 24/7 operational owner where needed.
- Write the agent's authorized job, users, affected parties, environments, data, tools, outputs, and explicit non-goals.
- Demonstrate why nondeterministic autonomy is justified over deterministic workflow automation.
- Classify autonomy per action, not with one label for the whole agent.

| Level | Behavior | Default governance |
|---|---|---|
| A0 | Advice/content only; no tool execution | Ordinary GenAI controls and human verification |
| A1 | Read-only retrieval from approved sources | Scoped identity, data controls, logging, injection testing |
| A2 | Drafts or prepares state changes; human executes | Preview, provenance, independent validation, user confirmation |
| A3 | Executes reversible, bounded actions | Per-action authorization, limits, monitoring, rollback, sampled review |
| A4 | Executes consequential or difficult-to-reverse actions | Human approval at the point of action, strong independent verification, enhanced assurance |
| A5 | Broad or open-ended autonomy | Presumptively prohibited unless a compelling case and exceptional controls exist |

The level should increase with permission, impact, speed, scale, delegation, unpredictability, and irreversibility.

## 2. Agent identity and delegated authority

- Give every production agent and sub-agent a unique, attributable non-human identity.
- Do not let agents borrow a user's full session or share blanket service accounts.
- Preserve the delegation chain: principal, initiating user/service, agent, sub-agent, tool, and affected resource.
- Bind tokens to the intended resource/audience and task context; use short-lived credentials and just-in-time elevation.
- Separate read, propose, approve, and execute roles for consequential actions.
- Re-evaluate authorization at execution time. The model's decision to call a tool is not authorization.
- Review and revoke agent identities, tools, scopes, and dormant credentials on a defined cadence.

For MCP deployments, use the current [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) and [NSA MCP security guidance](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/). Treat token passthrough, confused-deputy conditions, dynamic client registration, tool metadata, and local server execution as explicit threats.

## 3. Tools and action safety

Maintain an approved tool registry with owner, version, source, description, input/output schema, permissions, data classes, side effects, rate limits, dependency chain, and security review.

- Default tools to read-only and non-production.
- Allowlist tools and operations; do not grant arbitrary shell, browser, database, cloud, email, or payment access without narrow constraints.
- Treat tool names, descriptions, schemas, returned content, webpages, documents, emails, RAG chunks, and other-agent messages as untrusted input.
- Validate and canonicalize parameters outside the model. Use deterministic business rules for amounts, recipients, resources, and destinations.
- Show the human the exact action, target, data disclosed, and consequence at approval time. Reject stale or materially changed approvals.
- Use idempotency keys, transaction limits, two-person control, reversible operations, soft deletion, and delayed execution where appropriate.
- Separate secrets from prompts, context, memory, logs, and model-visible configuration.
- Pin and verify dependencies and tool endpoints; detect tool substitution and capability changes.

## 4. Bounded execution

Enforce independent limits on:

- elapsed time, steps, model/tool calls, tokens, cost, retries, and loop count;
- recursion and sub-agent/delegation depth;
- concurrent tasks and fan-out;
- network destinations, file paths, database rows, records, recipients, and transaction value;
- data volume, sensitivity, and cross-boundary transfer;
- calendar window, geographic region, tenant, and environment;
- goal modification and self-replication.

Crossing a limit should fail safe, preserve evidence, and route to a human—not invite the agent to rewrite the limit.

## 5. Data, context, and memory

- Classify and minimize every context source.
- Define what can enter working context, short-term state, long-term memory, logs, traces, caches, vector stores, and training/feedback pipelines.
- Record provenance, tenant, owner, purpose, sensitivity, creation time, expiry, and integrity for persistent memory.
- Separate instructions from untrusted content and keep authorization facts outside model-controlled text.
- Prevent cross-user, cross-task, and cross-tenant memory leakage.
- Require validation before an agent writes durable memory; make memory inspectable, correctable, and deletable.
- Test memory poisoning, stale facts, unauthorized inference, retrieval manipulation, and right-to-delete/retention behavior.

## 6. Orchestration and multi-agent systems

- Use the smallest number of agents that produces a measurable benefit. Multi-agent design adds identity, delegation, state, failure, and observability complexity.
- Define a contract for each agent: inputs, outputs, tools, authority, data, error behavior, and handoff conditions.
- Authenticate peers and verify advertised capabilities. Agent cards or capability descriptions are claims, not trust decisions.
- Constrain which agents may communicate and what context may cross each boundary.
- Carry provenance and policy obligations across handoffs.
- Prevent circular delegation, responsibility laundering, collusion, unbounded voting, and amplification of one corrupted message.
- Make a named orchestrator or deterministic workflow engine responsible for state, approvals, retries, timeouts, compensation, and termination.

Review the current [A2A specification](https://a2a-protocol.org/latest/specification/) for interoperability controls, but treat protocol conformance as only one layer of security.

## 7. Human oversight that is real

Choose the oversight mode per action:

- **Human-in-the-loop:** approval before execution. Use for consequential, privileged, novel, or difficult-to-reverse actions.
- **Human-on-the-loop:** live supervision with pause/override. Use only when the operator can understand and intervene at machine speed.
- **Post-action review:** sampling or audit after bounded, reversible, lower-risk actions.
- **Human-out-of-the-loop:** exceptional; document why the residual risk is acceptable and how independent constraints and shutdown work.

Measure approval load, time to review, override frequency, automation bias, reviewer agreement, missed failures, and whether operators can actually act.

## 8. Evaluation and assurance

Test the system and trajectories, not only final answers.

### Functional

- task success, partial completion, correct tool choice and parameters;
- state transitions, idempotency, retry and compensation behavior;
- calibrated uncertainty, escalation, abstention, and fallback;
- cost, latency, resource use, and long-horizon reliability.

### Safety and security

- direct and indirect prompt injection;
- goal hijacking, instruction conflicts, jailbreaks, and specification gaming;
- tool/agent impersonation, malicious metadata, poisoned RAG and memory;
- excessive agency, privilege escalation, credential theft, and data exfiltration;
- unsafe code, sandbox escape, SSRF, output injection, and supply-chain compromise;
- runaway loops, denial of wallet/service, delegation cascades, and coordinated failure;
- shutdown resistance, incomplete rollback, audit evasion, and recovery.

### Socio-technical

- performance across affected populations and realistic contexts;
- user comprehension, disclosure, consent where applicable, contest, and remedy;
- operator workload, automation bias, and accessibility;
- downstream and cumulative impact, abuse, and dual use.

Use an independent evaluator or validation function for higher-risk systems. Keep test cases protected where gaming or contamination is a concern. See [Anthropic's agent eval guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [Inspect](https://inspect.aisi.org.uk/), [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), and [MITRE ATLAS](https://atlas.mitre.org/).

## 9. Observability and evidence

Capture enough to reconstruct the action without storing unnecessary sensitive data:

- initiating principal, user/service, agent and sub-agent identities;
- time, purpose/task ID, policy and configuration version;
- model/provider/version, prompt/instruction template version, retrieval and memory references;
- tool discovery, selected tool, parameters (redacted where needed), authorization decision, credential scope, approval, response, and state change;
- limits, guardrail decisions, errors, retries, overrides, outcome, and rollback;
- data lineage and evidence integrity.

Record concise decision rationale or structured action summaries when useful. Do **not** depend on private chain-of-thought as an audit mechanism. Protect logs against tampering and unauthorized access; set retention by purpose and law.

Monitor both known thresholds and unknown behavior: unusual tool sequences, new destinations, permission denials, repeated retries, rising costs, action velocity, memory changes, cross-tenant access, and deviations from approved trajectories.

## 10. Containment, recovery, and incidents

Before release, prove that authorized operators can:

- pause a task and globally disable the agent;
- revoke identities, credentials, sessions, tools, network paths, and scheduled work;
- isolate affected hosts, data, memory, queues, and downstream agents;
- cancel or compensate pending actions;
- restore the last known safe state and validate recovery;
- preserve evidence and identify affected users, systems, data, and transactions;
- notify required internal and external parties;
- prevent automated restart until authorized.

Run tabletop and technical exercises. A dashboard “kill switch” that depends on the compromised agent or the same control plane is not sufficient.

## Minimum release bar

No production release unless all statements are true:

- [ ] The owner, authorized purpose, autonomy per action, prohibited behavior, and risk tier are documented.
- [ ] Each agent has a unique identity and every tool/action has independently enforced least privilege.
- [ ] High-impact actions require current, informed human approval or a formally accepted exception.
- [ ] Data and memory are minimized, separated, traceable, and subject to retention/deletion controls.
- [ ] Execution and delegation are bounded with fail-safe limits.
- [ ] Untrusted content cannot directly confer authority or silently change policy.
- [ ] Representative functional, adversarial, long-horizon, and recovery tests meet approved thresholds.
- [ ] The system is observable end to end without relying on hidden reasoning.
- [ ] Pause, revoke, contain, rollback, recover, and incident routes have been exercised.
- [ ] Model, prompt, data, tool, permission, protocol, and orchestration changes trigger proportionate retest.
- [ ] Residual risks, limitations, conditions, review date, and decision authority are recorded.

Use [`templates/agentic-risk-assessment.md`](../templates/agentic-risk-assessment.md), [`templates/agent-access-matrix.csv`](../templates/agent-access-matrix.csv), and [`templates/agent-evaluation-plan.md`](../templates/agent-evaluation-plan.md) to create the evidence.

## Primary references

- [Singapore Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf)
- [Australian Government Agentic AI Addendum](https://www.digital.gov.au/policy/ai/agentic-ai-addendum-introduction)
- [Joint Five Eyes guidance: Careful Adoption of Agentic AI Services](https://www.cyber.gc.ca/en/news-events/joint-guidance-careful-adoption-agentic-artificial-intelligence-services)
- [NIST AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Google Secure AI Framework—Agents](https://saif.google/focus-on-agents)
- [OpenAI Practical Guide to Building Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
