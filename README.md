# Gleb Lutfullin

**AI Engineer · Agentic Systems · AI Business Automation · Backend & Infrastructure**

I design AI-powered systems that automate real business operations — not isolated chatbots. My work spans multi-agent workflows, LLM integrations, CRM and acquisition automation, billing, customer access, monitoring, and production infrastructure.

Currently working at **Fortune Tavern Ltd (UK)**, where I build and operate AI products, backend services, internal tools, and distributed infrastructure.

## What I build

- Multi-agent workflows connected to APIs, PostgreSQL, internal tools, and business rules
- Structured LLM pipelines with schema validation, retries, deterministic fallbacks, safety checks, and human approval gates
- AI automation for research, content operations, CRM, acquisition, analytics, and operational decision support
- Production backend systems with authentication, billing, entitlements, webhooks, audit logs, and observability
- Distributed infrastructure with health-aware routing, staging, CI/CD, monitoring, rollback, and incident runbooks

## Selected work

### AI Marketing Operating System
A Python/FastAPI multi-agent system that turns trend and product signals into content ideas, scripts, QA decisions, approval tasks, publishing actions, metrics, and new hypotheses.

`Python` `FastAPI` `OpenAI Responses API` `Pydantic` `PostgreSQL` `Redis` `Temporal` `Docker` `GitHub Actions`

### AI-assisted CRM and acquisition platform
An internal CRM for managing partner outreach and attribution across web and Telegram funnels. Tracks pipeline stages, clicks, registrations, paid users, revenue, payouts, net revenue, and conversion. Includes automatically generated tracking links, CSV export, and agent-assisted maintenance and development.

`Go` `PostgreSQL` `REST API` `Telegram` `Attribution` `Analytics` `AI Agents`

### Fortune VPN platform
A multi-platform product with a Go control plane, PostgreSQL, Android/iOS clients, billing, entitlement management, telemetry, and a distributed VLESS/Xray relay network.

`Go` `PostgreSQL` `Kotlin` `Swift` `VLESS/Xray` `Prometheus` `Railway` `CI/CD`

### LLM-powered Telegram Mini App
A production-oriented LLM application with adaptive prompts, safety filtering, bounded outputs, cached generation, PostgreSQL, Telegram authentication, payments, and operational telemetry.

`TypeScript` `Fastify` `OpenRouter` `Prisma` `PostgreSQL` `React` `Sentry`

## Engineering principles

- Model business processes as explicit states, tools, permissions, and transitions
- Prefer structured outputs and validation over unbounded model text
- Design critical operations for idempotency and safe retries
- Keep AI agents fast in feature branches but gated away from production mutations
- Treat tests, observability, auditability, rollback, and recovery as product features
- Use coding agents for parallel analysis and implementation while retaining human ownership of architecture and production decisions

## Core stack

**AI:** OpenAI API, OpenRouter, agentic workflows, structured outputs, prompt engineering, evaluation, safety, human-in-the-loop  
**Backend:** Python, FastAPI, Go, TypeScript, Fastify, REST, webhooks, background jobs  
**Data:** PostgreSQL, SQLAlchemy, Alembic, Prisma, Redis  
**Infrastructure:** Docker, GitHub Actions, Railway, Linux, Bash, Prometheus, Sentry  
**Networking:** TCP/IP, VLAN, VLESS, Xray, relay infrastructure, health-aware routing

## Background

- **AI Engineer / Product Engineer — Fortune Tavern Ltd, UK**
- **Manual QA Engineer — BFT Holding**
- **Network Implementation Engineer — Gazinformservice**

[Detailed case studies](CASE_STUDIES.md) · [GitHub repositories](https://github.com/downmeansoff)
