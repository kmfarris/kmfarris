# PRCF on WikiText-2: when the alphabet changes, the LM follows

Standard subword tokenizers optimize for spelling frequency. PRCF asks a different question: if each word (and escape path) maps to positioned codes with invertible decode, do edits stay local—and does a small language model trained on merged *codes* behave differently from one trained on merged *characters*?

The working-scale bake-off on full WikiText-2 is in `results.json`; metric scope is in the repo evaluation note.

## The pipeline

Words in vocabulary receive injective bucket+slot ids. Out-of-vocabulary material routes through escape and character paths—lossless, but not free at the symbol level. CodeBPE merges adjacent code ids (never through escape), producing a second alphabet the LM sees. A six-layer, 384-dimensional body trains twice: once on text BPE, once on CodeBPE, with matched optimization budget.

## What moved

**Packing.** Train symbols-per-character tightened relative to text BPE (0.227 vs 0.240 in the working run). Validation remains looser than train—held-out text still pays escape tax. Report both.

**Bits per character.** Train BPC favored CodeBPE (1.76 vs 1.88). That is not SOTA perplexity; it is a matched-body comparison between alphabets on the same split.

**Locality and invertibility.** Single-word edits concentrate in a narrow code window; decode round-trips at 1.00 on the scored protocol. Early scoring mistakes (wrong index space) are part of the record—locality gold must align with codec `split()` streams.

## What did not pass

Direction 3’s scale ladder missed coarseness targets—mean unit length stalled short of the gate. Keeping that run visible matters: merge policy at 100k-word scale does not automatically inherit toy successes.

## Reproduce

```bash
git clone https://github.com/kmfarris/customLLM
cd customLLM
pip install -e '.[dev]'
python -m pytest tests/
# GPU working LM (see README):
PRCF_REQUIRE_GPU=1 PYTHONPATH=src:. python -m experiments.working_lm.run
```

## Next baselines

SentencePiece with matched vocabulary on the same split. A single validation packing table emitted beside every train metric cited in prose. Scale beyond WikiText-2 only after those anchors exist.
