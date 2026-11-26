---
type: templates
date: 2026-11-22
course: R4.2:6, R4.2:Tasks2
problem_card: problem-cards-r4.md, B-2
status: v1.4 (checked against FPF Library C.28, OPS.16, CONSEQUENCE-BEARERS, C.11.DUA, OPS.10, A.2.8, HCD.Reference:3; snapshots 20261122T121956Z, 20261125T054841Z)
hypotheses: hypotheses-case-queue-r4.md (v1.1, R4.3:Tasks1)
cause_effect: cause-effect-pairs-case-queue-r4.md (v1.2, R4.3:Tasks2)
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

Source of arrivals and urgents (added 26.11, R4.3:Tasks2): more and more functions join DG/DQ; the engagement department forwards even basic questions and asks the team to talk to each function directly (H4); urgents are mainly steward onboarding. The team does not resolve DQ problems - stewards do.

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

## Intervention 3. Repeatable onboarding product for functions and stewards

*Re-targeted in v1.4 (was: knowledge base for consultations). Per the user (26.11) the repeated demand is mainly explaining DG/DQ, its requirements and the platform functionality to new functions and onboarding their stewards.*

0. **Relies on refined H2 and on cause-effect pairs 18, 20-22, 24** (`cause-effect-pairs-case-queue-r4.md`): every new function is onboarded individually and urgently; trained stewards should reduce demand later.
1. **Direction:** prevent recurrence + change the method (individual onboarding → repeatable product).
2. **What we change:** a standard onboarding kit - what DG/DQ is, the steward role and what is required from a function, the main platform functionality, where and how to ask - **ourselves**; a monthly cohort for new functions with a fixed reserve of engineering time - format **ourselves**, the reserve needs the **DG lead**, routing functions into the cohort needs the **engagement department** (see intervention 4); self-service materials linked from the catalog - **ourselves**.
3. **Mechanism:** arrivals of explanation and onboarding work and urgent onboarding requests (pairs 18, 24, 7).
4. **Positive explanation (prediction, not tested):** one kit + monthly cohorts → explanation served once per cohort, not per function → fewer urgent onboarding requests → fewer stops of case work → more "done"; trained stewards resolve DQ problems themselves → fewer misrouted DQ cases.
5. **Reduces:** urgent onboarding, repeated explanation, misrouted DQ problems.
6. **Adapts to:** the growing number of functions (the rollout continues - that is a success).
7. **Feasibility:** kit ≈ 1-2 weeks of one engineer + PM, **taken from cases** - output drops temporarily; a cohort ≈ 2-3 h per month; effect in 2-3 months.
8. **Consequence-bearers:**

| Who | What may happen |
|---|---|
| New functions | wait up to a month for a cohort instead of an immediate session - may escalate |
| Engagement department | must route functions into cohorts; may see it as slowing the rollout |
| Stewards | a standard programme may not fit a specific function |
| Engineers | kit maintenance after platform changes becomes a permanent duty |
| Data consumers downstream | an outdated kit teaches stewards a wrong practice |

9. **Compatibility:** the kit is the tool for the first line in intervention 4 - prepare together with 4. Kit preparation takes engineering time - not during the first 4 weeks of 1b.
10. **Check:** observe - urgent onboarding requests per month (by subject), explanation hours, DQ issues resolved by stewards without team help (per onboarded function), misrouted DQ cases; compare with - baseline from recording urgents and forwarded questions started 26.11; **threats** - a slower rollout lowers urgents by itself (normalise per new function); intervention 4 acts on the same urgents; **solved** - urgent onboarding ≤ 1 per month and explanation time per new function halved after 3 months, and in each onboarded function at least one DQ issue resolved by stewards without team help; **revise** - functions bypass cohorts through urgents → the issue is the rule, not the material - go to intervention 4; **not enough data** - fewer than 3 new functions in the window.
11. **Conditions, stop, fallback, decision:** conditions - DG lead agrees to the reserve; the engagement department routes functions into cohorts; **early stop** - a function important for projects A or B is blocked by waiting for a cohort → serve it individually as an exception; **fallback** - individual sessions, but with the kit (reuse remains); measures - PM records; **decision** - PM with the DG lead.

## Intervention 4. Agreed division of labour with the engagement department

*Added in v1.4. Relies on H4 (`hypotheses-case-queue-r4.md` v1.1). The only intervention that **needs others** for its core change.*

0. **Relies on H4:** the engagement department forwards even basic questions and asks the team to talk to each function directly; the boundary of its duty is not written anywhere.
1. **Direction:** remove the cause by changing the rule between two departments.
2. **What we change:** record forwarded questions (from whom, basic or technical, time spent) for 4 weeks as evidence - **ourselves**, start now; propose an explicit boundary: the engagement department answers basic questions using the kit (first line), technical questions come to the team through intake and triage (second line), the engagement department runs the cohort and the team covers its technical part - **needs others**: the engagement department; raised by the **DG lead**; the **D&A lead** if the boundary must be set above both departments.
3. **Mechanism:** the forwarding practice and the undefined duty boundary (pairs 23, 25).
4. **Positive explanation (prediction, not tested):** an agreed boundary + a non-technical kit → basic questions stay at the first line → only technical questions reach the team → explanation load and urgent onboarding drop → more "done".
5. **Reduces:** forwarded basic questions; the team's invisible work.
6. **Adapts to:** the engagement department not going into technical details - accepted; the kit is written for non-technical staff.
7. **Feasibility:** outside team authority; the DG lead (decides budget and staff) must raise it; preparation - 4 weeks of records; effect 1-3 months after an agreement; the department's staff need time to learn the kit.
8. **Consequence-bearers:**

| Who | What may happen |
|---|---|
| Engagement department | more work for its staff; may resist - frame it as a faster rollout, not as a transfer of blame |
| New functions | a first answer from a non-technical person may be wrong - the kit needs a "when to forward" list |
| DG lead | spends political capital on the conversation |
| DG/DQ team | still maintains the kit and answers technical questions |
| Management | sees the division of labour explicitly; may be asked to arbitrate |

9. **Compatibility:** depends on 3 (the kit). Changes urgent arrivals and therefore output - would distort the check of 1b; record urgents separately; the agreement will most likely take effect after the 8-week window of 1b.
10. **Check:** observe - forwarded questions per month, share of basic vs technical, explanation hours; compare with - the 4-week baseline recorded before the conversation; **threats** - rollout pace (normalise per new function); **solved** - basic questions ≤ 20 % of forwarded after 2 months; **revise** - an agreement exists but forwarding does not change → the rule is not enforced, take it to the D&A lead; **not enough data** - fewer than 10 forwarded questions in the window.
11. **Conditions, stop, fallback, decision:** conditions - the DG lead is willing to raise it; baseline records exist; **early stop** - two or more complaints per month about wrong first-line answers → tighten the "when to forward" list; **fallback** - the team answers again, the kit stays; **decision** - the boundary is agreed between the heads of the two departments (DG lead and the engagement department head), the D&A lead if they disagree; the team does not decide it alone.

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
