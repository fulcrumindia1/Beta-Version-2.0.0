# -*- coding: utf-8 -*-
"""
CEO Briefing - Diagrams Module
Generates all 12 presentation-ready, cleanly styled Mermaid diagrams.
Fully sanitized for all Mermaid parser versions:
- Zero unquoted parentheses in edge labels
- Zero pipe characters inside node brackets
- Validated flowchart TD and flowchart LR syntax
"""

def get_diagrams_text():
    return r"""# Executive Briefing: The Fulcrum Architecture in Diagrams
## Visual Blueprints of Capabilities, Workflows, Infrastructure, and Strategic Roadmaps
**Companion Document to FULCRUM_CEO_BRIEFING_360.md | November 2026**

---

### How to Read These Diagrams
These visual blueprints illustrate the operational logic, security boundaries, cloud infrastructure, and commercial roadmaps of the Fulcrum platform. Each diagram is designed to be self-contained and accessible to executive leadership and board members.

---

### Diagram 1: Overall System Architecture & Operational Overview
This diagram illustrates how the four primary user portals interact with Fulcrum's custom business logic layer, external services, and underlying cloud infrastructure.

```mermaid
flowchart TD
    subgraph Users["Primary Platform Users"]
        U1["Founder A<br/>(Aspirant Portal)"]
        U2["Guide B<br/>(Mentor Portal)"]
        U3["SME C<br/>(Specialist Portal)"]
        U4["Admin D<br/>(Executive Command)"]
    end

    subgraph Interface["Presentation & Routing Layer"]
        CADDY["Caddy 2 Reverse Proxy<br/>(Automatic HTTPS & SSL Certificates)"]
        STREAMLIT["Streamlit Application Engine<br/>(Dockerized Python Container)"]
    end

    subgraph Engines["Core Custom Service Engines (31 Modules)"]
        E1["Role-Based Access Control (RBAC)"]
        E2["Deterministic Scheme Matcher (179 Schemes)"]
        E3["Mentorship Relationship Engine"]
        E4["Founder Journey Milestones"]
        E5["Confidential Consultation Threads"]
        E6["Legal Agreements & NDA Records"]
        E7["Account Lifecycle & Audit Logger"]
    end

    subgraph DataInfra["Cloud Data & Communications Infrastructure"]
        S_AUTH["Supabase GoTrue<br/>(Authentication & Tokens)"]
        S_DB["Supabase PostgreSQL 15<br/>(23 Relational Tables)"]
        S_S3["Encrypted Storage Buckets<br/>(Optimized WebP Avatars)"]
        RESEND["Resend SMTP<br/>(Transactional Emails)"]
        BACKUP["Encrypted Off-Site Storage<br/>(Daily Database Snapshots)"]
    end

    Users --> CADDY
    CADDY --> STREAMLIT
    STREAMLIT --> Engines
    Engines --> DataInfra
```

---

### Diagram 2: Multi-Role Ecosystem & Dynamic Workspace Switching
Fulcrum allows a single verified user account to dynamically switch between different organizational roles without logging out, while strictly isolating private data.

```mermaid
flowchart TD
    USER["Verified Single Account Login<br/>Email and Secure Token"] --> CONTEXT{"Active Workspace Selector"}

    CONTEXT -->|Founder Mode| ASP["Founder Workspace<br/>Aspirant Role"]
    CONTEXT -->|Mentor Mode| GDE["Mentor Workspace<br/>Guide Role"]
    CONTEXT -->|Specialist Mode| SME["Specialist Workspace<br/>SME Role"]
    CONTEXT -->|Admin Mode| ADM["Executive Portal<br/>Super Admin Role"]

    ASP --> D_ASP["Personal Venture Milestones<br/>Private Pitch Decks<br/>Curated Government Schemes"]
    GDE --> D_GDE["Assigned Mentees Review<br/>Advisory Feedback Logs<br/>Scheme Approval Gate"]
    SME --> D_SME["Technical Problem Tickets<br/>Conflict of Interest Declarations<br/>Domain Legal Advice"]
    ADM --> D_ADM["Full System Governance<br/>User Lifecycle Control<br/>Institutional Audit Archives"]

    subgraph SecurityBoundary["Strict Architectural Isolation Boundary"]
        D_ASP -.->|Zero Data Bleed| D_GDE
        D_GDE -.->|Zero Data Bleed| D_SME
    end
```

---

### Diagram 3: Administrative Governance & Command Flow (13 Tabs)
The Executive Administration Portal is divided into thirteen specialized operational tabs, providing full visibility and control over the platform.

```mermaid
flowchart LR
    subgraph AdminPortal["Executive Command Center (views/admin.py)"]
        direction TB
        T1["Tab 1: Command Metrics"]
        T2["Tab 2: User Verification"]
        T3["Tab 3: Mentor Assignments"]
        T4["Tab 4: Specialist Triage"]
        T5["Tab 5: Scheme Catalogue (179)"]
        T6["Tab 6: Journey Overviews"]
        T7["Tab 7: Help Ticket Triage"]
        T8["Tab 8: Complaint Arbitration"]
        T9["Tab 9: Conflict Declarations"]
        T10["Tab 10: Legal NDA Registry"]
        T11["Tab 11: Inactivity Alerts"]
        T12["Tab 12: Account Lifecycle Log"]
        T13["Tab 13: System Settings & Health"]
    end

    AdminPortal --> ACTION{"Administrative Decisions"}
    ACTION -->|User Management| U_MAN["User Lifecycle Updates"]
    ACTION -->|Mentorship| R_MAN["Mentorship Alignments"]
    ACTION -->|Catalogue Updates| S_MAN["Government Scheme Updates"]
    ACTION -->|Arbitration| C_MAN["Confidential Case Triage"]
```

---

### Diagram 4: Mentor Assignment & Consultation Lifecycle Flow
This diagram illustrates the step-by-step lifecycle when an entrepreneur requests guidance, showing how the system maintains institutional accountability at every stage.

```mermaid
flowchart TD
    A["Founder A Submits Profile & Initial Milestones"] --> B["Admin D Reviews Profile & Industry Sector"]
    B --> C["Admin D Assigns Guide B as Primary Mentor"]
    C --> D["Automated Notification Sent to Guide B via Resend"]
    D --> E["Guide B Reviews Founder A Pitch & Approves Assignment"]
    
    E --> F["Founder A Submits Specific Advisory Help Request"]
    F --> G{"Can Guide B Resolve Directly?"}
    
    G -->|Standard Mentorship| H["Guide B Conducts Consultation & Logs Advice"]
    H --> I["Action Items Recorded to Founder A Journey Timeline"]
    
    G -->|Requires Specialist| J["Guide B Refers Ticket to SME C"]
    J --> K["SME C Formally Declares No Conflict of Interest"]
    K --> L["SME C Provides Specialized Guidance"]
    L --> I
    
    I --> M["Permanent Audit Record Archived in Database"]
```

---

### Diagram 5: Deterministic Government Scheme Matching Engine
Unlike unverified artificial intelligence, Fulcrum uses a deterministic rules engine to evaluate entrepreneur eligibility against 179 state and national schemes with zero hallucinations.

```mermaid
flowchart TD
    S_CAT["Master Scheme Library<br/>(179 Central & Tamil Nadu Schemes)"] --> ENGINE["Deterministic Scheme Evaluation Engine"]
    
    A_PROF["Founder A Profile Parameters:<br/>• Age, Gender, Community<br/>• Education & Technical Degree<br/>• Business Stage (Ideation or Revenue)<br/>• District & Rural or Urban Location<br/>• Capital Investment Required"] --> ENGINE
    
    ENGINE --> RULES{"Evaluate Policy Eligibility Rules"}
    
    RULES -->|Ineligible| REJ["Filtered Out (Documented Reason)"]
    RULES -->|Eligible| MATCH["Candidate Scheme Matches Identified"]
    
    MATCH --> GATEKEEPER["Guide B (Mentor) Review Gate"]
    GATEKEEPER -->|Approved Relevance| REL["Released to Founder A Portal"]
    GATEKEEPER -->|Premature| HOLD["Held in Mentor Notes"]
    
    REL --> ACT["Founder A Accesses Application Checklist & Direct Portal Link"]
```

---

### Diagram 6: User Account Lifecycle, Status Transitions & Governance
Managing account statuses requires coordinated actions across database tables to ensure historical data is preserved even when accounts are suspended or deactivated.

```mermaid
flowchart TD
    START["New User Registration"] --> PEND["Status: Pending Approval"]
    
    PEND -->|Approved Credentials| ACT["Status: Active"]
    PEND -->|Rejected Application| REJ["Status: Rejected (Archived)"]
    
    ACT --> INACT_CHECK{"Inactivity Monitor<br/>30 Days No Login"}
    INACT_CHECK -->|Active Logins| ACT
    INACT_CHECK -->|Prolonged Inactivity| WARN["Status: Inactive Alert Triggered"]
    
    WARN -->|User Re-engages| ACT
    WARN -->|No Response| SUSP["Status: Suspended by Admin"]
    
    ACT -->|Policy Violation| REV["Status: Revoked or Offboarded"]
    SUSP -->|Administrative Decision| REV
    
    subgraph DataIntegrity["Mandatory Data Preservation Protocol"]
        REV --> P1["1. Terminate Active Session Tokens"]
        REV --> P2["2. Reallocate Assigned Mentees Gracefully"]
        REV --> P3["3. Lock Historical Notes from Modification"]
        REV --> P4["4. Retain Immutable Consultation Logs for Audit"]
    end
```

---

### Diagram 7: Confidential Grievance & Dispute Governance Flow
To protect institutional integrity, complaints regarding inappropriate mentor behavior or ethics violations follow an isolated, encrypted escalation path.

```mermaid
flowchart TD
    GRIEVANCE["Founder A or Mentor B Submits Confidential Complaint"] --> ENCRYPT["Payload Encrypted & Tagged with Unique Case ID"]
    
    ENCRYPT --> RESTRICT["Restricted Channel: Visible Only to Master Admin D"]
    
    subgraph BlindTriage["Confidential Protection Barrier"]
        RESTRICT -.->|Completely Hidden From| PEERS["Peer Mentors & Other Users"]
    end
    
    RESTRICT --> TRIAGE["Admin D Conducts Formal Review"]
    
    TRIAGE --> DECISION{"Administrative Determination"}
    DECISION -->|Unsubstantiated| DISMISS["Complaint Closed with Written Findings"]
    DECISION -->|Mediation Needed| MEDIATE["Facilitated Institutional Resolution"]
    DECISION -->|Policy Breach| ACTION["Mentor Assignment Revoked & Account Suspended"]
    
    DISMISS --> AUDIT["Complete Case Dossier Archived for Legal Compliance"]
    MEDIATE --> AUDIT
    ACTION --> AUDIT
```

---

### Diagram 8: Production Cloud Infrastructure & Network Flow
This diagram details the physical cloud topology hosted on Hostinger VPS and Supabase, illustrating the security boundaries protecting live user data.

```mermaid
flowchart TD
    CLIENT["Client Browser or Mobile Device<br/>End-User Web Traffic"] -->|Secure HTTPS Request| CADDY["Caddy 2 Reverse Proxy<br/>Automated Let's Encrypt TLS Termination"]
    
    subgraph HostingerVPS["Hostinger KVM 2 Cloud VPS - Ubuntu Linux, 8 GB RAM"]
        CADDY -->|Internal Docker Bridge| APP["Docker Container: Fulcrum Streamlit App<br/>Python 3.11 Runtime, app.py"]
        APP --> HEALTH["Local Health Check Agent<br/>Monitors Memory and Container Health"]
    end

    subgraph SupabaseCloud["Supabase Managed Cloud Platform - Dedicated Infrastructure"]
        APP -->|Pooled REST API Calls| DB["PostgreSQL 15 Database Engine<br/>23 Tables with Row-Level Security"]
        APP -->|JWT Session Validation| AUTH["GoTrue Authentication Service"]
        APP -->|Encrypted Multipart Uploads| S3["AWS S3-Compatible Storage Bucket<br/>Private Profile Headshots"]
    end

    subgraph ExternalServices["Third-Party Cloud Services"]
        APP -->|REST API Request| RESEND["Resend Email Cloud Gateway<br/>Transactional Alerts and Password Resets"]
        DB -.->|Scheduled Daily Snapshot| OFFSITE["Off-Site Encrypted Backup Archive<br/>Disaster Recovery Storage"]
    end
```

---

### Diagram 9: The Reality of Artificial Intelligence in Software Delivery
This diagram breaks down the productivity acceleration provided by AI coding tools versus the human engineering discipline required to achieve enterprise reliability.

```mermaid
flowchart TD
    subgraph AIAssistance["AI Productivity Acceleration (~15% of Delivery Effort)"]
        direction TB
        AI1["Drafting Initial Code Syntax"]
        AI2["Generating Repetitive HTML and CSS Scaffolding"]
        AI3["Synthesizing Standard SQL Query Boilerplate"]
        AI4["Generating Baseline Unit Test Cases"]
    end

    subgraph HumanExpertise["Human Engineering Oversight (~85% of Delivery Effort)"]
        direction TB
        H1["System and Relational Database Architecture"]
        H2["Interpreting Complex Government Policy Rules"]
        H3["Debugging Multi-User Session Race Conditions"]
        H4["Preventing Live Database Migration Data Loss"]
        H5["Adversarial Cybersecurity Hardening (OWASP ASVS)"]
        H6["Configuring Linux VPS, Docker, SSL and Networks"]
        H7["Conducting Real-User Usability Testing"]
        H8["Operational Accountability and Disaster Recovery"]
    end

    AIAssistance -->|Speeds Up Initial Drafting| SPEED["Faster Prototyping Velocity"]
    SPEED --> HumanExpertise
    HumanExpertise --> PROD["Secure, Reliable, Production-Ready Platform"]
```

---

### Diagram 10: Go-to-Market (GTM) Maturity Map
Inspired by modern technology venture maturity frameworks, this map shows where Fulcrum currently sits and the exact milestones required to achieve institutional scale.

```mermaid
flowchart LR
    subgraph Stage1["1. Prototype Phase<br/>Concept Testing"]
        S1["• Initial Alpha Code<br/>• Basic Streamlit UI<br/>• Local Database<br/>• Single-User Assumptions"]
    end

    subgraph Stage2["2. Working Beta<br/>Current Fulcrum State"]
        S2["• 28,330 Lines Core Code<br/>• Supabase Cloud DB<br/>• 179 Government Schemes<br/>• 4 Distinct Portals<br/>• VPS Docker Deployment<br/>📍 FULCRUM CURRENT POSITION"]
    end

    subgraph Stage3["3. Institutional Hardening<br/>Immediate Next Phase"]
        S3["• Close Verified QA Defects<br/>• Professional UI/UX Overhaul<br/>• Independent Security Audit<br/>• Daily Off-Site Backups<br/>• Monitored 100-User Pilot"]
    end

    subgraph Stage4["4. Scale-Up & Expansion<br/>Enterprise Maturity"]
        S4["• Decoupled Architecture<br/>• Multi-Tenant SaaS Capability<br/>• Grounded AI Scheme Pilot<br/>• Dedicated Operations Team<br/>• State-Wide Rollout"]
    end

    Stage1 --> Stage2
    Stage2 ==>|Funded Next Steps| Stage3
    Stage3 --> Stage4
```

---

### Diagram 11: Phased Roadmap to Enterprise Maturity
A practical, four-phase engineering roadmap designed to protect organizational capital and ensure structured delivery.

```mermaid
flowchart TD
    P0["Phase 0: Discovery, Reconciliation & Ownership<br/>Weeks 1 to 2 - Zero Production Changes"] --> P1["Phase 1: Defect Closure & Interface Stabilization<br/>Weeks 3 to 6 - Defect Closure and UI Polish"]
    
    P1 --> P2["Phase 2: Independent Assurance & Controlled Pilot<br/>Weeks 7 to 12 - Security Audit and Pilot"]
    
    P2 --> GATE{"Formal Release Acceptance Gate Passed?"}
    
    GATE -->|Defects Identified| P1
    GATE -->|Approved| P3["Phase 3: Strategic Expansion & Supervised AI<br/>Months 4 to 12 - New Modules and AI Pilot"]

    subgraph Phase0_Deliverables["Phase 0 Focus"]
        direction TB
        D0_1["Secure 100% IP and Credentials"]
        D0_2["Reconcile Live DB Migrations"]
        D0_3["Formalize Defect Triage Log"]
    end

    subgraph Phase1_Deliverables["Phase 1 Focus"]
        direction TB
        D1_1["Fix Lifecycle and Password Deficiencies"]
        D1_2["Set Up Isolated Staging Environment"]
        D1_3["Standardize Streamlit Design System"]
    end

    subgraph Phase2_Deliverables["Phase 2 Focus"]
        direction TB
        D2_1["Third-Party Penetration Test"]
        D2_2["Disaster Recovery Dry Run"]
        D2_3["Controlled Founder and Mentor Pilot"]
    end

    P0 --- Phase0_Deliverables
    P1 --- Phase1_Deliverables
    P2 --- Phase2_Deliverables
```

---

### Diagram 12: Architectural Complexity Matrix (2x2 Quadrant Chart)
This matrix illustrates why Fulcrum is technically demanding: it possesses high business-rule and workflow complexity, even though its user concurrency is currently lower than consumer mega-apps.

```mermaid
flowchart TD
    subgraph QuadrantChart["Architectural Complexity Matrix"]
        direction TB
        
        subgraph TopLeft["High Workflow Complexity / Lower Scale"]
            Q1["<b>FULCRUM PLATFORM</b><br/>• Deep multi-role permissions (7 roles)<br/>• 179 deterministic scheme rules<br/>• Confidential legal NDAs & records<br/>• Controlled institutional mentorship"]
        end

        subgraph TopRight["High Workflow Complexity / Extreme Scale"]
            Q2["<b>SWIGGY / FLIPKART</b><br/>• Real-time delivery dispatch<br/>• Millions of concurrent checkouts<br/>• Complex warehouse & inventory logic<br/>• Massive distributed microservices"]
        end

        subgraph BottomLeft["Low Workflow Complexity / Low Scale"]
            Q3["<b>BROCHURE WEBSITES & FORM BUILDERS</b><br/>• Typeform, WordPress, Wix<br/>• Simple data collection into sheets<br/>• Static public pages<br/>• Zero multi-role relational logic"]
        end

        subgraph BottomRight["Low Workflow Complexity / Extreme Scale"]
            Q4["<b>CRAIGSLIST / BASIC CLASSIFIEDS</b><br/>• Simple text ads & public listings<br/>• Minimal role differentiation<br/>• Massive database read traffic<br/>• Very basic transactional rules"]
        end
    end

    BottomLeft -->|Add Relational Rules & Roles| TopLeft
    TopLeft -->|Add High Concurrency & Scaled Traffic| TopRight
    BottomLeft -->|Add Massive Read Traffic| BottomRight
    BottomRight -->|Add Complex Business Logic| TopRight
```

*Executive Interpretation:* Fulcrum does not need Swiggy's infrastructure budget because it is not processing 50,000 food orders a minute. However, it cannot be built with a simple website builder because its **business rules, confidentiality requirements, and multi-role relationships are inherently complex.**
"""
