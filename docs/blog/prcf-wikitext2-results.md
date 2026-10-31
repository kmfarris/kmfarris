# Breaking text into better pieces for AI

AI language models can't read words. Before a model sees any text, the text is chopped into small pieces called **tokens**, and the model learns to guess the next piece. Almost every model in use today chops text by spelling: wherever certain letters show up together often, that cluster becomes a token.

That approach works, but the pieces have nothing to do with meaning. One word might be split into three pieces while another stays whole. Edit a single word and the pieces nearby can rearrange. Two different words that look alike can end up sharing pieces.

## A different way to chop

The customLLM project tries something else:

1. **Every known word gets its own code**, like a library call number. No two words share one.
2. **Unfamiliar words are spelled out** letter by letter, so the original text can always be rebuilt.
3. **Codes that often sit side by side are joined** into larger pieces, the way standard tokenizers join letters.

## A fair test

To find out whether this helps, two identical small AI models were trained on the same two million words of English from Wikipedia. One read standard tokens and the other read the new codes. Everything else was the same, so any difference comes from how the text was broken up.

## What happened

- **Nothing was lost.** Text converted to codes and back came out exactly as it went in.
- **Edits stayed local.** Changing one word only changed the codes right around it.
- **The model learned a little better.** The code-trained model needed about 6% less information per letter to predict the text (1.76 vs 1.88 bits per character).
- **The text packed slightly tighter** as codes than as standard tokens.

## What's left

On text the system hadn't seen, more words had to be spelled out, so the advantage shrank. The joined pieces are still roughly word-sized, and an attempt to build phrase-sized pieces fell short of its target. The test also used one dataset and small models. The next steps are comparing against other modern tokenizers on the same text, then trying much larger collections of text.

## Try it

```bash
git clone https://github.com/kmfarris/customLLM
cd customLLM
pip install -e '.[dev]'
python -m pytest tests/
```
