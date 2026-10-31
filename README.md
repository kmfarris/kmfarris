# Kelly Farris

### [customLLM](https://github.com/kmfarris/customLLM)

Language models read **tokens**, not letters. How you cut text into tokens changes what a model can keep local, reconstruct, and learn. customLLM builds **PRCF**—word-aligned codes instead of spelling fragments—and trains a small language model on them next to the usual method (BPE). On WikiText-2 the code alphabet round-trips, keeps one-word edits nearby, and reaches **1.76** vs **1.88** bits per character under the same model size. Held-out packing and larger-scale baselines are still open.

[Notes on WikiText-2](docs/blog/prcf-wikitext2-results.md)

### [IMOL](https://github.com/kmfarris/imol)

Coding assistants often write programs by dumping text onto disk. IMOL is a language and a runtime for the opposite order: **check** the program, **patch** it by stable ids, **preview** planned file and network actions, then approve. The toolchain builds and passes conformance on a clean clone. Spec versions for the language and for agent JSON still need a joint bump; a published package process is unfinished.

[Notes on the agent loop](docs/blog/imol-check-patch-workshop.md)

### [scatterbrain-steering](https://github.com/kmfarris/scatterbrain-steering)

Speech needs memory of the sentence *and* control over the next word. This project keeps a small decoder’s memory across the reply and, at every step, lets a plan and other turn signals **nudge** word choice. Tests and a 39-trajectory curriculum are in the repo. The decoder itself is not fluent yet (release gates failed on a smoke train), and the executive is still a designed poll, not a trained network.

[How steering is wired](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md)

---

[One-page summary](docs/RESEARCH_AND_SYSTEMS_SUMMARY.md)
