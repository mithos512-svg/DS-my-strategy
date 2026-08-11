---
type: project-approach
project: Data Quality System Usefulness Evaluation
created: 2026-08-10
method: FPF (fpf.sh) — C.11 Decision Theory, C.28 CausalUse-CAL, C.16 Measurement & Metrics
status: complete (5/5 steps)
---

# Approach: Evaluating the Usefulness of Implementing a Data Quality System — via FPF

Checked against the official FPF spec (fpf.sh), not the seminar-simplified
version, per repo rule 19 (day-rhythm-config.md). Core patterns used:
C.11 Decision Theory (Decsn-CAL), C.28 CausalUse-CAL, C.16 Measurement &
Metrics Characterization (MM-CHR), lightly A.19.ECS (Evaluation
CharacteristicSpace Construction) and E.9 (Design-Rationale Record) for the
closing write-up.

## Why not a plain ROI calculator

A vague "is it useful" question almost always secretly *is* a causal claim
("the DQ system will reduce cost/risk/rework") stapled onto an undefined
option set. FPF forces both pieces to be typed explicitly before any
conclusion is drawn — this is exactly what protects the final pitch from
being shredded in exec review.

## The 5 steps

1. **Frame as a C.11 decision.** Name the `DecisionSubject` explicitly (who
   is actually choosing, at what granularity), and freeze the actual
   `OptionSet` on the table now. If the option set itself is still unclear,
   that's C.18 (option generation) — an earlier, different question.

2. **C.28 causal triage on every benefit claim.** For each claimed benefit,
   state: causality-ladder rung (association / intervention / counterfactual)
   + support basis + supported use + unsupported use. One line each. This is
   what stops "this will save us $X" claims that can't survive scrutiny.

3. **Build the comparison basis honestly (C.16 lens).** List what's actually
   measurable now, state current baseline vs. expected change per option,
   mark clearly what's measured vs. assumed.

4. **Run the C.11 choice procedure.** State OptionSet + comparison basis +
   belief state + outcome model. Probe-worthiness check: is there a cheap
   next probe (e.g. short pilot) that could still flip the ranking before
   committing real budget? Emit one of: choose now / reject current set /
   probe again / reroute.

5. **Close with a short decision-rationale record** — decision, comparison
   basis, causal-use boundary stated honestly, next concrete action.

## Working session log

### 2026-08-10 — session 1

**Step 1 — C.11 framing:**

- `DecisionSubject`: leadership (org-level) — user's role is not the chooser,
  but the case-builder feeding leadership's C.11 process. "Done" for this
  work = a comparison basis leadership can trust, not a `ChoiceResult` itself.
- Context: DQ platform is already purchased (not build-vs-buy). Partial
  tooling already exists. Question in front of leadership is enterprise-wide
  extension across many domains.
- `OptionSet` (frozen, confirmed by user):

  | Option | Description |
  |---|---|
  | A — Status quo | Keep current partial tooling, no further extension |
  | B — Full enterprise-wide rollout | Extend across all domains now |
  | C — Phased rollout | Start with highest-pain domains, expand on evidence |
  | D — Targeted extension | Only extend into domains with a clear, already-visible problem |

**Step 2 — C.28 causal triage:**

Four benefit claims floated: (1) reduced downstream incidents/rework,
(2) time saved on manual reconciliation, (3) faster/more trusted reporting &
decisions, (4) audit/compliance risk reduction. Strongest current evidence
for all four: **anecdotal only, no systematic measurement.**

| Claim | Support basis | Supported use | Unsupported use |
|---|---|---|---|
| Reduced downstream incidents/rework | missing | state as hypothesis, motivates a measured pilot | any "$X saved" / "Y% fewer incidents" number |
| Time saved on manual reconciliation | missing | same | quantified hours-saved claim |
| Faster/more trusted reporting & decisions | missing | same | causal "decisions got faster" claim |
| Audit/compliance risk reduction | missing | same | "risk reduced by X%" claim |

None of the four claims clear even `observationalAssociationSupportBasis` —
anecdote without systematic observation is `missing` support basis in C.28
terms.

**Step 3 — comparison basis (C.16):**

| Characteristic | Current baseline | Status |
|---|---|---|
| Data incidents/rework | unknown | not trackable at all — no log exists |
| Manual reconciliation hours/week | unknown | no formal tracking, but estimable |
| Reporting/decision trust | unknown | no formal tracking, but estimable |
| Audit findings tied to data quality | known | **tracked** — real measured baseline exists |

Only one of four characteristics (audit/compliance) currently has real
tracked data. The other three are estimate-based hypotheses, not
measurements — must be labeled as assumptions in the case, matching the step
2 triage (their support basis is `missing`).

**Strategic implication for step 4:** the honest next move is likely not
"run a pilot and measure results" but **"first stand up baseline tracking"**
(incident log, reconciliation-time estimate method, a simple trust signal)
in whatever domain gets chosen for phased rollout — otherwise there's no
"before" to compare "after" against, and the C.28 triage stays `missing`
indefinitely. Audit/compliance is the one domain where a credible measured
before/after is possible right now.

**Step 4 — C.11 choice procedure:**

Probe-worthiness check: is there a cheap next step that could still flip
which option leadership should pick, before committing real budget? **Yes** —
a bounded, measured start in 1-2 domains generates real
`interventionalActionSupportBasis` evidence that no further analysis of
existing anecdotes can produce.

This eliminates two options:
- **Option B (full rollout)** — cannot be honestly defended now; no measured
  support for any benefit claim at that scale.
- **Option A (status quo)** — addresses nothing, generates no new evidence.

`ChoiceResult` = **probe again**, where the probe *is* Option C's phase 1
(not a throwaway pilot). C vs. D fork resolved in favor of **C**: the org
already purchased an enterprise-wide platform (signals real ambition beyond
patching visible problems), so phase 1 should be explicitly framed as a
stepping stone, conditional on what it measures — not a permanent, bounded
fix (which is what D would imply).

**Phase-1 probe domains (user-identified, highest pain):** Planning and
Master Data.

**Step 5 — closing decision-rationale record:**

- **Decision:** recommend Option C (phased rollout) to leadership, with
  Phase 1 scoped to Planning and Master Data domains.
- **Framing for leadership:** Phase 1 does double duty — it fixes known pain
  in the two highest-pain domains AND generates the missing baseline/measured
  evidence needed to justify (or rule out) further expansion. This is not
  "here's the ROI of full rollout" — it's "here's a bounded bet that tells us
  whether the bigger bet is worth making."
- **Causal-use boundary (per step 2):** all four benefit claims stay `missing`
  support basis until Phase 1 produces real before/after numbers. The case
  must present benefits as hypotheses to be tested, not proven savings —
  anything else oversells evidence that doesn't exist yet.
- **Comparison basis gap to close first (per step 3):** audit/compliance is
  the only domain with a pre-existing measured baseline. Before or alongside
  rollout in Planning/Master Data, baseline tracking must be stood up there
  too (an incident log, a reconciliation-time estimate method, a simple trust
  signal) — otherwise Phase 1 ends with the same `missing` evidence problem
  it was supposed to solve.
- **Next concrete actions:**
  1. Stand up baseline tracking in Planning and Master Data (incident log,
     reconciliation-time method, trust signal).
  2. Define Phase 1 success metrics and a fixed duration/review point.
  3. Take this framing to leadership — ask for a bounded Phase 1 budget,
     explicitly not a full-rollout budget, with the evidence question as
     the deliverable, not just the fix.

**Status: approach complete (all 5 steps).** This is a working case-builder
document, not the final leadership pitch — next natural step (separate task)
would be turning this into the actual presentation/write-up for leadership.
