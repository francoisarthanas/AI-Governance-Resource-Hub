# Start here

[← Resource hub](../README.md)

Choose the path that matches your next task. These are suggested learning sequences, not certifications or universal compliance checklists. Reading and reviewing the references requires no coding; running the technical tools may.

## If you have one hour

Use the hour to orient yourself and record questions, rather than trying to finish every source.

1. **10 minutes:** Watch the [NIST AI RMF explainer](LEARNING.md#nist-rmf-video) and identify the four functions.
2. **15 minutes:** Skim the executive summary and four dimensions of the [IMDA agentic framework](AGENTIC.md#imda-agentic-framework).
3. **15 minutes:** Choose one relevant case in the [AI Incident Database](RESEARCH.md#ai-incident-database) and inspect the underlying report.
4. **20 minutes:** Write down the system's purpose, affected people, accountable owner, allowed actions, required approvals, and evidence still missing.

The time boxes are suggested study allocations, not source runtimes.

## Learn the foundations

For newcomers, career changers, and colleagues who need a shared vocabulary.

| Step | Use this resource | Put it into practice |
|---|---|---|
| 1. Understand responsibilities and impacts | [University of Helsinki: Ethics of AI](LEARNING.md#ethics-of-ai) | Identify who benefits from an AI use case and who could be harmed. |
| 2. Organize risk management | [NIST AI RMF and Playbook](FOUNDATIONS.md#nist-ai-rmf) | Write one practical question under Govern, Map, Measure, and Manage. |
| 3. Challenge capability claims | [AI Snake Oil](BOOKS.md#ai-snake-oil-book) | Ask what evidence separates a persuasive demonstration from a suitable deployment. |
| 4. Understand assurance | [Introduction to AI Assurance](FOUNDATIONS.md#ai-assurance) | Distinguish a provider claim, a test result, an assessment, and independent review. |
| 5. Learn from failure | [AI Incident Database](RESEARCH.md#ai-incident-database) | Explain which decision or control assumption failed in one reported case. |

**Finish with:** a one-page explanation of a use case, its affected people, its main risks, and the evidence you would request.

For readers pursuing the professional credential, [IAPP AIGP training](LEARNING.md#aigp-training) is a paid structured option. It is not a prerequisite for using this hub.

## Build a governance program

For GRC teams, governance leads, auditors, and risk owners.

| Step | Use this resource | Put it into practice |
|---|---|---|
| 1. Establish the management structure | [ISO/IEC 42001](FOUNDATIONS.md#iso-42001) and [NIST AI RMF](FOUNDATIONS.md#nist-ai-rmf) | Define responsibilities, risk decisions, evidence owners, and management review. |
| 2. Assess impacts and suppliers | [OECD Due Diligence Guidance](FOUNDATIONS.md#oecd-due-diligence) | Follow adverse impacts through the value chain, including suppliers and remediation. |
| 3. Learn from real documentation | [UK Algorithmic Transparency Recording Standard](FOUNDATIONS.md#uk-atrs) and [Canada AIA](FOUNDATIONS.md#canada-aia) | Compare actual published records before designing your inventory and assessment fields. |
| 4. Check relevant requirements | [EU AI Act](FOUNDATIONS.md#eu-ai-act) and [ICO toolkit](FOUNDATIONS.md#ico-toolkit) | Establish jurisdiction, organizational role, applicability, and unresolved legal questions. |
| 5. Design a review that leaves evidence | [Closing the AI Accountability Gap](RESEARCH.md#internal-algorithmic-auditing) | Specify audit documents and who reviews them across the lifecycle. |

**Finish with:** a clear intake-to-review process, assigned owners, and a list of evidence needed for one deployment decision. The UK and Canadian examples are reusable models; their mandates do not automatically apply outside their stated scope.

Use [VerifyWise](TOOLS.md#verifywise) if you need a workspace to organize this information. The governance decisions still require accountable people.

## Review an AI agent

For anyone assessing an agent that can call tools, change records, communicate, spend money, or delegate.

| Step | Use this resource | Put it into practice |
|---|---|---|
| 1. Bound what it can do | [IMDA agentic framework](AGENTIC.md#imda-agentic-framework) | Record the allowed actions, permissions, autonomy, and reversibility of consequences. |
| 2. Define meaningful human control | [Practices for Governing Agentic AI Systems](AGENTIC.md#governing-agentic-systems) | Identify required approvals, escalation paths, interruption, and accountable owners. |
| 3. Inspect delegation | [Intelligent AI Delegation](AGENTIC.md#intelligent-delegation) | Explain what authority passes at a human-agent or agent-agent handoff. Treat the paper as a proposed framework. |
| 4. Define evidence and its limits | [Visibility into AI Agents](AGENTIC.md#agent-visibility) | Specify the identifiers, action records, oversight context, and privacy protections a reviewer needs. |
| 5. Check behavior and affected users | [Demystifying Evals for AI Agents](AGENTIC.md#agent-evals) and [The Ethics of Advanced AI Assistants](AGENTIC.md#ethics-ai-assistants) | Connect evaluations to authorized outcomes and examine impacts beyond cybersecurity. |

**Finish with:** an explanation of what the agent may do, what requires approval, how control can be withdrawn, and what evidence supports those claims. A successful task completion is only one part of that decision.

## Test controls and review evidence

For cybersecurity practitioners and reviewers working with technical teams.

| Step | Use this resource | Put it into practice |
|---|---|---|
| 1. Identify relevant threats | [OWASP Agentic Top 10](SECURITY.md#owasp-agentic-top10) and [MITRE ATLAS](SECURITY.md#mitre-atlas) | Build a short attack path relevant to the agent's actual tools and permissions. |
| 2. Review tool trust boundaries | [MCP Security Best Practices](SECURITY.md#mcp-security) and [the lethal trifecta](SECURITY.md#lethal-trifecta) | Examine how untrusted content might interact with private data and external communication. |
| 3. Choose the right test method | [PyRIT](TOOLS.md#pyrit), [Promptfoo](TOOLS.md#promptfoo), or [Inspect AI](TOOLS.md#inspect-ai) | Select targeted adversarial testing, regression checks, or full agent-task evaluation. Start with one. |
| 4. Inspect what happened | [Phoenix](TOOLS.md#phoenix) or the selected evaluator's own logs | Review actions and outcomes; explicitly capture authority and approval context where ordinary traces omit it. |
| 5. Check who experiences failure | [Fairlearn](TOOLS.md#fairlearn) and [Fairness and Machine Learning](BOOKS.md#fairness-book) | Assess relevant subgroup outcomes and explain the limits of chosen metrics. |

**Finish with:** a scoped test objective, acceptance criteria, observed results, limitations, and evidence from a remediation retest. Run adversarial exercises in an authorized test environment.

## Try one practical exercise

| Exercise | Resource | Useful output |
|---|---|---|
| Review a real system record without coding | [UK ATRS](FOUNDATIONS.md#uk-atrs) | Five unanswered governance questions grounded in an actual published record |
| Reconstruct a reported AI failure | [AI Incident Database](RESEARCH.md#ai-incident-database) | A timeline separating reported facts, missing evidence, and possible control failures |
| Compare an agent attack with a defense | [AgentDojo](TOOLS.md#agentdojo) | A comparison of legitimate task success and attack success; published examples can be studied before running code |
| Inspect an LLM safety test | [Project Moonshot](TOOLS.md#moonshot) | A test report with a plain-language explanation of coverage and limitations |
| Review a supplier's model documentation | [Model Cards](RESEARCH.md#model-cards) | A list of intended uses, exclusions, evaluation gaps, and follow-up evidence requests |

Choose an exercise that fits your access and skills. The goal is a better governance judgment backed by evidence.

