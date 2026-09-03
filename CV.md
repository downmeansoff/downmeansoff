# Gleb Lutfullin

**AI Engineer - Agentic Systems, RAG and LLM Backend**  
Samara, Russia · Remote · +7 917 948-11-93 · gleblutfullina@gmail.com · [Telegram](https://t.me/oldkindmvn)  
[GitHub](https://github.com/downmeansoff) · [Engineering Case Studies](CASE_STUDIES.md) · [Agentic LLM Portfolio](AGENTIC_LLM_PORTFOLIO.md)

## Summary

Three years in commercial engineering, the last nineteen months building LLM systems that run in production at a UK product company: multi-agent document processing, customer-facing agents and RAG on Python and FastAPI. I took a logistics client's 14-person document operation down to 2 people, shipped a patient-facing clinic agent in which patient identifiers are substituted before the model call and restored on our side, and cut LLM operating cost by ~35% measured per completed run. Retrieval is evaluated, not assumed: recall@1 0.50 to 0.65 on a labelled set of 54 questions, against a TF-IDF baseline I built first so there was something to compare with. Before AI, eighteen months across QA and network infrastructure, which is why reliability, staged rollout and incident response are part of how I build. English C1.

## Experience

### AI Engineer - Fortune Tavern Ltd
**February 2025 - Present · United Kingdom · Remote, English-speaking team**

- Automated a logistics client's document-handling operation - vehicle registration papers and inbound email - with a multi-agent extraction, validation and routing pipeline. The unit went from 14 people to 2; the remaining 12 were reassigned to other work.
- Shipped a patient-facing scheduling agent for a private clinic: booking, rescheduling, follow-up reminders and Q&A over clinic knowledge. Patient identifiers are substituted before the model call and restored on our side, so the prompt carries the request and not the person; context design kept per-conversation token cost bounded.
- Built the retrieval layer behind it - chunking, embeddings and vector search with an offline evaluation set of 54 labelled questions: recall@1 0.50 → 0.65 and MRR 0.62 → 0.72 against a TF-IDF baseline.
- Designed and shipped a 7-agent, 5-stage workflow (research → generation → QA → approval → analysis) that replaced 5 manual handoffs and cut the cycle from ~5 days to under 1 day.
- Cut LLM operating cost by ~35% via cache-first execution, reusable intermediate results, bounded context and request-count controls, with tracing per call rather than per service.
- Own agent reliability: three-tier confidence with escalation to a human, structured outputs with JSON Schema, tool calling, task routing, bounded retries, fallback models and audit logs.
- Operate a multi-platform product for 3,000+ users across 7 nodes and 5 client channels (web, Android, iOS, Telegram, external): Go control plane, health-aware routing, staging, smoke tests, rolling deploys and rollback. I am on call for what I ship and write the postmortems.

### Manual QA Engineer - BFT-Holding
**February 2024 - February 2025 · Samara, Russia · concurrent with Gazinformservice until May 2024**

- Authored ~140 API and Postman test cases across 25+ endpoints covering 30 core user flows; standardised functional, regression, negative and integration testing across UI, REST API and PostgreSQL.
- Logged 200+ defects across 12 releases, 18 critical and caught before production.
- Introduced 3-layer UI → API → database verification with clearer reproduction evidence, cutting reopened defects by ~35% and regression setup from ~6 hours to ~1.5 hours.

### Network Implementation Engineer - Gazinformservice
**August 2023 - May 2024 · St. Petersburg, Russia**

- Implemented, diagnosed and supported network and server infrastructure: node reachability, open ports, service health, TCP/IP, VLAN, SSH, Linux, Docker, PostgreSQL.
- Built 40+ automated health checks across 60 nodes with Python and Bash, cutting a routine verification cycle from ~45 to ~5 minutes; pre-deploy verification and a prepared rollback took failed deployments from ~20% to ~5%.

## Selected projects

Reference implementations, written to be read. None of them is a deployment, and each README says so.

- **[agent-runtime-reference](https://github.com/downmeansoff/agent-runtime-reference)** - a durable typed runtime for multi-step LLM agents: typed state machine over an append-only event log, resume and deterministic replay, four independent stop conditions, budget checked before each model call, schema-validated tools with permission tiers. 243 tests, runs offline with no API key. `DESIGN.md` records the rejected alternative and its cost for every decision.
- **[mcp-guarded-server](https://github.com/downmeansoff/mcp-guarded-server)** - an MCP server with an explicit security model: three permission tiers with human approval for destructive tools, a path jail that resolves and then checks containment component by component, tool results marked as untrusted data, a hash-chained audit log holding argument digests rather than arguments, and a 47-check protocol conformance suite. 974 tests. `THREAT_MODEL.md` states what it does not defend against.
- **[llm-gateway-reference](https://github.com/downmeansoff/llm-gateway-reference)** - one request surface in front of several LLM providers: routing by declared capability, projected request cost and provider health, virtual keys with scopes over upstream credentials the consumer never sees, request, token and budget quotas reserved before the call, fallback chains that record why every skipped provider was skipped, and a semantic cache with a discriminator guard. 951 tests, no HTTP client anywhere in the repository.
- **[agentic-rag-reference](https://github.com/downmeansoff/agentic-rag-reference)** - how to measure retrieval quality so that an improvement is distinguishable from noise: BM25 written out rather than imported, hybrid RRF, optional cross-encoder reranking, Hit Rate and Recall kept apart, McNemar and paired bootstrap. 166 tests.
- **[FortuneVoice for Windows](https://github.com/downmeansoff/fortunevoice-win)** - ported a colleague's macOS dictation app to Windows: Swift, WhisperKit and CoreML rebuilt on Python and faster-whisper, preserving the original's latency pipeline, safety nets and test suite. Inference runs entirely on-device, offline, no telemetry. 534 tests, CI green on Windows.
- **[Fortune Network Platform](https://github.com/downmeansoff/distributed-relay-platform)** - public sanitized architecture reference for the production system above: control-plane / data-plane separation, versioned API contracts, health-aware routing, guarded rollout with approval gates and rollback, runnable Docker demo and CI pipeline.

## Education & certification

**Specialist, Information Security of Automated Systems (10.05.03)** - 5th year, expected 2027  
Samara National Research University · Samara, Russia  
Positive Technologies (PT EdTechLab) - Network Attack Analysis with NTA, 2026.

## Technical skills

**AI & LLM** - Python, RAG, chunking, embeddings, vector search, pgvector, Qdrant, multi-agent orchestration, prompt engineering, structured outputs, JSON Schema, tool calling, MCP, LangChain, LangGraph, Temporal, OpenAI API + Agents SDK, Anthropic API + Claude Agent SDK, OpenRouter, retrieval evaluation (recall@k, MRR), guardrails, hallucination detection, LLM cost control.

**Backend & Data** - FastAPI, Pydantic, asyncio, REST APIs, webhooks, PostgreSQL, Redis, SQL, Go, TypeScript.

**DevOps & Observability** - Docker, Docker Compose, Linux, Bash, Git, GitHub Actions, CI/CD, n8n, Prometheus, Sentry, tracing, incident response.

**Languages** - Russian (native), English (C1), Hebrew (A1).
