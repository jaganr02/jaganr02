# TalentSync Technologies Inc. — Enterprise HRMS

A modern, full-lifecycle Enterprise Human Resource Management System (HRMS) built with **React 19**, **TypeScript**, **Tailwind CSS v4**, and **Motion**. Designed for high-velocity tech organizations, TalentSync provides end-to-end personnel operations across three distinct persona workflows: **Employee Self-Service (ESS)**, **Manager Pod Hub**, and **HR Administrative Portal**.

---

## 📑 Table of Contents

1. [Architecture & System Design](#architecture--system-design)
2. [Role-Based Workflows & Feature Matrix](#role-based-workflows--feature-matrix)
3. [Technology Stack](#technology-stack)
4. [Project Directory Structure](#project-directory-structure)
5. [Data Flow & State Management](#data-flow--state-management)
6. [Local Installation & Development Setup](#local-installation--development-setup)
7. [Build & Production Deployment](#build--production-deployment)
8. [Data Models & Schema Reference](#data-models--schema-reference)

---

## 🏗 Architecture & System Design

The application follows a **modular unidirectional component architecture** powered by a centralized reactive React Context engine (`HRISContext`). State mutations execute synchronously through strongly-typed action dispatchers, with automatic audit logging and persistence across user sessions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            Presentation Layer                               │
│  ┌───────────────────┬─────────────────────┬─────────────────────────────┐  │
│  │   Employee ESS    │   Manager Pod Hub   │    HR Operations Portal     │  │
│  │  - Attendance & IP│  - Team Radar       │    - Org Headcount Analytics│  │
│  │  - Leave Request  │  - Review Appraisal │    - Batch Payroll Engine   │  │
│  │  - Payslip Export │  - Leave Approvals  │    - ATS Candidate Pipeline │  │
│  │  - Goal Progress  │  - 1:1 Pod Logs     │    - Direct Onboarding      │  │
│  └───────────────────┴─────────────────────┴─────────────────────────────┘  │
│                                      │                                      │
├──────────────────────────────────────┼──────────────────────────────────────┤
│                                      ▼                                      │
│                      Centralized State Bus (HRISContext)                    │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  • AuthSession State (RBAC: Employee / Manager / HR-Admin)            │  │
│  │  • Master Directory & Employee Rosters                                │  │
│  │  • Real-time Clock-in / Clock-out Engine (Geo & IP Tagging)           │  │
│  │  • Leave Request State & Approval Workflow Dispatcher                 │  │
│  │  • ATS Candidate Stage Pipeline & 1-Click Onboarding                  │  │
│  │  • Compensation, Benefits & Gross-to-Net Payroll Processor             │  │
│  │  • Global Modals & Notifications Dispatcher                           │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
├──────────────────────────────────────┼──────────────────────────────────────┤
│                                      ▼                                      │
│                     Data Persistence & External Services                     │
│  ┌───────────────────────────────────┬───────────────────────────────────┐  │
│  │  Local Storage Storage Engine     │  Print / PDF Payslip Rendering    │  │
│  │  (Reactive Hydration & Fallback)  │  Canvas Confetti & UI FX Feedbacks│  │
│  └───────────────────────────────────┴───────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 👥 Role-Based Workflows & Feature Matrix

The system provides dedicated role-based portals tailored to organization permissions:

### 1. 💼 Employee Self-Service (ESS)
* **Attendance & Time Tracking**:
  * Geo-location and IP-verified clock-in / clock-out.
  * Active shift stopwatch timer with real-time break tracking.
  * Weekly timesheet log with overtime and total hours calculation.
* **Leave & Time Off**:
  * Real-time balance meters (Paid Leave, Sick Leave, Optional Holidays).
  * Modal-based leave application with document attachment simulation.
  * Live status tracker (Pending, Approved, Rejected).
* **Performance & OKRs**:
  * Active quarterly objectives with progress bars, weights, and milestone statuses.
  * View manager feedback and calibration scores.
* **Payroll & Compensation**:
  * Current salary breakdown (Basic, HRA, Special Allowances, PF, Professional Tax).
  * Printable/downloadable PDF-ready official monthly payslips.

### 2. 🛡 Manager Team Pod Hub
* **Team Radar**:
  * Real-time attendance grid for direct reports (Online, On Break, On Leave, Offline).
  * 1-click team check-in status overview.
* **Leave Approvals**:
  * One-click approval / rejection of pending leave requests from team members.
* **Performance Reviews**:
  * Quarterly performance evaluation modal for direct reports.
  * Goal scoring, KPI ratings, and developmental feedback recording.
* **Recruitment & Hiring Requests**:
  * Submit department hiring requisitions with title, budget, and headcount justification.

### 3. 🏢 HR Administrator Operations
* **Organization Analytics**:
  * Real-time company headcount metrics, attrition rates, and department distribution.
  * Organization-wide leave compliance tracking.
* **ATS Talent Acquisition Pipeline**:
  * Multi-stage candidate management (`Screening` ➔ `Assessment` ➔ `Interview` ➔ `Offer` ➔ `Hired`).
  * Candidate ratings, interview notes, and 1-click **"Hire & Onboard"** that directly transfers candidates into active employee directory and payroll.
* **Payroll Execution Engine**:
  * Batch payroll processor with gross-to-net tax calculations.
  * Disburse monthly payouts with automated audit trail generation.
* **Employee Management**:
  * Add new employees with automated employee ID generation, department assignment, and initial salary structures.

---

## 💻 Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Runtime & Framework** | React 19 + TypeScript 5.8 | Core reactive UI engine and static type safety |
| **Bundler & Dev Server** | Vite 6 | Sub-millisecond HMR and optimized production bundles |
| **Styling & Design System** | Tailwind CSS v4 | Utility-first responsive styling and dynamic themes |
| **Motion & Animation** | Motion (`motion/react` v12) | Modal transitions, layout animations, and tab fades |
| **Data Visualization** | Recharts 3.x | Department distribution, salary charts, and KPI trends |
| **Icons** | Lucide React | Clean, consistent enterprise icon system |
| **Celebration Effects** | Canvas Confetti | Milestone celebration and onboarding feedback |

---

## 📁 Project Directory Structure

```text
├── index.html                    # Single-page application root HTML
├── package.json                  # Dependencies, scripts, and package manifests
├── tsconfig.json                 # TypeScript strict compiler configuration
├── vite.config.ts                # Vite build and Tailwind plugin setup
├── src/
│   ├── main.tsx                  # Application entry point & React root mount
│   ├── App.tsx                   # Main layout container & modal registry
│   ├── index.css                 # Global Tailwind CSS imports & theme definitions
│   ├── types.ts                  # Shared TypeScript interfaces, types & enums
│   │
│   ├── context/
│   │   └── HRISContext.tsx       # Centralized state management & business logic
│   │
│   ├── data/
│   │   └── initialState.ts       # Seed data (Employees, Candidates, Directory, Leave)
│   │
│   ├── components/
│   │   ├── Auth/
│   │   │   └── LoginPage.tsx     # Role-based quick login & credential switch
│   │   │
│   │   ├── Navigation/
│   │   │   ├── Sidebar.tsx       # Collapsible navigation & persona badge
│   │   │   └── Header.tsx        # Top notification bar & quick action menu
│   │   │
│   │   ├── Employee/
│   │   │   ├── EmployeeDashboard.tsx # ESS main view
│   │   │   ├── AttendanceWidget.tsx  # Clock-in / clock-out stopwatch & IP tagger
│   │   │   ├── LeaveSummaryWidget.tsx# Time-off balance cards
│   │   │   └── GoalTrackerWidget.tsx # OKR & milestone progress
│   │   │
│   │   ├── Manager/
│   │   │   ├── ManagerDashboard.tsx       # Manager overview & team status
│   │   │   ├── TeamAttendanceWidget.tsx   # Live pod member status radar
│   │   │   └── ManagerAnalyticsWidget.tsx # Performance & score analytics
│   │   │
│   │   ├── HRAdmin/
│   │   │   ├── HRAdminDashboard.tsx       # HR command center
│   │   │   └── HRAnalyticsWidget.tsx      # Headcount & department metrics
│   │   │
│   │   ├── Recruitment/
│   │   │   └── RecruitmentView.tsx        # ATS candidate pipeline & hiring
│   │   │
│   │   ├── Performance/
│   │   │   └── PerformanceView.tsx        # Review cycles & OKR calibration
│   │   │
│   │   ├── Payroll/
│   │   │   └── PayrollView.tsx            # Salary distribution & batch runs
│   │   │
│   │   ├── Leave/
│   │   │   └── LeaveView.tsx              # Organization leave management
│   │   │
│   │   ├── Directory/
│   │   │   └── DirectoryView.tsx          # Searchable employee directory
│   │   │
│   │   └── Modals/
│   │       ├── ApplyLeaveModal.tsx        # Leave request submission
│   │       ├── ManagerReviewModal.tsx     # Performance review scoring
│   │       ├── RunPayrollModal.tsx        # Batch payroll disbursement
│   │       ├── ATSPipelineModal.tsx       # Fast-action candidate stage modal
│   │       ├── AddEmployeeModal.tsx       # Direct employee onboarding modal
│   │       ├── HireRequestModal.tsx       # Headcount requisition modal
│   │       └── PayslipPrintModal.tsx      # Official payslip print & export
```

---

## 🔄 Data Flow & State Management

The application uses an immutable, action-driven pattern inside `HRISContext.tsx`:

1. **State Store Initialization**: Hydrates initial records from `initialState.ts` or `localStorage`.
2. **Action Dispatch**: All user interactions call context methods (`clockIn`, `clockOut`, `applyLeave`, `updateRequestStatus`, `updateATSCandidate`, `processPayroll`, `addNewEmployee`).
3. **Audit Trail**: Every significant business event (approvals, salary disbursements, stage changes) automatically pushes a timestamped event into the `auditLogs` collection.
4. **Reactive Re-renders**: Subscribed components update immediately with zero prop-drilling.

---

## 🚀 Local Installation & Development Setup

Follow these steps to run the application locally on your machine:

### 1. Prerequisites
* **Node.js**: `v18.0.0` or higher (Recommended: `v20.x` or `v22.x LTS`)
* **Package Manager**: `npm` (v9+), `yarn`, or `pnpm`

### 2. Clone the Repository
```bash
git clone https://github.com/your-org/talentsync.git
cd talentsync-hrms
```

### 3. Install Dependencies
```bash
npm install
```

### 4. Start the Development Server
```bash
npm run dev
```

The application will start with hot module reloading enabled at:
```
http://localhost:3000
```

> **Note**: The dev server is preconfigured to bind to port `3000` on `0.0.0.0`.

### 5. Quick Persona Test Credentials
When on the login screen, click any of the persona profile cards to instantly switch roles:

| Role | Username | Department | Key Privileges |
|---|---|---|---|
| **Employee** | `priya.sharma` | Engineering | ESS clock-in, leave requests, payslip download, goals |
| **Manager** | `saravanan` | Engineering | Team attendance radar, leave approvals, Q3 performance reviews |
| **HR Administrator** | `kavitha` | Human Resources | Full system administration, batch payroll, ATS pipeline |

---

## 🛠 Build & Production Deployment

### 1. Type Check & Linting
Run TypeScript compiler check across the entire project:
```bash
npm run lint
```

### 2. Production Build
Compile and bundle the production assets with Vite:
```bash
npm run build
```
The optimized static assets will be output to the `/dist` directory.

### 3. Preview Production Build Locally
To test the production build locally:
```bash
npm run preview
```

### 4. Deploying to Static Hosting
The generated `/dist` directory can be deployed directly to any static web hosting platform:
* **Vercel**: `vercel deploy`
* **Netlify**: `netlify deploy --dir=dist --prod`
* **Cloudflare Pages**: Link repository with build command `npm run build` and output folder `dist`.
* **Nginx / Docker**: Serve the `/dist` directory using any standard static file server.

---

## 📊 Data Models & Schema Reference

### `Employee`
```typescript
interface Employee {
  id: string;
  name: string;
  role: string;
  department: string;
  email: string;
  phone: string;
  location: string;
  joinDate: string;
  salary: {
    basic: number;
    hra: number;
    allowances: number;
    pf: number;
    tax: number;
    net: number;
  };
  attendance: {
    status: 'Present' | 'Absent' | 'On Leave' | 'On Break';
    clockInTime?: string;
    clockOutTime?: string;
    totalHoursToday: number;
  };
  leaveBalances: {
    paid: number;
    sick: number;
    casual: number;
    optional: number;
  };
  goals: Goal[];
  performance: PerformanceReview;
}
```

### `ATSCandidate`
```typescript
interface ATSCandidate {
  id: string;
  name: string;
  role: string;
  email: string;
  stage: 'Screening' | 'Assessment' | 'Interview' | 'Offer' | 'Hired';
  rating: number;
  appliedDate: string;
  notes?: string;
}
```

### `LeaveRequest`
```typescript
interface LeaveRequest {
  id: string;
  employeeId: string;
  employeeName: string;
  leaveType: 'Paid' | 'Sick' | 'Casual' | 'Optional';
  startDate: string;
  endDate: string;
  days: number;
  reason: string;
  status: 'Pending' | 'Approved' | 'Rejected';
  appliedOn: string;
}
```

---

## 📄 License & Ownership
Copyright © 2026 TalentSync Technologies Inc. All rights reserved. Proprietary enterprise software.
