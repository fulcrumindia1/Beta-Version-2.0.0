# -*- coding: utf-8 -*-
"""
Part 2 of the Fulcrum Alpha-to-Beta Development Value, Cost and AI Feasibility Report.
Section 16: Complete Mermaid Diagrams (Diagrams 1 to 12) with 4-part executive explanations.
"""

def get_part2_text():
    return """## 16. VISUAL ARCHITECTURE AND MERMAID DIAGRAMS: MAKING COMPLEXITY VISIBLE

A non-technical executive or board member looking at a codebase can easily underestimate its underlying difficulty. A user interface may appear as simple buttons and forms, but behind those controls lies a sophisticated network of security boundaries, permission matrices, database triggers, and state machines.

The following 12 diagrams illustrate how Fulcrum-India operates, why its architecture is structured this way, and where engineering effort is invested.

---

### Diagram 1: Version Alpha vs. Version Beta System Evolution

```mermaid
flowchart TD
    subgraph AlphaScope ["Version Alpha Scope (Baseline MVP)"]
        A_User["Single-Role User"]
        A_Admin["6-Tab Admin Dashboard"]
        A_Schemes["~170 Seed Schemes (Uncurated)"]
        A_Journey["Basic Sequential Milestone Log"]
        A_Consult["Basic Help Inquiry Desk"]
    end

    subgraph BetaExpansion ["Version Beta Additions (Institutional Operating System)"]
        B_MultiRole["Multi-Role Architecture (Up to 7 Permutations)"]
        B_Admin["13-Tab Comprehensive Control Tower"]
        B_NDA["Mandatory Legal & Electronic NDA Gating"]
        B_Gatekeeper["Curated Guide Review & Release Engine (179 Schemes)"]
        B_Lifecycle["Full Account Lifecycle (Suspend / Archive / Purge)"]
        B_Governance["Confidential Whistleblower Complaints & SME Conflict Engine"]
        B_Inactivity["Automated 14-Day Mentor Inactivity Tracking"]
        B_Privacy["Relationship-Scoped Access & Masked Directorate"]
    end

    A_User -->|"Architectural Leap"| B_MultiRole
    A_Admin -->|"Expanded & Hardened"| B_Admin
    A_Schemes -->|"Governed Gatekeeping"| B_Gatekeeper
    A_Journey -->|"Revision History & PDF"| B_Privacy
    A_Consult -->|"8-Status State Machine"| B_Governance
    B_MultiRole --> B_NDA
    B_Admin --> B_Lifecycle
    B_Admin --> B_Inactivity
```

* **What this diagram means:** It maps the direct evolutionary transition from Fulcrum Alpha to Fulcrum Beta. Alpha provided an open directory for single-role users; Beta adds institutional governance layers that turn it into a regulated operational network.
* **Why it matters to the business:** Alpha was suitable only for informal, unmonitored pilot programs. Beta introduces the statutory compliance, legal protections, and quality controls necessary for an institutional rollout backed by government agencies, universities, or corporate venture funds.
* **What engineering work is involved:** This transition required rebuilding authentication, creating a multi-role mapping table, migrating database schemas across 12 revisions, implementing session context isolation, and developing 7 new administrative management modules.
* **What is currently implemented vs. proposed:** **100% Implemented.** All shown Beta capabilities are active, verified in production on the live VPS, and backed by automated regression tests.

---

### Diagram 2: Complete Fulcrum Production Architecture

```mermaid
flowchart TD
    subgraph ClientLayer ["1. Client Access Tier"]
        Browser["User Web Browser (Desktop / Mobile / PWA)"]
    end

    subgraph EdgeTier ["2. Edge & Reverse Proxy Tier (Hostinger KVM 2 VPS)"]
        Caddy["Caddy 2 Reverse Proxy (:443 / :80)\n- Automatic TLS / Let's Encrypt\n- Security Headers & Compression\n- Reverse Proxy to Port 8501"]
    end

    subgraph AppTier ["3. Application Container Tier (Docker: fulcrum-net)"]
        Streamlit["Fulcrum Core Engine (Python 3.11 / Streamlit :8501)\n- Single-Router Dispatcher (app.py)\n- Session State & Workspace Switcher\n- Role Authorization Guardrails"]
        Services["Domain Business Logic Services (services/*.py)\n- accounts, roles, schemes, journey, legal\n- inactivity, governance, help_requests\n- pdf_generator (ReportLab)"]
    end

    subgraph ExternalServices ["4. External Managed Cloud Services"]
        SupabaseAuth["Supabase GoTrue Auth\n- JWT Bearer Tokens\n- Password Reset & Session Recovery"]
        SupabasePG["Supabase Managed PostgreSQL 15\n- Row Level Security (RLS)\n- 23 Relational Tables\n- Schema Cache & Extensions"]
        SupabaseStorage["Supabase S3 Storage\n- Encrypted Buckets: photos & legal docs"]
        ResendSMTP["Resend Transactional Email API\n- Mentor Inactivity Alerts\n- Directives & Notifications"]
    end

    subgraph FallbackTier ["5. Local Headless Tier"]
        LocalSQLite["Local SQLite (cluster_a.db)\n- Headless QA & Emergency Fallback\n- Read-only in Production"]
    end

    Browser -->|"HTTPS (:443)"| Caddy
    Caddy -->|"HTTP (:8501)"| Streamlit
    Streamlit --> Services
    Services -->|"HTTPS REST API / PostgREST"| SupabasePG
    Services -->|"HTTPS GoTrue API"| SupabaseAuth
    Services -->|"S3 Upload / Download"| SupabaseStorage
    Services -->|"SMTP / REST API"| ResendSMTP
    Services -.->|"Local Fallback Only"| LocalSQLite
```

* **What this diagram means:** It illustrates the end-to-end technical infrastructure supporting Fulcrum, from the founder's browser to the edge reverse proxy, containerized Python runtime, and cloud database.
* **Why it matters to the business:** Demonstrates that Fulcrum uses modern, cost-efficient, containerized cloud infrastructure. By separating application compute (Hostinger VPS) from managed data storage (Supabase Cloud), the platform minimizes hosting costs while ensuring institutional-grade data durability.
* **What engineering work is involved:** Configuring Docker networks, Caddy auto-renewing SSL certificates, environment secret isolation, PostgREST API integration, connection pooling, and error handling for external network latency.
* **What is currently implemented vs. proposed:** **100% Implemented.** Running live on Hostinger KVM 2 (`187.126.114.81`) with active SSL certificates for `app.fulcrumindia.online`.

---

### Diagram 3: Complete Admin Responsibilities (13 Admin Tabs)

```mermaid
flowchart TD
    subgraph ControlTower ["Single Platform Administrator (Control Tower)"]
        AdminUser["Institutional Director (fulcrumindia1@gmail.com)\nMasked to Founders as 'Fulcrum Support'"]
    end

    subgraph TabsCore ["Core Ecosystem Management"]
        T1["Tab 1: Aspirants & Journeys\n- Directory, 4-part profiles, milestones"]
        T2["Tab 2: Guides Management\n- Institutional mentor roster & status"]
        T3["Tab 3: SMEs Management\n- Domain technical specialists roster"]
        T4["Tab 4: Mentor Assignments\n- Primary Guide, Co-Guide & SME allocation"]
    end

    subgraph TabsOperations ["Operations, Schemes & Directives"]
        T5["Tab 5: Mentor Inquiries & Directives\n- Escalate tickets & issue binding directives"]
        T6["Tab 6: Scheme Catalogue CRUD\n- 179 Canonical schemes & criteria"]
        T7["Tab 7: Multi-Role Grants\n- Grant Guide/SME to existing founders"]
        T8["Tab 8: Legal & NDA Records\n- Timestamped compliance audit logs"]
    end

    subgraph TabsGovernance ["Governance, Compliance & Lifecycle"]
        T9["Tab 9: Confidential Complaints\n- Founder whistleblower investigation"]
        T10["Tab 10: Inactivity Monitor\n- 14-day mentor SLA enforcement"]
        T11["Tab 11: Contact Aspirants\n- Directorate communications broadcast"]
        T12["Tab 12: SME Conflict Governance\n- Review statutory conflict declarations"]
        T13["Tab 13: Account Lifecycle & Archive\n- Suspend, archive, restore & purge"]
    end

    AdminUser --> TabsCore
    AdminUser --> TabsOperations
    AdminUser --> TabsGovernance
```

* **What this diagram means:** Displays all 13 specialized administrative control panels available to the platform directorate in `views/admin.py`.
* **Why it matters to the business:** A single administrator can oversee hundreds of mentors, specialists, and founders with automated checks on SLAs, legal compliance, and account statuses.
* **What engineering work is involved:** Each tab requires custom database queries, caching, pagination to prevent slow load times, role-based authorization gates, and audit-logging.
* **What is currently implemented vs. proposed:** **100% Implemented.** All 13 tabs are operational in production.

---

### Diagram 4: Seven Role Combinations and Session Context Isolation

```mermaid
flowchart TD
    subgraph UserPool ["One Human Identity (Supabase User Profile)"]
        User["Individual User Account (Email & Password)"]
    end

    subgraph RoleCombinations ["7 Supported Role Permutations"]
        R1["1. Aspirant Only\n(Grassroots Founder)"]
        R2["2. Guide Only\n(Institutional Mentor)"]
        R3["3. SME Only\n(Domain Specialist)"]
        R4["4. Aspirant + Guide\n(Founder who also Mentors)"]
        R5["5. Aspirant + SME\n(Founder who also Advises)"]
        R6["6. Guide + SME\n(Mentor who also has Domain Spec)"]
        R7["7. Aspirant + Guide + SME\n(Full Ecosystem Participant)"]
    end

    subgraph WorkspaceSwitching ["Session State Context Isolation"]
        Switcher["Dynamic Workspace Switcher (Sidebar Radio)\nSets st.session_state.active_workspace"]
        W_Asp["Aspirant Workspace\n- My Profile & My Journey\n- My Released Schemes\n- Consultations Desk"]
        W_Gde["Guide Workspace\n- My Caseload Mentoring\n- Scheme Review Gateway\n- Inactivity Status"]
        W_Sme["SME Workspace\n- Technical Tickets\n- Conflict Declarations\n- Specialist Roadmaps"]
    end

    User --> RoleCombinations
    R4 --> Switcher
    R5 --> Switcher
    R6 --> Switcher
    R7 --> Switcher
    Switcher -->|"Context: Aspirant"| W_Asp
    Switcher -->|"Context: Guide"| W_Gde
    Switcher -->|"Context: SME"| W_Sme
```

* **What this diagram means:** Shows how Fulcrum allows a single user to wear multiple hats (e.g., an entrepreneur who also acts as a mentor) without creating duplicate accounts or mixing private data.
* **Why it matters to the business:** In real-world innovation clusters, seasoned founders frequently mentor early-stage peers or provide technical advice on patents and GST. Forcing them to maintain separate login emails creates confusion, forgotten passwords, and data silos.
* **What engineering work is involved:** Managing a relational `user_roles` table, dynamic workspace routing in Streamlit, session state persistence, and filtering database queries so a user cannot see confidential mentee data when logged into their personal founder workspace.
* **What is currently implemented vs. proposed:** **100% Implemented.** Verified across all 7 role permutations in the 32-user test suite.

---

### Diagram 5: Complex Multi-Role Relationship Network

```mermaid
flowchart TD
    subgraph Users ["Ecosystem Participants"]
        A["Person A\n(Aspirant + Guide)"]
        B["Person B\n(Aspirant + SME)"]
        C["Person C\n(Aspirant Only)"]
        D["Person D\n(Guide Only)"]
        E["Person E\n(Aspirant + Guide)"]
    end

    subgraph MentorshipLinks ["Active Mentoring Relationships"]
        A -->|"Primary Guide"| B
        A -->|"Co-Guide Support"| E
        E -->|"Primary Guide"| B
        D -->|"Primary Guide"| A
        D -->|"Primary Guide"| C
        D -->|"Co-Guide Support"| B
    end

    subgraph AdvisoryLinks ["Specialist Advisory Relationships"]
        B -->|"GST / Tax Advisory"| A
        B -->|"FSSAI Advisory"| E
    end

    subgraph RevocationScenario ["Cascade Effect: What happens if Person A loses Guide role?"]
        RevokeA["Admin Revokes A's Guide Privileges"]
        A_AspRetained["A's Aspirant Account Remains Active"]
        A_AdvRetained["A continues receiving SME advice from B"]
        A_GuideRemoved["A unassigned from B and E"]
        B_Survives["B still guided by E and D (Zero Caseload Disruption)"]
        AuditLogged["Event recorded in Account Lifecycle Log"]
        
        RevokeA --> A_AspRetained
        RevokeA --> A_AdvRetained
        RevokeA --> A_GuideRemoved
        A_GuideRemoved --> B_Survives
        RevokeA --> AuditLogged
    end
```

* **What this diagram means:** Models an intricate real-world network where individuals guide one peer while receiving technical advice from another, and illustrates what happens when one role is revoked.
* **Why it matters to the business:** Demonstrates network resilience. If a mentor leaves the program or commits a policy violation, the platform can revoke their mentoring access without destroying their own business journey or disrupting their mentees.
* **What engineering work is involved:** Array-based relationship storage (`guide_ids` and `sme_ids`), partial unassignment logic, cascade triggers, and data validation preventing circular assignments.
* **What is currently implemented vs. proposed:** **100% Implemented.** Tested in `test_account_lifecycle_and_handover_chaos.py`.

---

### Diagram 6: Guide/SME Onboarding and Mandatory NDA Gating Workflow

```mermaid
stateDiagram-v2
    [*] --> AccountCreated: Admin Creates Mentor / SME Profile
    AccountCreated --> PendingNDA: Role Granted with is_active = FALSE
    
    state PendingNDA {
        [*] --> InitialLogin: User Authenticates via Password Reset / Login
        InitialLogin --> BlockedAccess: Attempt to Access Mentee Caseload
        BlockedAccess --> NDAModalEnforced: System Gating Intercepts Session
        NDAModalEnforced --> LegalReview: User Reviews Terms & Full NDA Text
    }
    
    LegalReview --> Rejected: User Refuses or Cancels
    Rejected --> PendingNDA: Access Remains Strictly Blocked
    
    LegalReview --> Accepted: User Clicks 'Accept & Sign Electronically'
    
    state ActiveRole {
        Accepted --> RoleActivated: is_active = TRUE in user_roles
        RoleActivated --> AuditStored: IP, Timestamp, Version Logged in legal_acceptances
        AuditStored --> EligibleForAssignment: Mentor Appears in Admin Caseload Picker
    }
    
    EligibleForAssignment --> [*]
```

* **What this diagram means:** The step-by-step security gate that prevents any mentor or specialist from viewing confidential entrepreneur business plans until they have executed an electronic Non-Disclosure Agreement.
* **Why it matters to the business:** Fiduciary and legal compliance. Entrepreneurs entrust Fulcrum with trade secrets, financial records, and patent ideas. Without enforceable NDA tracking, the platform faces severe legal liability.
* **What engineering work is involved:** Gating middleware in `services/roles.py`, modal interceptors in `views/login.py` and `views/legal_ui.py`, immutable record creation in `legal_acceptances`, and database constraints ensuring only active mentors appear in assignment dropdowns.
* **What is currently implemented vs. proposed:** **100% Implemented.** Fully active in production.

---

### Diagram 7: Consultation Lifecycle and Administrative Directives

```mermaid
stateDiagram-v2
    [*] --> OPEN: Aspirant Submits Technical Ticket
    
    OPEN --> IN_PROGRESS: Assigned Mentor / SME Reads Ticket
    
    state ActiveConsultation {
        IN_PROGRESS --> WAITING_ON_ASPIRANT: Mentor Replies with Questions / Guidance
        WAITING_ON_ASPIRANT --> WAITING_ON_GUIDE_SME: Aspirant Provides Requested Information
        WAITING_ON_GUIDE_SME --> IN_PROGRESS: Mentor Continues Technical Advisory
    }
    
    ActiveConsultation --> RESOLVED: Both Parties Agree Issue is Addressed
    
    state AdministrativeEscalation {
        ActiveConsultation --> ESCALATED: Mentor or Aspirant Flags Deadlock / Policy Issue
        ESCALATED --> PENDING_ADMIN: Ticket Routed to Admin Control Tower (Tab 5)
        PENDING_ADMIN --> DIRECTIVE_ISSUED: Admin Issues Binding Directorate Directive
        DIRECTIVE_ISSUED --> IN_PROGRESS: Parties Comply with Directive Instructions
        DIRECTIVE_ISSUED --> RESOLVED: Admin Formally Resolves & Closes Ticket
    }
    
    RESOLVED --> [*]
```

* **What this diagram means:** Illustrates the complete state machine governing founder help requests, including mentor dialogue loops and administrative escalation.
* **Why it matters to the business:** Prevents mentoring inquiries from falling through the cracks. If a mentor becomes unresponsive or a technical dispute arises, the directorate can intervene and issue an authoritative directive.
* **What engineering work is involved:** Database CHECK constraints (`migrations/011`), thread reply persistence, notification dispatching, role-based status updating, and administrative oversight tabs.
* **What is currently implemented vs. proposed:** **100% Implemented.** Status constraint expanded in Migration 011; tested end-to-end.

---

### Diagram 8: Scheme Matching Engine and Curated Gatekeeper Release

```mermaid
flowchart TD
    subgraph DataInput ["1. Founder Data Baseline"]
        Profile["Aspirant 4-Part Venture Profile\n- District, Sector, Entity Type\n- Annual Turnover, Capital Investment\n- Founder Gender, Caste, Minority Status"]
    end

    subgraph RulesEngine ["2. Deterministic Matching Engine"]
        Engine["scheme_matching_engine.py\n- Hard Rules & Boolean Criteria\n- District & Demographics Eligibility\n- 179 Canonical Central & State Schemes"]
        Matches["Potential Scheme Matches Identified\n(Categorized by Relevance Score)"]
    end

    subgraph GatekeeperLayer ["3. Human-in-the-Loop Gatekeeper"]
        GuideDesk["Guide Scheme Review Desk\n- Mentor evaluates business readiness\n- Identifies documentation gaps\n- Writes tailored preparation notes"]
        Decision{"Mentor Gatekeeper Decision"}
        Release["Release Scheme to Aspirant\n(Creates scheme_releases record)"]
        Defer["Defer / Mark Not Ready\n(Private Mentor Note Logged)"]
    end

    subgraph FounderWorkspace ["4. Entrepreneur Visibility"]
        AspirantPortal["Aspirant Scheme Dashboard\n- Displays ONLY officially released schemes\n- Direct access to application forms & links\n- Founder updates application milestones"]
    end

    Profile --> Engine
    Engine --> Matches
    Matches --> GuideDesk
    GuideDesk --> Decision
    Decision -->|"Vetted & Ready"| Release
    Decision -->|"Documentation Missing"| Defer
    Release --> AspirantPortal
```

* **What this diagram means:** Explains how government schemes are filtered. The algorithm performs mathematical eligibility checks, but the human mentor decides when the founder is ready to apply.
* **Why it matters to the business:** Prevents founder burnout. Prematurely applying for grants with incomplete documentation leads to government rejections. Mentors ensure founders apply only when their business documentation is complete.
* **What engineering work is involved:** Deterministic rules engine across 179 government schemes, database tracking of releases, and privacy isolation preventing founders from viewing internal grant criteria.
* **What is currently implemented vs. proposed:** **100% Implemented.** Powered by deterministic rules in `services/scheme_matching_engine.py`.

---

### Diagram 9: Security Boundaries, Privacy Controls and Relationship-Scoped Visibility

```mermaid
flowchart TD
    subgraph RequestingActors ["Requesting Actors"]
        Admin["Platform Admin (Control Tower)"]
        Guide["Assigned Guide (Mentor)"]
        SME["Assigned SME (Specialist)"]
        Unrelated["Unrelated Mentor / Other User"]
    end

    subgraph SecurityGate ["Authorization & Privacy Guardrails (services/profiles.py)"]
        Check{"Check Relationship Authorization\n_get_relationship_authorized_ids_supabase()"}
    end

    subgraph DataAccessMatrix ["Information Access Boundaries"]
        FullData["Full Operational Access\n- All Profiles, Financials, Photos, Complaints"]
        MentorData["Relationship-Scoped Access\n- Mentee Profile, Venture Data & Journey\n- Mentee Photo (If expressly authorized)\n- NO Access to Other Mentors' Caseloads"]
        SMEData["Technical Ticket Scoped Access\n- Assigned Founder Data & Relevant Consultations\n- NO Access to General Caseload or Financials"]
        StrictlyDenied["STRICTLY DENIED (403 Forbidden)\n- Cannot View Unrelated Profiles\n- Cannot View Unrelated Founder Photos\n- Cannot View Whistleblower Complaints"]
    end

    Admin --> Check -->|"Role = Admin"| FullData
    Guide --> Check -->|"Mentee ID in Assigned List"| MentorData
    SME --> Check -->|"Ticket Assigned to SME"| SMEData
    Unrelated --> Check -->|"Zero Assignment"| StrictlyDenied
    Guide -.->|"Attempt to view non-mentee"| StrictlyDenied
    SME -.->|"Attempt to view non-assigned"| StrictlyDenied
```

* **What this diagram means:** Maps the security layer that enforces data privacy between different users on the platform.
* **Why it matters to the business:** Protects confidential founder data. A mentor cannot browse entrepreneurs outside their assigned caseload, and mentors can never view whistleblower complaints filed against themselves.
* **What engineering work is involved:** Dynamic SQL filtering, authorization checks on every profile fetch, image URL signing, and security regression testing.
* **What is currently implemented vs. proposed:** **100% Implemented.** Verified in `test_argon_p0_negative_security.py` and `test_aspirant_photo_dashboard_visibility.py`.

---

### Diagram 10: Engineering & Testing Complexity Cascade: Revoking Guide Privileges

```mermaid
flowchart TD
    subgraph Trigger ["1. Single Administrative Action"]
        AdminClick["Admin clicks 'Revoke Guide Role' in Tab 7"]
    end

    subgraph SubsystemCascade ["2. Multi-System Impact Cascade (8 Interconnected Subsystems)"]
        S1["Subsystem 1: user_roles Table\n- Invalidate Guide grant & set is_active = FALSE\n- Flush cached role permissions"]
        S2["Subsystem 2: Mentorship Relationships\n- Freeze / detach active Guide allocations\n- Re-evaluate Co-Guide promotion logic"]
        S3["Subsystem 3: Consultation Tickets\n- Flag active help requests for reassignment\n- Prevent revoked mentor from replying"]
        S4["Subsystem 4: Notification Engine\n- Purge pending mentor reminders\n- Alert Admin to unassigned mentees"]
        S5["Subsystem 5: Caseload Tracking & SLAs\n- Decrement mentor active caseload counter\n- Remove from 14-day inactivity monitor"]
        S6["Subsystem 6: Founder Data Privacy\n- Revoke photo viewing tokens\n- Mask mentee phone/email from revoked mentor"]
        S7["Subsystem 7: Session Workspace UI\n- Invalidate active_workspace in active session\n- Remove Guide tab from sidebar dynamically"]
        S8["Subsystem 8: Audit & Governance Log\n- Write immutable event to account_lifecycle_log\n- Record admin ID, reason, and timestamp"]
    end

    subgraph VerificationNeeds ["3. Engineering & QA Verification Required"]
        Tests["Mandatory Automated Test Coverage\n- Unit test: role revocation\n- Integration test: relationship detachment\n- Security test: negative access verification\n- E2E Playwright test: browser tab switch"]
    end

    AdminClick --> SubsystemCascade
    SubsystemCascade --> Tests
```

* **What this diagram means:** Shows why a simple administrative button click is not simple. Revoking one role triggers automatic updates across 8 backend systems.
* **Why it matters to the business:** Explains development costs to executives. When adding or altering features, engineers must verify that all 8 connected subsystems remain stable and free of regressions.
* **What engineering work is involved:** Transaction management, cache invalidation, defensive database queries, and multi-service integration tests.
* **What is currently implemented vs. proposed:** **100% Implemented.** Covered by 12 regression tests in `test_qa32_fixes_regression.py`.

---

### Diagram 11: Proposed Future AI Integration Architecture

```mermaid
flowchart TD
    subgraph ExistingPlatform ["Existing Production Platform (Current Scope)"]
        User["User (Aspirant / Guide / SME / Admin)"]
        FulcrumApp["Fulcrum Streamlit Core (:8501)"]
        Supabase["Supabase DB (179 Schemes, Profiles, Journeys)"]
    end

    subgraph AIPipeline ["PROPOSED / FUTURE AI Integration Architecture"]
        AuthGate["1. Authorization & Privacy Scoping Gateway\n- Strip PII (Phone, Personal Email, Aadhaar)\n- Validate user access rights before query"]
        Orchestrator["2. AI Orchestration & Guardrails\n- Rate limiting & per-user token quotas\n- Prompt injection defense & schema validation\n- Deterministic rules pre-check"]
        VectorDB["3. Retrieval / RAG Engine (Optional)\n- Supabase pgvector or Serverless Vector DB\n- Embeddings for 179 Schemes & Guidelines"]
        LLMProvider["4. External Hosted LLM API\n- Primary: Economical Model (GPT-4o-mini / Flash)\n- Complex: Premium Model (GPT-4o / Claude Sonnet)\n- Server-side API key isolation"]
        Verification["5. Output Verification & Fact-Checking\n- Hallucination checks against official scheme text\n- Strict formatting & schema parser"]
        HumanReview["6. Mandatory Human-in-the-Loop Review\n- Mentor or Admin reviews AI suggestion\n- One-click approve, edit, or reject"]
    end

    User --> FulcrumApp
    FulcrumApp --> Supabase
    FulcrumApp -.->|"Proposed Request"| AuthGate
    AuthGate -.-> Orchestrator
    Orchestrator -.->|"Semantic Search"| VectorDB
    Orchestrator -.->|"Context + Prompt"| LLMProvider
    LLMProvider -.->|"Raw Generation"| Verification
    Verification -.->|"Curated Draft"| HumanReview
    HumanReview -.->|"Approved Output Only"| User
```

* **What this diagram means:** A conceptual architectural blueprint for safely adding AI capabilities to Fulcrum in the future without compromising data privacy or platform stability.
* **Why it matters to the business:** Ensures that if AI is introduced, it acts solely as an assistant with strict human oversight, rather than an unguided chatbot making false promises to entrepreneurs.
* **What engineering work is involved:** PII sanitization pipelines, prompt management, model integration, response parsing, and human-in-the-loop review screens.
* **What is currently implemented vs. proposed:** **0% Implemented — 100% PROPOSED.** Fulcrum currently contains zero AI dependencies.

---

### Diagram 12: Development Effort and Cost Comparison Across Delivery Models

```mermaid
flowchart LR
    subgraph SoloModel ["Solo Developer + AI Tools"]
        S_Dev["1 Senior Full-Stack Engineer\nArmed with AI Coding Assistants"]
        S_Speed["High Velocity on Boilerplate\nInstant Context Switching\nZero Coordination Overhead"]
        S_Risk["Bottleneck on Testing & Security\nPotential Code Review Blindspots\nBurnout Risk on Edge Cases"]
        S_Cost["Estimated Cost: $4,000 - $7,000 / mo\nTotal Build Cost: $18,000 - $32,000"]
    end

    subgraph LeanTeam ["Lean Professional Team + AI"]
        L_Team["3-4 Specialist Engineers\n- 1 Lead Architect\n- 1 Backend / DB Specialist\n- 1 QA / Automation Engineer\n- 1 Part-time PM / Designer"]
        L_Speed["Parallel Stream Execution\nRigorous Code Reviews & QA\nInstitutional Continuity"]
        L_Cost["Estimated Cost: $10,000 - $16,000 / mo\nTotal Build Cost: $35,000 - $55,000"]
    end

    subgraph AgencyModel ["Traditional IT Services Vendor"]
        A_Vendor["6-8 Person Agency Team\nAccount Managers, Tech Leads, Devs, Manual QA"]
        A_Speed["High Communication Overhead\nSlower Turnaround on Nuances\nRigid Change-Request Billing"]
        A_Cost["Estimated Billing: $18,000 - $30,000 / mo\nTotal Quoted Cost: $65,000 - $115,000+"]
    end
```

* **What this diagram means:** Compares the resource requirements, speed, delivery risks, and commercial costs of building a platform like Fulcrum across three organizational structures.
* **Why it matters to the business:** Informs executive budgeting decisions. It demonstrates why a skilled solo developer using AI can achieve remarkable initial velocity, but why a lean team is required for institutional long-term stability.
* **What engineering work is involved:** Managing development workflows, sprint planning, automated testing infrastructure, and technical governance.
* **What is currently implemented vs. proposed:** **Methodological Benchmark.** Reflects current software market economics in India and global IT services.
"""

