---
type: project-approach
project: Data Quality System Usefulness Evaluation
created: 2026-08-10
method: FPF (fpf.sh) — C.11 Decision Theory, C.28 CausalUse-CAL, C.16 Measurement & Metrics
status: in progress
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

**Implication for step 4 (preview):** this evidence picture makes Option B
(full rollout) the hardest to honestly defend to leadership right now — no
measured support for any claimed benefit at that scale. It makes Option C
(phased rollout) the natural "probe again" answer: a measured start in 1-2
high-pain domains is the cheap next probe that could turn these anecdotes
into real `interventionalActionSupportBasis` evidence before asking for the
full commitment.

Next: Step 3 — build the actual comparison basis (C.16): list measurable
characteristics, current baseline, expected change per option.
