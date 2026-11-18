---
type: templates
date: 2026-11-18
course: R4.2:4, R4.2:Tasks1
status: v1.0
---

# Problem card templates for the DG/DQ team

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/02-problem-formulation-epistemology-and-problem-solving/07-creating-and-structuring-the-problem-card.md`; card blocks from R4.2:4 (commit faed795, 2026-11-04).

**Principle (R4.2:4):** do not mix context, signal, problem statement, causes and solution options; keep several hypotheses and several intervention options open. A solution written into the problem statement ("the problem is that we have no rule X") closes other explanations and options too early.

Two templates for two problem classes:
- **A - data quality problems reported by data consumers;**
- **B - problems of developing the DG/DQ product** (funding, priorities, demand vs team capacity). B adds the field "who decides and with which authority", because budget and headcount decisions are outside the team.

---

## Template A. Data quality problem card

**Header:** number, date, card author, **who reported the signal** (role, unit). Signals are recorded per agent: the same signal can point to different problems for different consumers.

| # | Block | How to fill in |
|---|---|---|
| 1 | Problem statement | What is wrong with the data and for whom, one sentence. **No cause, no solution.** Wrong: "no DQ rule for GTIN". Right: "some new products have no GTIN when product data is sent to retailers". |
| 2 | Subject and context | Data domain and dataset; data elements as system.table.field; systems on the data path from source to consumer (lineage if available); period and population of records. Do not pick "the main thing" yet. |
| 3 | Established state of affairs (signal) | What was observed - count and share of records with the deviation, with unit and date; which method - DQ rule run, profiling, cross-system reconciliation, user report; who recorded it and where, with links to evidence. No "often" or "always" without numbers. |
| 4 | For whom and how it is unfavourable | Which expectation is broken (business definition, rule threshold, deadline); which consumer processes or reports are affected. **Breach and damage are separate lines.** Unknown damage is "not established", not "none" and not "lost revenue". |
| 5 | Important unknowns | Questions whose answer would change the understanding: is there an agreed definition or rule for the element; since when; all sources or one; all records or a class. Each question linked to the hypothesis or option that depends on it. |
| 6 | Hypotheses on causes (not tested) | **Several** hypotheses, each with how to test it. |
| 7 | Intervention options (not chosen) | Several options, each linked to a hypothesis. |
| 8 | Sign of improvement | Observable sign in the data and at the consumer, with threshold and observation window (e.g. trend of failed records of the rule). |

### Example A-1. Missing GTIN for new products (real case)

1. **Problem:** some new products have no GTIN when product data is sent to retailers.
2. **Subject and context:** product master data, domain "product". Data element: GTIN in the product record in ERP. Data path: PLM → ERP → product data transfer to retailers. Products created in the last 3 months.
3. **Signal:** at the pre-transfer check, 300 of 1,200 new products (25 %) had an empty GTIN (01.11). Method: GTIN completeness rule run in the DQ module. Recorded by the data steward of the product domain; link to the run result.
4. **For whom unfavourable:** for the team sending data to retailers - the transfer of these products is delayed (breach of the transfer deadline). Damage: not established - unknown whether product launches on shelves moved.
5. **Unknowns:** at which step is the GTIN assigned - PLM or ERP? Is the field mandatory at creation? Do the 300 belong to one category or brand? Do they have a GTIN in PLM?
6. **Hypotheses:** a) GTIN is not mandatory at creation in ERP - test: form settings and fill dates; b) GTIN exists in PLM but is not carried over by the integration - test: PLM vs ERP reconciliation for the 300 products; c) GTIN is assigned later by process and the check runs too early - test: the assignment procedure.
7. **Options:** for (a) make the field mandatory; for (b) fix field mapping in the integration; for (c) move the check point or the transfer deadline.
8. **Sign of improvement:** number of new products without GTIN at transfer = 0 for 4 consecutive weeks on the rule trend; no transfer delays for this reason.

---

## Template B. DG/DQ product development problem card

**Header:** number, date, author, **who reported the signal** (role), **decision level**: team / DG lead / finance and senior management.

| # | Block | How to fill in |
|---|---|---|
| 1 | Problem statement | What is unfavourable and for whom. **No chosen solution.** Wrong: "prepare a funding request", "hire an analyst". Right: "catalog development in 2027 may remain unfunded". |
| 2 | Subject and context | Product or module (Data Catalog, Lineage, DQ); period (budget cycle, quarter); requesters and dependent projects; current resources (people, budget, licences). |
| 3 | Established state of affairs (signal) | Facts with source - tracker, budget procedure, letter, decision; numbers with units and dates. |
| 4 | For whom and how it is unfavourable | Which commitments or expectations are broken or at risk (project deadlines, agreements with requesters). **Breach and damage separately.** |
| 5 | Who decides and with which authority | Roles (R4.1:Mod1): administrator (budget, headcount), strategist (direction), requester (project), approvers. What is within the team's authority and what is not. |
| 6 | Important unknowns | Questions linked to hypotheses and options. |
| 7 | Hypotheses on causes (not tested) | Several, each with how to test it. |
| 8 | Intervention options (not chosen) | Several, each with **whose authority** it needs. |
| 9 | Sign of improvement | An **observed effect**, not performed work. "Request submitted" is work; "projects A and B receive results on time" is an effect. |

### Example B-1. Funding of data catalog development for 2027

**Header:** reported by the product manager; decision level: finance and senior management.

1. **Problem (candidates, not chosen yet):** a) data catalog development in 2027 may remain unfunded or underfunded; b) the value of the catalog is not shown in the terms used for budget decisions; c) the current team capacity does not cover demand (case arrivals ~4× throughput, projects A and B wait for work products).
2. **Subject and context:** company budget cycle for 2027; data catalog (Data Catalog, Data Lineage), 2 engineers; requesters - projects A and B, data consumers.
3. **Signal:** the 2027 budget cycle has started (funding is decided per cycle). From R4.1: ~11 cases arrive per month, 2-3 are closed, ~100 open; ~10 % of engineers' time goes to cases.
4. **For whom unfavourable:** if unfunded or underfunded - for projects A and B a delay of their results if they need catalog functions; for data consumers the case queue keeps growing. **Damage not established:** unknown what exactly A and B would miss and when.
5. **Who decides:** the request is prepared by the product manager (team authority); first decision - DG lead (administrator: budget and headcount); **approval - the CFO and the D&A lead** (DG lead's manager). Projects A and B are requesters: they do not manage the catalog budget but can support the request or co-fund.
6. **Unknowns:** submission deadline in the budget cycle; what "catalog development 2027" includes (licences, people, new source integrations, functions for A and B); which 2026 results can be shown as an **observed effect**, not as performed work (#workitems: work ≠ result ≠ effect); competition for the same budget inside D&A.
7. **Hypotheses:** a) funding is reviewed each cycle and is not extended without a request - test: budget procedure; b) catalog value is not measured, so the request is hard to justify - test: availability of usage and effect metrics; c) demand grows faster than capacity - test: tracker data (R4.1).
8. **Options (with authority):** funding request - team prepares, DG lead decides, CFO and D&A lead approve; reprioritisation within the DG budget - DG lead; co-funding by projects A and B - project leads; narrowing the scope to what A and B need - team with DG lead; collect effect metrics first - team.
9. **Sign of improvement:** 2027 funding approved by the CFO and the D&A lead for the agreed scope; projects A and B receive catalog results on time.

### Example B-2. The case queue keeps growing

1. **Problem:** requests to the DG/DQ team wait for months and the queue keeps growing.
2. **Subject and context:** the team's case flow (consultations, management questions, new functions, development). Team: product manager (triage), 2 engineers DQ, 2 engineers Catalog/Lineage. ~10 % of engineers' time goes to cases.
3. **Signal:** 100 open cases; 9-13 arrive per month, 2-3 are closed (tracker, 13.11). All 10 oldest cases wait for resources (sample, 13.11).
4. **For whom unfavourable:** requesters wait for months; deadlines of the work products for projects A and B are at risk. **Damage not established:** unknown whether requesters work around the team and whether A and B deadlines slipped.
5. **Who decides:** triage and flow rules - product manager (team authority); engineers' time for cases and headcount - DG lead; urgent questions come from management - outside the team's authority.
6. **Unknowns:** how many of the 100 cases are actually solved or no longer relevant; share by class; number of interruptions by urgent questions per month.
7. **Hypotheses:** a) triage is done ad hoc and became the constraint - test: time in queue before triage; b) engineer capacity is insufficient regardless of triage - test: throughput after regular triage; c) interruptions by urgent questions eat the time - test: work episodes per case.
8. **Options (with authority):** weekly triage slot and intake template - product manager; duty rotation in engineering pairs - team; more engineer time for cases - DG lead; explicit "not now" for part of the cases - product manager with requesters.
9. **Sign of improvement:** cases closed per month ≥ cases arrived, 3 months in a row; the number of open cases does not grow.

---

## Colleague review (task item 3) - to do

Give one card of each type to a steward or engineer and ask:
1. Is it clear *what* the problem is without verbal explanations?
2. Does the problem statement already contain a solution?
3. What is missing to start testing the hypotheses?

Record the answers here.
