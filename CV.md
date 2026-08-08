# Gleb Lutfullin

**AI Engineer — Agentic Systems, RAG & LLM Backend**  
Samara, Russia · Remote · +7 917 948-11-93 · gleblutfullina@gmail.com · [Telegram](https://t.me/oldkindmvn)  
[GitHub](https://github.com/downmeansoff) · [Engineering Case Studies](CASE_STUDIES.md) · [Agentic LLM Portfolio](AGENTIC_LLM_PORTFOLIO.md)

## Summary

AI Engineer at a UK product company, building LLM systems that run in production: multi-agent document processing, customer-facing agents and RAG on Python and FastAPI. I took a logistics client's 14-person document operation down to 2 people, shipped a patient-facing clinic agent under Russian personal-data law (152-FZ), and cut LLM operating cost by ~35%. Retrieval is evaluated, not assumed: recall@1 0.50 to 0.65 on a labelled set of 54 questions. Before AI I spent a year in QA and a year in network infrastructure, which is why reliability, staged rollout and incident response are part of how I build. English C1.

## Experience

### AI Engineer — Fortune Tavern Ltd
**February 2025 — Present · United Kingdom · Remote, English-speaking team**

- Automated a logistics client's document-handling operation — vehicle registration papers and inbound email — with a multi-agent extraction, validation and routing pipeline. The unit went from 14 people to 2; the remaining 12 were reassigned to other work.
- Shipped a patient-facing scheduling agent for a private clinic: booking, rescheduling, follow-up reminders and Q&A over clinic knowledge, with 152-FZ personal-data handling and context design that kept per-conversation token cost bounded.
- Built the retrieval layer behind it — chunking, embeddings and vector search with an offline evaluation set of 54 labelled questions: recall@1 0.50 → 0.65 and MRR 0.62 → 0.72 against a TF-IDF baseline.
- Designed and shipped a 7-agent, 5-stage workflow (research → generation → QA → approval → analysis) that replaced 5 manual handoffs and cut the cycle from ~5 days to under 1 day.
- Cut LLM operating cost by ~35% via cache-first execution, reusable intermediate results, bounded context and request-count controls, with tracing for cost and failure analysis.
- Own agent reliability: human-in-the-loop approval on critical operations, structured outputs with JSON Schema, tool calling, task routing, bounded retries, fallback models and audit logs.
- Operate a multi-platform product for 3,000+ users across 7 nodes and 5 client channels (web, Android, iOS, Telegram, external): Go control plane, health-aware routing, staging, smoke tests, rolling deploys and rollback.

### Manual QA Engineer — BFT-Holding
**February 2024 — February 2025 · Samara, Russia · concurrent with Gazinformservice until May 2024**

- Authored ~140 API and Postman test cases across 25+ endpoints covering 30 core user flows; standardised functional, regression, negative and integration testing across UI, REST API and PostgreSQL.
- Logged 200+ defects across 12 releases, 18 critical and caught before production.
- Introduced 3-layer UI → API → database verification with clearer reproduction evidence, cutting reopened defects by ~35% and regression setup from ~6 hours to ~1.5 hours.

### Network Implementation Engineer — Gazinformservice
**August 2023 — May 2024 · St. Petersburg, Russia**

- Implemented, diagnosed and supported network and server infrastructure: node reachability, open ports, service health, TCP/IP, VLAN, SSH, Linux, Docker, PostgreSQL.
- Standardised diagnostic checklists and health checks with Python and Bash scripting, cutting a routine verification cycle from ~45 to ~5 minutes; documented deployment, recovery and rollback.

## Selected projects

- **[FortuneVoice for Windows](https://github.com/downmeansoff/fortunevoice-win)** — ported a colleague's macOS dictation app to Windows: Swift, WhisperKit and CoreML rebuilt on Python and faster-whisper, preserving the original's latency pipeline, safety nets and test suite. Inference runs entirely on-device — offline, no telemetry.
- **[Fortune Network Platform](https://github.com/downmeansoff/distributed-relay-platform)** — public sanitized architecture reference for the production system above: control-plane / data-plane separation, versioned API contracts, health-aware routing, guarded rollout with approval gates and rollback, runnable Docker demo and CI pipeline.
- **Personal automation agents** — scheduled LLM agents I run daily: next-day calendar assembly, a world-news digest and a personal digest. Python, cron jobs, structured outputs, cost-bounded prompts.

## Education & certification

**Specialist, Information Security of Automated Systems (10.05.03)** — 5th year, expected 2027  
Samara National Research University · Samara, Russia  
Positive Technologies (PT EdTechLab) — Network Attack Analysis with NTA, 2026.

## Technical skills

**AI & LLM** — Python, RAG, embeddings, vector search, multi-agent orchestration, prompt engineering, structured outputs, JSON Schema, tool calling, MCP, LangGraph, Temporal, OpenAI API + Agents SDK, Anthropic API + Claude Agent SDK, OpenRouter, retrieval evaluation (recall@k, MRR), LLM cost control.

**Backend & Data** — FastAPI, Pydantic, asyncio, REST APIs, webhooks, PostgreSQL, Redis, SQL, Go, TypeScript.

**DevOps & Observability** — Docker, Linux, Bash, Git, GitHub Actions, CI/CD, n8n, Prometheus, Sentry, tracing, incident response.

**Languages** — Russian (native), English (C1), Hebrew (A1).
