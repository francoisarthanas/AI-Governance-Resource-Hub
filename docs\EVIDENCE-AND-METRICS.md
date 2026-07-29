# Evidence and Metrics

The program should be able to show what was known, what was tested, who decided, what remains risky, and whether controls continue to work.

## Evidence principles

- **Decision-useful:** every artifact supports a decision or control.
- **System-specific:** generic policy is not evidence that a deployed system complies with it.
- **Versioned:** tie evidence to model, prompt, data, code, tool, policy, configuration, and environment.
- **Reproducible:** retain enough method, input, configuration, and result detail for qualified review.
- **Attributable:** name the preparer, reviewer, approver, owner, date, and source.
- **Tamper-evident and access-controlled:** assurance evidence may contain high-value security, personal, or confidential information.
- **Proportionate:** deeper evidence for higher impact, autonomy, uncertainty, and irreversibility.
- **Fresh:** define expiry and material-change triggers.

## Evidence index

For each material system, maintain an index with:

| Area | Examples |
|---|---|
| Authority | Charter, owner, RACI, decision rights, risk appetite |
| Scope | Inventory record, use case, users, affected parties, system/context/data flow, alternatives |
| Applicability | Jurisdictions, roles, classification, obligations, standards, contract requirements |
| Risk | Impact, privacy, security, safety, abuse, human-rights, accessibility, supplier assessments |
| Components | System/model/data cards, prompts, retrieval, agents, tools, dependencies, AI/ML-BOM |
| Controls | Control owner, design, implementation, configuration, exception, compensating control |
| Verification | Requirements, test cases/data, runs, results, findings, remediation, independent validation |
| Release | Decision, conditions, limitations, residual risk, owner, expiry/review date |
| Operations | Monitoring, samples, alerts, complaints, appeals, overrides, access reviews, incidents, changes |
| Resilience | Fallback, business continuity, shutdown, revocation, rollback, recovery drills |
| Retirement | Dependency analysis, disablement, credential revocation, data disposition, archive/legal hold |

## Metrics that matter

Pair every metric with a definition, data source, owner, frequency, threshold, segmentation, and action. A green dashboard without a response rule is decoration.

### Coverage and ownership

- percentage of in-scope systems inventoried and attested;
- percentage with current accountable business and technical owners;
- discovery confidence and unresolved shadow-AI leads;
- percentage with current risk tier, applicable-obligation review, and evidence index;
- agent identities, tools, privileges, and persistent memories without owners or expiry.

### Flow and enablement

- time from intake to decision by tier;
- percentage routed through the fast lane;
- review rework caused by missing evidence;
- blocked experiments and reason;
- approved-pattern reuse;
- realized value, quality, adoption, cost, and user satisfaction versus baseline.

### Control health

- overdue conditions, exceptions, access reviews, revalidations, and retirements;
- high-risk systems without current independent validation;
- material changes deployed before required review/retest;
- percentage of agent actions with valid principal, authorization, approval, and trace;
- dormant/overprivileged agent credentials and unapproved tools/endpoints;
- recovery and shutdown tests completed successfully.

### Performance and impact

- task success and critical failure rate in representative contexts;
- false positive/negative rates and error severity;
- subgroup/context disparities and confidence intervals where appropriate;
- abstention, escalation, human override, appeal, and correction outcomes;
- affected-user complaints, harm reports, accessibility failures, and remedy time;
- agent wrong-tool, wrong-parameter, unauthorized-action, loop, and rollback rates.

### Security, safety, and incidents

- critical/high findings open past target;
- adversarial and abuse test coverage/pass rate;
- prompt injection, policy-denial, exfiltration, tool-spoofing, or anomaly signals;
- incidents and near misses by severity, cause, system, supplier, and affected group;
- mean time to detect, decide, pause, revoke, contain, recover, correct, and notify;
- recurrence rate and percentage of incidents converted into regression tests.

### Human oversight

- reviewer load and time available per decision;
- reviewer agreement, override rate, missed-failure rate, and automation-bias indicators;
- percentage of consequential actions that received timely, informed approval;
- operator training competence and drill performance.

## Board and executive dashboard

Keep it decision-focused:

1. AI portfolio by risk, value, status, autonomy, and critical dependency.
2. Top residual risks and decisions required.
3. High-risk/agentic systems with stale evidence or failed thresholds.
4. Material incidents, near misses, harms, complaints, and lessons.
5. Control exceptions and overdue remediation.
6. External change: law, regulator, standard, provider, threat, or concentration risk.
7. Capability and resource constraints.
8. Value realized and systems to expand, revise, suspend, or retire.

Do not report only counts of models, policies, training completions, or meetings.

## Independent assurance

Assurance should test both design and operating effectiveness:

- Is the control capable of addressing the stated risk?
- Is it implemented in the production system and process?
- Did it operate for the sampled period, including exceptions and incidents?
- Is evidence complete, accurate, protected, and tied to the approved version?
- Could management override it, and were overrides governed?
- Is the residual risk still within authority and appetite?

Use the [IIA AI Auditing Framework](https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework), [GAO AI Accountability Framework](https://www.gao.gov/products/gao-21-519sp), and relevant standards/regulator guidance. Independence, competence, access, scope, and method matter more than an “AI audit” label.

## Anti-metrics

These can mislead when reported alone:

- policies published;
- people trained or completion rate;
- models/tests/prompts run;
- benchmark score without context or uncertainty;
- tools purchased;
- systems “compliant” based on a questionnaire;
- zero incidents where detection/reporting is weak;
- human approvals without workload or decision-quality evidence.
