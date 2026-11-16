# -*- coding: utf-8 -*-
"""
Feasibility Report - Sections 9 through 12
"""

def get_part9_to_12_text():
    return r'''---

## 9. AI Assistance During Software Development: With and Without AI

A prevailing misconception in modern management is that because an engineer utilizes AI coding assistants (such as GitHub Copilot, Cursor, or Claude), the engineering labor cost drops to zero, and delivery should occur in days.

To evaluate software investment accurately, leadership must understand **where AI genuinely accelerates work, where it introduces friction, and where human accountability is irreplaceable**.

### 9.1 Software Development Lifecycle (SDLC) Stage-by-Stage Comparison

| SDLC Phase | Velocity With AI Coding Assistance | Velocity Without AI (Traditional) | What Remains Strictly Under Human Professional Judgment |
| :--- | :--- | :--- | :--- |
| **1. Requirements & Scoping** | Rapid generation of draft user stories, edge cases, and change card outlines. | Slower manual composition of technical specifications and acceptance criteria. | Aligning organizational policy, defining legal liability boundaries, and negotiating client acceptance criteria. |
| **2. Frontend Implementation** | Fast generation of Streamlit container scaffolding, HTML wrappers, and UI forms. | Hand-crafting every widget layout, session-state binding, and CSS rule. | Intuitive layout, visual hierarchy, mobile viewport usability, and cross-browser consistency. |
| **3. Backend & Business Logic** | Instant drafting of Python service functions, data models, and REST adapters. | Manual authoring of data manipulation logic, loops, and error handlers. | Designing rock-solid RBAC permissions, preventing hybrid role context bleed, and session isolation. |
| **4. Database & SQL Engineering** | Synthesizes complex PostgreSQL DDL, foreign key syntax, and migration scripts. | Writing SQL DDL and migration scripts manually from documentation. | Ensuring cascading rules do not accidentally purge active data; preserving live records during structural schema updates. |
| **5. QA & Test Automation** | Generates hundreds of boilerplate test assertions, mocks, and fixtures in minutes. | Hand-writing every single unit test case, mock object, and assertion. | Designing realistic multi-user concurrency scenarios, adversarial attack cases, and interpreting test failures. |
| **6. Cybersecurity & Privacy** | Flags common static code vulnerabilities (e.g. SQL injection, exposed API keys). | Manual code inspection and running commercial SAST/DAST command-line tools. | Adversarial penetration testing, verifying business logic flaws, and legal compliance under Indian DPDP Rules. |
| **7. DevOps & Infrastructure** | Drafts Dockerfiles, Caddy reverse-proxy directives, and shell automation scripts. | Authoring configuration files and deployment scripts from memory or man pages. | Live server terminal debugging, SSL handshake configuration, secret key rotation, and disaster recovery. |
| **8. Support & Runbooks** | Produces clear technical documentation, markdown runbooks, and user FAQ drafts. | Manual authoring of operational documentation and troubleshooting guides. | Real-time incident triage, handling panicked user escalations, and taking accountability for live outages. |

### 9.2 Debunking the Myth: "AI Wrote It, So Cost Is Zero"
When an AI assistant generates 500 lines of Python, the developer's job is not finished—**in many ways, it has just begun.**
1. **The Code Verification Burden:** AI models frequently hallucinate function signatures, invent non-existent database columns, or introduce subtle concurrency bugs. The human engineer must inspect every single line with extreme skepticism.
2. **The 15 / 85 Engineering Effort Reality:** 
   * **15% of Time (Drafting):** Typing out the initial code syntax (where AI provides massive 5x to 10x speedups).
   * **85% of Time (Hardening):** Integrating the code into the existing architecture, wiring session-state across 7 role combinations, debugging edge-case race conditions, executing database migrations, testing on mobile devices, and taking legal accountability.
3. **Accountability Cannot Be Outsourced:** When a live database locks up during an institutional demo or private founder financial records leak, an organisation cannot blame an AI model. Professional engineering fees compensate for the **human responsibility, verification rigor, and domain expertise** required to deploy production-safe systems.

---

## 10. Future AI Integrated Workflows: Feasibility and Governance

A critical distinction must be drawn between **AI used to write the software** and **AI functionality embedded inside the software** for end-users.

### 10.1 Current Reality: Deterministic Rules, Not an LLM
In the current Fulcrum Beta 2.0.0 release, the scheme matching engine is **strictly deterministic**:
* It relies on programmed Python rules, database queries, and conditional logic (e.g., `WHERE target_gender = 'Woman' AND state = 'Tamil Nadu'`).
* **There is currently no Large Language Model (LLM) or autonomous agent operating in production.** This is an architectural strength: deterministic matching guarantees that scheme recommendations are transparent, predictable, and free from AI hallucinations.

### 10.2 Recommended Safe Initial AI Use Cases
If leadership decides to introduce model-based AI into Fulcrum, it should be deployed exclusively in **narrowly scoped, human-in-the-loop workflows**:
1. **Scheme Document Plain-Language Explainer:** A Guide (mentor) asks for a plain-language summary of a 40-page government gazette. The AI retrieves the approved PDF, extracts eligibility rules, drafts a bulleted summary with exact page citations, and displays it to the Guide for review.
2. **Consultation Thread Summarizer:** An entrepreneur and Guide complete a 3-week consultation thread spanning 45 messages. With one click, the Guide generates a structured "Action Plan & Next Steps" summary. The Guide reviews and edits the summary before officially saving it to the entrepreneur's Journey.
3. **Bilingual Translation Assistance (Tamil & English):** Generating high-quality Tamil translations of Central government scheme descriptions, allowing rural Tamil Nadu entrepreneurs to understand eligibility criteria, with human policy review.
4. **Administrative Follow-Up Drafting:** Drafting personalized re-engagement emails for inactive entrepreneurs. The Admin reviews the draft before hitting "Send"—no automated bot emails founders without human approval.

### 10.3 Safe AI Scheme Advice Architecture Flowchart

```mermaid
flowchart TD
    U["1. Authorized Guide Submits Scheme Inquiry"] --> P["2. Granular RBAC Verification: Check Access Rights"]
    P --> S["3. Semantic Retrieval: Query Approved Official Scheme Documents"]
    S --> AI["4. LLM Generates Draft Explanation with Direct Citations"]
    AI --> V["5. Automated Guardrail: Verify Citations & Filter Hallucinations"]
    V --> H{"6. Human Guide In-the-Loop Review"}
    H -->|Rejected or Needs Edit| R["Guide Manually Corrects Summary"]
    H -->|Approved| E["Official Verified Guidance Published to Founder Journey"]
```

### 10.4 Governance Frameworks: NIST AI RMF & DPDP Compliance
Any future AI integration must adhere to recognized AI risk governance standards:
* **NIST AI Risk Management Framework (AI RMF 1.0) Generative AI Profile:** Establishing explicit metrics for validity, reliability, safety, transparency, and accountability.
* **Source Grounding (RAG):** The AI must never answer from its pre-trained general knowledge. It must be constrained via Retrieval-Augmented Generation (RAG) to cite only verified government notifications stored in Fulcrum's knowledge base.
* **Strict DPDP Privacy Guardrails:** No personal identifiable information (PII)—such as founder names, Aadhaar numbers, phone numbers, or proprietary financial forecasts—may ever be transmitted to external, third-party model APIs (such as OpenAI or Anthropic) without explicit enterprise data processing agreements ensuring zero training retention.

### 10.5 AI Expansion Scenarios & Realistic Timeframes (Increased, Brutal Times)

| Expansion Scope | Calendar Duration: With AI Coding | Calendar Duration: Traditional (No AI) | Required Engineering Team Composition | Estimated One-Time Implementation Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Scenario 1: Controlled Document-Explainer Pilot** | **6 – 10 weeks** | **9 – 16 weeks** | Full-Stack / LLM Engineer, QA Engineer, Scheme Policy Expert, Security Reviewer. | **₹3,00,000 – ₹8,00,000** |
| **Scenario 2: Daily Workflow Assistant (Summaries & Bilingual)** | **3 – 5 months** | **5 – 8 months** | Senior Backend Engineer, AI/RAG Specialist, Frontend Dev, Fractional QA, Domain Lead. | **₹10,00,000 – ₹25,00,000** |
| **Scenario 3: Advanced Autonomous Knowledge Operations** | **5 – 9+ months** | **8 – 14+ months** | Dedicated AI Lead, Data Pipeline Engineer, Senior Backend, QA Lead, Platform DevOps, Legal Counsel. | **₹25,00,000 – ₹60,00,000+** |

### 10.6 Recurring Monthly Operational Costs for AI
Operating an AI-enabled platform incurs ongoing monthly service expenditures beyond server hosting:
* **Model Inference APIs:** Per-token charges for LLM processing (input prompt tokens + output completion tokens) across cloud providers (e.g. Google Vertex AI, Anthropic, or AWS Bedrock).
* **Vector Database & Embeddings:** Managed vector storage (e.g., pgvector on Supabase, Pinecone, or Qdrant) and embedding model execution fees.
* **Knowledge Base Maintenance:** Continuous human policy auditing to ensure government scheme updates, gazette amendments, and deadline extensions are reflected in the vector store.
* **Continuous Evaluation & Guardrails:** Automated testing pipelines executing regression benchmarks against golden question-answer datasets to catch model drift.
* **Monthly Operating Estimate:** A supervised, controlled pilot requires **₹25,000 to ₹75,000 per month** in combined API tokens, vector infrastructure, and fractional oversight. A scaled institutional deployment with thousands of daily queries can exceed **₹1,50,000 to ₹3,50,000 per month** in direct operating overhead.

---

## 11. Scalability, Availability and Business Continuity

A fundamental responsibility of programme leadership is ensuring the platform can reliably support growth without crashing during peak usage.

### 11.1 Concurrency Reality in Streamlit Architecture
To evaluate scalability honestly, leadership must understand the underlying technical mechanics:
1. **Single-Process Python & The Global Interpreter Lock (GIL):** Streamlit applications execute in a Python runtime. While asynchronous event loops handle I/O, heavy computational logic runs on a single thread.
2. **WebSocket Session Memory Overhead:** Unlike traditional stateless web applications (which serve a request and immediately close the connection), Streamlit maintains a **persistent, stateful WebSocket connection** for every open browser tab.
3. **Memory Consumption:** On Fulcrum's current Hostinger KVM 2 VPS (8 GB RAM):
   * Base operating system and Docker runtime: ~1.5 GB.
   * Caddy reverse proxy and monitoring agents: ~0.5 GB.
   * Available memory for Streamlit: ~6.0 GB.
   * Each active user session holding complex dataframes, scheme lists, and profile objects consumes approximately **80 MB to 150 MB of RAM**.
   * **Real-World Concurrency Ceiling:** The existing single container can comfortably support **30 to 50 simultaneous active users** performing concurrent operations (clicking buttons, uploading decks, filtering schemes) before memory swapping or page re-run lag occurs.
4. **Registration Scale vs Concurrent Load:** Having 5,000 registered users in PostgreSQL is trivial; database storage easily handles tens of thousands of dormant rows. The true performance bottleneck is how many individuals are actively navigating the interface at the exact same minute.

### 11.2 Programme Scale Cohorts & Technical Milestones

| Programme Scale Cohort | Concurrent User Target | Architectural Emphasis | Mandatory Empirical Proof Required |
| :--- | :--- | :--- | :--- |
| **Cohort 1: Controlled Pilot (Up to 100 Registered Users)** | 10 – 25 concurrent users | Role-based data isolation; zero session cross-bleed; rapid bug fixing. | Passing circular E2E test suites; verified staging deployment. |
| **Cohort 2: Growing Live Programme (~1,000 Registered Users)** | 50 – 100 concurrent users | Streamlit caching optimizations; connection pooling on Supabase; off-site daily backups. | Simulated browser load tests (Locust / k6) showing < 2s response times. |
| **Cohort 3: Institutional Scale (5,000 – 10,000 Users)** | 250 – 500+ concurrent users | Architectural transition: Decoupled FastAPI backend; stateless React/Next.js frontend; Redis caching. | Multi-node autoscaling; load balancer stress testing; SOC-2 Type II audit. |

### 11.3 Incident Lifecycle & Disaster Recovery Flowchart

```mermaid
flowchart TD
    A["Live Production Service Monitored 24/7"] --> B["Automated Health Check Detects Container Crash or High Memory"]
    B --> C{"Alert Triggered to Designated On-Call Engineer"}
    C -->|Minor Performance Lag| D["Execute Graceful Container Restart & Flush Cache"]
    C -->|Critical Database Corruption or Host Outage| E["Initiate Disaster Recovery Protocol"]
    
    E --> F["1. Freeze DNS / Activate Maintenance Landing Page"]
    F --> G["2. Provision Standby VPS or Failover Node"]
    G --> H["3. Restore Database from Latest Encrypted Off-Site Backup"]
    H --> I["4. Verify Schema Parity & Execute Automated Health Suite"]
    I --> J["5. Redirect Caddy DNS & Resume Production Traffic"]
    J --> K["6. Issue Incident Root-Cause Analysis (RCA) to Leadership"]
```

### 11.4 Operational Service Level Agreements (SLAs)
To establish institutional trust, the technology team must commit to measurable operational baselines:
* **Support Availability:** Business Hours Support (9:00 AM – 6:00 PM IST, Monday through Friday) for standard pilot operations.
* **Severity-0 (P0) Outage Target:** Initial triage within **60 minutes**; resolution or rollback within **4 hours**.
* **Severity-1 (P1) Defect Target:** Triage within **4 hours**; hotfix release within **24 to 48 hours**.
* **Recovery Point Objective (RPO):** Maximum allowable data loss window: **< 24 hours** (guaranteed via daily automated PostgreSQL snapshot exports stored on isolated off-site S3 storage).
* **Recovery Time Objective (RTO):** Maximum allowable service downtime during a catastrophic VPS failure: **< 4 hours** to rebuild container infrastructure from documented runbooks.

---

## 12. Three-Year Budgeting and Responsibility Model

A common financial mistake in early-stage programmes is treating software investment as a single, one-time project fee. Modern digital platforms operate under continuous lifecycles requiring three distinctly budgeted capital accounts.

### 12.1 The Three Capital Accounts

```mermaid
flowchart TD
    BUDGET["Comprehensive Technology Investment"] --> ACC1["Account 1: Complete & Verify Today's Beta<br/>(One-Time Project CapEx)"]
    BUDGET --> ACC2["Account 2: Operate, Support & Maintain<br/>(Recurring Monthly/Annual OpEx)"]
    BUDGET --> ACC3["Account 3: Strategic Platform Expansion<br/>(Approved Discretionary Initiatives)"]
    
    ACC1 --> D1["Close P0/P1 Defects, UI/UX Overhaul, Security Penetration Test, Handover"]
    ACC2 --> D2["Hostinger VPS, Supabase DB, S3 Storage, Monitoring, Core Engineering Retainer"]
    ACC3 --> D3["React/Workers Migration, AI Document Explainer, Investor Portal, Mobile App"]
```

1. **Account 1: Complete and Verify Today's Beta (One-Time CapEx):** Dedicated milestone funding to resolve open defects, overhaul user interface consistency on Streamlit, complete independent security audits, and achieve formal institutional sign-off.
2. **Account 2: Operate, Maintain, and Support (Recurring OpEx):** Non-negotiable recurring expenditure to keep the live platform secure, online, backed up, patched, and supported by a qualified technical owner.
3. **Account 3: Strategic Platform Expansion (Discretionary CapEx):** Individually budgeted business cases for major future capabilities: building a dedicated mobile app, rewriting the frontend in React, or launching an enterprise AI assistant.

### 12.2 Three-Year Financial Planning Matrix (Scenarios)
The following projections model realistic expenditure across three operating modes. These are planning benchmarks based on current Indian market rates, not contractual quotes.

| Operating Mode | Year 1: Complete & Launch | Year 2: Operate & Optimize | Year 3: Scale & Expand | 3-Year Cumulative Total |
| :--- | :--- | :--- | :--- | :--- |
| **Mode 1: Owner-Led Small Pilot**<br/>*(Technical Owner part-time retainer + cloud hosting + annual security check)* | **CapEx:** ₹12,00,000<br/>**OpEx:** ₹6,00,000<br/>**Total:** ₹18,00,000 | **CapEx:** ₹4,00,000<br/>**OpEx:** ₹7,50,000<br/>**Total:** ₹11,50,000 | **CapEx:** ₹5,00,000<br/>**OpEx:** ₹9,00,000<br/>**Total:** ₹14,00,000 | **₹43,50,000** |
| **Mode 2: Lean Managed Platform**<br/>*(Recommended: 2.4 FTE engineering team + hosting + bi-annual audits)* | **CapEx:** ₹20,00,000<br/>**OpEx:** ₹90,84,000<br/>**Total:** ₹1,10,84,000 | **CapEx:** ₹10,00,000<br/>**OpEx:** ₹98,00,000<br/>**Total:** ₹1,08,00,000 | **CapEx:** ₹12,00,000<br/>**OpEx:** ₹1,05,00,000<br/>**Total:** ₹1,17,00,000 | **₹3,35,84,000** |
| **Mode 3: Growth-Stage Institution**<br/>*(6.75 FTE cross-functional team + enterprise cloud + full AI operations)* | **CapEx:** ₹35,00,000<br/>**OpEx:** ₹1,84,80,000<br/>**Total:** ₹2,19,80,000 | **CapEx:** ₹25,00,000<br/>**OpEx:** ₹2,10,00,000<br/>**Total:** ₹2,35,00,000 | **CapEx:** ₹30,00,000<br/>**OpEx:** ₹2,35,00,000<br/>**Total:** ₹2,65,00,000 | **₹7,19,80,000** |

### 12.3 Financial Commentary for the Board
* **Choosing the Right Mode:** An early-stage programme should operate under **Mode 1 or a modified Mode 2**. Moving directly to Mode 3 before achieving product-market fit or securing recurring multi-year institutional funding will lead to premature financial exhaustion.
* **Infrastructure is Cheap; Skilled Talent is the Investment:** Cloud hosting on Hostinger VPS and Supabase accounts for less than **3% to 5%** of the total budget. **95% of software expenditure is human engineering, testing, security auditing, and domain verification.**
'''
