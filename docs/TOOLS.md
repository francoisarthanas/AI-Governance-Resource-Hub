# Projects and practical tools

[← Resource hub](../README.md) · [Start here](START-HERE.md)

Use these projects to organize governance work or generate evidence through inspection, testing, and evaluation. A tool's output still needs interpretation; installation alone does not establish compliance.

**10 selected resources**

- [VerifyWise](#verifywise)
- [AI Verify Toolkit](#ai-verify)
- [Project Moonshot](#moonshot)
- [Microsoft PyRIT](#pyrit)
- [NVIDIA garak](#garak)
- [Promptfoo](#promptfoo)
- [Inspect AI](#inspect-ai)
- [Arize Phoenix](#phoenix)
- [AgentDojo](#agentdojo)
- [Fairlearn](#fairlearn)

<a id="verifywise"></a>

### [VerifyWise](<https://github.com/verifywise-ai/verifywise>)

**Publisher:** VerifyWise / BlueWave Labs  
**Format:** Source-available web application · **Access:** BSL 1.1 source-available; internal self-hosting under its grant. External hosting requires a commercial license; infrastructure costs apply. Paid hosted plans.  
**For:** GRC, risk owners and governance teams; browser-based daily use, technical administration for self-hosting

**Why it matters:** Connects AI inventories, risks, controls, owners, evidence and approvals in a practical governance workspace.

**Put it into practice:** Register an AI use case, assign its owner, document risk treatment and attach test evidence; generate a review report. The workspace organizes evidence but does not establish compliance or control effectiveness by itself.

<a id="ai-verify"></a>

### [AI Verify Toolkit](<https://github.com/aiverify-foundation/aiverify>)

**Publisher:** AI Verify Foundation  
**Format:** Open-source testing toolkit and documentation · **Access:** Apache 2.0; no toolkit license fee; infrastructure and technical setup required  
**For:** AI assurance teams with ML/engineering support

**Why it matters:** Provides a structured route from responsible-AI principles to technical tests and process evidence for conventional machine learning.

**Put it into practice:** Test supported supervised classification/regression models using tabular or image data and assemble assurance evidence. Scope is not general autonomous-agent validation; use Moonshot for LLM application evaluation.

<a id="moonshot"></a>

### [Project Moonshot](<https://github.com/aiverify-foundation/moonshot>)

**Publisher:** AI Verify Foundation  
**Format:** Open-source evaluation toolkit with web UI, CLI and APIs · **Access:** Apache 2.0; local installation is free; connected model endpoints, LLM judges and compute may incur charges  
**For:** Compliance and assurance reviewers using a configured web UI; engineers configure endpoints and tests

**Why it matters:** Combines structured benchmarks and red-team testing with recipes and guided workflows for IMDA's LLM application safety testing starter kit.

**Put it into practice:** Run a chosen safety-test recipe, inspect an HTML report and export raw JSON results as review evidence. Benchmark coverage and grader accuracy must be judged for the actual use case.

<a id="pyrit"></a>

### [Microsoft PyRIT](<https://github.com/microsoft/PyRIT>)

**Publisher:** Microsoft  
**Format:** Open-source red-team framework, scanner and graphical interface · **Access:** MIT; framework is free; attacker, target and scoring model APIs or compute may cost money  
**For:** Security testers and engineers; human reviewers can use a configured CoPyRIT UI

**Why it matters:** Supports repeatable multi-turn adversarial campaigns with configurable targets, attack strategies, scoring and persistent evidence.

**Put it into practice:** Test a scoped failure objective, inspect conversations and scores, then rerun after remediation. Automated attack success labels require human validation and do not establish complete risk coverage.

<a id="garak"></a>

### [NVIDIA garak](<https://github.com/NVIDIA/garak>)

**Publisher:** NVIDIA / garak contributors  
**Format:** Open-source command-line scanner · **Access:** Apache 2.0; scanner is free; target API calls, local model hardware and compute can cost money  
**For:** Cybersecurity practitioners comfortable with terminal commands and endpoint configuration

**Why it matters:** Provides a practical baseline scan across prompt injection, leakage, jailbreaks and other unwanted LLM behaviors.

**Put it into practice:** Run selected probes against an authorized test endpoint and retain attempt-level JSONL records and failure rates. Pair broad scanning with application-specific agent tests; a clean scan is not proof of safety.

<a id="promptfoo"></a>

### [Promptfoo](<https://github.com/promptfoo/promptfoo>)

**Publisher:** Promptfoo  
**Format:** Open-source CLI/library with browser results viewer · **Access:** MIT core; free community tier; some hosted red-team generation/grading features have usage limits and paid enterprise options. Target/judge model API charges are separate.  
**For:** Engineers and technical assurance analysts; reviewers can inspect browser reports

**Why it matters:** Turns governance requirements into repeatable pass/fail checks that can run after prompt, model or application changes.

**Put it into practice:** Build a small test set for prohibited actions and required behavior, compare versions, and preserve results in release evidence. Review grader quality and cloud-backed data flows before using sensitive examples.

<a id="inspect-ai"></a>

### [Inspect AI](<https://inspect.aisi.org.uk/>)

**Publisher:** UK AI Security Institute and Meridian Labs  
**Format:** Open-source Python evaluation framework · **Access:** MIT; free framework; model APIs and sandbox infrastructure may incur charges  
**For:** Technical AI assurance teams and researchers; governance reviewers can inspect logs

**Why it matters:** Supports evaluating complete tool-using agent tasks with reusable datasets, scorers, sandboxing and detailed transcripts.

**Put it into practice:** Define an agent task and acceptance criteria, run it in a sandbox, and review the transcript with scores. Criteria and recorded context must cover delegated authority and approval requirements; the framework does not supply those governance judgments automatically.

<a id="phoenix"></a>

### [Arize Phoenix](<https://github.com/Arize-ai/phoenix>)

**Publisher:** Arize AI  
**Format:** Source-available tracing and evaluation application · **Access:** Elastic License 2.0 source-available; self-hosting permitted subject to license restrictions. Infrastructure and evaluator APIs may cost money; managed commercial products are separate.  
**For:** Engineers instrument applications; risk reviewers inspect traces and annotate evidence in the UI

**Why it matters:** Makes agent tool calls, retrieval, model calls and evaluation results inspectable so reviewers can investigate what happened.

**Put it into practice:** Trace an agent run, inspect tool activity, annotate failures and compare a corrected version on the same dataset. Explicitly record authority, policy versions and approvals; ordinary traces alone may not capture that context.

<a id="agentdojo"></a>

### [AgentDojo](<https://github.com/ethz-spylab/agentdojo>)

**Publisher:** ETH Zurich and Invariant Labs researchers  
**Format:** Open-source benchmark environment with paper and trace examples · **Access:** MIT; free benchmark code and published results; rerunning model-based tests may incur API/compute costs  
**For:** Technical security and assurance practitioners; non-coders can study published traces

**Why it matters:** Tests whether tool-using agents complete legitimate tasks while resisting prompt injection, making the utility/security tradeoff observable.

**Put it into practice:** Run or inspect a task under an attack and a defense; compare legitimate task success, attack success and the full action trace. Transfer findings cautiously: benchmark scenarios are not an enterprise's real controls or deployment environment.

<a id="fairlearn"></a>

### [Fairlearn](<https://fairlearn.org/>)

**Publisher:** Fairlearn contributors  
**Format:** Open-source Python library, examples and practitioner guide · **Access:** MIT; free library and learning materials; local data/compute required  
**For:** Data scientists and quantitative auditors; GRC practitioners can use the assessment guide with technical support

**Why it matters:** Provides methods for assessing differences in model performance and outcomes across groups, with guidance on mitigation and trade-offs.

**Put it into practice:** Compare error rates or outcomes across relevant groups, examine uncertainty and document mitigation tradeoffs. Fairness is context-dependent; a metric does not establish legal compliance, justice or due process.
