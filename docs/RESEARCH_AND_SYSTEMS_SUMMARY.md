# Research and systems summary

**Kelly Farris** · [github.com/kmfarris](https://github.com/kmfarris)

---

## customLLM / PRCF

**Question:** If text is represented as positioned residual codes rather than spelling-BPE pieces, do edit locality and invertibility improve—and can a matched small LM prefer that alphabet?

**Result (WikiText-2, 6L/384d):** Bucket+slot injective in-vocab coding with CodeBPE merges yields train BPC **1.76** vs text BPE **1.88** (ratio **0.94**), train packing **0.227** vs **0.240** sym/char, invertibility **1.00**, ±2 locality **1.00** in codec index space. Direction 3 scale ladder failed coarseness gates; documented in repo.

**Artifact:** [`experiments/working_lm/results.json`](https://github.com/kmfarris/customLLM/blob/main/experiments/working_lm/results.json)

**Scope note:** [`docs/SCOPE_AND_LIMITS.md`](https://github.com/kmfarris/customLLM/blob/main/docs/SCOPE_AND_LIMITS.md)

---

## IMOL

**Question:** How should agents edit programs without corrupting structure or firing tools on invalid IR?

**Mechanism:** ID-keyed patches, JSON oracle (`imol agent check`), in-memory patch re-check, workshop dry-run trace before approval. MCP tools for the same contracts.

**Verify:** `npm run check` on clone.

**Design:** [`docs/DESIGN.md`](https://github.com/kmfarris/imol/blob/main/docs/DESIGN.md)

---

## scatterbrain-steering

**Question:** Can executive state steer a persistent decoder without replacing LM memory?

**Mechanism:** `ExecutivePoller` → `InfluenceSignal` → residual logit bias; conscience curriculum with fail-closed teacher; pytest + release gate harness.

**Status:** Smoke LM training has not cleared all release gates; dataset and influence ablation are the portable contribution.

**Architecture:** [`docs/STEERING.md`](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md)

---

## Contact

Repositories above; issues and PRs welcome on each project.
