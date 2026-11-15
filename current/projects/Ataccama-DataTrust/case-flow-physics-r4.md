---
type: model
date: 2026-11-14
course: R4.1:Tasks2
object: Case flow of the DG/DQ team
time_scope: run time (current operation)
status: v1.0
builds_on: case-journey-flow-r4.md (R4.1:Tasks1)
---

# Enterprise physics of the case flow

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/01-using-workflow-models-in-enterprise-operations/12-identifying-the-physics-of-your-enterprise.md`; concepts from R4.1:7-R4.1:9 (commit faed795, 2026-11-04).

**Line:** cases of the DG/DQ team - user consultations, management questions, new functions (system development counted separately). Route: triage → clarification with requester → analysis and solution → implementation → review → hand-over and confirmation.

**Observed (R4.1:Tasks1):** 100 open cases; 2-3 closed per month; 9-13 arrive per month.

## Estimates

| Quantity | Value | Basis |
|---|---|---|
| Class mix | 45 % consultations (~1 h), 20 % management questions (~2.5 h), 35 % new functions (~10 h) | assumption (confirmed 2026-11-14) |
| Pure flow time (touch, no rework, no waiting) | ≈ 4.5 h ≈ 1 productive day per case (5 productive h/day) | weighted from class mix |
| Time available for cases | 4 people × 25 productive h/week × 10 % = 10 h/week | assumption (confirmed 2026-11-14) |
| Capacity | 10 / 4.5 ≈ 2.2 cases/week ≈ 9-10 cases/month (ideal conditions) | calculation |
| Real throughput | 2-3 cases/month | observation |
| Extended capacity | = capacity (9-10/month): no overtime, no external help | observation 2026-11-14 |
| Capacity utilisation | incoming / capacity = 9-13 / 9-10 ≈ 100-130 % | calculation |

**Reading.** Capacity > throughput holds, but the gap (3-4×) is far larger than normal losses: in practice cases get less than 10 % of the time, or touch time is larger because of rework and switching - most likely both. Utilisation around and above 100 % explains the non-linear growth of flow time (second principle of enterprise physics): WIP grows by 7-10 cases/month, Little's law gives ≥ 40 months.

**Urgent management questions** do not add capacity: they **pre-empt** it. When an urgent question arrives, all other cases stop. This is not extended capacity but reallocation of the same capacity plus switching: started cases are paused, their context is lost, flow time of the paused cases grows, and Little's law stops describing the queue (a priority change has the same effect as multitasking, R4.1:9).

## Concepts on our line

**Variability**
- Common cause (can be planned for with a buffer): class mix (one-hour consultation next to a two-day function); waiting for requester answers; holidays; reporting peaks; **regular urgent management questions** - being regular, they are a common cause, not a special one.
- Special cause (cannot be planned): platform outage or upgrade; reorganisation; unplanned audit; key person leaving.

**Rework**
- Case returned after hand-over ("not what we asked for"); new function fails review; closed case reopened.
- Main common cause: incompletely stated request at entry - no full kitting (clarification before work starts).
- Additional rework from pre-emption: a paused case has to be "re-entered" (context recovery) when work resumes.

**WIP**
- 100 open cases mixing: the queue nobody started; started and abandoned cases (hidden WIP, time already spent); cases paused by urgent questions.
- The average age of WIP grows - a sign that the constraint has reached its utilisation limit and planning no longer works for it.

**Inventory and resources**
- Resources: people (product manager for triage; 2 engineers on DQ, 2 on Data Catalog and Data Lineage; no analysts - clarified 2026-11-15), their productive time, platform and environment access, vendor support hours.
- Negative inventory: the queue of not-accepted cases; its value decays (requests become outdated, requesters work around the team).
- Missing positive inventory: a knowledge base of answers to typical questions that could turn part of consultations into self-service.

**Information flows**
- Assignee question → requester answer (feedback lag).
- Hand-over → confirmation and closure.
- For management: no visibility of the queue; the arrivals-vs-closed ratio is not visible, so the capacity gap is not discussed as a fact.

**Constraint**
- The most loaded "station" is not one person but **the team time allocated to cases** - it is not allocated at all; cases get what is left after projects.
- Inside the flow: probably the engineer on new functions (longest touch time). **Superseded by Tasks3 (2026-11-15):** with 4 engineers (2 per domain, 50/50 split) neither pair stands out (~115 % each); the current constraint is triage by the product manager (~40-case queue, ~270 %). See `case-flow-constraint-r4.md`.
- Missing regular triage: no prioritisation across the whole queue; urgent management questions pass as queue-jumpers and stop everything else.

## Implications (inputs for next R4 tasks)

- Align entry with exit: accept no more than we close; the rest is an explicit "not now" decision.
- Allocate capacity to cases explicitly, with a **buffer for urgent management questions** (e.g. part of the 10 h/week reserved), so that urgent questions are served from the buffer instead of stopping all other cases.
- Make the arrivals/closed ratio visible.
- Full kitting at entry to reduce rework; knowledge base to reduce consultation load.
