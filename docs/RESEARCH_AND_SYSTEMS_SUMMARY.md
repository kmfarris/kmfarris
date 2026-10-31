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

## scatterbrain-steering: steering what an AI says while it's speaking

**What it is.** An experiment in guiding an AI's reply word by word, while the reply is being written.

**The problem.** A text-generating AI chooses each word based on what it has already written. A goal such as "mention these three points" or "stay calm" is usually stated once at the start, and the model may drift away from it partway through.

**How it works.** A small language model writes one word at a time and keeps a running memory of the whole reply. Before each word, a separate "executive" looks at the plan for the reply and the system's current state, then gives a small push toward words that fit and away from words that don't. The language model still writes the sentence. The executive only shifts the odds.

The training examples came from a local AI "teacher" that wrote questions, good answers, bad answers, and plans based on source text. Anything that broke the rules was thrown out automatically, and 39 examples passed.

**Results so far.**
- The steering mechanism works and is covered by 15 automated tests.
- Turning the executive's push on or off measurably changes which words get chosen.

**Still to do.**
- The small language model hasn't been trained enough to write fluent sentences yet. It repeats itself.
- The executive follows rules written by hand instead of rules it learned from the training examples.
- It stays switched off in the main Scatterbrain project until it passes its quality checks.

[How steering works](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md)
