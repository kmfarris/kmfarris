# Kelly Farris — technical summary

[github.com/kmfarris](https://github.com/kmfarris)

---

## customLLM / PRCF

**Problem:** Subword tokenization optimizes spelling fragments; edits are often non-local in id space, and swapping an entity may require retokenizing the whole span.

**Approach:** Positioned codes per word, bucket+slot packing with lossless escape for OOV, CodeBPE merges adjacent code ids, then train matched LMs on text BPE vs CodeBPE alphabets.

**Status:** Full WikiText-2 working run recorded—train BPC **1.76** vs **1.88**, packing **0.227** vs **0.240** sym/char, invertibility and ±2 locality **1.00** in codec index space. Direction 3 missed coarseness gates. WikiText-2 scale only; see [`SCOPE_AND_LIMITS.md`](https://github.com/kmfarris/customLLM/blob/main/docs/SCOPE_AND_LIMITS.md).

[`results.json`](https://github.com/kmfarris/customLLM/blob/main/experiments/working_lm/results.json)

---

## IMOL

**Problem:** LLM agents patch and invoke tools against source that may not parse; line-based diffs drift after fmt.

**Approach:** IMOL modules with `@id` declarations, fmt as IR, JSON agent oracles, workshop dry-run traces, MCP skill codebook for closed-model hosts.

**Status:** Toolchain ships; **`npm run check`** passes. Language **0.5** (shell, async preview); agent stdout **0.4**. [`DESIGN.md`](https://github.com/kmfarris/imol/blob/main/docs/DESIGN.md)

---

## scatterbrain-steering

**Problem:** Turn-level plans and affect should steer an open-vocabulary decoder without resetting memory each token.

**Approach:** GRU articulator + `ExecutivePoller` → `InfluenceSignal` → residual logit bias; conscience curriculum with local teacher fail-closed validation.

**Status:** **15** pytest tests pass; curriculum v1 artifact with **39** approved trajectories; articulator release gates failed on smoke training (fluency / repetition). Not default speech in Scatterbrain. [`STEERING.md`](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md) · [`SPEECH_STATUS.md`](https://github.com/kmfarris/scatterbrain-steering/blob/main/SPEECH_STATUS.md)

---

Issues and PRs welcome on each repository.
