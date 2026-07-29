# AI Governance Operating Model

The purpose of the operating model is to make sound decisions at the speed and level where the work happens.

## Decision rights

| Decision | Accountable role | Required challenge |
|---|---|---|
| Approve the business purpose and risk tier | Business/system owner | Governance lead; legal/privacy/security/domain specialists as triggered |
| Accept residual business risk | Executive risk owner at the tier's delegated level | Independent second-line review for material/high risk |
| Approve data use | Data owner | Privacy, legal, security, records, and domain review as applicable |
| Approve model/vendor | Technology or product owner | Procurement, security, privacy, legal, resilience, and model-risk review |
| Approve agent permissions and tools | System owner and each resource owner | IAM/security; business process owner for action authority |
| Approve production release | Product/system owner | Evidence owners for every release condition; independent validation for high risk |
| Pause or shut down | Named incident commander and operations owner | No committee permission required when an emergency threshold is met |
| Resume after a material incident | Executive risk owner | Root-cause, corrective-action, retest, and affected-function sign-offs |
| Retire and delete | System and data owners | Records, legal hold, privacy, access revocation, and dependency checks |

No committee can absorb accountability from the owner. A governance forum supplies challenge, consistency, escalation, and a recorded decision.

## Risk-tiered lanes

### Tier 0 — Prohibited

The use is illegal, violates policy or rights, creates unacceptable risk, or lacks a credible control path. Record the rejection and prevent deployment.

### Tier 1 — Low

Internal, reversible, low-impact assistance using approved tools and non-sensitive data. Owner self-assessment plus automated policy checks can be sufficient. Sample and audit.

### Tier 2 — Moderate

Material business output, sensitive data, external users, or meaningful reliance. Require multidisciplinary review, documented testing, monitoring, and explicit release approval.

### Tier 3 — High/Critical

Rights-, safety-, financial-, legal-, employment-, healthcare-, infrastructure-, or similarly consequential use; high autonomy; broad privileged access; or regulated classification. Require specialist review, independent validation, executive risk acceptance, strict deployment constraints, continuous oversight, and enhanced incident readiness. Some cases remain prohibited.

Risk tier is contextual. Model size alone is not a risk tier.

## Lifecycle gates and evidence

| Gate | Decision | Minimum evidence |
|---|---|---|
| Intake | Is this a legitimate AI use case? | Owner, purpose, alternatives, users, affected people, initial system boundary |
| Triage | Which lane and obligations apply? | Inventory record, jurisdiction/sector scan, data and decision impact, autonomy level |
| Design | Are risks addressed by design? | Impact assessment, threat model, data flow, control plan, supplier assessment, human oversight design |
| Verify | Does evidence meet release criteria? | Representative evaluations, security tests, subgroup/context analysis, failure and recovery tests, open findings |
| Release | Who accepts the residual risk and conditions? | Signed decision, limitations, monitoring plan, user/operator instructions, incident and rollback plan |
| Operate | Is the approved case still true? | Metrics, samples, alerts, incidents, complaints, overrides, drift, cost, access reviews |
| Change | Is re-review or retest required? | Versioned change record and impact analysis for model/data/prompt/tool/policy/permission/context changes |
| Retire | Is access removed and evidence retained correctly? | Shutdown, credential revocation, dependency update, data disposition, archive/legal hold record |

## Three lines, adapted

- **First line — build and operate:** business, product, engineering, data, and operations own outcomes, controls, tests, documentation, and incidents.
- **Second line — set rules and challenge:** legal, compliance, privacy, security, model risk, enterprise risk, responsible AI, and safety define the framework and challenge evidence.
- **Third line — independent assurance:** internal audit assesses whether governance and controls are designed and operating effectively. It does not approve the system for management.

Smaller organizations can combine roles, but should preserve independent challenge for higher-risk decisions.

## Change triggers

Re-triage when any of these materially changes:

- purpose, user, affected population, geography, scale, or decision consequence;
- provider, base model, fine-tune, system prompt, retrieval corpus, evaluation set, or threshold;
- data source, classification, retention, residency, or lawful basis;
- tool, API, MCP/A2A integration, agent, delegation path, permission, credential, memory, or action budget;
- output presentation, human review, appeal, fallback, monitoring, or incident process;
- law, regulator guidance, contract, standard, known vulnerability, incident, or threat intelligence.

Define tolerances in advance so a harmless patch does not require the same process as a new consequential capability.

## Fast governance that still works

- Publish approved patterns and pre-cleared components.
- Use a short, common intake and trigger specialist questions only when relevant.
- Give Tier 1 a self-service lane with controls, expiration, and sampling.
- Hold reviewers to service-level targets and measure review rework.
- Shift controls into pipelines: inventory synchronization, policy checks, eval thresholds, access rules, artifact capture, and release blocks.
- Record exceptions with owner, rationale, compensating controls, expiry, and review date.
- Make the safe path easier than shadow AI.
