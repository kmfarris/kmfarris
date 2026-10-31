# Kelly Farris

## Projects

| | |
|---|---|
| [**customLLM**](https://github.com/kmfarris/customLLM) | PRCF tokenization — bucket+slot codes, CodeBPE merges, matched LM runs on WikiText-2 |
| [**IMOL**](https://github.com/kmfarris/imol) | Language for agent-authored programs; `check`, id-keyed `patch`, workshop dry-run, MCP oracles |
| [**scatterbrain-steering**](https://github.com/kmfarris/scatterbrain-steering) | GRU decoder with per-token executive logit bias; conscience curriculum and release gates |

```bash
git clone https://github.com/kmfarris/customLLM && cd customLLM && pip install -e '.[dev]' && python -m pytest tests/

git clone https://github.com/kmfarris/imol && cd imol && npm install && npm run check

git clone https://github.com/kmfarris/scatterbrain-steering && cd scatterbrain-steering && pip install -r requirements-dev.txt && PYTHONPATH=. python -m pytest tests/ -q
```

## Notes

- [PRCF on WikiText-2](docs/blog/prcf-wikitext2-results.md)
- [IMOL: parse, patch, workshop](docs/blog/imol-check-patch-workshop.md)
- [Technical summary](docs/RESEARCH_AND_SYSTEMS_SUMMARY.md)
