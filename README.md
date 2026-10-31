# Kelly Farris

Research and systems work at the boundary of **tokenization**, **agent runtimes**, and **decoder control**—with reproducible artifacts first, narrative second.

## Flagship repositories

| Project | Focus |
|---------|--------|
| [**customLLM**](https://github.com/kmfarris/customLLM) | PRCF: positioned codes, bucket+slot invertibility, matched LM bake-offs on WikiText-2 |
| [**IMOL**](https://github.com/kmfarris/imol) | Agent language: check → patch → workshop dry-run, MCP oracle tools |
| [**scatterbrain-steering**](https://github.com/kmfarris/scatterbrain-steering) | Executive logit bias on a persistent GRU decoder; conscience curriculum + release gates |

## Verify in one command each

```bash
git clone https://github.com/kmfarris/customLLM && cd customLLM && pip install -e '.[dev]' && python -m pytest tests/

git clone https://github.com/kmfarris/imol && cd imol && npm install && npm run check

git clone https://github.com/kmfarris/scatterbrain-steering && cd scatterbrain-steering && pip install -r requirements-dev.txt && PYTHONPATH=. python -m pytest tests/ -q
```

## Writing

- [PRCF on WikiText-2](docs/blog/prcf-wikitext2-results.md) — locality, packing, matched BPC
- [IMOL agent loop](docs/blog/imol-check-patch-workshop.md) — structure before side effects

## Summary

One-page overview for hiring: [`docs/RESEARCH_AND_SYSTEMS_SUMMARY.md`](docs/RESEARCH_AND_SYSTEMS_SUMMARY.md) (export to PDF from your editor or `pandoc`).
