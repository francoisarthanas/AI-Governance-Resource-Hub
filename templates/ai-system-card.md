# AI System Card

> Document the complete deployed system, not only the model. Update on material change.

## Document control

- System record ID / name:
- Card version / date:
- System version/release:
- Status/environment:
- Business owner / technical owner / risk owner:
- Authors / reviewers / approver:
- Next review and material-change triggers:

## 1. Purpose and context

- Problem, intended outcome, and success measures:
- Intended users and affected parties:
- Intended, restricted, and prohibited uses:
- Operating environment, geography, sector, scale, and dependencies:
- Alternatives considered and why AI is appropriate:
- Risk tier and applicable obligations/standards:

## 2. System boundary and workflow

Attach a context/data-flow diagram and describe:

- user interfaces and upstream/downstream processes;
- models and providers;
- prompts/instructions and orchestration;
- training/fine-tuning, retrieval, context, and evaluation data;
- agents, sub-agents, tools, plugins, MCP servers, A2A peers, APIs, and devices;
- memory, caches, queues, vector stores, logs, and feedback loops;
- human decisions, approvals, overrides, appeals, and fallback;
- trust boundaries, external parties, and subprocessors.

## 3. Component and provenance record

| Component | Owner/provider | Version | Source/provenance | License/rights | Integrity check | Update process |
|---|---|---|---|---|---|---|
| | | | | | | |

Link the AI/ML-BOM if used.

## 4. Data governance

- Data purpose, classes, sources, owners, provenance, and quality:
- Personal/sensitive data, lawful authority/basis, consent where applicable:
- Collection, minimization, annotation, transformation, access, isolation, and lineage:
- Retention, deletion, residency, backup, recovery, and data-subject/affected-person processes:
- Provider use of prompts, outputs, telemetry, feedback, and customer data:
- Known gaps, bias, representativeness, contamination, poisoning, and rights constraints:

## 5. Model and behavior

- Model architecture/family and access method:
- Training/fine-tuning/retrieval approach known to the deployer:
- Capabilities and intended tasks:
- Known limitations, uncertainty, failure modes, unsafe behavior, and misuse potential:
- Explainability/interpretability and audience needs:
- Model/provider release and deprecation process:

Do not copy a provider model card without analyzing this use context.

## 6. Agentic behavior (if applicable)

- Authorized goals and maximum autonomy by action:
- Identity and principal/delegation chain:
- Allowed tools, resources, data, destinations, and credential scopes:
- Human approval points:
- Step/time/cost/retry/recursion/delegation/transaction limits:
- Memory types, write validation, retention, and deletion:
- Independent authorization, sandbox, egress, and validation controls:
- Pause, revoke, rollback, compensation, recovery, and decommissioning:

Link the agent assessment and access matrix.

## 7. Risks and controls

| Risk ID | Risk/affected party | Prevent | Detect | Respond/recover | Owner | Evidence | Residual risk |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Link impact, privacy, security, supplier, and risk-register records.

## 8. Evaluation and validation

- Requirements and acceptance thresholds:
- Evaluation datasets/cases, representativeness, protected holdouts, and version:
- Metrics, graders, uncertainty, subgroup/context analysis, and human review:
- Functional, safety, security, privacy, abuse, accessibility, human-factors, performance, resilience, and agent-trajectory tests:
- Production-like configuration and control coverage:
- Independent validation/red team scope:
- Results, failed cases, limitations, remediation, and retest:

Link reproducible test evidence.

## 9. Deployment and operations

- Release process and approved configuration:
- Monitoring signals, outcomes, thresholds, dashboards, and owners:
- User/operator instructions, disclosure, support, contest, appeal, and remedy:
- Incident severity, route, pause authority, evidence, notification, and recovery:
- Change control, drift, revalidation, access review, and supplier review:
- Business continuity, manual fallback, and retirement:

## 10. Decision and limitations

- Decision: approved / conditional / deferred / rejected / retired
- Approved scope and conditions:
- Residual risks and acceptance owner:
- Known limitations to communicate:
- Expiry/next review:
- Decision record link:
