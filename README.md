# Kelly Farris

## [customLLM](https://github.com/kmfarris/customLLM): a new way to break text into pieces for AI

AI language models, like the ones behind chat assistants, can't read words directly. Text is first chopped into small pieces called **tokens**, and the model learns to predict one piece after another. The standard method chops text wherever letter combinations are common. Because of that, changing one word can reshuffle pieces somewhere else in the sentence, and the pieces don't line up with whole words.

customLLM gives every known word its own fixed code, a bit like a library call number. Words the system has never seen are spelled out letter by letter, so nothing is lost. Codes that often appear side by side are joined into larger pieces. To test the idea fairly, two identical small AI models were trained on the same two million words of English text, one using the standard pieces and one using these codes.

The code version turned text back into the exact original every time. Changing one word only affected the codes right next to it. The model trained on codes also learned the text slightly better. It still works less well on text it hasn't seen before, and it has only been tested at small scale.

[Read more](docs/blog/prcf-wikitext2-results.md)

## [IMOL](https://github.com/kmfarris/imol): a programming language built for AI coding assistants

When an AI assistant writes or edits code, it usually produces text that gets pasted straight into a file. Mistakes surface later, sometimes after the program has already changed files or reached out to the internet. Edits that point at "line 40" break as soon as anything above them moves.

IMOL gives every part of a program a permanent name tag, so an assistant can say "replace this function" instead of "replace line 40." Before anything is saved, IMOL checks the program and reports mistakes in a form the assistant can read and fix. Each program must state up front what it's allowed to do, such as reading files, writing files, using the internet, or running commands. A rehearsal mode lists every action the program would take without doing any of them. Nothing real happens until a person approves.

All of the tools work, the automated tests pass, and IMOL connects to the Cursor code editor. It isn't yet available as an installable package.

[Read more](docs/blog/imol-check-patch-workshop.md)

## [scatterbrain-steering](https://github.com/kmfarris/scatterbrain-steering): steering what an AI says while it's speaking

An AI that writes text picks each next word based on the words before it. If you want a goal to keep mattering through the whole reply, such as "cover these points" or "stay gentle," you usually have to state it at the start and hope the model sticks with it.

Here, a small language model writes the reply one word at a time and remembers everything it has written so far. Before each word, a separate "executive" component checks the plan for the reply and gives a small push toward words that fit it. The language model still writes the sentence. The executive only tilts the odds.

The steering works: turning the push on or off measurably changes which words get picked, and 15 automated tests cover it. The small language model isn't fluent yet, and the executive follows hand-written rules rather than rules it learned.

[How it works](https://github.com/kmfarris/scatterbrain-steering/blob/main/docs/STEERING.md)

---

[One-page summary](docs/RESEARCH_AND_SYSTEMS_SUMMARY.md)
