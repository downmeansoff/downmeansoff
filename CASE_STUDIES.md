# Engineering Case Studies

These case studies describe selected systems I designed, coordinated, and developed. Production secrets, customer data, private domains, infrastructure identifiers, credentials, and proprietary business logic are intentionally omitted.

## 1. Fortune Network Platform — multi-platform product, Go control plane and AgentOps

### Business problem

A consumer network product had to support Android, iOS, web, Telegram, and external clients while sharing one source of truth for authentication, devices, subscriptions, access policy, usage, telemetry, and infrastructure operations.

The platform also needed to operate across unreliable and sometimes restricted network paths without duplicating business logic in every client or allowing infrastructure failures to cascade across the product.

### Scale and product surface

- **1,000+ users**
- **7 production infrastructure nodes**
- **5 client channels**: web, Android, iOS, Telegram, and external clients
- distributed VLESS/Xray data plane
- PostgreSQL-backed product and operational state
- shared backend contracts across all client applications

### My responsibility

I led product and technical delivery across:

- product requirements, architecture, task decomposition, and acceptance criteria;
- Android and iOS application delivery coordination;
- shared API contracts and PostgreSQL data models;
- authentication, device lifecycle, entitlements, billing flows, sessions, and usage policy;
- distributed infrastructure, health-aware routing, observability, and incident readiness;
- CI/CD, staging validation, rolling rollout, rollback, and production verification;
- an AI-assisted AgentOps workflow for implementation, QA, security review, and documentation.

My role combined product ownership, architecture, engineering coordination, production validation, and operational reliability.

### Product architecture

```text
Web / Android / iOS / Telegram / External clients
                         ↓
                 Shared API contracts
                         ↓
                  Go control plane
      Auth · Devices · Entitlements · Billing
      Sessions · Usage · Telemetry · Support
                         ↓
                    PostgreSQL
                         ↓
             Distributed network layer
                  7 production nodes
```

The private production control plane coordinates:

- guest, email OTP, Apple, and Google authentication;
- account and device lifecycle;
- account-level entitlements and client capabilities;
- billing and rewarded-access flows;
- region and transport policy publication;
- session allocation, rotation, and revocation;
- server-side usage accounting and quota enforcement;
- telemetry, support metadata, metrics, and audit events;
- guarded orchestration of distributed relay nodes.

### Mobile delivery

Android and iOS clients use versioned backend contracts instead of reimplementing product policy locally. The applications receive server-owned state for authentication, devices, entitlements, available regions, transport policy, session recovery, and error handling.

I coordinated requirements, client-server integration, testing, release preparation, and production issue resolution across the mobile delivery lifecycle.

### Key engineering decisions

#### One control plane for every client

Product state and access rules remain server-owned. This avoids separate implementations of authentication, entitlements, usage limits, and transport behavior across five client channels.

#### Control-plane and data-plane separation

The Go backend owns product state and orchestration decisions. Infrastructure nodes execute restricted transport operations. This limits the blast radius of node-level changes and separates customer-facing logic from network runtime.

#### Server-side enforcement

Access, device limits, traffic quotas, and capabilities are derived from account entitlements and server-side usage data rather than trusting local client state.

#### Health-aware routing and recovery

Node health, routing decisions, fallback paths, and egress verification are explicit platform behavior. Unhealthy nodes can be excluded automatically, while clients receive stable recovery signals.

#### Versioned contracts

Clients and backend use versioned status, error, and recovery contracts. Runtime failures are easier to reproduce, diagnose, and handle consistently across platforms.

### Reliability and operational controls

- component-level health checks and degraded-state reporting;
- health-aware routing and automatic unhealthy-node exclusion;
- egress verification before a session is treated as valid;
- staging and feature-flagged rollout;
- smoke tests and runtime evidence collection;
- rolling deployment with health gates;
- structured logs, telemetry, metrics, and audit events;
- role-separated operational access;
- rollback and recovery procedures;
- human approval for high-impact production mutations;
- incident and support runbooks.

### AgentOps workflow

```text
Product requirement
        ↓
Architecture, scope and acceptance criteria
        ↓
Specialized coding agents in isolated branches
        ↓
QA, regression checks, tests and security review
        ↓
CI/CD, staging validation and smoke evidence
        ↓
Human-controlled production decision
```

Specialized agents assist with repository analysis, scoped implementation, test generation, regression checks, documentation, and security review. Architecture, production boundaries, permissions, risk decisions, and releases remain human-controlled.

### Business value

- avoided duplicating core auth, entitlement, usage, and transport logic across five client channels;
- enabled one backend and data model to support mobile, web, Telegram, and external products;
- supported growth to 1,000+ users while keeping product policy and network operations centrally controlled;
- reduced operational risk by separating staging, production, roles, and high-impact actions;
- shortened incident diagnosis through stable contracts, health data, telemetry, and evidence collection;
- allowed infrastructure nodes to be changed or removed without redesigning every client;
- accelerated engineering delivery through controlled use of coding agents without giving them unrestricted production access.

### Public portfolio boundary

The public [`distributed-relay-platform`](https://github.com/downmeansoff/distributed-relay-platform) repository is a sanitized architecture reference. It demonstrates Docker topology, a minimal API, PostgreSQL, monitoring, health checks, CI/CD, staging, and rolling deployment.

The production Go backend, billing integrations, mobile source code, customer data, private infrastructure, credentials, and proprietary business logic remain private.

---

## 2. Multi-agent marketing operating system

### Business problem

Research, creative production, review, publishing, and performance analysis required repeated manual work and produced inconsistent outputs.

### System

Designed a multi-step workflow with specialized agents for trend scanning, audience analysis, idea generation, creative selection, script generation, quality assurance, approval, and learning from metrics.

The system uses **7 specialized agents** across **5 workflow stages** and models each handoff as an explicit state transition rather than an informal prompt chain.

### Reliability controls

- OpenAI Responses API with strict JSON Schema outputs;
- Pydantic validation and application-side business-rule checks;
- retry policy and deterministic fallback behavior;
- risk classification and automatic rejection of unsafe output;
- human approval for medium-risk content;
- LLM call tracing and audit logs;
- end-to-end pipeline tests and CI.

### Business value

Reduced repetitive work across research, drafting, QA, approval, and reporting; made the process reproducible; and created a foundation for scaling content operations without scaling manual coordination at the same rate.

---

## 3. AI-assisted CRM and acquisition automation

### Business problem

Partner outreach, campaign attribution, conversion analysis, payouts, and follow-ups were fragmented across manual notes and separate tools.

### System

Built an internal CRM that models the acquisition funnel from prospect to active partner. It tracks platform, audience, stage, owner, contact history, tracking codes, web and Telegram links, clicks, registrations, paid users, revenue, payouts, net revenue, and conversion.

### Automation and metrics

- **8 pipeline stages**;
- **9 automatically calculated KPIs**;
- automatic unique tracking-code generation;
- web and Telegram funnel attribution;
- unique-click counting and conversion calculation;
- revenue, payout, and net-revenue aggregation;
- search, filtering, stage management, and CSV export;
- agent-assisted feature development, audits, regression analysis, and maintenance.

### Business value

Created one source of truth for acquisition operations, reduced manual reconciliation, made partner performance visible, and shortened the path from campaign activity to operational decisions.

---

## 4. LLM-powered Telegram product

### Business problem

The product needed personalized generated responses while preserving output quality, safety, response bounds, payments, and operational reliability.

### System

Built an LLM integration with adaptive Russian and English prompts, user-question anchoring, controlled styles, pre-generation safety checks, cached partial outputs, database persistence, Telegram authentication, and payment flows.

The product combines a TypeScript/Fastify backend, PostgreSQL, Prisma, OpenRouter, Telegram Mini Apps, Telegram Stars, React, Railway, and Sentry.

### Engineering controls

- bounded model outputs;
- safety checks and fallback behavior;
- idempotent payment processing;
- cached partial generation;
- structured persistence and auditability;
- server-side access control;
- production logs and Sentry-based operational visibility.

### Business value

Converted an LLM capability into a complete product workflow rather than a standalone model call, while improving response consistency, reducing repeated generation, and supporting production operations.

---

## How I work with AI agents

I use coding agents as an engineering force multiplier for repository analysis, implementation, tests, documentation, regression checks, and security reviews.

I define the architecture, scope, acceptance criteria, safety constraints, data contracts, production permissions, and release boundaries. Agent output is verified through code review, tests, CI, staging, smoke checks, logs, and operational validation before production delivery.
