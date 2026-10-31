# Kelly Farris: project summary

[github.com/kmfarris](https://github.com/kmfarris)

---

## customLLM: a new way to break text into pieces for AI

**What it is.** A research project that tests a different way of preparing text before an AI language model reads it.

**The problem.** AI language models read text as a sequence of small pieces called tokens. The standard way of making tokens splits text wherever letter combinations are common. The pieces don't match whole words, and editing one word can change pieces elsewhere in the sentence. That makes it hard to see what changed, to swap one name for another, or to treat a word as the same thing every time it appears.

**How it works.** Every known word gets its own fixed code. Unfamiliar words are spelled out letter by letter, so the original text can always be rebuilt. Codes that often sit next to each other are joined into larger pieces. Two identical small AI models were then trained on the same two million words of English text (the WikiText-2 dataset), one with standard tokens and one with these codes, so the only difference was how the text was broken up.

**Results so far.**
- Text converted to codes and back came out identical every time.
- Changing a single word only affected the codes immediately around it.
- The model trained on codes predicted the text slightly better, using about 6% less information per letter (1.76 vs 1.88 bits per character).
- The codes packed the text a little more tightly than standard tokens.

**Still to do.**
- On text the system hasn't seen, more words have to be spelled out, so the advantage shrinks.
- The joined pieces are still roughly word-sized. An attempt to build larger, phrase-sized pieces didn't reach its target.
- It has only been tested on one dataset with small models, and hasn't yet been compared against other modern tokenizers.

[Results data](https://github.com/kmfarris/customLLM/blob/main/experiments/working_lm/results.json)

---

## IMOL: a programming language built for AI coding assistants

**What it is.** A programming language and a set of tools designed so AI assistants can write and change programs safely.

**The problem.** AI coding assistants usually produce code as plain text that gets dropped into a file. Errors show up only later, sometimes after the program has already deleted or changed files or contacted the internet. Edits that refer to line numbers break as soon as the file shifts.

**How it works.**
- **Name tags.** Every part of a program carries a permanent tag, so an edit can say "replace this function" rather than "replace lines 40 to 62."
- **Checking first.** The program is checked for mistakes before anything is saved. Problems come back in a structured form the assistant can read and fix on its own.
- **Declared permissions.** Each program states up front what it's allowed to do: read files, write files, use the network, or run commands.
- **Rehearsal mode.** The program can be run as a rehearsal that lists every action it would take without doing any of them. Real actions need explicit approval.

**Results so far.** The language, the checker, the editing tools, and the rehearsal runtime all work, and the full automated test suite passes. IMOL connects to the Cursor code editor so an assistant can use these checks directly.

**Still to do.** The language has gained new features faster than the format it uses to talk to assistants, and the two need to be brought back in step. It isn't yet published as an installable package, and there's no formal written definition of the language.

---

## scatterbrain-steering: an SNN conscience for inference-time alignment

**What it is.** An alignment experiment in which a spiking neural network (SNN) acts as a conscience, steering a language model's word choices as it generates.

**The problem.** Alignment is usually applied before a model is used. Fine-tuning methods such as RLHF and DPO build preferences into the weights, and system prompts state rules at the start of the conversation. During generation, the model has to keep to those rules through attention over its context alone. As a reply grows, the instructions carry less weight and the output can drift.

**How it works.**
- **Conscience SNN.** A 128-neuron spiking network holds core values (empathy, compassion, truth, and others) and a list of *poison pairs*, such as "manipulate" alongside "truth." At each step it excites value-aligned candidate words and inhibits words that would complete a violation. Its values are deliberately hard to change: learning is slow and gated, so one adversarial input can't rewrite them.
- **Executive.** Combines the conscience's state, a plan listing the concepts the reply should cover, and simulated neuromodulator levels into one bias with a bounded strength.
- **Logit steering.** The bias is added to the language model's next-token scores before each word is chosen: `final = model scores + strength × conscience bias`. The alignment signal is applied again at every token instead of being read once from the prompt.
- **Conscience curriculum.** A local teacher model turns seed lessons into grounded questions, preferred answers, rejected answers, and concept plans. Anything the source material doesn't support is rejected automatically. Thirty-nine examples passed and were recorded as step-by-step training trajectories.

**Results so far.**
- On held-out lessons, steering raised the output's match to the aligned reference from 0.0 (conscience off) to 0.1125 (conscience on), on the same model.
- The conscience SNN's excitation, inhibition, and resistance to change are verified by tests. Eighteen automated tests cover the full pipeline.
- The steering rule works with any model that exposes its next-token scores, including locally run open-source models.

**Still to do.**
- The small language model being steered has had only a short training run. It isn't fluent and doesn't yet cover every planned concept.
- The conscience's bias strengths are set by hand. The next step is learning them from the curriculum.
- **LoRA fine-tuning (planned):** adapt a small open-weight model on the conscience curriculum with the conscience active during training, then confirm that the model follows the conscience's signal by testing with that signal zeroed and shuffled.

[How steering works](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md)
