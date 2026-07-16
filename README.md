# Gleb Lutfullin

## AI Engineer · Agentic Systems · Backend & Infrastructure

I build AI agents and production systems that automate real business processes — from research and content operations to CRM, billing, customer access, monitoring, and infrastructure management.

Currently working at **Fortune Tavern Ltd (UK)**, where I design and ship AI-powered products, backend services, internal automation, and distributed infrastructure.

### What I work on

- Multi-agent systems and long-running agentic workflows
- AI automation of business operations and internal processes
- LLM integration with APIs, databases, business rules, and external services
- Structured outputs, validation, retries, fallbacks, tracing, and human approval
- Production backend systems, billing, authentication, telemetry, and security
- Distributed infrastructure, CI/CD, monitoring, incident response, and safe rollout

### Selected work

#### AI Marketing Operating System
A multi-agent platform that automates the content operations loop:

`trend scanning → audience analysis → idea generation → strategy → script generation → QA → approval → publishing → metrics → learning`

Built with Python, FastAPI, OpenAI Responses API, Pydantic, PostgreSQL, Redis, Temporal, Docker, and GitHub Actions.

Key engineering decisions:
- schema-constrained LLM outputs with application-side validation;
- retry and deterministic fallback paths;
- platform-risk and brand-safety QA;
- human-in-the-loop approval for medium-risk output;
- idempotent publishing and product-metric ingestion;
- feedback loop that converts performance data into new hypotheses.

#### AI-assisted CRM and business automation
Designed an internal CRM for partner and acquisition operations. The system manages the full funnel from prospect to active partner and automatically connects outreach activity with product outcomes.

Capabilities include:
- pipeline stages, ownership, notes, contacts, and follow-up state;
- automatically generated partner codes and tracked web/Telegram links;
- attribution of clicks, registrations, paid users, revenue, payouts, and net result;
- conversion calculations, search, filtering, and CSV export;
- agent-assisted maintenance, audits, implementation, testing, and documentation.

This replaced fragmented manual tracking with a single operational system and reduced time spent reconciling acquisition data across different tools.

#### Fortune VPN
A multi-platform VPN product with a Go control plane, PostgreSQL, Android/iOS clients, VLESS/Xray transport, billing, entitlements, monitoring, and distributed relay infrastructure.

Areas I own or contribute to:
- API and account-level entitlement model;
- device and transport-session management;
- relay orchestration and health-aware routing;
- payment idempotency and subscription correctness;
- authentication and security hardening;
- telemetry, monitoring, runbooks, rollback, and incident response;
- agentic development workflow with human approval for production-impacting work.

#### Distributed Relay Platform
A sanitized portfolio reference for a real distributed network platform: common API, PostgreSQL, Docker relay nodes, health-aware load balancing, custom monitoring, staging, CI/CD, smoke checks, and rolling deployment.

Repository: [distributed-relay-platform](https://github.com/downmeansoff/distributed-relay-platform)

### Engineering approach

- I start with the business process, states, constraints, and failure modes — not with the prompt.
- I use structured outputs wherever downstream code must trust an LLM response.
- Critical operations are idempotent, observable, testable, and recoverable.
- Agents work inside explicit permissions, scopes, branch rules, and approval gates.
- I use coding agents as an engineering team multiplier while retaining responsibility for architecture, review, testing, and production decisions.

### Core stack

**AI / LLM:** OpenAI Responses API, OpenRouter, structured outputs, JSON Schema, Pydantic, prompt engineering, agent workflows, human-in-the-loop, evaluation and safety checks

**Backend:** Python, FastAPI, Go, TypeScript, Fastify, REST APIs, background jobs, webhooks

**Data:** PostgreSQL, SQLAlchemy, Alembic, Prisma, Redis

**Infrastructure:** Docker, GitHub Actions, Railway, Linux, Bash, SSH automation, Prometheus, Sentry, VLESS, Xray

**Quality:** pytest, API testing, SQL verification, regression testing, security audits, incident runbooks

### Experience

- **AI Engineer / Product Engineer — Fortune Tavern Ltd, UK** · 2026–present
- **Manual QA Engineer — BFT Holding** · 2025–2026
- **Network Implementation Engineer — Gazinformservice** · 2024–2025

### Current focus

I am interested in AI Engineer roles involving agentic workflows, LLM tools, business-process automation, backend integrations, evaluation, and production deployment.

[Technical case studies](./CASE_STUDIES.md)
