---
type: model
date: 2026-11-05
course: R3.4:7, R3.4:Mod3
object: DQ Issue Remediation Control System
status: v0.2 (checked against FPF Library, snapshot 20261105T084056Z)
---

# Levels of detail: DQ Issue Remediation Control System

> Assignment source: MimEcoSys/docs, `professional/modeling-2/04-practice-of-creating-models/12-levels-of-detail-in-descriptions.md` and `13-defining-description-levels-of-detail.md` (commit faed795, 2026-11-04).
> Description: checklist template "How good looks like for DQ Issue Remediation" (a description of classes, typical representative). Customer: product manager; recipient: implementation project team.

Types (R3.2): CFO - class of functional objects; CMO - class of material (constructive) objects; TP - temporal part; D - description.

## A. Functional breakdown

| Level 0 | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| Data management function of the organisation :: CFO | DQ Issue Remediation Control System :: CFO | Issue detection subsystem :: CFO | — (below: black box of the check engine) |
| | | Issue registration and routing subsystem :: CFO | — |
| | | Remediation coordination subsystem :: CFO | — |

## B. Constructive breakdown (what the same system is built from)

| Level 0 | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| Organisation :: CMO | DQ Issue Remediation Control System :: CMO | Configured DG/DQ platform :: CMO | DQ module :: CMO :: CFO (detection subsystem) |
| | | | Issue register and workflow module :: CMO :: CFO (registration subsystem) |
| | | DQ team :: CMO | Team member :: CMO :: CFO (role: data steward) |
| | | | Team member :: CMO :: CFO (role: issue owner) |

## C. Work breakdown (what the system does over time)

| Level 1 | Level 2 |
|---|---|
| Handling cycle of one issue :: TP (work of the system) | Detection (check run) :: TP |
| | Assignment :: TP |
| | Remediation :: TP |
| | Verification :: TP |

## D. Descriptions used (not parts of the system)

DQ rule :: D (the threshold is part of it), issue record :: D, issue lifecycle model :: D, remediation SLA agreement :: D.

## Rationale for the chosen levels

- **Level 0** is needed because of the customer's pragmatic goal - "ready to play its role in the supersystem": it shows which function the system performs for the organisation.
- **Level 1** is the system that performs remediation control, not the process itself (R3.4:7, FPF A.1).
- **Level 2** is where the recipient works: configuring detection, the register and routing, assigning people to roles.
- **Level 3** is the last transparent level: platform modules and people in roles - what the checklist items verify.
- **Not going lower**: the internals of the check engine and fixing individual records in source systems are a black box for the recipient. "Speaking" test: "we checked that every issue has an assigned owner" makes sense; "we checked the execution plan of the rule's SQL query" no longer does.
- **Not parts, but context**: source systems, datasets and data elements are what the system works on. They go to R3.4:Mod5 as relations.

## FPF check (v0.1 → v0.2)

1. Descriptions (rule, threshold, record, lifecycle model, SLA) are not components of the system - moved to block D (A.6.H:4.4).
2. Roles are not parts of the team: the parts are people, the role is given as a type (A.2).
3. Work (cycle, check run, remediation) is not a phase of the system but a separate work breakdown (A.6.H:4.4, A.15.1).
4. "Closure" is a state, not a temporal part; removed from the breakdown, goes to attributes (R3.4:Mod5).
5. Functional and constructive structures are kept separate (C.30.ASV:4.5a).
6. Level 0: "organisation" / "data management function" instead of "Data Governance" as a practice (A.1).

## For the LK form (R3.4:Mod3)

Breakdowns A and B go into the LK table; C and D as a note or in the post. If only one breakdown is allowed - B (the recipient cares most about who works on what).
