# Cutting text differently, then training the same small model twice

Before a language model can learn English, the text is cut into **tokens**. The usual cut follows spelling: common letter groups become common tokens (BPE). customLLM tries a different first cut. Each known word gets a code. Unknown words are spelled out so nothing is lost. Nearby codes may merge, the way BPE merges letters. Then two copies of the same small model train—one on ordinary BPE, one on the code alphabet—on the full WikiText-2 corpus.

The purpose of that bake-off is simple: if the *pieces* change, does the *same* model still learn, and do edits stay near the change?

## What moved

**Density.** On training text, the code stream used 0.227 symbols per character vs 0.240 for BPE. Validation is looser than train because held-out words more often take the spell-out path. Both numbers are in `results.json`.

**Bits per character.** Training BPC was 1.76 (codes) vs 1.88 (BPE). That is a comparison of alphabets under one model size, not a claim about the largest models in the world.

**Locality and round-trip.** A one-word edit stays in a narrow window of codes. Decode returns the original text (score 1.00 on the protocol in the repo). Early locality scores were wrong when labels used the wrong index space; the scored protocol uses the codec’s own `split()` stream.

## What still needs work

A coarser-merge experiment on a 100k-word slice missed its length targets. Phrase-sized units are not there yet. SentencePiece with a matched vocabulary on the same split is the obvious next baseline. Scaling past WikiText-2 waits on that.

## Reproduce

```bash
git clone https://github.com/kmfarris/customLLM
cd customLLM
pip install -e '.[dev]'
python -m pytest tests/
PRCF_REQUIRE_GPU=1 PYTHONPATH=src:. python -m experiments.working_lm.run
```
