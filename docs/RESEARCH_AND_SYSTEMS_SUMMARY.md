# Kelly Farris — technical summary

[github.com/kmfarris](https://github.com/kmfarris)

---

## customLLM / PRCF

**Purpose.** Cut English into word-aligned codes (not spelling fragments), keep edits local, decode without collisions, and see whether a small language model trained on those codes can match or beat the usual tokenizer (BPE) when the model body is the same.

**What works.** Full WikiText-2, six-layer 384-wide models: train BPC **1.76** vs **1.88**, train packing **0.227** vs **0.240** symbols per character, invertibility **1.00**, ±2 locality **1.00**.

**What still needs work.** Validation packing is looser than train. Merges are still near word length. Direction 3 missed coarseness gates. SentencePiece on the same split and anything larger than WikiText-2 are not measured yet.

[`results.json`](https://github.com/kmfarris/customLLM/blob/main/experiments/working_lm/results.json) · [`SCOPE_AND_LIMITS.md`](https://github.com/kmfarris/customLLM/blob/main/docs/SCOPE_AND_LIMITS.md)

---

## IMOL

**Purpose.** Give coding agents a language they can typecheck and a runtime they can dry-run: parse first, patch by stable ids, preview tool calls, then approve writes and network.

**What works.** Parser, checker, formatter, patcher, workshop, CLI, and MCP oracles ship. **`npm run check`** passes on a clean clone.

**What still needs work.** Language spec 0.5 vs agent JSON 0.4 should migrate together. Formal semantics and npm publish are unfinished.

[`DESIGN.md`](https://github.com/kmfarris/imol/blob/main/docs/DESIGN.md)

---

## scatterbrain-steering

**Purpose.** Keep a decoder’s memory of the sentence while a separate executive signal nudges each next word (plan, guidance, chemical levels). Measure that steering with tests, ablations, and a teacher-built curriculum.

**What works.** Fifteen tests pass. Curriculum v1 has 39 approved trajectories; failed lessons are kept. Influence changes scores in ablation.

**What still needs work.** Smoke-trained decoder failed fluency and coverage gates. The poller is designed, not trained on the curriculum. Track C is off by default in Scatterbrain.

[`STEERING.md`](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md) · [`SPEECH_STATUS.md`](https://github.com/kmfarris/scatterbrain-steering/blob/main/SPEECH_STATUS.md)
