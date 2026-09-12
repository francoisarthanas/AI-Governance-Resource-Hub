# Tools and Test Stack

Tools produce signals and evidence; they do not make the risk decision. Select them after defining the use case, threat model, required metrics, acceptance thresholds, and evidence owner.

## Minimal production stack

| Capability | Minimum outcome |
|---|---|
| Discovery/inventory | A current system/use-case inventory tied to owners, data, models, agents, tools, vendors, and status |
| Version/provenance | Reconstruct the model, prompt, code, data, retrieval, tool, policy, configuration, and dependency versions used |
| Evaluation | Repeatable task, safety, security, subgroup/context, and agent-trajectory tests with release thresholds |
| Runtime policy | Independently enforced identity, authorization, data, tool, action, budget, approval, and egress rules |
| Observability | Traces that connect user/principal, agent, model, retrieval, memory, tool calls, policy decisions, approvals, state changes, cost, and outcome |
| Incident/response | Detection, case management, evidence preservation, revocation, containment, rollback, recovery, and notification |
| Assurance | Evidence index, control ownership, findings, exceptions, attestations, and management reporting |

## Open and authoritative testing tools

### General and agent evaluations

- **[Inspect](https://inspect.aisi.org.uk/)** — UK AI Security Institute's open framework for model and agent evaluations. Strong for composable tasks, sandboxes, tool use, agent trajectories, approvals, and reproducible logs. Start here when building a serious eval harness.
- **[NIST Dioptra](https://pages.nist.gov/dioptra/)** — Reproducible, trackable AI test workflows, especially for adversarial ML and lab/audit settings. Heavier operational footprint than a simple library.
- **[OpenAI Evals guidance](https://platform.openai.com/docs/guides/evals)** — Practical patterns for dataset-driven and trace/agent evaluation. Product-specific features require an OpenAI context; reuse the evaluation discipline across platforms.
- **[MLCommons AILuminate](https://mlcommons.org/ailuminate/safety-resources/)** — Standardized risk and reliability benchmarks; use as a shared baseline, not as proof that a specific application is safe.
- **[AILuminate Agentic](https://mlcommons.org/ailuminate/agentic/)** — Emerging product maturity ladder for agent reliability. Track maturity and scope before relying on it for release decisions.

### Red teaming and vulnerability discovery

- **[Microsoft PyRIT](https://github.com/microsoft/PyRIT)** — Extensible red-team orchestration, attack strategies, target adapters, scoring, and memory for GenAI systems.
- **[NVIDIA garak](https://github.com/NVIDIA/garak)** — Broad probe/detector scanner for common LLM weaknesses. Good for quick baseline discovery; manually validate findings and add application-specific tests.
- **[Project Moonshot](https://aiverifyfoundation.sg/project-moonshot/)** — Open benchmarking and red-teaming toolkit with UI and CI/CD use; useful for teams wanting guided test flows.
- **[promptfoo](https://github.com/promptfoo/promptfoo)** — Open-source prompt/app evaluation and red teaming that fits CI pipelines. Confirm test quality and keep high-risk cases outside one tool's defaults.
- **[Giskard](https://github.com/Giskard-AI/giskard)** — Open-source testing/scanning for ML and LLM applications, with commercial extensions. Evaluate license, data handling, and enterprise features separately.

### Fairness, robustness, and explainability

- **[Fairlearn](https://fairlearn.org/)** — Group fairness assessment and mitigation. Metrics require contextual and legal interpretation; incompatible fairness definitions cannot be solved by selecting every metric.
- **[AI Fairness 360](https://github.com/Trusted-AI/AIF360)** — Broad fairness metrics and mitigation algorithms for classic ML.
- **[Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)** — Attacks and defenses for ML model robustness across modalities.
- **[AI Explainability 360](https://github.com/Trusted-AI/AIX360)** — Explainability algorithms and examples. Test whether explanations are faithful and useful for the intended audience and decision.
- **[Evidently](https://github.com/evidentlyai/evidently)** — Open-source evaluation and monitoring for ML/LLM outputs and data drift. Commercial offerings exist; assess deployment and data paths.

### Governance testing and documentation

- **[AI Verify](https://aiverifyfoundation.sg/what-is-ai-verify/toolkit/)** — Governance testing framework and toolkit for traditional AI, with process checks and technical tests. Confirm scope; use Moonshot for LLM-specific testing.
- **[CycloneDX ML-BOM](https://www.cyclonedx.org/capabilities/mlbom/)** — Machine-readable model, dataset, dependency, and service inventory for supply-chain transparency.
- **[SPDX](https://spdx.dev/)** — ISO-standardized system/package data exchange with growing AI, data, safety, and security coverage.
- **[Model Card Toolkit](https://github.com/tensorflow/model-card-toolkit)** and **[Data Cards Playbook](https://sites.research.google/datacardsplaybook/)** — Structured transparency artifacts; use this repository's system card to add deployment context, integrations, and controls.

## Security taxonomies are test inputs

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)
- [MITRE ATLAS](https://atlas.mitre.org/) — tactics, techniques, mitigations, and real cases, including agentic AI.
- [NIST AI 100-2e2025](https://doi.org/10.6028/NIST.AI.100-2e2025) — adversarial ML taxonomy and mitigation limitations.
- [Google Secure AI Framework](https://saif.google/secure-ai-framework) — risk map, control catalog, self-assessment, and agent-specific extensions.

Map applicable threats to a test case, preventive control, observable signal, response action, evidence, and owner.

## Runtime policy and observability building blocks

- **[Open Policy Agent](https://www.openpolicyagent.org/)** — general policy-as-code engine. Useful for deterministic authorization and release rules around AI; it does not understand context by itself.
- **[Cedar](https://www.cedarpolicy.com/)** — policy language/engine designed for authorization. Model agent, principal, resource, action, and context explicitly.
- **[OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)** — emerging portable telemetry conventions. Check stability and redact/minimize sensitive prompt, output, and retrieval data.
- **[Langfuse](https://github.com/langfuse/langfuse)** — open-source LLM tracing, evaluation, prompt management, and metrics. Review the current license and hosted/self-hosted data path.
- **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** — open-source AI observability and evaluation with OpenTelemetry support.
- **[MLflow](https://mlflow.org/)** — model/experiment registry and GenAI evaluation/tracing. Governance quality depends on required metadata, ownership, and release integration.

These components require secure architecture. A trace store full of unredacted prompts and credentials can create a new high-value breach target.

## A test program, not a test event

### Before release

1. Translate business, legal, safety, security, and user needs into testable requirements.
2. Build representative normal, edge, ambiguous, out-of-scope, adversarial, and failure cases.
3. Separate development, validation, and protected holdout cases for higher-risk systems.
4. Define metrics, graders, uncertainty, sample size, subgroup/context analysis, and pass/fail thresholds before seeing the final result.
5. Run complete-system tests with the production configuration and controls.
6. Record failures, severity, remediation, retest, limitation, and the owner who accepted any residual risk.

### In production

1. Monitor leading signals, outcomes, complaints, appeals, overrides, incidents, cost, access, and drift.
2. Sample real traces with appropriate privacy and access controls.
3. Turn production failures and near misses into regression tests.
4. Re-evaluate on material changes and at a risk-based cadence.
5. Periodically test whether monitoring, human oversight, incident, shutdown, and recovery work.

## Tool-selection rubric

Score candidates with evidence, not demo polish:

- coverage of your systems, modalities, agents, protocols, and deployment environments;
- open interfaces and export of raw evidence, test cases, policies, findings, and traces;
- reproducibility, versioning, lineage, access control, isolation, and tamper evidence;
- data handling, residency, retention, encryption, secrets, tenant separation, and provider training use;
- false-positive/negative characterization and human review workflow;
- integration with CI/CD, registries, IAM, SIEM, incident, GRC, and ticketing;
- scalability, latency, cost, availability, support, and exit;
- maintainer health, release cadence, security policy, license, and independent validation.

Do not send sensitive production data or attack payloads to an unapproved hosted evaluator.
