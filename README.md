<div align="center">

<img width="100%" src="./assets/header.svg" alt="Gleb Lutfullin — Agentic LLM Engineer, RAG and Production AI Systems" />

[![Telegram](https://img.shields.io/badge/Telegram-@oldkindmvn-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/oldkindmvn)
[![Email](https://img.shields.io/badge/Email-gleblutfullina%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gleblutfullina@gmail.com)
[![Agentic Portfolio](https://img.shields.io/badge/Agentic_LLM_Portfolio-111827?style=for-the-badge&logo=readthedocs&logoColor=white)](AGENTIC_LLM_PORTFOLIO.md)
[![Case Studies](https://img.shields.io/badge/Engineering_Case_Studies-374151?style=for-the-badge&logo=readthedocs&logoColor=white)](CASE_STUDIES.md)
[![CV](https://img.shields.io/badge/View_CV-2563EB?style=for-the-badge&logo=readme&logoColor=white)](CV.md)

<br/>

![Agents](https://img.shields.io/badge/Production_AI_agents-7-8B5CF6?style=flat-square)
![Cycle](https://img.shields.io/badge/Workflow_cycle-%E2%88%9280%25-22C55E?style=flat-square)
![Cost](https://img.shields.io/badge/LLM_cost-%E2%88%9235%25-16A34A?style=flat-square)
![RAG](https://img.shields.io/badge/RAG_eval_questions-54-F59E0B?style=flat-square)
![Users](https://img.shields.io/badge/Production_users-3000%2B-0EA5E9?style=flat-square)

</div>

## Profile

I am an **Agentic LLM Engineer / AI Product Engineer at Fortune Tavern Ltd (UK)** focused on production multi-agent systems, RAG, LLM reliability, backend architecture, and AI-native development.

I work across the full lifecycle: business discovery, architecture, tool and data contracts, implementation, evaluation, CI/CD, observability, staged rollout, customer feedback, and production support.

### Selected results

- Designed and operated a **7-agent production workflow** across research, generation, QA, approval, execution, and feedback
- Reduced an end-to-end process from **~5 days to under 1 day** and average LLM cost per completed run by **~35%**
- Built RAG evaluation over **54 labeled questions**, improving paraphrase **Recall@1 from 0.50 to 0.65** and **MRR from 0.62 to 0.72**
- Delivered AI automations for external businesses across marketing, sales, analytics, and operations
- Operated a distributed production platform for **3,000+ users**, **7 nodes**, and **5 client channels**
- Built a controlled AgentOps workflow with isolated branches/worktrees, tests, security checks, staging evidence, and human production approval

---

## Featured agentic and RAG work

### [Agentic LLM & RAG Engineering Portfolio](AGENTIC_LLM_PORTFOLIO.md)

Detailed production-oriented portfolio covering:

- multi-step agent orchestration and state transitions;
- tool/function calling and structured Pydantic contracts;
- context and memory boundaries;
- retries, fallbacks, stop conditions, and degraded states;
- evaluation, tracing, regression scenarios, and human review;
- hybrid retrieval, reranking boundaries, Recall@k, and MRR;
- self-hosted serving readiness and vLLM operational concepts.

### [MCP Guarded Server](https://github.com/downmeansoff/mcp-guarded-server)

[![CI](https://github.com/downmeansoff/mcp-guarded-server/actions/workflows/ci.yml/badge.svg)](https://github.com/downmeansoff/mcp-guarded-server/actions/workflows/ci.yml)

A Model Context Protocol server with a security model, and the tests that prove it. An
MCP server is a remote-code-execution surface driven by a language model on the user's
behalf, so the interesting engineering is not how to expose a tool but how to expose one
that a confused or manipulated model cannot misuse.

- three permission tiers: `SAFE` auto-allowed, `GUARDED` requires an explicit policy
  grant, `PRIVILEGED` requires a human approval callback and is refused when none is wired;
- a path jail that resolves and then verifies containment component-wise rather than by
  string prefix, opened with `O_NOFOLLOW` and `O_NONBLOCK` so neither a symlink nor a FIFO
  can defeat or wedge it, with an adversarial traversal battery in the tests;
- tool results wrapped as untrusted data with a per-call nonce, and an injection detector
  that reports rather than filters, with the reasoning written down;
- a token-bucket rate limiter with an injected clock, a concurrency cap and a per-session
  byte budget, so the limits are deterministic and testable;
- an append-only, hash-chained audit log that stores argument digests and never raw
  arguments;
- a 47-check protocol conformance suite driven over the wire: handshake ordering, version
  negotiation, framing, id echo, JSON-RPC error codes.

974 tests, no network and no API keys.
[`THREAT_MODEL.md`](https://github.com/downmeansoff/mcp-guarded-server/blob/main/THREAT_MODEL.md)
states the attacker, the trust boundaries, the residual risk per threat and what is
explicitly out of scope.

### [Agent Runtime Reference](https://github.com/downmeansoff/agent-runtime-reference)

[![CI](https://github.com/downmeansoff/agent-runtime-reference/actions/workflows/ci.yml/badge.svg)](https://github.com/downmeansoff/agent-runtime-reference/actions/workflows/ci.yml)

A durable, typed runtime for multi-step LLM agents. The premise: the hard part of an agent
is not the prompt, it is state, failure and cost.

- a typed state machine over an append-only event log, so a run can be resumed after a
  crash and replayed deterministically against recorded model and tool results;
- discriminated-union transitions, so a step cannot forget to say what happens next;
- four independent stop conditions (step limit, budget, terminal transition, no-progress
  detection), with `DEGRADED` as a first-class outcome carrying a machine-readable reason;
- budget checked before every model call rather than after, across tokens, cost and calls;
- tools validated against a JSON Schema before execution, with permission levels and a
  human approval gate for destructive actions;
- structured output with a single repair round that feeds the validation error back;
- guardrails that deliberately do not use the model's self-reported confidence as a signal;
- a regression suite of 16 scripted failure scenarios asserting 92 named invariants.

243 tests, no network and no API keys.
[`DESIGN.md`](https://github.com/downmeansoff/agent-runtime-reference/blob/main/DESIGN.md)
states each decision as problem, chosen solution, rejected alternative and the cost of the
choice.

### [Agentic RAG Reliability Reference](https://github.com/downmeansoff/agentic-rag-reference)

[![CI](https://github.com/downmeansoff/agentic-rag-reference/actions/workflows/ci.yml/badge.svg)](https://github.com/downmeansoff/agentic-rag-reference/actions/workflows/ci.yml)

Standalone runnable repository. `python benchmark.py` reproduces every number in
[`reports/results.md`](https://github.com/downmeansoff/agentic-rag-reference/blob/main/reports/results.md).

- Pydantic chunk and search contracts;
- BM25 implemented from scratch alongside TF-IDF, so the lexical baseline is explainable;
- reciprocal-rank fusion for hybrid search, as a testable free function;
- cross-encoder reranking behind an optional interface;
- Recall@k, MRR, retrieval failure taxonomy;
- McNemar and paired bootstrap intervals, so a delta is separated from noise;
- an annotation protocol for the golden set, with inter-annotator agreement;
- interchangeable vector stores (in-memory, pgvector, Qdrant) and model providers;
- 166 tests, no network and no keys, green in GitHub Actions on Python 3.11 and 3.12.

A shortened copy of this material also lives [in this repository](agentic-rag-reference/README.md).

---

## Production platform experience

### [Distributed Secure Access Platform](https://github.com/downmeansoff/distributed-relay-platform)

Sanitized architecture reference for a private production system used by **3,000+ users** across **7 nodes** and **5 client channels**.

**Relevant controls**

`Health-aware routing` `Automatic node exclusion` `Versioned API contracts` `Staging` `Smoke tests` `Rolling deployment` `Rollback` `Prometheus` `Sentry` `Audit logs` `Incident response`

This background shapes how I design LLM systems: agents need the same discipline around contracts, failure isolation, permissions, observability, rollout safety, and recovery as any other distributed component.

---

## Core stack

### Agentic LLM Systems

`Python` `FastAPI` `Pydantic` `OpenAI Responses API` `OpenAI Agents SDK` `Claude Agent SDK` `LangGraph` `Temporal` `MCP` `Tool Calling` `Structured Outputs` `JSON Schema` `Human-in-the-loop` `Context Management` `Bounded Retries` `Fallbacks` `Stop Conditions`

### RAG, Evaluation & LLMOps

`Chunking` `Embeddings` `Lexical Search` `Vector Search` `Hybrid Retrieval` `Reranking Patterns` `Recall@k` `MRR` `Golden Sets` `Regression Scenarios` `Tracing` `Error Taxonomy` `Prompt/Model Versioning` `Langfuse Familiarity`

### Backend, Data & Production

`PostgreSQL` `Redis` `SQL` `REST APIs` `Webhooks` `Docker` `Linux` `GitHub Actions` `CI/CD` `Prometheus` `Sentry` `Health Checks` `Staged Rollout` `Rollback` `Incident Response`

### AI-native Development

`Claude Code` `Codex` `Cursor` `OpenCode` `Git Worktrees` `AgentOps` `Automated Tests` `Security Review` `Documentation`

---

## Education

**Samara National Research University**  
5th-year Specialist student — **Information Security of Automated Systems (10.05.03)**  
Expected graduation: **2027** · English: **C1**

---

<div align="center">

### Open to Agentic LLM Engineer · AI Engineer · RAG / LLMOps opportunities

[![Telegram](https://img.shields.io/badge/Let's_talk_on_Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/oldkindmvn)
[![Email](https://img.shields.io/badge/Contact_by_email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gleblutfullina@gmail.com)

</div>
