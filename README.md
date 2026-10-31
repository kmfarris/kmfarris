# Kelly Farris

### [customLLM](https://github.com/kmfarris/customLLM) — token streams that stay local when text edits

Spelling-BPE churns tokens when you change a single word. customLLM implements **PRCF**: word-aligned codes, injective bucket+slot ids for in-vocabulary items, CodeBPE merges on code sequences, and matched small LMs on WikiText-2. The working-scale run is in the tree—CodeBPE beats text BPE on train BPC under a shared 6-layer body; direction 3’s coarseness ladder failed at an intermediate slice, and that failure is logged beside the passes.

`pip install -e '.[dev]' && python -m pytest tests/` · [blog](docs/blog/prcf-wikitext2-results.md)

### [IMOL](https://github.com/kmfarris/imol) — parse before patch, trace before side effects

Agent-authored programs need the same discipline as human ones: valid IR, stable patch targets, tool invokes you can dry-run. IMOL is the language, checker, workshop runtime, and MCP oracles (`check`, id-keyed `patch`, `workshop-plan`). Language surface is at spec 0.5; agent JSON remains 0.4 for integrators. **`npm run check`** on a clean clone is the bar.

[blog](docs/blog/imol-check-patch-workshop.md) · [DESIGN](https://github.com/kmfarris/imol/blob/main/docs/DESIGN.md)

### [scatterbrain-steering](https://github.com/kmfarris/scatterbrain-steering) — executive bias on a persistent decoder

Track C does not throw away LM memory—it adds a per-token executive poll that biases logits while a GRU carries state across the reply. Conscience curriculum data and fail-closed teacher boundaries ship with the code; smoke LM training has **not** cleared fluency release gates, so this remains research infrastructure with tests green, production flag off in the parent project.

`pip install -r requirements-dev.txt && PYTHONPATH=. python -m pytest tests/ -q` · [STEERING](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md)

---

Longer write-ups: [technical summary](docs/RESEARCH_AND_SYSTEMS_SUMMARY.md)
