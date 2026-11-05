# Catalog item approval-readiness checklist - v0.1

**Status:** draft v0.1, 2026-10-18. Built with the R2.6:3 method (case → role
→ ontology of objects of attention → states → actions → control questions),
in the R2.6:2 form "method subject - target state" (as in an aviation
checklist: "covers - removed"), based on FPF `A.15.PROD` (three production
questions) and `E.24.PUB` (publication as a separate event). Source of the
states - `journey-catalogued-dataset.md` v0.3.

**What it closes:** node 8 of the journey model (approval workflow) - the place
where work most often turns into "returned for rework" cycles. The checklist replaces
email threads: the steward checks before submitting, the approver checks against the same
rows.

---

## 1. Case, roles, where it lives

| Parameter | Value |
|---|---|
| **Case / scenario** | Submitting a catalog item about a dataset for approval in the DG/DQ system and its review by the approver |
| **Performer role** (fills in) | Data Steward - before clicking "Submit for approval" |
| **Reviewer role** (checks) | Approver (Data Governance Lead) - during review |
| **Journeying object** | Catalog item about dataset X (episteme); the dataset is the referent |
| **Target state after the case** | Item "approved"; then automatically "published" (self-service; once MCP launches, also to agents) |
| **Where the checklist lives** (R2.6:3: in the performer's operational exocortex) | Option A: custom attributes / checklist field in the item card in DG/DQ (0 clicks). Option B: template in SharePoint `IWE-Work/memory/Checklists/`, linked from the workflow step description. Not in a separate "control system" |
| **Regulation** (separate from the checklist, R2.6:3) | The team's cataloguing instruction - the checklist refers to it, does not repeat it |

## 2. Ontology: objects of attention

Major objects and next-level objects (R2.6:3):

- **Catalog item** → description, classification/terms, owner, DQ rules, lineage link, workflow status
- **Dataset (referent)** → physical asset in the source, access, schema
- **Owner** → role, person, confirmation
- **Quality rules** → rule set, run result
- **Publication audience** → self-service, (MCP), access rights
- **Approver** → approver, completeness checklist, decision

## 3. Checklist in classes (template)

Form "subject - target state", mark "yes / no / n/a". The groups
correspond to the three A.15.PROD questions plus E.24.PUB publication.

### Block A. Cataloguing work done part by part (A.15.PROD, question 1: which work)

| # | Method subject | Target state | How we know (event) | Yes/No/n/a |
|---|---|---|---|---|
| A1 | Referent dataset | exists and is accessible in the source | source scan successful, schema read | |
| A2 | Item metadata | imported and current | date of last scan ≤ team threshold (e.g., 30 days) | |
| A3 | Data profile | built | profiling job finished, statistics in the card | |
| A4 | Item description | written by a human, not auto-generated | Description field not empty, differs from the technical name | |
| A5 | Glossary terms / classification | assigned | ≥1 business term linked, classification selected | |
| A6 | Quality rules | bound, first run exists | ≥1 DQ rule, run result visible | |
| A7 | Lineage link | created (non-blocking) | upstream/downstream visible **or** explicit mark "lineage: n/a" | n/a allowed |

### Block B. Entity defined (A.15.PROD, question 2: when it exists)

| # | Method subject | Target state | How we know | Yes/No |
|---|---|---|---|---|
| B1 | Identity rule "catalogued dataset" | applied to this item | steward confirms: the item claims the state "published to all audiences", not "is in the catalog" | |
| B2 | Item ↔ physical asset link | unambiguous | one asset, one ID, no duplicate candidates for the same asset | |
| B3 | Owner | assigned **and confirmed** | Owner field filled + confirmation exists (not just assignment) | |

### Block C. Completion criterion and work closure (A.15.PROD, question 3)

| # | Method subject | Target state | How we know | Yes/No |
|---|---|---|---|---|
| C1 | Checklist (this one) | fully filled in by the steward | all rows A-D marked, "no" with a comment | |
| C2 | Returns from previous cycles | closed | every "returned" in workflow history has an answer | |
| C3 | Approver's decision | made against the checklist, not via email | approver marks the same rows; a discrepancy = a row, not an email | |

### Block D. Publication (E.24.PUB: availability to the audience is a separate event)

| # | Method subject | Target state | How we know | Yes/No |
|---|---|---|---|---|
| D1 | Item access rights | set for the target audience | self-service group sees the item in preview/test | |
| D2 | Publication form | defined | self-service; once MCP launches - marked whether exposed to agents | |
| D3 | Sensitive data | classified before publication | PII/confidentiality marked, access agreed | |

## 4. Legend (R2.6:3: a checklist without a legend does not work)

- **Yes** - state reached, the event is observable in the system.
- **No** - not reached; a comment "what blocks it" is mandatory - it
  becomes a "work cycle" row in the records (R2.6:7).
- **n/a** - not applicable for this dataset (allowed only for A7 and D2;
  for the rest "n/a" = "no").
- **Submit for approval is allowed** when blocks A-C have no "no" and block D
  has no "no" on D1 and D3.
- The approver marks the same rows; a discrepancy on a row is the **only**
  acceptable reason for a return. A return without a row reference signals that
  the checklist is incomplete: add a row, do not write an email.

## 5. Instance for a specific object (R2.6:2: the checklist is printed per individual)

```
Approval-readiness checklist
Item: ______________________ (ID ____)  Referent dataset: ______________
Domain: ______________  Steward: ______________  Submission date: __________
Approver: ______________  Decision date: __________  Cycle #: ____

A1 [ ]  A2 [ ]  A3 [ ]  A4 [ ]  A5 [ ]  A6 [ ]  A7 [ ] / n/a
B1 [ ]  B2 [ ]  B3 [ ]
C1 [ ]  C2 [ ]  C3 [ ]
D1 [ ]  D2 [ ]  D3 [ ]
Comments on "no": _________________________________________________
Decision: approved / returned (rows: ____)
```

First instance - product catalog (roadmap Phase 1): fill in at the
next submission for approval; this will be the first cycle measurement.

## 6. What to measure with the checklist (R2.6:4)

| Metric | Source | Why |
|---|---|---|
| Share of items approved in the 1st cycle | "Cycle #" in instances | does the checklist work |
| Most frequent rows with "no" | comments on "no" | where the method, not the performer, is the issue |
| Returns without a row reference | approver's decisions | checklist completeness |

## 7. Rollout (R2.6:3)

1. Discuss with the team (stewards + approver) - 30 min; the checklist will change,
   that is normal.
2. Put it where it is filled in: the item card or the workflow step, not
   a separate file "somewhere".
3. Run it 5-7 times on real items before considering it rolled out;
   more reminders are needed than it seems.
4. Fill-in control - in the manager's schedule (Week Close).

## 8. Open questions

1. Does the DG/DQ system allow adding the checklist as card attributes (option A) - or only SharePoint (option B)?
2. Metadata currency threshold in A2 - 30 days or other?
3. Is a row on the quality SLA needed (DQ SLA, roadmap 2.4) - not included now, too early.

---

Sources: R2.6:2 "Checklists and changes of object states", R2.6:3 "Checklists
as a way to hold attention" (docs-courses, `professional/modeling-1/06-...`);
FPF Library `A.15.PROD` (https://fpf.tools/A.15.PROD), `E.24.PUB`
(https://fpf.tools/E.24.PUB:4), snapshot 20261015T182921Z-219aa77d287d7d2d;
`journey-catalogued-dataset.md` v0.3. Created: 2026-10-18. Translated to English: 2026-11-05 (content unchanged).
