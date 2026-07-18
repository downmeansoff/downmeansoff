# Engineering Case Studies

These case studies describe selected systems I designed and developed. Production secrets, customer data, private domains, infrastructure identifiers, and proprietary business logic are intentionally omitted.

## 1. Multi-agent marketing operating system

### Business problem

Research, creative production, review, publishing, and performance analysis required repeated manual work and produced inconsistent outputs.

### System

Designed a multi-step workflow with specialized agents for trend scanning, audience analysis, idea generation, creative selection, script generation, quality assurance, and learning from metrics.

### Reliability controls

- OpenAI Responses API with strict JSON Schema outputs
- Pydantic validation and application-side business-rule checks
- Retry policy and deterministic fallback behavior
- Risk classification and automatic rejection of unsafe output
- Human approval for medium-risk content
- LLM call tracing and audit logs
- End-to-end pipeline tests and CI

### Business value

Reduced repetitive work across research, drafting, QA, and reporting; made the process reproducible; and created a foundation for scaling content operations without scaling manual coordination at the same rate.

## 2. AI-assisted CRM and acquisition automation

### Business problem

Partner outreach, campaign attribution, conversion analysis, payouts, and follow-ups were fragmented across manual notes and separate tools.

### System

Built an internal CRM that models the outreach funnel from prospect to active partner. It tracks platform, audience, stage, owner, contact history, tracking codes, web and Telegram links, clicks, registrations, paid users, revenue, payouts, net revenue, and conversion.

### Automation

- Automatic unique tracking-code generation
- Web and Telegram funnel attribution
- Unique-click counting and conversion calculation
- Revenue and payout aggregation
- Search, filtering, stage management, and CSV export
- Agent-assisted feature development, audits, regression analysis, and maintenance

### Business value

Created one source of truth for acquisition operations, reduced manual reconciliation, made partner performance visible, and shortened the path from campaign activity to operational decisions.

## 3. Multi-platform network platform and distributed control plane

### Business problem

A consumer network product had to support several client platforms, multiple access models, distributed relay infrastructure, server-side usage limits, device management, payments, observability, and safe production operations without duplicating core logic across clients.

### Scale and constraints

- 1,000+ users
- 7 infrastructure nodes
- 5 client channels: web, Android, iOS, Telegram, and external clients
- distributed VLESS/Xray data plane
- unreliable and sometimes restricted network paths
- production secrets and operational access that cannot be exposed publicly

### My responsibility

Designed and developed the control-plane, product, and operational architecture around the service. The work covered backend contracts, data models, access policy, node orchestration, deployment safety, monitoring, recovery paths, and coordination between mobile, web, Telegram, and external clients.

### Production architecture

The private production system uses a **Go control plane** backed by PostgreSQL. It coordinates:

- guest, email OTP, Apple, and Google authentication;
- account and device lifecycle;
- account-level entitlements and client capabilities;
- billing and rewarded-access flows;
- region and transport policy publication;
- transport session allocation, rotation, and revocation;
- server-side usage accounting and quota enforcement;
- telemetry, support metadata, metrics, and audit events;
- guarded orchestration of distributed relay nodes.

The network data plane is separated from product state. Restricted node operations apply transport credentials and export usage data, while the control plane remains the source of truth for users, devices, entitlements, access decisions, and recovery semantics.

### Key engineering decisions

#### Shared control plane

Web, Android, iOS, Telegram, and external clients use shared backend contracts. Product and access rules are server-owned instead of being independently reimplemented in each client.

#### Entitlement-driven access

Access is derived from account entitlements and capabilities rather than local purchase state. Device limits, subscription status, and client access are evaluated centrally.

#### Server-side usage enforcement

Traffic usage is collected from infrastructure and applied to server-side quota state. Clients receive the resulting policy instead of being trusted to enforce their own limits.

#### Health-aware routing and fallback

Node health, routing decisions, fallback paths, and egress verification are treated as explicit system behavior. Unhealthy infrastructure can be excluded from rotation, while clients and operations receive stable recovery signals.

#### Versioned contracts

Backend and client behavior use versioned status, error, and recovery contracts. This reduces ambiguity across platforms and makes runtime failures easier to diagnose and reproduce.

### Reliability and operational controls

- component-level health checks and degraded-state reporting
- health-aware routing and automatic unhealthy-node exclusion
- staging and feature-flagged rollout
- smoke tests and runtime evidence collection
- rolling deployment with health gates
- audit logs and structured operational events
- role-separated operational access
- rollback and recovery procedures
- human approval for high-impact production mutations
- incident and support runbooks

### Business value

- avoided duplicating core auth, entitlement, usage, and transport logic across five client channels;
- enabled one backend and data model to support several product surfaces;
- reduced operational risk by separating staging, production, roles, and high-impact actions;
- shortened incident diagnosis through stable contracts, health data, telemetry, and evidence collection;
- allowed infrastructure nodes to be changed or removed without redesigning every client;
- supported growth to 1,000+ users while keeping product policy and network operations centrally controlled.

### Public portfolio boundary

The public [`distributed-relay-platform`](https://github.com/downmeansoff/distributed-relay-platform) repository is a sanitized architecture reference. It demonstrates Docker topology, a minimal API, PostgreSQL, monitoring, health checks, CI/CD, staging, and rolling deployment.

The production Go backend, billing integrations, mobile applications, customer data, private infrastructure, credentials, and proprietary business logic remain private. The public project explicitly documents the difference between the production system and the safe demonstration implementation.

## 4. LLM-powered Telegram product

### Business problem

The product needed personalized generated responses while preserving output quality, safety, response bounds, payments, and operational reliability.

### System

Built an LLM integration with adaptive Russian and English prompts, user-question anchoring, controlled styles, pre-generation safety checks, cached partial outputs, database persistence, Telegram authentication, and payment flows.

### Business value

Converted an LLM capability into a complete product workflow rather than a standalone model call, while improving response consistency, reducing repeated generation, and supporting production operations.

## How I work with AI agents

I use coding agents as an engineering force multiplier for repository analysis, implementation, tests, documentation, and security reviews. I define the architecture, scope, acceptance criteria, safety constraints, and production boundaries, then verify the result through code review, tests, CI, staging, and operational checks.
