# -*- coding: utf-8 -*-
"""
CEO Briefing - Part 5: Risks, Governance, Practical Roadmap, and References
"""

def get_part5_text():
    return r"""---

## 13. Current Risks, Limitations & Practical Governance

To protect the institution's capital and ensure smooth operations, leadership must address existing operational limitations before scaling public onboarding.

### 13.1 Current Technical Limitations to Address

1. **Streamlit Concurrent Active User Ceiling:** The current frontend runs on Streamlit inside Docker on an 8 GB RAM Hostinger VPS. Because Streamlit maintains an active, persistent connection for every open browser tab, the server comfortably supports **30 to 50 simultaneous active users** before memory lag occurs. This is completely adequate for an institutional pilot with 1,000 registered users, but cannot support a live, simultaneous mass-login event without scaling.
2. **Database Inactivity & Memory Alerts:** The project currently operates on Supabase's Free Tier. As noted in system telemetry, memory commitment is flagged as high due to baseline background services, and the free database will auto-pause if inactive for seven consecutive days. Upgrading to Supabase Pro ($25/mo ≈ ₹2,100/mo) resolves this permanently.
3. **Reconciling the 32-User QA Scorecard:** The packaged QA report in the repository tested git commit `988127b` and noted three critical defects (account lifecycle logging, hybrid user consultation context, and temporary password handling). While fix code was written subsequently, an evidence-backed release check must be run on the live server to formally close these items.

### 13.2 Institutional Governance: The One-Page Change Card Protocol
To eliminate scope creep, budget disputes, and software instability, leadership should mandate that **no developer touches the codebase without an approved One-Page Change Card**:

* **What business outcome is needed, and why now?**
* **Which user roles see or use it?** (Founder, Guide, SME, or Admin?)
* **What existing data, permissions, and historic records are affected?**
* **What must be preserved when an account changes or leaves?**
* **What are the exact, testable acceptance criteria for completion?**
* **Is this a warranty bug fix, a minor enhancement, or a new module?**
* **Who is the authorized executive signing off on scope and payment?**

---

## 14. Phased Next-Stage Execution Roadmap

To transition Fulcrum from a working Beta into a hardened, enterprise-ready platform, the organisation should execute a structured, **four-phase delivery plan**.

### Phase 0: Discovery, Reconciliation & Ownership (Weeks 1 – 2)
* **Goal:** Establish absolute operational clarity and legal protection.
* **Key Actions:**
  1. Complete formal intellectual property assignment, ensuring 100% of source code, repositories, and documentation belong to the institution.
  2. Place all root cloud credentials (Hostinger, Supabase, Resend, domain DNS) into secure institutional escrow.
  3. Reconcile the live cloud deployment against the Git repository to verify all 12 database migrations are active.
  4. Formally inventory open defects and prioritize them into warranty fixes versus new enhancements.
* **Governance Rule:** Zero production changes or feature additions during this phase.

### Phase 1: Defect Closure & Interface Stabilization (Month 1 / Weeks 3 – 6)
* **Goal:** Ensure existing features work flawlessly across all user roles.
* **Key Actions:**
  1. Resolve verified P0 and P1 defects on the live server (account lifecycle logging, hybrid consultation isolation, and password resets).
  2. Set up an isolated staging server so testing does not disrupt live data.
  3. Standardize navigation, button placements, and error messages across all four portals on the existing Streamlit framework.
  4. Execute automated regression test suites to prove that fixing one bug does not break older features.

### Phase 2: Independent Assurance & Controlled Pilot (Months 2 – 3 / Weeks 7 – 12)
* **Goal:** Prove system security, resilience, and usability under real-world conditions.
* **Key Actions:**
  1. Commission an independent third-party cybersecurity review scoped to **OWASP ASVS 5.0.0 Level 2**.
  2. Conduct structured User Acceptance Testing (UAT) with a closed cohort of 20 real founders and 5 senior mentors.
  3. Perform a formal disaster recovery rehearsal: delete the staging database and restore operations from an encrypted off-site backup within 4 hours.
  4. Launch a controlled pilot with active monitoring, bug triage, and daily off-site backups.

### Phase 3: Strategic Expansion & Supervised AI Pilot (Months 4 – 12)
* **Goal:** Expand platform capabilities and pilot high-value AI workflows safely.
* **Key Actions:**
  1. Process approved Change Requests (e.g., dedicated Investor Portal or automated SMS gateways).
  2. Pilot a narrowly scoped, document-grounded AI Scheme Explainer with mandatory mentor review before publishing advice.
  3. Monitor user growth and evaluate whether future transaction volumes justify a long-term transition to a decoupled React/FastAPI architecture.

---

## 15. Summary of Recommendations for Executive Leadership

1. **Protect the Asset:** Acknowledge that the solo developer constructed substantial, highly valuable business logic that would have cost ₹35 Lakh to ₹65 Lakh if commissioned through an agency. Secure the code and IP immediately.
2. **Avoid an Expensive Full Rewrite:** Do not scrap the working Streamlit engine to build a React application from scratch. Polish the existing user interface for ₹4L to ₹9L instead of spending ₹50L+ on an unnecessary 8-month rewrite.
3. **Fund a Lean Operational Support Model:** Budget an ongoing operational support retainer (₹1.5L to ₹2.5L/month for a pilot; ₹7.57L/month for a lean managed team) to ensure the platform is patched, monitored, backed up, and supported by accountable engineers.
4. **Mandate Independent Verification:** Never rely solely on developer self-testing. Commission independent quality assurance and external cybersecurity testing before publicly onboarding real entrepreneur financial records.
5. **Enforce Change Card Discipline:** Require written business justification and impact analysis before authorizing any new software modifications.

---

## References and Market Benchmarks

1. **Adecco India Salary Guide 2026:** Comprehensive compensation data for Indian software engineering, QA automation, DevOps, and technology leadership roles across Tier-1 and Tier-2 technology centers.
2. **Michael Page India Salary Report 2026:** Benchmark data for senior software architects, engineering management, and enterprise cybersecurity specialists in India.
3. **Clutch Custom Software Development Pricing Guide 2026:** Industry billing rates, project timelines, and delivery model cost comparisons across boutique, mid-market, and enterprise software firms.
4. **OWASP Application Security Verification Standard (ASVS 5.0.0):** The global benchmark for verifying role-based access controls, data boundaries, and web application security.
5. **NIST AI Risk Management Framework (AI RMF 1.0) Generative AI Profile:** Standards for governing safety, transparency, hallucination mitigation, and data privacy in enterprise AI deployments.
6. **MeitY Digital Personal Data Protection (DPDP) Act 2023 & Rules 2025:** Statutory Indian data privacy standards governing user consent, personal data retention, and grievance redressal.
"""

