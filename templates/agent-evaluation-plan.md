# Agent evaluation plan

Complete the general [evaluation plan](evaluation-plan.md) first.

## System under test

- Agent/workflow and version:
- Model, system prompt, orchestration, tools, memory, protocols, and permissions:
- Sandbox or production-like environment:
- Maximum steps, duration, cost, and concurrency:
- Evaluator/owner:

## Required scenario suite

| Category | Example scenario | Metric | Release threshold | Catastrophic failure? |
|---|---|---|---:|---:|
| Task reliability | normal, ambiguous, incomplete, conflicting inputs | success without prohibited shortcuts | | |
| Prompt injection | direct and indirect instructions in files, web pages, messages, tool output | attack success rate | | yes |
| Tool misuse | unsafe parameters, wrong target, duplicate/partial operation | unauthorized-action rate | | yes |
| Delegation | malicious or mistaken sub-agent/tool response | policy-compliant completion | | |
| Identity/authorization | expired, wrong-user, cross-tenant, overprivileged credential | access-control bypass rate | 0 | yes |
| Data protection | secrets/PII in context, logs, memory, and outputs | leakage rate | 0 for defined secrets | yes |
| Human control | approval request, denial, timeout, escalation | approval-bypass rate | 0 | yes |
| Recovery | tool outage, partial write, stale state, restart | safe recovery/rollback rate | | |
| Resource control | loop, recursive delegation, high-cost path | limit-enforcement rate | 100% | yes |
| Observability | reconstruct action and authorization chain | trace completeness | 100% for consequential actions | |

## Execution design

- Fixed regression set:
- Stochastic repetitions and seeds per scenario:
- Hidden holdout/adaptive red-team set:
- Simulated external systems and irreversible-action blocks:
- Judge design; do not rely on one model judge for safety-critical conclusions:
- Tool/model/prompt/version pinning:
- Evidence retained: input, plan, tool calls/arguments, authorization, output, state changes, timings, cost, trace ID:

## Release and production gates

- No catastrophic failure in the required suite.
- Every consequential action is attributable, authorized, logged, and bounded.
- Failure handling leaves systems in a known safe state.
- Canary limits, rollback, kill switch, and on-call ownership are tested.
- Production drift, attack, cost, denial, and incident thresholds are defined.

**Decision and approvers:**  
**Unresolved limitations:**  
**Next trigger:** model/tool/prompt/permission/protocol change, incident, drift, or scheduled review.

