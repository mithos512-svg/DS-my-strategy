---
type: templates
date: 2026-11-18
course: R4.2:4, R4.2:Tasks1
status: v1.1 (checked against FPF Library C.22.2 ProblemCard, snapshot 20261118T201845Z)
---

# Problem card templates for the DG/DQ team

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/02-problem-formulation-epistemology-and-problem-solving/07-creating-and-structuring-the-problem-card.md`; card blocks from R4.2:4 (commit faed795, 2026-11-04). Checked against FPF C.22.2 ProblemCard.

**Principle (R4.2:4, FPF C.22.2):** do not mix context, signal, problem statement, causes and solution options; keep several hypotheses and several intervention options open. A solution written into the problem statement closes other explanations and options too early. A solution-shaped request ("prepare a funding request") is a legitimate **signal**, but not the problem.

**Rules for both templates:**
- **One card - one subject.** If the claims concern different subjects, split the card (C.22.2:2.2).
- **Claim family** in block 1: *actual condition* (observed now) / *anticipated condition* (forecast - state horizon and assumptions) / *solvability claim* (about available means). They need different checks.
- **Fill only what changes the next use** (C.22.2 "pay only for current complexity"). An empty block is fine if it does not change what happens next; write "not established" only where the gap matters for the next use.
- **Hypotheses and options are cues, not choices:** keep them short; choosing a method and planning work belong to the next step.
- **A card without a next use is not finished** (C.22.2:2.2).

Two templates for two problem classes:
- **A - data quality problems reported by data consumers;**
- **B - problems of developing the DG/DQ product** (funding, priorities, demand vs team capacity). B adds "who decides and with which authority", because budget and headcount decisions are outside the team.

---

## Template A. Data quality problem card

**Header:** number, date, card author, **who reported the signal** (role, unit). Who reported, the subject of the card and who is affected can be three different parties.

| # | Block | How to fill in |
|---|---|---|
| 1 | Problem statement + claim family | What is wrong with the data and for whom, one sentence. **No cause, no solution.** Mark: actual / anticipated (horizon, assumptions) / solvability. Wrong: "no DQ rule for GTIN". Right: "some new products have no GTIN when product data is sent to retailers" (actual). |
| 2 | Subject and context | Data domain and dataset; data elements as system.table.field; systems on the data path from source to consumer (lineage if available); period and population of records. |
| 3 | Established state of affairs (signal) | What was observed - count and share of records with the deviation, with unit and date; which method - DQ rule run, profiling, cross-system reconciliation, user report; who recorded it and where, with links to evidence. No "often" or "always" without numbers. |
| 4 | For whom and how it is unfavourable | Which expectation is broken (business definition, rule threshold, deadline); which consumer processes or reports are affected. **Breach and damage are separate lines.** |
| 5 | Important unknowns | Only questions whose answer changes the next use; each linked to the hypothesis or option that depends on it. |
| 6 | Hypotheses on causes (not tested) | Several, short, each with how to test it. |
| 7 | Intervention options (not chosen) | Several, short, each linked to a hypothesis. |
| 8 | Sign of improvement | Observable sign in the data and at the consumer, with threshold and observation window (e.g. trend of failed records of the rule). |
| 9 | **Next use** | One next step for the card: collect data / test a hypothesis / compare formulations / hand over to method selection / no change. |

### Example A-1. Missing GTIN for new products (real case)

**Header:** reported by the data steward of the product domain; affected: the team sending product data to retailers.

1. **Problem (actual):** some new products have no GTIN when product data is sent to retailers.
2. **Subject and context:** product master data, domain "product". Data element: GTIN in the product record in ERP. Data path: PLM → ERP → product data transfer to retailers. Products created in the last 3 months.
3. **Signal:** at the pre-transfer check, 300 of 1,200 new products (25 %) had an empty GTIN (01.11). Method: GTIN completeness rule run in the DQ module; link to the run result.
4. **For whom unfavourable:** for the team sending data to retailers - the transfer of these products is delayed (breach of the transfer deadline). Damage: not established - unknown whether product launches on shelves moved.
5. **Unknowns:** at which step is the GTIN assigned - PLM or ERP? Is the field mandatory at creation? Do the 300 have a GTIN in PLM?
6. **Hypotheses:** a) GTIN not mandatory at creation in ERP - test: form settings and fill dates; b) GTIN exists in PLM but is not carried over by the integration - test: PLM vs ERP reconciliation for the 300 products; c) GTIN is assigned later by process and the check runs too early - test: the assignment procedure.
7. **Options:** (a) make the field mandatory; (b) fix field mapping in the integration; (c) move the check point or the transfer deadline.
8. **Sign of improvement:** new products without GTIN at transfer = 0 for 4 consecutive weeks on the rule trend; no transfer delays for this reason.
9. **Next use:** reconcile PLM and ERP for the 300 products - this tests hypothesis (b) and splits the population for (a) and (c).

---

## Template B. DG/DQ product development problem card

**Header:** number, date, author, **who reported the signal** (role), **decision level**: team / DG lead / finance and senior management.

| # | Block | How to fill in |
|---|---|---|
| 1 | Problem statement + claim family | What is unfavourable and for whom. **No chosen solution.** Mark: actual / anticipated (horizon, assumptions) / solvability. Wrong: "prepare a funding request". Right: "catalog development in 2027 may remain unfunded" (anticipated). |
| 2 | Subject and context | Product or module (Data Catalog, Lineage, DQ); period (budget cycle, quarter); requesters and dependent projects; current resources (people, budget, licences). |
| 3 | Signal | What made us stop: fact, constraint, request (also a solution-shaped one), with source and date. |
| 4 | Why it is worth addressing / for whom unfavourable | Which commitments or expectations are broken or at risk; for an anticipated condition - the positive grounds (who needs the result and when). **Breach and damage separately.** |
| 5 | Who decides and with which authority | Roles (R4.1:Mod1): administrator (budget, headcount), strategist (direction), requester (project), approvers. What is within the team's authority and what is not. |
| 6 | Important unknowns | Only questions that change the next use. |
| 7 | Hypotheses / rival formulations | Several, short, each with how to test it. A rival formulation of the problem goes here; a different subject goes to its own card. |
| 8 | Intervention options (not chosen) | Several, short, each with **whose authority** it needs. |
| 9 | Sign of improvement | An **observed effect**, not performed work. "Request submitted" is work; "projects A and B receive results on time" is an effect. |
| 10 | **Next use** | One next step for the card. |

### Example B-1. Funding of data catalog development for 2027

**Header:** reported by the product manager; decision level: finance and senior management.

1. **Problem (anticipated; horizon - 2027 budget cycle; assumption - funding is decided per cycle and not extended without a request):** data catalog development in 2027 may remain unfunded or underfunded.
2. **Subject and context:** company budget cycle for 2027; data catalog (Data Catalog, Data Lineage), 2 engineers; requesters - projects A and B, data consumers.
3. **Signal:** the 2027 budget cycle has started; the initial formulation was solution-shaped - "prepare and approve a funding request for catalog development in 2027".
4. **Why worth addressing:** projects A and B need catalog work products; without funding their results may be delayed. **Damage not established:** unknown what exactly A and B would miss and when.
5. **Who decides:** request prepared by the product manager (team authority); first decision - DG lead (administrator: budget and headcount); **approval - the CFO and the D&A lead** (DG lead's manager). Projects A and B are requesters: they can support the request or co-fund.
6. **Unknowns:** submission deadline; what "catalog development 2027" includes (licences, people, new source integrations, functions for A and B); which 2026 results can be shown as an observed effect, not as performed work.
7. **Hypotheses / rival formulations:** rival formulation - "the value of the catalog is not shown in the terms used for budget decisions" (actual; if confirmed, a separate card); hypothesis - funding is reviewed each cycle and not extended without a request - test: budget procedure. The capacity gap of the team is a different subject - see **card B-2**.
8. **Options (with authority):** funding request - team prepares, DG lead decides, CFO and D&A lead approve; reprioritisation within the DG budget - DG lead; co-funding by projects A and B - project leads; narrowing the scope to what A and B need - team with DG lead; effect metrics first - team.
9. **Sign of improvement:** 2027 funding approved by the CFO and the D&A lead for the agreed scope; projects A and B receive catalog results on time.
10. **Next use:** find out the submission deadline and what A and B need from the catalog in 2027 - this defines the scope and decides whether the rival formulation needs its own card.

### Example B-2. The case queue keeps growing

1. **Problem (actual):** requests to the DG/DQ team wait for months and the queue keeps growing.
2. **Subject and context:** the team's case flow (consultations, management questions, new functions, development). Team: product manager (triage), 2 engineers DQ, 2 engineers Catalog/Lineage. ~10 % of engineers' time goes to cases.
3. **Signal:** 100 open cases; 9-13 arrive per month, 2-3 are closed (tracker, 13.11). All 10 oldest cases wait for resources (sample, 13.11).
4. **For whom unfavourable:** requesters wait for months; deadlines of the work products for projects A and B are at risk. **Damage not established:** unknown whether requesters work around the team and whether A and B deadlines slipped.
5. **Who decides:** triage and flow rules - product manager (team authority); engineers' time for cases and headcount - DG lead; urgent questions come from management - outside the team's authority.
6. **Unknowns:** how many of the 100 cases are actually solved or no longer relevant; number of interruptions by urgent questions per month.
7. **Hypotheses:** a) triage is done ad hoc and became the constraint - test: time in queue before triage; b) engineer capacity is insufficient regardless of triage - test: throughput after regular triage; c) interruptions by urgent questions eat the time - test: work episodes per case.
8. **Options (with authority):** weekly triage slot and intake template - product manager; duty rotation in engineering pairs - team; more engineer time for cases - DG lead; explicit "not now" for part of the cases - product manager with requesters.
9. **Sign of improvement:** cases closed per month ≥ cases arrived, 3 months in a row; the number of open cases does not grow.
10. **Next use:** introduce the weekly triage slot and compare throughput after 4 weeks - this distinguishes hypotheses (a) and (b).

---

## Colleague review (task item 3) - to do

Give one card of each type to a steward or engineer and ask:
1. Is it clear *what* the problem is without verbal explanations?
2. Does the problem statement already contain a solution?
3. What is missing to start testing the hypotheses?

Record the answers here.

## Changes v1.0 → v1.1 (FPF C.22.2)

- Block "Next use" added to both templates and all examples.
- Claim family marked in block 1 (actual / anticipated / solvability).
- Rule "fill only what changes the next use"; hypotheses and options kept as short cues.
- B-1 narrowed to one subject (funding 2027, anticipated condition); solution-shaped request moved to the signal; "value not shown" kept as a rival formulation; capacity gap moved to a reference to B-2.
