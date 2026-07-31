# Engineering Case Studies

Selected systems I designed, coordinated, and developed. Production secrets, customer data, private domains, credentials, and proprietary business logic are intentionally omitted.

## 1. Production multi-agent workflow

### Problem

Research, preparation, QA, approval, execution, and feedback required repeated manual handoffs. A single long prompt was expensive to retry, hard to observe, and unsafe to connect directly to external actions.

### System

Designed a workflow with **7 specialized agents** across explicit state transitions. The system used OpenAI Responses/Agents SDK, Claude Agent SDK, Pydantic contracts, PostgreSQL, Redis, Temporal orchestration, and controlled tool access.

### My responsibility

- agent and workflow architecture;
- tool/function schemas and permissions;
- JSON Schema and Pydantic structured outputs;
- state, context, and memory boundaries;
- bounded retries, fallbacks, timeouts, and stop conditions;
- risk routing and Human-in-the-Loop;
- cost/failure tracing, regression scenarios, monitoring, and production support;
- customer discovery, demos, feedback, and iteration planning.

### Reliability controls

- each step persists validated state;
- failed steps can be retried without replaying the full workflow;
- external writes are isolated behind policy checks and idempotency;
- model choice and context size are routed by complexity and risk;
- unsafe or ambiguous output follows deterministic refusal or approval paths;
- prompt/model changes are checked against repeatable scenarios before rollout.

### Result

- **~5 days → under 1 day** end-to-end cycle;
- **~35% lower** average LLM cost per completed run;
- five manual handoffs replaced by observable state transitions;
- failures attributable to a specific step, model, prompt version, or tool call.

---

## 2. Supply-Chain RAG and retrieval evaluation

### Scope

Built a Python/FastAPI RAG service with document preparation, chunking, embeddings, cosine vector retrieval, a `/query` endpoint, and offline evaluation over **54 labeled questions**.

### Evaluation approach

- compared TF-IDF lexical retrieval with neural embeddings;
- measured Recall@k and MRR;
- separated paraphrase, keyword, and factual query classes;
- reviewed context sufficiency and retrieval edge cases;
- tracked the first relevant chunk rather than only whether one appeared anywhere.

### Result

- paraphrase Recall@1: **0.50 → 0.65**;
- MRR: **0.62 → 0.72**;
- keyword queries showed that dense retrieval was not universally better;
- recommended hybrid lexical+dense retrieval and a reranking stage.

### Public reference

[`agentic-rag-reference`](agentic-rag-reference/README.md) demonstrates normalized Pydantic contracts, lexical+dense reciprocal-rank fusion, an optional reranker boundary, Recall@k/MRR, failure buckets, and deterministic tests.

---

## 3. VibeSpec — public AI reliability project

[VibeSpec](https://github.com/downmeansoff/vibespec) is a Python contract, safety, and observability layer for autonomous clients of a changing AI generation API.

### Engineering controls

- live capability discovery with no hard-coded model list;
- per-model JSON Schema compilation and local validation;
- free server-side cost estimate before paid execution;
- safety check, explicit approval, cost ceiling, and idempotency;
- exact `Retry-After` handling for `429` and `503` with bounded attempts;
- webhook HMAC verification;
- capability snapshots and schema-drift reports;
- secret-safe JSONL traces and offline HTML reports;
- stable JSON envelopes for Codex, Claude Code, CI, or another orchestrator;
- tests and CI on Python 3.11–3.13.

### Why it matters

Agent systems depend on changing model and API contracts. VibeSpec makes drift, retries, paid actions, and failures explicit and machine-readable rather than hidden inside prompts.

---

## 4. AI automations for external businesses

### Work

Delivered AI automation across marketing, sales, analytics, and operations. Work started with process discovery and identifying the actual bottleneck, then moved through solution selection, architecture, integrations, pilot rollout, demos, and user feedback.

### Typical components

- Python/FastAPI and n8n workflows;
- CRM and external API integrations;
- segmentation and structured data preparation;
- personalized messaging and content workflows;
- scheduling, deduplication, delivery status, retries, and audit logs;
- evaluation of hosted models and cost/quality trade-offs;
- user training and rollout support.

### Business approach

Measured the effect through cycle time, manual hours, repeated work, error rate, throughput, and LLM/infrastructure cost rather than treating model output as the final metric.

---

## 5. Distributed Secure Access Platform

### Scale

- **1,000+ users**;
- **7 production nodes**;
- **5 client channels**: web, Android, iOS, Telegram, and external clients.

### My responsibility

Product requirements, backend architecture, API contracts, PostgreSQL data models, mobile delivery coordination, infrastructure, monitoring, rollout, rollback, and production incident readiness.

### Reliability decisions

- server-owned product state and versioned contracts;
- control-plane and data-plane separation;
- health-aware routing and automatic unhealthy-node exclusion;
- staging, smoke evidence, rolling deployment, and rollback;
- structured logs, telemetry, Prometheus, Sentry, and incident runbooks;
- role-separated access and human approval for high-impact actions.

### Public reference

[`distributed-relay-platform`](https://github.com/downmeansoff/distributed-relay-platform) is a sanitized runnable architecture reference. Production code, customer data, and private infrastructure remain private.

---

## AI-native development workflow

```text
Business goal and acceptance criteria
        ↓
Architecture and implementation plan
        ↓
Coding agents in isolated branches/worktrees
        ↓
Tests, QA, regression and security checks
        ↓
CI/CD, staging and smoke evidence
        ↓
Human-controlled production decision
```

Daily tools include Claude Code, Codex, Cursor, OpenCode, MCP servers, Git worktrees, and GitHub Actions. Agents assist with repository analysis, implementation, tests, documentation, regression checks, and review. Architecture, permissions, production boundaries, and release decisions remain human-owned.
