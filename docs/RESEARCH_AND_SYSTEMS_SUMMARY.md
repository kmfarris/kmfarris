# Kelly Farris — technical summary

[github.com/kmfarris](https://github.com/kmfarris)

---

## customLLM / PRCF

Positioned residual codes and bucket+slot packing define an invertible word-level alphabet; CodeBPE merges adjacent code ids (never through escape tokens). On full WikiText-2, a six-layer 384-d LM trained on that alphabet reaches train BPC **1.76** vs **1.88** for text BPE at the same width, train packing **0.227** vs **0.240** sym/char, invertibility **1.00**, ±2 edit locality **1.00** in codec index space. The direction-3 scale ladder missed coarseness gates at an intermediate slice; those numbers stay in the repo.

[`experiments/working_lm/results.json`](https://github.com/kmfarris/customLLM/blob/main/experiments/working_lm/results.json) · [`docs/SCOPE_AND_LIMITS.md`](https://github.com/kmfarris/customLLM/blob/main/docs/SCOPE_AND_LIMITS.md)

---

## IMOL

Programs are parsed and diagnosed before patches or tool invokes land on disk. Patches target declaration `@id`s; fmt output is the IR. `imol agent workshop-plan` dry-runs plan invokes under workshop caps; execution requires explicit approval. Agent stdout JSON remains at spec **0.4** while the language surface evolves (**0.5** shell/async preview).

`npm run check` on a clean clone · [`docs/DESIGN.md`](https://github.com/kmfarris/imol/blob/main/docs/DESIGN.md)

---

## scatterbrain-steering

Track C: each decode step runs the GRU, polls executive state, adds `α · bias` to logits. Conscience curriculum data was built with a fail-closed teacher boundary; smoke training has not passed every release gate. Influence ablations and the trajectory manifest are the stable deliverables.

[`docs/STEERING.md`](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md)

---

Issues and PRs on the repositories above.
