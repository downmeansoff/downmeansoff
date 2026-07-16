# Engineering Case Studies

These case studies describe selected systems I designed and developed. Production secrets, customer data, private domains, and proprietary business logic are intentionally omitted.

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

## 3. Production VPN platform and distributed infrastructure

### Business problem
A consumer VPN product required one control plane for multiple clients, reliable access delivery, payments, device management, traffic policies, distributed nodes, and safe operations.

### System
Developed a Go control plane backed by PostgreSQL and integrated with Android, iOS, web, Telegram, billing providers, and a distributed VLESS/Xray network.

### Engineering focus
- Account-level entitlements and device management
- Payment idempotency and duplicate-delivery protection
- Health-aware relay routing and egress verification
- Monitoring, metrics, audit logging, and incident runbooks
- Staging, feature flags, smoke tests, and rollback procedures
- Agentic CI/CD rules that prevent agents from mutating production without explicit human approval

### Business value
Improved service reliability, reduced operational risk, shortened incident diagnosis, and enabled product development across multiple clients and payment channels without duplicating core business logic.

## 4. LLM-powered Telegram product

### Business problem
The product needed personalized generated responses while preserving output quality, safety, response bounds, payments, and operational reliability.

### System
Built an LLM integration with adaptive Russian and English prompts, user-question anchoring, controlled styles, pre-generation safety checks, cached partial outputs, database persistence, Telegram authentication, and payment flows.

### Business value
Converted an LLM capability into a complete product workflow rather than a standalone model call, while improving response consistency, reducing repeated generation, and supporting production operations.

## How I work with AI agents

I use coding agents as an engineering force multiplier for repository analysis, implementation, tests, documentation, and security reviews. I define the architecture, scope, acceptance criteria, safety constraints, and production boundaries, then verify the result through code review, tests, CI, staging, and operational checks.
