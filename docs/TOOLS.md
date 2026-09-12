# Projects and practical tools

[← Resource hub](../README.md) · [Start here](START-HERE.md)

Use these projects to organize governance work or generate evidence through inspection, testing, and evaluation. A tool's output still needs interpretation; installation alone does not establish compliance.

**10 selected resources · Catalog reviewed 2026-09-12.**

<!-- Generated from catalog/resources.json. Edit the catalog, then run python scripts/generate_catalog.py. -->

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

**Why it earns a place:** Connects AI inventories, risks, controls, owners, evidence and approvals in a practical governance workspace.

**Use it to:** Register an AI use case, assign its owner, document risk treatment and attach test evidence; generate a review report. The workspace organizes evidence but does not establish compliance or control effectiveness by itself.

**Version / status:** Current repository and license inspected 2026-09-12; default branch develop  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Canonical project and non-archived status checked. README documents inventories, risks, controls, evidence and reports. The [license](https://github.com/verifywise-ai/verifywise/blob/develop/LICENSE.md) restricts the additional production-use grant to internal operations.

</details>

<a id="ai-verify"></a>

### [AI Verify Toolkit](<https://github.com/aiverify-foundation/aiverify>)

**Publisher:** AI Verify Foundation  
**Format:** Open-source testing toolkit and documentation · **Access:** Apache 2.0; no toolkit license fee; infrastructure and technical setup required  
**For:** AI assurance teams with ML/engineering support

**Why it earns a place:** Provides a structured route from responsible-AI principles to technical tests and process evidence for conventional machine learning.

**Use it to:** Test supported supervised classification/regression models using tabular or image data and assemble assurance evidence. Scope is not general autonomous-agent validation; use Moonshot for LLM application evaluation.

**Version / status:** 2.0 documentation linked in current repository; checked 2026-09-12  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official metadata archived=false. README explicitly states supported model/data types and that testing does not guarantee freedom from risks or bias or complete safety.

</details>

<a id="moonshot"></a>

### [Project Moonshot](<https://github.com/aiverify-foundation/moonshot>)

**Publisher:** AI Verify Foundation  
**Format:** Open-source evaluation toolkit with web UI, CLI and APIs · **Access:** Apache 2.0; local installation is free; connected model endpoints, LLM judges and compute may incur charges  
**For:** Compliance and assurance reviewers using a configured web UI; engineers configure endpoints and tests

**Why it earns a place:** Combines structured benchmarks and red-team testing with recipes and guided workflows for IMDA's LLM application safety testing starter kit.

**Use it to:** Run a chosen safety-test recipe, inspect an HTML report and export raw JSON results as review evidence. Benchmark coverage and grader accuracy must be judged for the actual use case.

**Version / status:** README identifies version 0.7.6; checked 2026-09-12  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official metadata archived=false. README verifies web/CLI interfaces, starter-kit integration, HTML reports and JSON exports. Results support an assessment, not legal certification.

</details>

<a id="pyrit"></a>

### [Microsoft PyRIT](<https://github.com/microsoft/PyRIT>)

**Publisher:** Microsoft  
**Format:** Open-source red-team framework, scanner and graphical interface · **Access:** MIT; framework is free; attacker, target and scoring model APIs or compute may cost money  
**For:** Security testers and engineers; human reviewers can use a configured CoPyRIT UI

**Why it earns a place:** Supports repeatable multi-turn adversarial campaigns with configurable targets, attack strategies, scoring and persistent evidence.

**Use it to:** Test a scoped failure objective, inspect conversations and scores, then rerun after remediation. Automated attack success labels require human validation and do not establish complete risk coverage.

**Version / status:** Official documentation currently redirects to 1.1.0; checked 2026-09-12  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official non-archived repository and documentation reviewed. Documentation covers single- and multi-turn attacks, the interface, persistent records, and exported conversations and scores. The canonical repository is microsoft/PyRIT.

</details>

<a id="garak"></a>

### [NVIDIA garak](<https://github.com/NVIDIA/garak>)

**Publisher:** NVIDIA / garak contributors  
**Format:** Open-source command-line scanner · **Access:** Apache 2.0; scanner is free; target API calls, local model hardware and compute can cost money  
**For:** Cybersecurity practitioners comfortable with terminal commands and endpoint configuration

**Why it earns a place:** Provides a practical baseline scan across prompt injection, leakage, jailbreaks and other unwanted LLM behaviors.

**Use it to:** Run selected probes against an authorized test endpoint and retain attempt-level JSONL records and failure rates. Pair broad scanning with application-specific agent tests; a clean scan is not proof of safety.

**Version / status:** Current main README inspected 2026-09-12; pin a release when reproducing tests  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official metadata archived=false. README verifies probe categories, endpoint support, command-line usage, and per-attempt JSONL reports. Separate role from PyRIT: breadth of packaged scanning versus custom adversarial campaigns.

</details>

<a id="promptfoo"></a>

### [Promptfoo](<https://github.com/promptfoo/promptfoo>)

**Publisher:** Promptfoo  
**Format:** Open-source CLI/library with browser results viewer · **Access:** MIT core; free community tier; some hosted red-team generation/grading features have usage limits and paid enterprise options. Target/judge model API charges are separate.  
**For:** Engineers and technical assurance analysts; reviewers can inspect browser reports

**Why it earns a place:** Turns governance requirements into repeatable pass/fail checks that can run after prompt, model or application changes.

**Use it to:** Build a small test set for prohibited actions and required behavior, compare versions, and preserve results in release evidence. Review grader quality and cloud-backed data flows before using sensitive examples.

**Version / status:** Current README, FAQ and pricing inspected 2026-09-12  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official non-archived repository, license, pricing and FAQ reviewed. The MIT core is distinct from paid enterprise features and limited hosted services; some modes transmit test data for generation, grading or sharing.

</details>

<a id="inspect-ai"></a>

### [Inspect AI](<https://inspect.aisi.org.uk/>)

**Publisher:** UK AI Security Institute and Meridian Labs  
**Format:** Open-source Python evaluation framework · **Access:** MIT; free framework; model APIs and sandbox infrastructure may incur charges  
**For:** Technical AI assurance teams and researchers; governance reviewers can inspect logs

**Why it earns a place:** Supports evaluating complete tool-using agent tasks with reusable datasets, scorers, sandboxing and detailed transcripts.

**Use it to:** Define an agent task and acceptance criteria, run it in a sandbox, and review the transcript with scores. Criteria and recorded context must cover delegated authority and approval requirements; the framework does not supply those governance judgments automatically.

**Version / status:** Current official documentation and repository inspected 2026-09-12  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official metadata for UKGovernmentBEIS/inspect_ai archived=false; LICENSE verifies MIT. Documentation verifies tools, sandbox environments, multi-turn agents and Inspect View. Suitable for advanced agent assessments, not a no-code GRC workflow.

</details>

<a id="phoenix"></a>

### [Arize Phoenix](<https://github.com/Arize-ai/phoenix>)

**Publisher:** Arize AI  
**Format:** Source-available tracing and evaluation application · **Access:** Elastic License 2.0 source-available; self-hosting permitted subject to license restrictions. Infrastructure and evaluator APIs may cost money; managed commercial products are separate.  
**For:** Engineers instrument applications; risk reviewers inspect traces and annotate evidence in the UI

**Why it earns a place:** Makes agent tool calls, retrieval, model calls and evaluation results inspectable so reviewers can investigate what happened.

**Use it to:** Trace an agent run, inspect tool activity, annotate failures and compare a corrected version on the same dataset. Explicitly record authority, policy versions and approvals; ordinary traces alone may not capture that context.

**Version / status:** Current README and official docs inspected 2026-09-12  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official non-archived repository, documentation and license reviewed. The project uses Elastic License 2.0, so this catalog identifies it as source-available. Traces require added authority and approval context for governance review.

</details>

<a id="agentdojo"></a>

### [AgentDojo](<https://github.com/ethz-spylab/agentdojo>)

**Publisher:** ETH Zurich and Invariant Labs researchers  
**Format:** Open-source benchmark environment with paper and trace examples · **Access:** MIT; free benchmark code and published results; rerunning model-based tests may incur API/compute costs  
**For:** Technical security and assurance practitioners; non-coders can study published traces

**Why it earns a place:** Tests whether tool-using agents complete legitimate tasks while resisting prompt injection, making the utility/security tradeoff observable.

**Use it to:** Run or inspect a task under an attack and a defense; compare legitimate task success, attack success and the full action trace. Transfer findings cautiously: benchmark scenarios are not an enterprise's real controls or deployment environment.

**Version / status:** NeurIPS 2024 benchmark; current repository and docs checked 2026-09-12  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official metadata archived=false and LICENSE verifies MIT. Docs warn that package API is evolving. Published results explicitly are not a leaderboard because attack/defense coverage differs across models; do not rank products directly from that table.

</details>

<a id="fairlearn"></a>

### [Fairlearn](<https://fairlearn.org/>)

**Publisher:** Fairlearn contributors  
**Format:** Open-source Python library, examples and practitioner guide · **Access:** MIT; free library and learning materials; local data/compute required  
**For:** Data scientists and quantitative auditors; GRC practitioners can use the assessment guide with technical support

**Why it earns a place:** Adds the fairness and subgroup-impact assessment that a security-only AI governance toolkit would miss.

**Use it to:** Compare error rates or outcomes across relevant groups, examine uncertainty and document mitigation tradeoffs. Fairness is context-dependent; a metric does not establish legal compliance, justice or due process.

**Version / status:** Current repository and guide inspected 2026-09-12; match notebook documentation to installed release  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official non-archived repository and guide reviewed for metrics, mitigation algorithms, notebooks and sociotechnical limitations. Development documentation may differ from an installed stable release.

</details>
