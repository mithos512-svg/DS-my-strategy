---
type: templates
date: 2026-11-22
course: R4.2:6, R4.2:Tasks2
problem_card: problem-cards-r4.md, B-2
status: v1.3 (checked against FPF Library C.28, OPS.16, CONSEQUENCE-BEARERS, C.11.DUA, OPS.10; snapshots 20261122T121956Z, 20261125T054841Z)
hypotheses: hypotheses-case-queue-r4.md (R4.3:Tasks1)
uncertainty: uncertainty-case-queue-r4.md (R4.2:Mod3)
---

# Intervention template and interventions for the case queue

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/02-problem-formulation-epistemology-and-problem-solving/10-planning-and-designing-strategic-interventions.md`; lesson R4.2:6 (commit faed795, 2026-11-04).

**Principle (R4.2:6):** solving a problem needs two explanations - a **negative** one (why the current state is bad) and a **positive** one (why the intervention improves it, for whom, and **which side effects** it causes). Distinguish changes we make **ourselves**, changes that need **others**, and circumstances **outside our control**. Besides removing the cause, consider indirect directions: damage reduction, prevention of recurrence, adaptation, abandoning the activity - and always **"do nothing"**.

**FPF guards (v1.1):**
- Keep the causal rungs apart (C.28:2): data from R4.1 are **observations**; a positive explanation is an **intervention claim, not yet tested**; "do nothing" keeps the natural mechanism, so its forecast is a **trend extrapolation under unchanged conditions** (observational rung, C.28:4.1, 4.10), not a counterfactual.
- A check result is evidence, not a decision: the decision stays with whoever has the authority (C.28:2, authority collapse).
- A trial needs conditions, stop rules, fallback, observation burden and a decision maker (OPS.16:4.3-4.4).
- Side effects are listed **by consequence-bearer** - who may be affected - to find omitted ones (CONSEQUENCE-BEARERS).

## Intervention template

| # | Section | How to fill in |
|---|---|---|
| 0 | Problem and negative explanation | Link to the problem card and its general statement. Short mechanism of how the unfavourable state arises now; if several explanations exist, name them and the one the intervention relies on. |
| 1 | Direction | remove the cause / reduce damage / prevent recurrence / adapt / abandon the activity / do nothing |
| 2 | What we change | Concrete changes in rules, method, tracker, time allocation. For each: **we ourselves** / **needs others (whom)** / **outside our control**. |
| 3 | Mechanism affected | The link of the negative explanation the change acts on; if none (damage reduction, adaptation), say so. |
| 4 | Positive explanation + status | Chain "change → mechanism → effect → for whom". Mark the status: **prediction, not tested; based on observations of …**. Without the chain an intervention is a wish. |
| 5 | Undesired consequence reduced or stopped | From the "for whom unfavourable" block of the problem card. |
| 6 | What we adapt to | The condition we do not change - because we cannot or should not. |
| 7 | Feasibility | Resources (time, people, tools) - **counted against the same people's current work: what stops or shrinks**; authority (who must agree); time to effect. |
| 8 | Consequence-bearers and side effects | Table "who → what may happen to them", now and **under changed circumstances** (demand growth, a person leaving, management priorities change). Go through: requesters, data consumers downstream, engineers (incl. the duty engineer), PM, management, projects, IT/vendor. |
| 9 | Compatibility with other measures | Reinforce, hinder or neutral; **does one measure change the quantities used to check another**; what must not start at the same time. |
| 10 | Check | **Observe** (quantity, unit, source); **compare with** (baseline, window); **threats to the conclusion** - what else could produce the same result (seasonality, concurrent changes, natural fall-back from a peak); **"solved"** (threshold); **"revise"** (threshold or sign; what shows the rival explanation is true); **"not enough data - extend observation"**. |
| 11 | Conditions, stop, fallback, decision | Conditions the trial relies on (authority, support, protection of current service); **early stop rule**; **how to return to the previous order**; who collects the measures and at what cost; **who decides** keep / change / cancel after the check. |

## Problem (card B-2)

**Requests to the DG/DQ team wait for months and the queue keeps growing.**

Negative explanation (from observations, R4.1, 13.11) - two hypotheses, not yet distinguished: (a) triage is done ad hoc and became the constraint (40 untriaged, triage ≈ 270 %); (b) engineering capacity is insufficient regardless of triage (≈ 115 %, 9-13 arrive per month, 2-3 closed). Amplifier: urgent management assignments interrupt other work.

## Intervention 0. Do nothing

- **Direction:** do nothing.
- **Trend extrapolation under unchanged conditions** (observational rung; assumption: arrivals stay at 9-13/month, throughput at 2-3/month, no seasonal drop): WIP grows by 7-10 cases/month, ≈ 150 in six months; flow time for new cases keeps growing; projects A and B get results only when their cases break through as urgent.
- **Consequence-bearers:** requesters (longer waits, more workarounds); projects A and B (slips); engineers (permanent interruption mode).
- **Why consider:** baseline for comparison and the cost of inaction - an argument for the DG lead.

## Intervention 1. Regular triage with an explicit "not now"

0. **Relies on hypothesis (a).**
1. **Direction:** remove the cause + restructure the process.
2. **What we change:** weekly triage slot 1.5 h - **ourselves** (PM); intake template (class, subject, need, date, reason) - **ourselves**; each case gets "accept / not now / reject", "not now" with a review date - **ourselves**, needs **requesters' agreement** that "not now" is not a refusal; assignments from chats go to the tracker (#workitems post 255) - **ourselves**, needs **agreement with management**; **staged launch** - first 4 weeks "not now" only in one case class (e.g., new functions not related to A and B), then all classes if no workaround signs (launch condition from `uncertainty-case-queue-r4.md`, question 3).
3. **Mechanism:** the queue before triage and the implicit "everything is accepted".
4. **Positive explanation (prediction, not tested; based on R4.1 observations and estimates):** slot + template bring triage utilisation from ≈ 270 % to ≈ 73 % → the 40 untriaged cases get a decision within 4-6 weeks → only accepted cases reach engineers, in priority order → A and B go to their dates; "not now" stops hanging silently in the queue.
5. **Reduces:** months of waiting without an answer; invisibility of demand for management.
6. **Adapts to:** engineering capacity (unchanged).
7. **Feasibility:** 1.5 h/week of PM - **open: which PM work shrinks to free it** (the PM also holds the methodologist, org-designer and partly leader roles, R4.1:Mod1); template 1-2 days; within team authority; effect in 2-4 weeks.
8. **Consequence-bearers:**

| Who | What may happen |
|---|---|
| Requesters with "not now" | escalate to management → more urgent assignments; **or work around the team** - own extracts, shadow tables, which worsens data quality |
| Engineers | if (a) is wrong, queues just move to them |
| PM | the slot displaces other PM work |
| Management | sees the "not now" list - may question priorities |

9. **Compatibility:** reinforced by 2 ("not now" gets a date), but **2 changes arrivals** (long published dates discourage new requests) and would distort the check of 1 → start 2 two to three weeks after 1, and track arrivals separately. Not at the same time as 3.
10. **Check:** observe - untriaged cases (weekly), cases closed per month - **"done" and "closed as not relevant" counted separately**, arrivals per month, queues at engineering pairs, **waiting measured from the original request date** (incl. time under "not now"), new unregistered extracts in the domains of "not now" cases; compare with - baseline 13.11 (40 untriaged, 2-3 closed/month, 9-13 arrivals, 21 per pair); **threats** - December holidays and end of the budget cycle lower arrivals by themselves; intervention 2 lowers arrivals; **solved** - untriaged ≤ 10 after 6 weeks **and** accepted arrivals ≤ "done" per month after 2 months **and** 85 % of accepted cases within the promised time counted from the request date (criterion to be agreed with the DG lead before start); **revise** - time to decision does not fall → triage is not the issue; (throughput is checked in intervention 1b, not here - triage alone speeds decisions, not output); **not enough data** - arrivals dropped strongly (season) → extend observation by 4 weeks.
11. **Conditions, stop, fallback, decision:** conditions - PM slot protected in the calendar, requesters informed about "not now", DG lead's answer on routing urgent assignments through triage (until then the check covers only tracker arrivals), criterion of "solved" agreed; **gate after stage 1** - workaround signs in the pilot class → "not now" only with an alternative (self-service path, temporary dataset marked with its quality status) or intervention 2/3 moves earlier; **early stop** - two or more escalations per week about "not now", or a confirmed shadow extract/table created because of "not now"; **fallback** - return "not now" cases to the queue in their original order; measures collected by the PM from the tracker (≈ 15 min/week); **decision** keep / change / cancel - PM, informing the DG lead.

## Intervention 1b. WIP limit per engineering pair

0. **Relies on hypothesis H1b** (`hypotheses-case-queue-r4.md`): too many cases in progress at once (≈ 21 per pair) → switching and losses → few closures. Pre-experimental argument (R4.3:Tasks1): of the cheap measures only this one can raise output; triage alone shortens time to decision.
1. **Direction:** remove the cause + restructure the process.
2. **What we change:** each pair holds at most 3-4 cases in progress; a new case starts only when one is done or explicitly parked - **ourselves** (PM with the pairs); "in progress" date recorded in the tracker - **ourselves**; urgent assignments count against the limit - needs **agreement with management** (same conversation as intervention 1).
3. **Mechanism:** parallel work at the pairs (switching, restarting after interruptions).
4. **Positive explanation (prediction, not tested; no comparable period in history - the limit never existed):** fewer cases in progress → less switching and restarting → more cases finished per month → A and B reach their dates.
5. **Reduces:** low output; cases that are "in progress" for months.
6. **Adapts to:** headcount (4 engineers, 50/50).
7. **Feasibility:** one meeting with the pairs to pick the 3-4 cases each; tracker field; effect in 4-8 weeks; within team authority.
8. **Consequence-bearers:**

| Who | What may happen |
|---|---|
| Requesters of parked cases | a case that was formally "in progress" is now openly waiting - may escalate |
| Engineers | idle time while waiting for a requester answer on a blocked case - needs a rule for blocked cases |
| Management | an urgent assignment now visibly displaces a named case |

9. **Compatibility:** starts together with 1 - the outcomes differ (1: time to decision; 1b: output "done" per month), so the two effects can be told apart; 2 and 3 as before.
10. **Check:** observe - cases in progress per pair (weekly), "done" per month, time in progress per case; compare with - baseline ≈ 21 per pair, 2-3 done/month; **threats** - closing obsolete cases during triage inflates "closed" (count "done" only); December holidays; **solved** - "done" ≥ 5/month after 2 months with ≤ 4 in progress per pair; **revise** - limit held but output flat → hypothesis H2 (capacity, hidden support work), next step is the capacity conversation with the DG lead; **not enough data** - limit not held for at least 4 weeks.
11. **Conditions, stop, fallback, decision:** conditions - pairs agree to the limit, rule for blocked cases; **early stop** - a project A/B date at risk because of the limit; **fallback** - raise the limit to 6-8, not back to unlimited; measures - PM from the tracker (≈ 10 min/week); **decision** - PM with the pairs, informing the DG lead.

## Intervention 2. Realistic promises and protection of projects A and B

0. **Not tied to a hypothesis:** acts on consequences, not causes.
1. **Direction:** reduce damage + adapt.
2. **What we change:** publish expected flow time per class with probability (SLE, e.g. "85 % of consultations within N weeks") from tracker history - **ourselves**, **depends on case classes being in the tracker** (minimum classification set); the requester gets the expected date at intake, early notice if at risk - **ourselves**; A and B cases get class "fixed date" and a separate time reserve - **needs DG lead and project leads**.
3. **Mechanism:** neither triage nor capacity; changes requesters' expectations and the order for dated work.
4. **Positive explanation (prediction, not tested):** the requester knows the real date → can re-plan or find a workaround → fewer "when?" follow-ups and fewer surprises; A and B get results by their dates at the expense of other cases.
5. **Reduces:** damage from unknown dates; risk of slipping A and B.
6. **Adapts to:** current capacity and throughput.
7. **Feasibility:** SLE - one day once classes and created/closed dates exist; before that - one overall SLE with a stated limitation; reserve for A and B - DG lead decision; effect immediately after publication.
8. **Consequence-bearers:**

| Who | What may happen |
|---|---|
| Requesters | see long dates (months) - some stop submitting and work around the team |
| Management | sees long dates - may respond with pressure rather than a capacity decision |
| Other requesters (not A/B) | the reserve for A and B slows them down |
| PM | must revise dates constantly if demand grows |

9. **Compatibility:** reinforces 1 but changes arrivals - start 2-3 weeks after 1; no conflict with 3.
10. **Check:** observe - share of cases closed within the promised date, status follow-ups, A and B results by their dates, arrivals; compare with - no dates promised now; follow-up baseline from the last month (tracker or mail); **threats** - fewer follow-ups may come from fewer arrivals, not from better information; **solved** - ≥ 85 % within the promised date, follow-ups halved relative to arrivals, no A/B slips caused by the team; **revise** - promised dates keep growing → without changing capacity or entry (1 or 3) this only records deterioration; **not enough data** - fewer than ~20 closed cases in the window.
11. **Conditions, stop, fallback, decision:** conditions - DG lead agrees to the A/B reserve; **early stop** - promised dates exceed what requesters can accept and arrivals fall sharply (sign of workarounds); **fallback** - stop publishing dates, keep only early notice; measures - PM from tracker and mail; **decision** - PM for dates, DG lead for the A/B reserve.

## Intervention 3. Reduce consultation demand through self-service

0. **Relies on part of hypothesis (b):** capacity is eaten by repeated consultations (~45 % of arrivals, assumption from R4.1).
1. **Direction:** prevent recurrence + change the method.
2. **What we change:** knowledge base of answers to typical questions (finding a dataset, term meaning, technical vs business metadata) - **ourselves**; each consultation starts with checking the base, a new answer is added - **ourselves**; link to the base in the intake template and catalog UI - **ourselves**, possibly with **vendor or IT** for the UI.
3. **Mechanism:** arrivals of consultation cases (incoming load).
4. **Positive explanation (prediction, not tested):** users close part of the questions themselves → consultation arrivals drop → engineering time is freed for new functions → function throughput grows, incl. for A and B.
5. **Reduces:** engineers' load with repeated questions.
6. **Adapts to:** headcount (hiring an analyst is outside team authority).
7. **Feasibility:** first 20-30 answers ≈ a week of work spread across engineers, **taken from cases** - throughput drops temporarily; effect in 2-3 months.
8. **Consequence-bearers:**

| Who | What may happen |
|---|---|
| Data consumers downstream | an outdated answer leads to decisions on a wrong understanding of the data |
| Users | do not find the answer and write anyway - double effort |
| Engineers | maintenance of the base becomes a permanent extra duty |
| Requesters of all classes | temporary throughput drop at start |

9. **Compatibility:** fits 1 and 2, but **not at the same time as 1**. Sequence: 1 → after 4-6 weeks 3.
10. **Check:** observe - share of consultations in arrivals, base hits, new function throughput; compare with - baseline ≈ 45 % (refine by tracker after classes are introduced); **threats** - consultation share can drop seasonally or because intervention 2 discourages requests; **solved** - consultations ≤ 30 % after 3 months and function throughput up; **revise** - base hardly used or share unchanged → questions are not typical; **not enough data** - classes introduced less than 2 months ago.
11. **Conditions, stop, fallback, decision:** conditions - an owner for each answer and a review date; **early stop** - more than one complaint about a wrong answer per month; **fallback** - remove or mark outdated answers, return to answering by case; measures - from base statistics and tracker; **decision** - PM with the engineers.

## Overall compatibility

**Sequence: 1 + 1b → (2-3 weeks) → 2 → (4-6 weeks after 1) → 3.** Interventions 1 and 1b first: cheap, within team authority; 1 checks H1a by time to decision, 1b checks H1b against H2 by output. Intervention 2 changes arrivals, so it starts after 1 and arrivals are tracked separately in every check. Intervention 3 - once it is clear where the constraint is. If 1b ends in "revise", the next step is not 3 but a capacity conversation with the DG lead - an "involves others" option deliberately left out of the three (adding people is outside team authority).

## Changes v1.2 → v1.3 (R4.3:Tasks1, FPF C.28)

- New intervention 1b - WIP limit per pair (hypothesis H1b); started together with 1 because the outcomes differ.
- Intervention 1 "revise" branch: judged by time to decision, not output; the output question moved to 1b.
- "Do nothing" relabelled: trend extrapolation under unchanged conditions (observational rung), not a counterfactual forecast (C.28:4.1, 4.10).
- For H1a, H1b, H2 history has no comparable periods (no triage, no limit, fixed team) - only the interventions themselves can give rung-2 evidence.

## Changes v1.1 → v1.2 (R4.2:Mod3, FPF C.11.DUA, OPS.10)

- Staged launch of intervention 1: "not now" first in one case class; gate after 4 weeks on workaround signs (uncertainty question 3, the only one that can reverse the choice).
- Waiting measured from the original request date, so that "not now" does not move waiting outside the measured boundary (OPS.10:4.4).
- "Done" and "closed as not relevant" counted as separate populations (OPS.10:4.1).
- Criterion "solved" changed from "closed ≥ 5/month" to stability (accepted arrivals ≤ done) plus a probabilistic time criterion; to be agreed with the DG lead.
- Management agreement on urgent assignments is a launch condition, not assumed (CC-C11DUA.7).

## Changes v1.0 → v1.1 (FPF)

- Status of the positive explanation (intervention claim, not tested) and of "do nothing" (counterfactual forecast with assumptions) - C.28:2.
- Section 8 by consequence-bearers; found omitted risks: requesters working around the team (shadow extracts), duty engineer overload, PM time, management reaction, outdated answers for downstream consumers - CONSEQUENCE-BEARERS.
- Section 10: threats to the conclusion and a third branch "not enough data".
- New section 11: conditions, early stop, fallback, observation burden, decision maker - OPS.16:4.3-4.4; check result ≠ decision - C.28:2.
- Compatibility of 1 and 2 corrected: 2 changes arrivals and would distort the check of 1.
- Intervention 2 depends on case classes in the tracker; PM time for intervention 1 is an open question.
