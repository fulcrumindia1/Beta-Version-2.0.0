# Executive Readiness Scorecard: The Fulcrum Platform
## One-Page Production Readiness Status, Business Metrics, Risk Register, and Board Decisions
**Companion Executive Dashboard to FULCRUM_FINAL_CEO_BRIEFING.md | November 2026**

---

## 1. Production Readiness Scorecard (Current Status)

| Functional Readiness Dimension | Status | Assessment in Plain Business Language | Mandatory Next Action |
| :--- | :---: | :--- | :--- |
| **1. Business Service Logic** | 🟢 **GREEN** | 28,330 lines of verified core Python logic covering 31 service modules. | Maintain code freeze during Phase 0 audit. |
| **2. Relational Database Schema** | 🟢 **GREEN** | 23 PostgreSQL tables with foreign keys, cascading rules, and 12 migrations. | Reconcile migration `011` on live staging server. |
| **3. Policy Scheme Matching** | 🟢 **GREEN** | 179 pre-seeded Central & Tamil Nadu schemes with deterministic rules. | Establish quarterly gazette review schedule. |
| **4. Cloud VPS & SSL Hosting** | 🟢 **GREEN** | Dockerized on Hostinger KVM 2 VPS with Caddy 2 automated SSL termination. | Maintain automated health monitoring agent. |
| **5. Multi-Role Permission Isolation** | 🟡 **AMBER** | Working 7-role dynamic workspace switching; verified in automated tests. | Re-verify on live staging to prevent session bleed. |
| **6. User Interface & Mobile Usability** | 🟡 **AMBER** | Clean functional Streamlit screens across 4 portals; needs visual polish. | Execute UI/UX consistency overhaul (₹4L–₹9L). |
| **7. Production Defect Closure** | 🟡 **AMBER** | Fixes committed for 32-user trial findings (lifecycle, passwords, context). | Execute formal release gate re-test on live VPS. |
| **8. Independent Cybersecurity** | 🔴 **RED** | Internal security controls exist; zero external penetration testing conducted. | Commission independent OWASP ASVS audit (₹3L–₹8L). |
| **9. Disaster Recovery Rehearsal** | 🔴 **RED** | Automated backup script exists; zero formal database drop-and-restore rehearsal. | Execute formal staging disaster recovery dry run. |
| **10. Legal & DPDP Compliance** | 🔴 **RED** | Digital NDAs built; formal Indian DPDP Act 2023 legal review uncertified. | Retain qualified Indian privacy counsel. |

---

## 2. Business Success Metrics for the Institutional Pilot

To measure whether the platform is achieving institutional impact during the upcoming pilot, leadership should monitor four objective Key Performance Indicators (KPIs):

```
====================================================================================================
PILOT PHASE BUSINESS SUCCESS METRICS (50-FOUNDER COHORT)
====================================================================================================
Metric Category              | Objective Definition                      | Target Pilot Threshold
-----------------------------+-------------------------------------------+--------------------------
1. Onboarding Completion     | Percentage of registered founders who     | > 85% completion within
   Rate                      | complete profiles and upload pitch decks. | 7 days of onboarding.
-----------------------------+-------------------------------------------+--------------------------
2. Mentorship Engagement     | Frequency of structured advisory sessions | Minimum 2 consultations
   Velocity                  | logged to founder journey timelines.      | per founder per month.
-----------------------------+-------------------------------------------+--------------------------
3. Scheme Recommendation     | Percentage of mentor-approved schemes     | > 40% of active founders
   Relevance                 | that result in formal grant applications. | apply for matched grants.
-----------------------------+-------------------------------------------+--------------------------
4. User Experience           | Founder and Guide satisfaction rating     | Net Promoter Score (NPS)
   Satisfaction              | collected via end-of-pilot surveys.       | of +40 or higher.
====================================================================================================
```

---

## 3. Operational Risk Register

| Risk Event | Business & Institutional Impact | Severity | Planned Mitigation Strategy | Named Responsible Owner |
| :--- | :--- | :---: | :--- | :--- |
| **1. Multi-Role Session Cross-Contamination** | Guide sees private notes of another mentor's mentee; legal confidentiality breached. | **HIGH** | Strict session-state purge on workspace switch; automated 7-role test suite on every release. | Lead Technical Architect |
| **2. Unverified Live Database Migrations** | Administrative screen crashes during live session due to missing production column. | **HIGH** | Automated schema diff check between Git migrations and live database before deployment. | Database / DevOps Lead |
| **3. Mobile Viewport Abandonment** | Rural founders drop off onboarding due to layout misalignment on low-cost smartphones. | **MEDIUM** | Comprehensive mobile-first CSS styling and usability testing across Android viewports. | UI/UX Product Designer |
| **4. Cloud Database Inactivity Pausing** | Free-tier Supabase pauses after 7 inactive days, showing connection failure to users. | **HIGH** | Upgrade to Supabase Pro ($25/mo) to permanently disable auto-pausing. | Cloud Platform Engineer |
| **5. Solo Developer Key-Person Risk** | Operations stall if the original creator becomes unavailable ("Bus Factor 1"). | **CRITICAL** | Complete operational runbooks; place all cloud credentials and Git repositories in escrow. | Programme Leadership |
| **6. Unverified Government Scheme Data** | Founder applies for an expired subsidy based on outdated statutory criteria. | **HIGH** | Establish quarterly gazette review schedule; assign named domain expert; display legal disclaimer. | Scheme Policy Expert |
| **7. Premature AI Hallucinations** | Unmonitored LLM provides inaccurate eligibility advice to early-stage entrepreneurs. | **HIGH** | Constrain AI strictly to verified gazette retrieval with mandatory human mentor sign-off. | Technical Lead & Domain Expert |
| **8. Commercial Scope Creep Disputes** | Disagreements between leadership and developers over warranty fixes vs new features. | **MEDIUM** | Enforce mandatory One-Page Change Card protocol before touching production code. | Product Manager / Client Lead |

---

## 4. The CEO Decision Checklist

The following six decisions require immediate board and executive determination:

- [ ] **Decision 1: Baseline Architecture Approval:** Formally approve continuing with the established Streamlit/Python Beta foundation, rejecting an expensive and unnecessary 8-month full React rewrite.  
  *Responsible: Chief Executive Officer | Target Date: Week 1*
- [ ] **Decision 2: Contractual & Intellectual Property Review:** Conduct a formal legal review of existing contracts to confirm intellectual property ownership, licensing terms, and remaining milestone payment schedules.  
  *Responsible: Legal Counsel & Finance Lead | Target Date: Week 2*
- [ ] **Decision 3: Cloud Credential & Repository Escrow:** Ensure all administrative credentials (GitHub, Supabase, Hostinger VPS, Resend, and domain DNS) are transferred to institutional ownership.  
  *Responsible: Programme Director | Target Date: Week 2*
- [ ] **Decision 4: Staging Release Gate Authorization:** Authorize the execution of an evidence-backed release check on an isolated staging environment to verify P0/P1 defect closure and migration parity.  
  *Responsible: Lead Technical Architect | Target Date: Week 4*
- [ ] **Decision 5: Independent Security Audit Commissioning:** Commission a scoped third-party application security review (OWASP ASVS Level 2) before publicly launching real founder financial records.  
  *Responsible: Board Audit Committee | Target Date: Week 6*
- [ ] **Decision 6: Monthly Operational Retainer Allocation:** Allocate an ongoing operational maintenance budget (₹1.5L–₹2.5L/month for pilot; ₹7.57L/month for lean managed team) to ensure platform uptime and support.  
  *Responsible: Chief Financial Officer | Target Date: Week 4*
