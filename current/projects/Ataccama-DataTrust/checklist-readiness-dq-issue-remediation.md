---
type: checklist-template
date: 2026-11-07
course: R3.4:10, R3.4:Tasks4
object: DQ Issue Remediation Control System
time_scope: design time (pre-operation readiness)
status: v1.0
file: dq-issue-remediation-readiness-checklist.xlsx (Excel; sent in chat 2026-11-07)
---

# Readiness checklist template: DQ Issue Remediation Control System

> Assignment source: MimEcoSys/docs, `professional/modeling-2/04-practice-of-creating-models/18-creating-descriptions-or-description-templates.md` and `19-preparing-the-system-description.md` (commit faed795, 2026-11-04).
> Built from: `glossary-dq-issue-remediation.md` (v0.3), `levels-of-detail-dq-issue-remediation.md` (v0.3), `classifiers-dq-issue-remediation.md` (v0.2), `attributes-relations-dq-issue-remediation.md` (v0.4).

**Description:** "How good looks like for DQ Issue Remediation" - checklist template (form to fill in), Excel.
**Customer:** product manager - pragmatic goal: make sure the new system is ready to play its role in the supersystem.
**Recipient:** implementation project team.
**Language:** English; DQ domain and project domain.
**Time scope:** design time (pre-operation readiness). The checklist checks that the way of working is defined and set up, not that the work goes well. Operational values (per-issue times, trends, outcomes) belong to an operation report (FPF B.3.3:4, CC-B3.3.5). The only item relying on performed work is the trial run on pilot data (J1).

## Workbook structure

| Sheet | Content |
|---|---|
| Readiness | Header (system, operating model, domains in scope, customer, recipient, date, author) - filled by the author; calculated summary (items, Yes/No/N/A, not filled, unmet critical/non-critical, suggested verdict); final verdict and reason - filled by the author |
| Checklist | 36 items in 10 sections; columns: ID, Section, Subject, Target state, How we verify (evidence), Critical, Status (Yes/No/N/A), Comment, Owner, Model reference |
| Classifiers | 14 classifiers with classes (dropdown sources) + severity membership criteria (placeholders) |
| Legend | Purpose, time scope, trial run, what to fill, status values, critical, verdict logic, example row, model sources |

**Suggested verdict logic:** Incomplete if any item has no status; Not ready if any critical item is No; Ready with remarks if only non-critical items are No; otherwise Ready. The author records the final verdict and the reason if it differs.

## Checklist items

| ID | Subject | Target state | How we verify (evidence) | Critical | Model reference |
|---|---|---|---|---|---|
| **A** | **Scope and system** | | | | |
| A1 | System identity | Name, operating model and coverage (data domains in scope) agreed and recorded | Readiness sheet header filled; operating model chosen from classifier | Y | levels A/B; attributes T1 |
| A2 | Customer and recipient | Customer (product manager) and recipient (implementation team) confirmed | Named on Readiness sheet | N | R3.4:Mod2 |
| A3 | Data elements in scope | Each in-scope data element identified as system.table.field, with data domain and data class | Scope list exists and is complete | Y | attributes T1 (Data Element) |
| A4 | Source systems | Source system identified (IT registry code, system class) for every in-scope data element | Scope list has source system per element | Y | attributes T2 |
| **B** | **Platform and subsystems** | | | | |
| B1 | Issue detection subsystem | Set up on the DQ module (setup status = set up) | Module configured; test rule runs | Y | levels A/B |
| B2 | Issue registration and routing subsystem | Set up on the issue register and workflow module | Test issue can be created and routed | Y | levels A/B |
| B3 | Remediation coordination subsystem | Set up: routing to source system teams and their contacts | Contact list and routing rules exist | Y | levels A; attributes T2 |
| B4 | Platform module versions | Recorded at judgement date | Versions listed | N | attributes T1 |
| **C** | **Team and roles** | | | | |
| C1 | Data stewards | A data steward assigned for every data domain in scope | Assignment list per domain | Y | glossary; attributes T2 |
| C2 | Issue owner assignment rule | Rule configured: who becomes issue owner for a new issue | Rule in workflow; test issue got an owner | Y | attributes T2 |
| C3 | Remediation contacts | Remediation contact agreed in each source system team | Named contact per source system | Y | attributes T2 |
| C4 | Time on roles | Planned share of time per role agreed (% FTE) | Agreed with line managers | N | attributes T1 |
| **D** | **Rules and detection** | | | | |
| D1 | DQ rules | Defined for every in-scope data element; each rule covers one data element in one source system | Rule list vs scope list: no gaps, no multi-system rules | Y | attributes T1/T2 |
| D2 | Rule types | Rule type assigned from classifier for each rule | Field filled | N | classifiers |
| D3 | Thresholds | Set for each rule as condition: operator + cut value, unit % of passed records | Threshold field filled in the stated form | Y | glossary (Threshold) |
| D4 | Run schedule | Run frequency scheduled for each rule | Schedule visible in DQ module | Y | attributes T1 |
| D5 | Issue creation | Issue created automatically on threshold breach | Test breach created an issue | Y | attributes T2 |
| **E** | **Issue record (data model of operation)** | | | | |
| E1 | Issue record template | Set up: record number DQ-NNNN, linked data element, detection date-time, number of affected records | Template fields exist | Y | attributes T1 (R) |
| E2 | Classification fields | Quality dimension, severity, detection channel, closure outcome set up with their classifiers | Dropdowns present | Y | attributes T1; classifiers |
| E3 | Root cause field | Root cause class (classifier) and evidence link set up | Fields exist | N | attributes T1/T2 |
| E4 | Check run results | Stored per run: pass rate (%), checked records, failed records (count), run date-time | Results history available | Y | attributes T1 (R) |
| E5 | Handling-cycle measures | Available from fields or workflow history: wait/touch time per stage, cycle time, returns | Report can be built from history | N | attributes T1 (R) |
| **F** | **Classifiers** | | | | |
| F1 | Classifiers loaded | All classifiers on the Classifiers sheet set up in the platform | Each list present | Y | classifiers |
| F2 | Severity criteria | Each severity class has a written membership criterion | Criteria text agreed | Y | classifiers (FPF C.16.P:5) |
| F3 | Reference lists source | Data domains and source system classes taken from MDM / reference data, not invented | Source of lists named | N | classifiers |
| **G** | **Handling method and workflow** | | | | |
| G1 | Lifecycle model | Approved: Open → Assigned → In remediation → In verification → Closed; exits Rejected and Risk accepted | Model approved by customer | Y | levels C |
| G2 | Workflow | Implements the lifecycle model (states and transitions configured) | Walk through all transitions in test | Y | levels C |
| G3 | Verification step | Re-check against threshold is mandatory before closure as remediated | Workflow blocks closure without re-check | Y | attributes T2 |
| G4 | Closure without remediation | Rejected / Risk accepted requires a documented decision and its author | Mandatory decision field | Y | glossary (Closure) |
| **H** | **Remediation SLA** | | | | |
| H1 | SLA per severity | Agreed time to closure per severity class (working days) | SLA agreement signed off | Y | attributes T1 |
| H2 | Working calendar | Team working calendar fixed (country, hours, holidays) | Calendar referenced in SLA | Y | attributes conventions |
| H3 | SLA reporting | Reports show distribution by severity class; no averaging of severity | Report layout agreed | N | attributes conventions |
| **I** | **After closure** | | | | |
| I1 | Rule stays in monitoring | Rules are not unscheduled when an issue is closed | Setting / procedure checked | Y | attributes (rule trend) |
| I2 | Trend review | Review of the trend of failed records per rule assigned (who, when) | Named reviewer and cadence (e.g. Week Close) | N | attributes (rule trend) |
| **J** | **Trial run** | | | | |
| J1 | Trial end-to-end run | Passed on pilot data from detection to closure (incl. verification) | Trial run record with date | Y | glossary (Readiness) |
| J2 | Trial findings | Findings of the trial run fixed or explicitly accepted | Findings list closed | Y | — |

## Mapping to the models

- Items with **design-time values** (Scope = D in attributes Table 1): A1-A4, B1-B4, C1-C4, D1-D4, H1-H2.
- Items checking that the **data model of operation is set up** (Scope = R fields): E1-E5.
- Items from **design-time counterparts of relations** (attributes Table 2): C2, C3, D5, G3, G4.
- Items from the **handling method** (levels block C): G1-G2.
- Items from the **rule trend decision** (2026-11-06): D1 (narrow rules), E4, I1-I2.
- **Trial run**: J1-J2.

## Open points

- Placeholders to replace with the real setup: operating models, data domains, source system classes, severity membership criteria, SLA values, working calendar.
- Discuss with the implementation team before first use (R2.6:3: the checklist will change, that is normal).
