# Engineering Case Studies

Systems I designed and built at Fortune Tavern Ltd. Production secrets, customer data, private domains, credentials, and proprietary business logic are intentionally omitted.

## 1. Multi-agent document processing for a logistics client

### Problem

A 14-person unit hand-processed vehicle registration papers and inbound email: reading documents, keying fields into internal systems, deciding where each case should go. Volume was growing, accuracy depended on who was on shift, and the backlog was visible to customers.

### System

A multi-agent pipeline for extraction, validation and routing. Documents and mail enter a common intake, specialised agents extract fields, a validation stage checks them against business rules and known formats, and a routing stage decides the destination or escalates.

### My responsibility

- pipeline and agent architecture, stage boundaries and handoff contracts;
- extraction schemas and Pydantic/JSON Schema validation;
- confidence thresholds and escalation rules for ambiguous documents;
- human review path for anything the pipeline refuses to decide;
- audit logs for every automated decision;
- rollout alongside the existing manual process before switching over.

### Result

- the unit went from **14 people to 2**; the remaining 12 were reassigned to other work;
- the two remaining operators handle exceptions and review, not routine keying;
- every automated decision is traceable to a document, a stage and a model version.

---

## 2. Patient-facing scheduling agent for a private clinic

### Problem

A clinic needed booking, rescheduling, follow-up reminders and answers to routine questions without adding reception staff. The domain carries two hard constraints: identifiable patient data must never reach the model, and an assistant that talks to patients all day can quietly become expensive.

### System

A conversational agent over the clinic's knowledge base and scheduling system: it books and moves appointments, sends follow-up reminders, and answers questions about services and procedures.

### My responsibility

- conversation and context design with a bounded token cost per dialogue;
- patient identifiers substituted before the model call and restored on our side, so the prompt carries the request and not the person;
- knowledge-base retrieval behind the answers (see case 3);
- refusal and handover paths for clinical questions the agent must not answer;
- reminder scheduling with idempotency, so a retry never double-books or double-notifies.

### Result

- routine scheduling and repeat questions handled without a human in the loop;
- per-conversation cost stays inside a defined ceiling instead of scaling with chattiness;
- clinical and edge-case questions route to staff by design, not by accident.

---

## 3. Retrieval evaluation behind the clinic assistant

### Scope

A Python/FastAPI retrieval service with document preparation, chunking, embeddings, cosine vector retrieval, a `/query` endpoint, and offline evaluation over **54 labeled questions**.

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

[`agentic-rag-reference`](agentic-rag-reference/README.md): runnable code showing the same controls on generic data: Pydantic chunk and search contracts, lexical + dense reciprocal-rank fusion, an optional reranker boundary, Recall@k and MRR, retrieval failure buckets, and deterministic tests.

---

## 4. Production multi-agent workflow

### Problem

Research, preparation, QA, approval, execution, and feedback required repeated manual handoffs. A single long prompt was expensive to retry, hard to observe, and unsafe to connect directly to external actions.

### System

A workflow with **7 specialized agents** across explicit state transitions, using OpenAI Agents SDK, Claude Agent SDK, Pydantic contracts, PostgreSQL, Redis, Temporal orchestration, and controlled tool access.

### My responsibility

- agent and workflow architecture;
- tool/function schemas and permissions;
- JSON Schema and Pydantic structured outputs;
- state, context, and memory boundaries;
- bounded retries, fallbacks, timeouts, and stop conditions;
- risk routing and human-in-the-loop;
- cost/failure tracing, regression scenarios, monitoring, and production support.

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

## 5. AI automations for external clients

Delivered across marketing, sales, analytics, and operations for Fortune Tavern's clients. Work started with process discovery and identifying the actual bottleneck, then moved through solution selection, architecture, integrations, pilot rollout, demos, and user feedback.

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

## 6. Distributed Secure Access Platform

### Scale

- **3,000+ users**;
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

[`distributed-relay-platform`](https://github.com/downmeansoff/distributed-relay-platform) is a sanitized runnable architecture reference. Production code, customer data, and private infrastructure details are not included.
