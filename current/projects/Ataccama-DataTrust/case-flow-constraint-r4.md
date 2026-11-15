---
type: model
date: 2026-11-15
course: R4.1:10, R4.1:Tasks3
object: Case flow of the DG/DQ team
time_scope: run time (current operation)
status: v1.0
builds_on: case-journey-flow-r4.md (Tasks1), case-flow-physics-r4.md (Tasks2)
---

# Finding the constraint of the case flow

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/01-using-workflow-models-in-enterprise-operations/14-identifying-and-finding-system-constraints.md`; buffers from R4.1:10 (commit faed795, 2026-11-04).

## Team structure (2026-11-15)

- **Triage and prioritisation:** the product manager (one person).
- **DQ:** 2 engineers. **Data Catalog and Data Lineage:** 2 engineers.
- **No analysts:** engineers do everything in their domain - consultations, management questions, new functions.
- Cases split between the two domains about **50/50**.

Assumptions carried from Tasks2: ~11 cases arrive per month; class mix 45 % consultations (~1 h), 20 % management questions (~2.5 h), 35 % new functions (~10 h); each engineer has ~2.5 h/week ≈ 10.75 h/month for cases.

## Utilisation by station

| Station | Demand per month | Capacity per month | Utilisation |
|---|---|---|---|
| Triage + full kitting (PM) | 11 × 0.5 h triage + 3.9 new functions × 1.5 h clarification ≈ 11.5 h | ≈ 4.3 h (≈ 1 h/week, done ad hoc - assumption) | **≈ 270 %** |
| DQ pair (2 engineers) | ≈ 25 h | ≈ 21.5 h | ≈ 115 % |
| Catalog/Lineage pair (2 engineers) | ≈ 25 h | ≈ 21.5 h | ≈ 115 % |
| Whole engineering team | ≈ 49.5 h | ≈ 43 h | ≈ 115 % |

## 1. Most probable constraint and signs

**Hypothesis (three layers):**
1. **Capacity constraint: the triage station (product manager).** The largest single queue (≈ 40 cases not triaged) and the highest estimated utilisation (~270 %). Without triage, cases neither reach the engineers in priority order nor get an explicit "not now".
2. **Next constraint: both engineering pairs equally (~115 %).** With 50/50 split neither pair stands out; once triage is fixed, the constraint is expected to move here - and the whole team is above 100 %.
3. **Policy constraint:** urgent management questions stop all other cases - and with no analysts they stop the engineers directly, i.e. the constraint after triage.

**Signs:** 40 untriaged cases; all 10 oldest cases "wait for resources"; new functions (≈ 80 % of touch time) are not released; urgent management questions are answered while consultations wait.

## 2. Measurements and an example on imagined data

**Measurements (4-6 weeks):**
- case class and domain (DQ / Catalog / Lineage);
- statuses per station: untriaged, clarification, at engineers (DQ / Catalog), awaiting confirmation;
- weekly queue length before each station; time in each column;
- interruptions by urgent questions (which cases stopped, for how long);
- PM time actually spent on triage per week.

**Imagined data, 12 weeks:**

| Class | Arrived (DQ / Catalog) | Closed |
|---|---|---|
| Consultations | 15 (8 / 7) | 2 |
| Management questions | 7 (4 / 3) | 6 |
| New functions | 12 (6 / 6) | 0 |
| **Total** | **34 (~11/month)** | **8 (~2.7/month)** |

WIP at the end (100): untriaged 40; clarification 8; at DQ pair 21; at Catalog pair 21; awaiting confirmation 10.

Average time in column: untriaged 6+ weeks (oldest - months); clarification 2 weeks; at engineers (incl. queue) 20+ weeks; awaiting confirmation 2 weeks.

**Key parameters:**
- largest queue and highest utilisation - triage (40 cases, ~270 %): the constraint by the R4.1:10 criteria;
- engineering pairs ~115 % each, queues growing ~2 cases/month each, new functions throughput 0;
- management questions closed 6 of 7, consultations 2 of 15 - trace of the policy constraint;
- Little's law for the engineering queues: ~21 cases each with throughput near 0 - flow time unbounded.

**Planned changes (TOC steps):**
1. **Exploit / elevate triage cheaply:** fixed weekly triage slot (1-1.5 h); each case gets accept / not now / reject; new functions get clarified (full kit) before reaching engineers. Expected: the 40-case queue drains and the constraint moves to the engineering pairs.
2. **Subordinate to the engineering constraint:** a new function enters a pair only when the pair pulls one from its buffer; urgent questions go to the duty engineer, not to the one working on functions.
3. **Elevate if needed:** more engineer time for cases, or vendor support - the whole team is at ~115 %, so buffers alone will not stop queue growth; entry must be aligned with exit.

## 3. Buffers

**Existing de facto (not formalised):**
- An implicit, unbounded time buffer: no dates are promised ("when resources free up"), all waiting is silently moved to the requester.
- The 100 open cases are an unmanaged queue, not a buffer: no purpose, no minimum size, no entry signal.
- There is **no** capacity buffer: without analysts, urgent questions hit the engineers directly.

**Proposed:**

| Type | Where | Example |
|---|---|---|
| Capacity | PM triage | fixed weekly triage slot as reserved PM time |
| Capacity | each engineering pair | weekly duty rotation: one engineer per pair handles urgent management questions and consultations from reserved time; the other works on new functions without interruptions |
| Inventory (Drum-Buffer-Rope) | before each engineering pair | 2-3 clarified new functions ready to start; minimum size by Little's law for the triage station (its throughput × flow time); a new function enters only when the pair pulls one |
| Time | promises to requesters of new functions | promise date = forecast from release history + one buffer at the end (e.g. +50 %); work as if there were no buffer, consume it on delays |
