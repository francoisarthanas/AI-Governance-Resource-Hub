# Agentic AI risk assessment

Use this supplement after the general [AI impact assessment](ai-impact-assessment.md). One assessment should cover one agent, orchestrated workflow, or materially distinct deployment.

## 1. Scope and authority

- Agent/workflow name and owner:
- Business objective:
- Users and affected people:
- Environments: development / test / production
- Models, agents, tools, data stores, memory, protocols, and external services:
- Decisions or actions the agent may propose:
- Decisions or actions the agent may execute:
- Explicitly prohibited actions:
- Maximum spend, transaction value, data sensitivity, and operational blast radius:

## 2. Autonomy profile

| Dimension | Selected level | Evidence and rationale |
|---|---|---|
| Planning horizon | single step / bounded multistep / open-ended | |
| Execution | recommend / prepare / execute with approval / execute autonomously | |
| Tool access | read / write / transact / administer | |
| Identity | shared service / delegated user / dedicated workload identity | |
| Memory | none / session / persistent | |
| Environment | sandbox / limited production / broad production | |
| Reversibility | fully reversible / compensating action / irreversible | |

## 3. Trust-boundary and abuse analysis

For each external input, tool, agent, memory store, and output sink, record:

| Boundary/component | Trust level | Credentials/data exposed | Failure or abuse mode | Preventive control | Detection | Response owner |
|---|---|---|---|---|---|---|
| | | | | | | |

Cover at minimum:

- indirect prompt injection and untrusted retrieved content;
- tool poisoning, description manipulation, and dependency compromise;
- confused-deputy and excessive-delegation paths;
- identity propagation, token forwarding, and cross-tenant leakage;
- memory poisoning, stale state, and sensitive-data persistence;
- unsafe code, shell, browser, email, payment, or infrastructure actions;
- agent-to-agent impersonation, task redirection, and cascading failure;
- runaway loops, resource exhaustion, denial of wallet, and duplicate actions;
- inadequate human oversight, automation bias, and inaccessible appeals;
- monitoring blind spots and evidence tampering.

## 4. Required control decisions

| Control | Required? | Implementation/evidence | Owner | Test cadence |
|---|---:|---|---|---|
| Dedicated least-privilege identity per agent/workload | | | | |
| Explicit tool allowlist and parameter constraints | | | | |
| Read/write separation and just-in-time privilege | | | | |
| Human approval for consequential or irreversible actions | | | | |
| Spend/rate/time/step limits | | | | |
| Sandboxing and network/egress restrictions | | | | |
| Input provenance and untrusted-content isolation | | | | |
| Output validation before action execution | | | | |
| Signed/pinned tools, servers, packages, and manifests | | | | |
| Memory scoping, TTL, encryption, and user controls | | | | |
| End-to-end trace of plans, tool calls, approvals, and outcomes | | | | |
| Kill switch, credential revocation, and safe degraded mode | | | | |
| Adversarial, misuse, and recovery evaluation | | | | |

## 5. Evaluation and release gate

Link the [agent evaluation plan](agent-evaluation-plan.md). Define pass thresholds for task success, prohibited actions, approval bypass, prompt injection, tool misuse, privacy leakage, recovery, and cost/latency. Record residual risk, exceptions, expiry dates, and approvers.

**Release decision:** approve / approve with conditions / pilot only / reject  
**Approvers:** business owner / risk owner / security / privacy / safety / compliance  
**Review trigger:** model, tool, prompt, permission, data, user population, jurisdiction, or autonomy change; incident; threshold breach; scheduled review.

