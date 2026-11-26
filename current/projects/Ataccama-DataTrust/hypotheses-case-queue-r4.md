---
type: model
date: 2026-11-25
course: R4.3:1, R4.3:2, R4.3:Tasks1
problem_card: problem-cards-r4.md, B-2
interventions: interventions-case-queue-r4.md (v1.4)
status: v1.1 (checked against FPF Library C.28:4.1, 4.3, 4.9, 4.10, A.2.8:4; snapshot 20261125T054841Z)
cause_effect: cause-effect-pairs-case-queue-r4.md (v1.2)
---

# Research question and hypotheses for the case queue

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/03-understanding-causality-and-counterfactual-thinking/03-framing-problems-and-formulating-hypotheses.md`; lessons R4.3:1 "Events and probabilities", R4.3:2 "Ladder of causation" (commit faed795, 2026-11-04). Continues the B-2 line (R4.1 flow models, R4.2 problem card, interventions, uncertainty) instead of R2.4:Tasks4.

**Principles:**
- Seeing A together with B - P(B | A) - is association; doing A - P(B | do(A)) - is intervention; "would B have happened in this case without A" is counterfactual (R4.3:2).
- Association arises when A causes B, when B causes A, and when a common cause C produces both; observation alone cannot tell them apart (R4.3:1).
- The rung names the **question**, not its support; naming an intervention does not mean it was performed (C.28:4.1). An average effect of a policy over all cases is a rung-2 question; "what would have happened to this case, given its history" is rung 3.
- Compare a new policy with the **current policy**, not with an overall probability: P(Y | do(new)) vs P(Y | do(as now)) (C.28:4.1).
- Keeping the natural mechanism ("do nothing") is forecast on the observational rung (trend extrapolation), not counterfactually (C.28:4.10).

## 1. Research question and objects

**Question:** why does the DG/DQ team close 2-3 cases per month while 9-13 arrive, and which intervention will raise output without making data quality in the company worse?

| Object | Event class | Example of a concrete (4D) event |
|---|---|---|
| Case (unit of accounting and coordination) | arrival, intake decision, start of work, interruption, closure | the GTIN case closed in a given week |
| Triage (PM role) | decision "accept / not now / reject" | the 40 untriaged cases never triaged |
| Engineering pairs (DQ; Catalog + Lineage; 2 engineers each) | work on a case, switching | the DQ pair holding ≈ 21 cases in parallel |
| Urgent management assignment | displacement of other work | an urgent request from the D&A lead after which a pair stopped for N days |
| Projects A and B | waiting for a result by a date | a slipped date in project A |
| Tracker | a **description** of events, not the events; urgent assignments are not recorded in it | - |

**Quantities:** arrivals per month; output per month ("done" and "closed as not relevant" counted separately); cases in progress per pair; time from request to intake decision; waiting from the request date; urgent assignments per week.

**Unit of observation:** the team per month (cases share the same engineers, so they are not independent units). Evidence will be one time series with before/after comparison over a few months; seasonality and concurrent changes are the main threats.

## 2. Hypotheses

- **H1a - triage.** There is no regular triage → requesters wait months for a decision. Outcome: time from request to decision.
- **H1b - work in progress.** Pairs hold too many cases at once (≈ 21 per pair) → switching and restarts → few closures. Outcome: "done" per month.
- **H2 - capacity.** Even with triage and a limit, four engineers are not enough (load ≈ 115 %); part of their time goes to work nobody counts - **mainly explaining DG/DQ, its requirements and the platform functionality to new functions and onboarding their stewards** (refined 26.11), plus platform support. Outcome: "done" per month.
- **H3 - urgent assignments.** Urgent management assignments - **mainly engaging and training stewards for new functions** (refined 26.11) - displace all cases and cause the dips in output. Outcome: closures per week.
- **H4 - division of labour (added 26.11).** A separate department is responsible for engaging new functions, but does not go into technical details and forwards even basic questions, asking the team to talk to each function directly. With no agreed boundary of that department's duty, basic onboarding work lands on the DG/DQ team and is repeated function by function. Outcome: explanation hours per new function; share of basic questions among forwarded ones.

**Common cause behind H2, H3, H4:** the rollout of DG/DQ to more and more functions - it raises arrivals, explanation load and urgent onboarding at the same time (`cause-effect-pairs-case-queue-r4.md`, pair 11).

H1a was split from the earlier single "triage" hypothesis after the FPF check: "do(triage)" mixed two different interventions - deciding on cases and limiting work in progress - and only the second can raise output.

## 3. Pre-experimental argumentation

**H1a.** Chain: no regular triage → untriaged cases pile up → no answer for months. Assumption: decisions, not engineering work, are what requesters wait for first. Triage can shorten time to decision; it **cannot by itself raise output** if engineers are fully loaded.

**H1b.** Chain: ≈ 21 cases per pair → frequent switching, restarting after interruptions, cases blocked on requesters → low completion. Key assumption: switching losses are significant (not measured). Thought test (comparing worlds): if the team had six engineers but kept working on everything at once, would the queue still grow? If yes, H1b acts independently of H2.

**H2.** Chain: ≈ 11 arrivals × effort per case > time of four engineers → output limited. Assumptions: effort per case (from memory) and the share of platform support (not recorded). If that share is large, the constraint is invisible work, not cases.

**H3.** Chain: urgent assignment → pair drops cases → restart after return → dip in output. All three traps from R4.3:1 apply:

| Link | How it could look here |
|---|---|
| A causes B | urgent assignments really lower output |
| B causes A (reverse) | long waits produce escalations, and escalations become urgent assignments |
| C causes A and B (common cause) | budget cycle or quarter end produces urgent assignments and also distracts engineers |

**H4.** Chain: new function interested → engagement department forwards its questions → the team explains individually → explanation time grows with every function → less time for cases. Assumption: a large share of forwarded questions is basic (answerable without technical depth) - based on the PM's observation, not recorded. The duty boundary of the engagement department is not written anywhere: that is a missing rule, not a proven refusal of a duty (A.2.8:4.2). The team's explanation work is performed by the team but counted as the engagement department's result ("function engaged") - duty bearer and performer differ (A.2.8:4.6).

**What is missing even for rung 1:** today there are only aggregate numbers (100 open, 2-3 closures per month, 2-3 arrivals per week). Associations need the tracker export with created/closed (and, where available, started) dates and a retrospective list of urgent assignments.

## 4. Threat screen (C.28:4.3)

| Threat | Finding | Consequence |
|---|---|---|
| Intervention well defined | "do(triage)" mixed triage and a WIP limit | H1 split into H1a and H1b with different outcomes |
| Overlap - comparable periods exist | No period with regular triage, no WIP limit ever, team composition unchanged | **History cannot give rung-2 answers for H1a, H1b, H2**; only the interventions can. History is a baseline. For H3 history may help if weeks without urgent assignments exist - check first |
| Confounding | For H1a the association "untriaged cases wait longer" is nearly circular, and case importance / requester rank speeds both triage and closure. For H3: budget cycle, quarter end | Rung-1 evidence for H1a has low value; H3 needs the common cause separated |
| Temporal order | H3: escalations after long waits could precede urgent assignments | Record dates of escalation and of assignment |
| Interference | Cases compete for the same engineers | Unit of observation is the team-month, not the case |
| Confounding (H4) | The pace of the rollout drives both forwarded questions and urgents | Normalise explanation hours and forwarded questions per new function |
| Missing data / measurement | Urgent assignments not in the tracker (recall bias when reconstructed); closing obsolete cases during triage changes what "output" means | Start recording urgent assignments now; count "done" separately from "closed as not relevant" |

## 5. Rungs of causation

| Hypothesis | Outcome | Current support (C.28:4.9) | Rung 1 - association | Rung 2 - intervention vs current policy | Rung 3 - counterfactual for a concrete case |
|---|---|---|---|---|---|
| **H1a** | time from request to decision | **undecided**: "triage ≈ 270 %" is a calculation from estimates, not an observation | weak, confounded by importance: P(decision in < 2 weeks \| case from management) > P(decision in < 2 weeks \| other) | P(decision ≤ 2 weeks \| do(weekly triage)) vs P(… \| do(as now)) | Would the GTIN requester have had a decision in the first month with weekly triage? |
| **H1b** | "done" per month | **undecided**: switching losses not measured | P(more closures in a month \| fewer cases in progress at the pair) - if start dates exist | E[done \| do(≤ 3-4 cases per pair)] vs E[done \| do(as now)] | Would the DQ pair have closed the A and B cases in October holding 4 cases instead of ≈ 21? |
| **H2** | "done" per month | **undecided**: 115 % is an estimate; history cannot answer (team unchanged) | P(low output \| month with much support work) - once support is recorded | E[done \| do(H1a + H1b)] ≈ E[done \| do(as now)], but E[done \| do(less consultation/support)] higher | Would the queue have grown all year if triage and the limit had been in place since spring? |
| **H3** | closures per week | **observation without records**; direction and common cause not excluded | P(0 closures in a week \| urgent assignment that week) > P(0 closures \| none) - if such weeks exist | E[output \| do(urgent assignments only through triage)] vs E[output \| do(as now)] | Would the project A case have closed in October without the urgent assignment that week? |
| **H4** | explanation hours per new function; share of basic questions among forwarded | **observation without records** (PM's experience) | P(question reaches the team \| basic question from a new function) - from a record of forwarded questions started now | E[explanation hours per function \| do(agreed boundary + kit)] vs E[… \| do(as now)] | Would the team have spent less time on the last onboarded function if the engagement department had answered its basic questions from a kit? |

## 6. Conclusions and next steps

- All hypotheses currently sit lower on the ladder than they sound: H1a, H1b and H2 are intervention claims without observed associations; H3 and H4 are associations "by feel", not recorded.
- The tracker history **will not answer the main question** - there are no comparable periods. Export it anyway as a baseline (created/closed dates).
- History is worth mining only for H3 - first check whether weeks without urgent assignments exist; in parallel start recording urgent assignments.
- H4 (added 26.11) points to the main source of arrivals and urgents; its rung-1 evidence is cheap - start recording forwarded questions (from whom, basic or technical) now. The intervention it suggests needs others (the engagement department, the DG lead).
- The pre-experimental argument added a new intervention: **WIP limit per pair (H1b)** - the only cheap measure that can raise output. Added to `interventions-case-queue-r4.md` v1.3 as intervention 1b, started together with triage because the outcomes differ.

## Changes

- v1.1 (2026-11-26): after R4.3:Tasks2 and the user's domain facts - H2 refined (invisible work = mainly explanation and steward onboarding), H3 refined (urgents = mainly steward onboarding), H4 added (undefined division of labour with the engagement department), common cause "rollout of DG/DQ" named; H4 rows in argumentation, threat screen and rung table (A.2.8:4).
- v1.0 (2026-11-25): first version after the FPF check - H1 split into H1a/H1b; overlap finding (no comparable periods for H1a, H1b, H2); circular rung-1 formulation for H1a replaced and marked as confounded; unit of observation = team-month; rung-2 formulations compare with the current policy; "do nothing" moved to the observational rung.

---

Sources: R4.3:1, R4.3:2, R4.3:Tasks1 (MimEcoSys/docs, commit faed795); FPF Library `C.28:4` (https://fpf.tools/C.28:4), `A.2.8:4` (https://fpf.tools/A.2.8:4), snapshot 20261125T054841Z-7b084255babf17c2.
