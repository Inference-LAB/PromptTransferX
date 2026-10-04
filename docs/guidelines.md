# Seven Evidence-Based Design Guidelines

These guidelines are derived directly from the empirical findings of PromptTransferX.
Each guideline is quantitatively grounded; the supporting data are in the `results/` directory.

---

## G1 — Anchor on explicit structure

**Recommendation:** Prefer specifications that encode behavioral intent through explicit
structural constraints: ordered step sequences, fill-in-the-blank templates, format
prescriptions, section labels.

**Evidence:** Class I specifications (PSI < 0.15) achieve Π ≥ 0.75 across all six
tested backends. Structural specifications achieve mean portability 0.726 vs. 0.432
for Pragmatic/mixed (r = 0.62, p < 0.01).

---

## G2 — Build on Class I structural cores

**Recommendation:** Build composite specifications using Class I patterns
(P05, P15, P18, P23) as the structural backbone, layering Class II specifications
for task-specific enhancement.

**Evidence:** Class I Transfer ≥ 0.75 on all models; stable cross-generationally
(Claude Opus 4.6 and Qwen3-14B, Aug 2026).

---

## G3 — Validate on the weakest model first

**Recommendation:** A specification achieving PTS ≥ 0.65 on Mistral-7B achieves
PTS ≥ 0.73 on frontier models in 94% of evaluated cases. Use PSI > 0.30 as a
deployment-risk flag.

**Evidence:** Mean Mistral-7B PTS = 0.627; mean GPT-4o PTS = 0.793. Cross-tier
correlation justifies using the weakest open-weight model as a lower bound.

---

## G4 — Account for the Claude-family behavioral fingerprint

**Recommendation:** When deploying on Claude-family models, anticipate systematic
behavioral differences on constraint-adjacent specifications (P07, P10, P11, P21).
Task-specific system prompts partially mitigate the fingerprint (+0.05 PTS for P21).
Class I structural equivalents are the more reliable alternative.

**Evidence:** P11 Claude PTS = 0.12 vs. Mistral-7B = 0.72 (Z = 6.84, p < 0.001,
r = 0.87). Fingerprint confirmed by all three judges. Persists across system prompt
conditions. Intensifies in Claude Opus 4.6 (PTS = 0.09).

---

## G5 — Validate per task category

**Recommendation:** Creative Writing (mean Transfer = 0.588) and Hallucination
Resistance (0.611) show substantially lower portability than Mathematical Reasoning
(0.741) and Instruction Following (0.752). Aggregate portability scores do not
substitute for task-specific validation.

**Evidence:** Task-category Transfer range = 0.588–0.752 (delta = 0.164). See
`results/task_category_transfer.csv`.

---

## G6 — Report paraphrastic variance

**Recommendation:** Report mean PTS across at least three paraphrastic variants.
Phrasing variation accounts for 22.7% of PTS variance (partial η² = 0.227).
Reporting only the best phrasing may inflate transferability claims by this margin.

**Evidence:** Two-way mixed ANOVA: phrasing variation partial η² = 0.227.
Mistral-7B shows 34.2% phrasing-attributable variance vs. 15.8% for GPT-4o
(Levene's F = 8.34, p < 0.001).

---

## G7 — Annotate with volatility class and recalibrate PSI

**Recommendation:** For each new specification, assign a volatility class (I–IV)
based on Transfer evaluated across at least three heterogeneous backends. Recalibrate
PSI thresholds against the contemporaneous weakest general-purpose open-weight model
as the landscape evolves.

**Evidence:** Qwen3-14B (2026) achieves mean PTS = 0.681 on Mathematical Reasoning
vs. Mistral-7B = 0.627, indicating that the proprietary-open gap is narrowing.
PSI thresholds calibrated on Mistral-7B may need revision as 14B+ open-weight models
become the weak-tier baseline.
