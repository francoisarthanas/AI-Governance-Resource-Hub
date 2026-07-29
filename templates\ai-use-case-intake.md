# AI Use-Case Intake

> Complete enough to route the work. Do not force low-risk ideas to answer questions that belong in enhanced review.

## 1. Request

- Intake ID:
- Date / requested decision date:
- Requester and team:
- Accountable business owner:
- Technical owner:
- Proposed lifecycle status: idea / experiment / pilot / production / material change / renewal / retirement

## 2. Problem and value

- What problem or user need will this solve?
- What measurable outcome and baseline will show value?
- Why use AI rather than a deterministic rule, ordinary automation, search, process change, or additional human capacity?
- What is the smallest, safest useful scope?
- What would make us stop or not proceed?

## 3. System and workflow

- Describe the AI's role in the end-to-end workflow.
- AI type: predictive / classification / recommendation / generative / multimodal / agentic / other
- Provider/product/model and version if known:
- Build, buy, open source, or embedded vendor feature:
- Users and expected volume:
- People or groups directly/indirectly affected:
- Output, recommendation, decision, or action:
- External-facing? At what scale?
- Geographies and sector/regulatory context:

Attach a draft system/context/data flow if material.

## 4. Data

- Inputs, sources, owners, and provenance:
- Personal, sensitive, confidential, regulated, children's, biometric, health, financial, employment, or third-party data:
- Training, fine-tuning, retrieval, prompt, telemetry, feedback, and output data uses:
- Proposed retention, deletion, residency, access, and onward sharing:
- Intellectual-property, confidentiality, consent, or licensing constraints:

## 5. Decisions, actions, and human role

- What will people rely on the system to decide or do?
- What happens if it is wrong, unavailable, manipulated, discriminatory, or misused?
- Is the result reversible, correctable, explainable, contestable, and appealable?
- Human role before, during, and after use:
- Can the human realistically detect a bad result and intervene at expected speed/volume?

## 6. Agentic capabilities

Complete if the system plans or acts:

- Goals and non-goals:
- Read tools/data sources:
- State-changing tools/actions:
- Systems, networks, files, recipients, and environments reachable:
- Identity and credentials used:
- Persistent memory and cross-session state:
- Can it delegate, create sub-agents, modify goals, write/execute code, spend money, send communications, change records, or operate devices?
- Maximum action impact and reversibility:
- Proposed human approval gates and execution limits:

Attach [`agentic-risk-assessment.md`](agentic-risk-assessment.md) for any production agent.

## 7. Initial risk triggers

Mark yes/no/unknown and explain every yes or unknown.

- [ ] Rights, eligibility, employment, credit, insurance, healthcare, education, law enforcement, essential services, safety, or critical infrastructure
- [ ] Profiling, sensitive inference, biometrics, emotion recognition, or vulnerable/child population
- [ ] Personal/sensitive/confidential/regulated data or uncertain data rights/provenance
- [ ] External or high-scale content, recommendation, decision, or action
- [ ] Material financial, legal, physical, reputational, democratic, or environmental consequence
- [ ] Difficult to reverse, explain, contest, correct, or provide human fallback
- [ ] Autonomous tool use, privileged access, persistent memory, delegation, code execution, or irreversible action
- [ ] New/unproven provider, model, capability, protocol, integration, or open-source supply chain
- [ ] Known analogous incidents, high misuse/abuse potential, or credible adversary interest
- [ ] Cross-border use or uncertain legal/regulatory role/classification

## 8. Existing evidence

- Provider/system/model/data documentation:
- Security/privacy/compliance reports:
- Test/evaluation results:
- Supplier and contract records:
- Prior approvals or similar approved pattern:

## 9. Routing decision (governance use)

- Inventory record ID:
- Risk tier and rationale:
- Prohibited? If yes, authority and rationale:
- Required reviewers:
- Required assessments/evidence:
- Pilot constraints:
- Decision authority:
- Target review service level:
- Next action, owner, and due date:
