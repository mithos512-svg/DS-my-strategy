---
type: model
date: 2026-11-13
course: R4.1:Tasks1
object: Case in the DG/DQ team case management
time_scope: run time (current operation)
status: v1.0 (checked against FPF Library, snapshot 20261112T230943Z)
---

# Case journey through the DG/DQ team - production chain and flow

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/01-using-workflow-models-in-enterprise-operations/05-describing-and-mapping-the-production-chain.md` (commit faed795, 2026-11-04).
> Object changed on 2026-11-13: first draft used the catalog item journey (R2.6); replaced by the case journey because cases show the real flow problem of the team.

## 1. The journeying object

A **case** is a **work item** of the DG/DQ team: a unit of accounting and coordination of work - an agreement on what the team accounts for and coordinates, from acceptance to a result handed over to the requester. A case is **not** the work itself, the card, the work product, the plan, a work episode, the expected user outcome or the observed effect. The actual work is attributed to a case by the team's rules; the card in the tracker is the record of the case (FPF A.7; #workitems series, posts 213, 215, 248-249 - refined 2026-11-17).

**Demand type - a composite classification for capacity allocation** (renamed 2026-11-19). These four classes mix several bases (result, source, size); per #workitems post 257 a composite classification is acceptable when it serves one task - allocating capacity shares to demand types in advance and comparing plan with fact. For other questions use the single-basis classifiers in "Work item classification" below.

| Class | Example |
|---|---|
| User consultation | "how do I find a dataset", "what does this term mean" |
| Management question | request for a summary, analysis, status |
| New function | configuration, new rule, new report |
| System development | larger changes, integrations - **counted as a separate class** (decision 2026-11-13) |

**Policies per class** (proposed 2026-11-17; different classes need different policies - #workitems post 237):

| Class | Allowed size | Service order | Completion |
|---|---|---|---|
| User consultation | ≤ 2 h | duty engineer of the pair, in order of arrival | answer given, requester has no follow-up |
| Management question | variable ("assignment" - from a day to a project, post 224) - size it at triage; if > 1 day, split | expedite class, served from the duty engineer's reserved time, does not interrupt the engineer on new functions | answer delivered, no edits expected |
| New function | 1-3 working days | pulled by the pair from its buffer of clarified functions; projects A and B first | work product handed over, no further edits expected, short review done (post 231) |
| System development | not a case: a larger unit | split into work items of 1-3 days before entering the flow (post 224) | per item as for new function; the larger unit closes when all items are done |

**Result-centred units for projects A and B** (post 244): the result a project needs from us is a parent unit; the cases of the DQ pair and the Catalog/Lineage pair are child work items under it.

## 1a. Work item classification (2026-11-19)

> Source: #workitems series, posts 252-253 (15 classification bases) and 255-257 (bases in practice), t.me/product_operations; course R3.4:8 (one classifier - one basis). **One work item can be classified by several bases at once - each answers its own question** (post 252).

| Basis (author's #) | Classes for the DG/DQ team | Question it answers |
|---|---|---|
| Reason for singling out work (13) | data user request; management assignment; project requirement (A, B); event (DQ rule failure, platform update); internal team question | where demand comes from - traceability from request to result (post 255) |
| Subject of work (3) | DQ; Data Catalog; Data Lineage; platform and infrastructure | which engineering pair; several initiatives touching one component |
| Position in the structure (11) | initiative → epic → story / function → task (1-3 days) | how to split large items; forecasting by tasks (posts 224, 256) |
| Priority category (6) | urgent; fixed date (projects A and B, budget cycle); standard; deferred | order of start, buffers, right to interrupt (R4.1:10) |
| Contribution type (8) | work producing the result; enabling work (preparation, approvals, access requests) | are missing start conditions visible in advance; enabling work can exceed result work (post 256) |
| Kind of activity (4) | investigate and clarify (discovery: triage, problem card); implement (delivery) | who performs (product manager or engineers); where the constraint is (Tasks3: discovery side) |
| Organisational coordination boundary (12) | within a pair; between DQ and Catalog pairs; with projects A and B; with IT or vendor | where work items get lost in "grey zones" between teams (post 257) |
| Severity for the recipient (7) | blocks a process or a regulatory submission; hinders, workaround exists; inconvenience | what to do first among DQ problems; linked to the issue severity classifier |
| Type of expected effect (2) | risk reduction (quality, compliance); cost reduction (manual reconciliations); support of revenue processes (data for sales and retailers) | how to justify initiatives, incl. the **2027 funding request** (problem card B-1, rival formulation "value not shown") |
| Use of work products (10) | for one result; shared component for several (e.g. a source connection needed by both A and B) | do not count a shared component twice |
| Composite: demand type (post 257) | consultations; management assignments; new functions; development | **capacity share per demand type in advance**, then plan vs fact |

**Example:** connecting the ERP source to the catalog for project A - reason: project requirement; subject: Data Catalog; position: epic, split into tasks; priority: fixed date; contribution: producing the result; boundary: with project A and IT; effect: support of revenue processes; use: shared component if project B also needs it; demand type: new functions.

**Not classes of work items** (posts 248-249): card status (state of the record), card type in the tracker (property of the description), work episode, work product, observed effect - other objects, accounted separately.

**Minimum to start** (pay only for current complexity):
1. **Reason** - all demand in the tracker; assignments from chats moved to the tracker, nothing done that is not recorded (post 255).
2. **Subject** - routing to the engineering pair.
3. **Priority category** - urgent via the duty engineer, projects A and B to their dates.
4. **Composite demand type with capacity shares** - placeholder: consultations and management assignments 30 %, new functions 60 %, development 10 % of case time; compare with fact monthly.
5. **Type of effect** - for initiatives only; needed for the 2027 budget justification.

## 2. Segment and workstations

| Workstation | Who works | Classes |
|---|---|---|
| Triage and prioritisation | product manager | all |
| Clarification with the requester | assignee ↔ requester | all, often |
| Analysis and solution | engineer of the domain (DQ or Catalog/Lineage) | all |
| Implementation (configuration, development) | engineer of the domain; sometimes IT or vendor | new function, development |
| Review | second engineer of the pair | new function, development |

| Hand-over and confirmation | assignee → requester | all |

Team (clarified 2026-11-15): product manager (triage); 2 engineers on DQ, 2 on Data Catalog and Data Lineage; no analysts; cases split ~50/50 between the domains. See `case-flow-constraint-r4.md`.

Triage and clarification are the **discovery** side (is the request worth solving, what exactly is needed); analysis, implementation and review are the **delivery** side (#workitems posts 237-238). The constraint found in Tasks3 - triage - is on the discovery side.

The queue before triage (created, not yet accepted) is outside the segment - but the tracker does not separate it today (see §8).

## 3. Start event and state

**Event:** case accepted into work - triaged, assignee set, priority set (commitment point).
**State:** it is known who works on it and with which priority; the request content may still be incomplete.

## 4. End event and state

**Event:** the requester received the result and confirmed it; no further edits are expected; the case is closed as resolved. For new functions - plus a short review of what to improve (#workitems post 231). The card status alone is not proof of completion: card status may not reflect reality (post 248).
**State:** result delivered and accepted. Cases closed without resolution (duplicate, rejected, "not ours") are not throughput; counted separately.

## 5-7. Observed figures and flow time

| Quantity | Value | Status |
|---|---|---|
| Open cases (WIP) | 100 | observation, 2026-11-13; no split by class; includes cases not yet accepted |
| Throughput (closed) | 2-3 per month | observation |
| Arrivals (created) | 2-3 per week ≈ 9-13 per month | observation |
| Little's law: WIP / throughput | 100 / 2-3 ≈ 33-50 months (≈ 40) | calculation - valid only for a stable flow, see below |

**The flow is not stable.** Arrivals (≈ 9-13 per month) are about four times the throughput (2-3 per month). WIP grows by about 7-10 cases per month. Under these conditions Little's law does not describe a steady state (FPF OPS.Reference:1.3: it relates consistent long-run averages); the ≈ 40 months is a **lower bound** for a new case under first-in-first-out, and it keeps growing. With prioritisation, some cases pass quickly and others effectively never.

## 8. Touch time (estimate from experience)

| Class | Touch time |
|---|---|
| User consultation | 0.5-2 h |
| Management question | 1-4 h |
| New function | 1-3 working days |
| System development | weeks |

Even at one full working day per case on average, touch time is under 0.1 % of the computed flow time.

## 9. Where the waiting comes from

**Observation (2026-11-13):** all 10 oldest open cases are waiting for resources to be freed. This confirms real overload and rejects, for these cases, the hypotheses "resolved but not closed" and "no longer relevant". Caveat: the oldest cases are a biased sample - they are likely the deprioritised ones; the rest of the 100 may contain resolved or dead cases.

**Main explanation:** a capacity gap. The team closes 2-3 cases per month while 9-13 arrive. Cases most likely get the capacity left over from other work (projects, operations) - there is no reserved capacity for the case flow. Waiting is therefore mostly **queue time for a free resource**, not waiting inside the work.

Further hypotheses (to check by reading case histories, since the tracker has no waiting statuses):

| Hypothesis | Check |
|---|---|
| Management questions jump the queue and interrupt started work | cases of other classes paused while an urgent case was done |
| Waiting for clarification from requesters | time between assignee question and requester answer in comments |
| Waiting for other teams (IT, vendor) | mentions of external teams in history |
| Many cases per person, switching | open cases per assignee |
| Closure lag (result delivered, not confirmed) | time from hand-over to closure |

## Work item measures to add (2026-11-17, #workitems series)

| Measure | What it shows | Source |
|---|---|---|
| Work episodes per case (interval from start or resume to finish or interruption) | losses from interruptions: urgent management questions create several episodes per case | post 249 |
| Expected user outcome vs observed effect - who checks the effect and when, for new functions and for results for projects A and B | whether delivered functions bring value; closes the feedback loop | posts 244, 249 |
| SLE per class (flow time with a stated probability, e.g. 85 % of consultations within N days) | forecast per class instead of one mixed Little's-law average | post 248 |

Of the three reasons to agree on work items (post 244) - agreed customer value, feasible commitments with available capacity, closed feedback loop - the team today covers only the first, partly (intake template planned). Feasibility (no "not now") and feedback (no effect check) are not covered - consistent with the findings of Tasks1-4.

## Data limitations

- No split by case class - the average mixes one-hour consultations and multi-month development.
- No waiting statuses - waiting causes can be checked only by sampling histories.
- No "created" vs "accepted" separation - the start boundary is blurred; WIP includes the queue before triage.

## Inputs for the next R4 tasks (improvement candidates)

- Make the capacity gap explicit: arrivals vs throughput per month, reported regularly.
- Reserve capacity for the case flow, or limit admission (WIP limit, explicit "not now" decision).
- Introduce case classes and a separate "accepted into work" point.
- Introduce waiting statuses (waiting for requester / external team).
- Review the open backlog: close resolved and no longer relevant cases.

## FPF check

- Little's law applied with consistent boundaries and checked for stability (OPS.Reference:1.3); instability stated explicitly.
- Measurement constructions named: interval start/end, population, window (OPS.15.1:2).
- Units: flow time in calendar months; touch time in working hours/days (C.16:5.2).
- Epistemic status per figure: observation / calculation / estimate / hypothesis; waiting causes kept as hypotheses with checks (CAUSAL-USE).
