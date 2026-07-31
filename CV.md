# Gleb Lutfullin

**Agentic LLM Engineer · Multi-Agent Systems · RAG · LLM Backend**  
Samara, Russia · Remote  
[GitHub](https://github.com/downmeansoff) · [Agentic LLM Portfolio](AGENTIC_LLM_PORTFOLIO.md) · [Telegram](https://t.me/oldkindmvn) · [Email](mailto:gleblutfullina@gmail.com)

## Professional Summary

Agentic LLM Engineer with **4 years of Python experience**, **3+ years of commercial engineering**, and **1.5+ years building production LLM systems**. Designs multi-step agent workflows, RAG services, AI automations, backend APIs, and production reliability controls with Python, FastAPI, Pydantic, PostgreSQL, Redis, Docker, and CI/CD.

Delivered a 7-agent production workflow that reduced turnaround from approximately 5 days to under 1 day and LLM cost per completed run by approximately 35%. Built retrieval evaluation over 54 labeled questions, operated a distributed platform for 1,000+ users across 7 nodes, and delivered AI automations for external businesses. Experienced with tool calling, structured outputs, stateful orchestration, bounded retries, fallbacks, human approval, tracing, offline evaluation, monitoring, and incident response. English B2+.

## Professional Experience

### Fortune Tavern Ltd — AI Engineer / Product Engineer
**Remote · United Kingdom · 2026–Present**

- Designed and operated a 7-agent workflow across research, generation, QA, approval, execution, and feedback; replaced 5 manual handoffs and cut end-to-end turnaround from approximately 5 days to under 1 day.
- Defined agent roles, tool/function schemas, structured outputs, Pydantic contracts, state transitions, memory boundaries, stop conditions, risk routing, bounded retries, deterministic fallbacks, audit logs, and human approval.
- Reduced average LLM cost per completed run by approximately 35% through cache-first execution, reusable intermediate results, narrow context, model routing, and retry limits; traced cost and failures by workflow step.
- Built evaluation and regression scenarios for prompts, retrieval, structured outputs, and critical tool paths; used production feedback to improve quality, latency, and failure handling.
- Delivered AI automations for external businesses across marketing, sales, analytics, and operations, taking work from process discovery and architecture through integrations, pilot rollout, demos, and user feedback.
- Built an internal CRM with 8 pipeline stages and 9 automatically calculated KPIs linking attribution, conversion, revenue, payouts, and decisions.
- Operated a distributed production platform for 1,000+ users across 7 nodes and 5 client channels with health-aware routing, staging, smoke tests, rolling deployment, monitoring, rollback, and incident response.

### Gastrohub — Python / LLM Developer
**Remote · Kazakhstan · 2025**

- Built a multi-agent AI automation platform for research, segmentation, campaign planning, content generation, QA, approval, and performance analysis.
- Developed Python/FastAPI services and n8n workflows integrating OpenAI, Anthropic, OpenRouter, PostgreSQL, Redis, CRM segments, and external APIs.
- Implemented structured outputs, Pydantic validation, scheduling, deduplication, delivery-status handling, retries, fallbacks, audit logs, Docker/CI/CD, monitoring, and LLM cost controls.

### BFT-Holding — Manual QA Engineer
**Russia · 2024–2025**

- Authored approximately 140 API/Postman test cases across 25+ endpoints and 30 core user flows; covered functional, regression, negative, integration, UI/API, and PostgreSQL data checks.
- Reduced regression setup from approximately 6 hours to 1.5 hours and reopened defects by approximately 35%; logged 200+ defects including 18 critical pre-release issues across 12 releases.

### Gazinformservice — Network Implementation Engineer
**Russia · 2023–2024**

- Automated 40+ health checks across 60 nodes with 15 Python/Bash scripts, reducing routine diagnostics from approximately 45 minutes to 5 minutes.
- Added pre-deployment validation, structured logging, and rollback-ready procedures for Linux/Docker services; reduced failed deployments from approximately 20% to 5% across 30+ rollouts.

## Selected Projects

### Supply-Chain RAG

Built document preparation, chunking, embeddings, cosine vector search, a FastAPI `/query` endpoint, and offline evaluation over 54 labeled questions. Improved paraphrase Recall@1 from 0.50 to 0.65 and MRR from 0.62 to 0.72 versus a TF-IDF baseline. Keyword results led to a hybrid lexical+dense retrieval design with a reranking boundary.

### VibeSpec — Public AI Reliability Project

Python contract, safety, and observability layer for autonomous AI API clients: live schema discovery, local validation, approval and cost gates, idempotency, exact retry handling, schema drift detection, secret-safe tracing, HTML reports, tests, and CI.  
https://github.com/downmeansoff/vibespec

### Agentic RAG Reliability Reference

Public reference with Pydantic schemas, TF-IDF and injected dense retrieval, reciprocal-rank fusion, an optional reranker interface, Recall@k/MRR, failure buckets, and deterministic tests.  
https://github.com/downmeansoff/downmeansoff/tree/main/agentic-rag-reference

### Distributed Secure Access Platform

Go control plane, PostgreSQL, Docker, GitHub Actions, Prometheus, and Bash. Health-aware routing, automatic node exclusion, staging, smoke tests, rolling deployment, monitoring, and rollback for 1,000+ users across 7 nodes.  
https://github.com/downmeansoff/distributed-relay-platform

## Technical Skills

**Agentic LLM Systems:** OpenAI Responses API, OpenAI Agents SDK, Claude Agent SDK, LangGraph, Temporal, MCP, tool/function calling, structured outputs, JSON Schema, Pydantic, stateful orchestration, context management, memory boundaries, bounded retries, fallbacks, stop conditions, human-in-the-loop.

**RAG & Quality:** document preparation, chunking, embeddings, lexical and vector search, hybrid retrieval, reranking patterns, Recall@k, MRR, golden sets, regression scenarios, LLM tracing, error taxonomy, prompt/model versioning, human review loops.

**Backend & Data:** Python, FastAPI, async/await, typing, testing, PostgreSQL, Redis, SQL, REST APIs, webhooks, Go, TypeScript, Fastify, Prisma.

**Production & AI-native Development:** Docker, Linux, GitHub Actions, CI/CD, Prometheus, Sentry, Langfuse familiarity, structured logging, health checks, staged rollout, rollback, incident response, Claude Code, Codex, Cursor, OpenCode, Git worktrees.

**LLM Serving Fundamentals:** OpenAI-compatible serving, continuous batching, KV cache, quantization, context/concurrency trade-offs, latency and throughput monitoring; primary production ownership has been with hosted models rather than a vLLM cluster.

## Education

### Samara University

**Specialist, Information Security of Automated Systems (10.05.03)**  
5th year · Expected graduation: February 2028
