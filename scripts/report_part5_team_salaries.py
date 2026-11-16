# -*- coding: utf-8 -*-
"""
Part 5 of the Fulcrum Alpha-to-Beta Development Value, Cost and AI Feasibility Report.
Section 19: AI Implementation Team, Expertise, Salaries and Staffing Models.
Comprehensive benchmark of 10 roles across India, US, and UK, plus 3 staffing models.
"""

def get_part5_text():
    return """# 19. AI IMPLEMENTATION TEAM, EXPERTISE AND SALARIES

Building, integrating, and operating AI capabilities within a regulated enterprise platform requires specific technical competencies. While software vendors often pitch a single "AI developer" who can do everything, production AI systems fail when data privacy, security, model evaluation, and backend database integrations are neglected.

This section provides a rigorous breakdown of the **10 specialist competencies** involved in enterprise AI delivery, current market salary benchmarks in India, comparison rates in the US and UK, and three practical staffing models.

---

### Detailed Specification of the 10 Specialist Roles

1. **AI Solution Architect**
   * *Responsibilities:* High-level system design, vendor API selection, privacy architecture, latency budgeting, model routing strategy, and total cost of ownership (TCO) management.
   * *Required Experience:* 8–12+ years total software engineering, with 3+ years in production AI/ML deployments.
   * *Core Skills:* Python, Distributed Systems, Cloud Architecture (AWS/GCP), API Security, Cost Optimization, LLM Governance.
   * *Indian Compensation (2025–2026):* INR 30–50 LPA (INR 2,50,000 – INR 4,15,000 / month).
   * *Indian Contractor Rate:* $45 – $75 / hour (INR 3,800 – INR 6,300 / hr).
   * *US / UK Comparable Benchmark:* US: $180,000 – $260,000 / yr ($110 – $175 / hr). UK: £90,000 – £140,000 / yr (£80 – £130 / hr).
   * *Expected Project Allocation:* 20% – 30% fractional (advisory, architectural oversight, and milestone reviews).

2. **LLM / Application Engineer**
   * *Responsibilities:* Prompt engineering, few-shot contextual design, structured output parsing (JSON/Pydantic schemas), tool calling, API wrapper resilience, and retry logic.
   * *Required Experience:* 3–6 years software engineering, with 1.5+ years working directly with GenAI APIs.
   * *Core Skills:* Python, OpenAI / Anthropic / Gemini SDKs, LiteLLM, Prompt Caching, Token Optimization, Async I/O.
   * *Indian Compensation:* INR 14–26 LPA (INR 1,15,000 – INR 2,15,000 / month).
   * *Indian Contractor Rate:* $25 – $45 / hour (INR 2,100 – INR 3,800 / hr).
   * *US / UK Comparable Benchmark:* US: $130,000 – $185,000 / yr ($80 – $125 / hr). UK: £65,000 – £95,000 / yr (£55 – £85 / hr).
   * *Expected Project Allocation:* 100% full-time during active feature implementation.

3. **Python Backend Integration Engineer**
   * *Responsibilities:* Connecting AI outputs to Fulcrum's database services (`services/*.py`), writing PostgreSQL queries, managing database transactions, and building UI controls in Streamlit.
   * *Required Experience:* 4–7 years backend Python engineering.
   * *Core Skills:* Python 3.11+, Streamlit, PostgreSQL / Supabase, PostgREST, Docker, Session State Management, Linux VPS.
   * *Indian Compensation:* INR 12–22 LPA (INR 1,00,000 – INR 1,85,000 / month).
   * *Indian Contractor Rate:* $20 – $38 / hour (INR 1,700 – INR 3,200 / hr).
   * *US / UK Comparable Benchmark:* US: $120,000 – $165,000 / yr ($70 – $110 / hr). UK: £60,000 – £85,000 / yr (£50 – £75 / hr).
   * *Expected Project Allocation:* 100% full-time during active development.

4. **Data Engineer (Knowledge Structuring)**
   * *Responsibilities:* Ingesting, parsing, cleaning, and structuring 179+ government scheme guidelines from PDF gazettes into machine-readable JSON metadata.
   * *Required Experience:* 3–5 years data engineering / ETL.
   * *Core Skills:* Python, PyPDF, Regex, Data Cleaning, PostgreSQL Schema Design, JSONB Indexing.
   * *Indian Compensation:* INR 10–18 LPA (INR 85,000 – INR 1,50,000 / month).
   * *Indian Contractor Rate:* $18 – $30 / hour (INR 1,500 – INR 2,500 / hr).
   * *US / UK Comparable Benchmark:* US: $115,000 – $155,000 / yr. UK: £55,000 – £80,000 / yr.
   * *Expected Project Allocation:* 40% part-time during data preparation phase.

5. **Retrieval / RAG Engineer (Semantic Search)**
   * *Responsibilities:* Implementing chunking strategies, generating vector embeddings, managing Supabase `pgvector` indexes (HNSW), and tuning similarity search relevance.
   * *Required Experience:* 3–6 years software / ML engineering.
   * *Core Skills:* Vector Databases (pgvector, Pinecone), Sentence Transformers, Cosine Similarity, Hybrid Keyword+Semantic Search.
   * *Indian Compensation:* INR 15–28 LPA (INR 1,25,000 – INR 2,30,000 / month).
   * *Indian Contractor Rate:* $28 – $50 / hour (INR 2,350 – INR 4,200 / hr).
   * *US / UK Comparable Benchmark:* US: $140,000 – $195,000 / yr. UK: £70,000 – £105,000 / yr.
   * *Expected Project Allocation:* 30% part-time (only required if Phase 3 RAG search is built).

6. **AI Evaluation & Quality Assurance Specialist**
   * *Responsibilities:* Building benchmark datasets of real founder queries, measuring hallucination rates, testing prompt variations against ground truth, and running automated regression suites.
   * *Required Experience:* 3–6 years test automation / QA, with experience in model evaluation frameworks.
   * *Core Skills:* Pytest, Playwright, LLM-as-a-Judge Evaluation, Prompt Drift Detection, Precision/Recall Metrics.
   * *Indian Compensation:* INR 9–16 LPA (INR 75,000 – INR 1,35,000 / month).
   * *Indian Contractor Rate:* $18 – $32 / hour (INR 1,500 – INR 2,700 / hr).
   * *US / UK Comparable Benchmark:* US: $105,000 – $145,000 / yr. UK: £50,000 – £75,000 / yr.
   * *Expected Project Allocation:* 50% part-time across build and pre-deployment gates.

7. **Cloud / MLOps Engineer**
   * *Responsibilities:* Managing VPS infrastructure, Caddy reverse proxies, Docker container health, logging, API quota alerting, and automated container rebuilds.
   * *Required Experience:* 4–7 years DevOps / Site Reliability Engineering.
   * *Core Skills:* Docker, Docker-Compose, Linux (Ubuntu), Bash Scripting, Reverse Proxies (Caddy/Nginx), Supabase Ops.
   * *Indian Compensation:* INR 12–24 LPA (INR 1,00,000 – INR 2,00,000 / month).
   * *Indian Contractor Rate:* $22 – $40 / hour (INR 1,850 – INR 3,400 / hr).
   * *US / UK Comparable Benchmark:* US: $125,000 – $175,000 / yr. UK: £60,000 – £90,000 / yr.
   * *Expected Project Allocation:* 20% fractional (deployment, monitoring setup, and security hardening).

8. **Application Security & Privacy Specialist (Mandatory Reviewer)**
   * *Responsibilities:* PII data masking verification, prompt injection defense audits, role-scoped access policy validation, and DPDP Act compliance checks.
   * *Required Experience:* 6–10+ years cybersecurity and application penetration testing.
   * *Core Skills:* OWASP Top 10 for LLMs, Data Privacy Regulation (India DPDP Act 2023, GDPR), Cryptographic Token Isolation.
   * *Indian Compensation:* INR 22–40 LPA (INR 1,80,000 – INR 3,30,000 / month).
   * *Indian Contractor Rate:* $40 – $70 / hour (INR 3,400 – INR 5,900 / hr).
   * *US / UK Comparable Benchmark:* US: $160,000 – $225,000 / yr. UK: £80,000 – £125,000 / yr.
   * *Expected Project Allocation:* 15% fractional (independent pre-production audit).

9. **Domain Expert: Indian Government Schemes & MSME Policy**
   * *Responsibilities:* Reviewing AI-generated scheme summaries for statutory accuracy, verifying eligibility nuances, and validating Tamil legal terminology.
   * *Required Experience:* 8+ years working with Tamil Nadu Industries Department, MSME-DI, TiE Chennai, or leading state incubators (e.g., IIT Madras Incubation Cell, EDII-TN).
   * *Core Skills:* Government Gazette Interpretation, PMEGP/NEEDS/UYEGP Guidelines, Banking Loan Sanction Norms.
   * *Indian Retainer Compensation:* INR 40,000 – INR 80,000 / month (Part-time institutional retainer).
   * *Expected Project Allocation:* 15% fractional (periodic content audits and validation).

10. **Product / Business Analyst**
    * *Responsibilities:* User story mapping, workflow definition, UX copy, acceptance criteria definition, and mentor feedback synthesis.
    * *Required Experience:* 4–7 years product management in B2B SaaS or edtech.
    * *Indian Compensation:* INR 14–25 LPA (INR 1,15,000 – INR 2,10,000 / month).
    * *Indian Contractor Rate:* $22 – $38 / hour.
    * *Expected Project Allocation:* 30% part-time.

---

### Which Roles Can Be Combined by a Capable Full-Stack Engineer?

In software development, hiring 10 separate individuals for a platform of Fulcrum's scale is financially irresponsible and creates excessive managerial overhead.

A **Senior Full-Stack Python / AI Engineer** can comfortably execute the responsibilities of:
* Role 1 (AI Solution Architect - for standard hosted API integrations);
* Role 2 (LLM / Application Engineer);
* Role 3 (Python Backend Integration Engineer);
* Role 4 (Data Engineering / Data Extraction);
* Role 5 (Basic Semantic Search / Embeddings);
* Role 7 (Cloud / Docker Deployment Ops).

However, **the following two competencies MUST NEVER be performed solely by the building engineer:**
1. **Application Security & Privacy Audit (Role 8):** The developer who writes the code has cognitive blind spots regarding their own assumptions. An independent security review (even for 15–20 hours) is essential before production release.
2. **Domain Expert Policy Review (Role 9):** Software engineers do not understand the subtle bureaucratic clauses of Tamil Nadu state industrial subsidies. A domain consultant must verify scheme summaries before they are presented to entrepreneurs.

---

### Three Practical Staffing Models

```
========================================================================================================================
STAFFING MODEL 1: SOLO EXPERIENCED DEVELOPER + SPECIALIST REVIEWS (Recommended for Minimal/Practical AI)
========================================================================================================================
Team Composition:
  - 1 Senior Full-Stack Python & AI Engineer (Full-time: 160 hrs/mo) : $2,800 - $3,500/mo (INR 2.35L - 2.95L)
  - 1 Fractional Security & Privacy Specialist (Audit Retainer: 15 hrs) : $750 - $1,000 one-time
  - 1 MSME Scheme Policy Consultant (Review Retainer: 15 hrs)         : $500 - $750 one-time
Total Monthly Burn Rate: $2,800 - $3,500 / month
Strengths: Extremely high development velocity, minimal communication overhead, direct accountability, lowest cost.
Weaknesses: Relies on one primary individual; potential delivery delays if unexpected operational blockers arise.

========================================================================================================================
STAFFING MODEL 2: LEAN AI INTEGRATION POD (Recommended for Advanced AI Platform)
========================================================================================================================
Team Composition:
  - 1 Lead Full-Stack / AI Architect (100% full-time)                : $3,200 - $4,200/mo
  - 1 Backend & Database Integration Engineer (100% full-time)       : $2,000 - $2,800/mo
  - 1 QA Automation & Model Evaluation Specialist (50% part-time)    : $1,000 - $1,500/mo
  - 1 Part-time Product & Scheme Policy Analyst (30% part-time)      : $800 - $1,200/mo
Total Monthly Burn Rate: $7,000 - $9,700 / month (INR 5.8L - 8.1L / mo)
Strengths: High throughput, peer code reviews, formal test automation, institutional continuity.
Weaknesses: Requires structured sprint coordination and project management.

========================================================================================================================
STAFFING MODEL 3: ENTERPRISE AI DELIVERY TEAM (Commercial Vendor / Corporate Implementation)
========================================================================================================================
Team Composition:
  - 1 Engagement Manager / Product Owner (50% allocation)            : $3,500/mo
  - 1 Lead AI Solutions Architect (30% allocation)                   : $3,000/mo
  - 2 Senior Full-Stack Developers (100% allocation)                 : $6,000/mo combined
  - 1 Data / RAG Specialist (100% allocation)                        : $2,800/mo
  - 1 Full-time QA Engineer (100% allocation)                        : $2,000/mo
  - 1 Security, Compliance & DevOps Specialist (50% allocation)      : $2,500/mo
  - Agency Management & Infrastructure Markup (25%)                  : $4,950/mo
Total Monthly Agency Billing: $24,750 / month (INR 20.8 Lakhs / month)
Strengths: Formal SLA guarantees, enterprise insurance, extensive documentation, multi-tier escalation paths.
Weaknesses: Very high burn rate, rigid change-request billing, slower turnaround on quick iterations.
========================================================================================================================
```
"""

