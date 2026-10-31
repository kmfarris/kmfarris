# IMOL: check the program, then change it, then preview side effects

Coding assistants usually treat a source file as a text buffer. They propose a diff, the host applies it, and errors show up later—sometimes after the file on disk is already wrong. IMOL exists to reverse that order.

**Check** parses the program and returns JSON (`ok`, diagnostics, optional declaration ids). The assistant can retry from a machine-readable failure instead of scraping stderr.

**Patch** names declarations by UUID: replace this function, insert after that type, delete this tool. Formatting the file does not break the patch, because the formatted program *is* the stored form.

**Workshop-plan** lists the tool calls the program intends (read a file, write, shell, MCP) under explicit caps. Dry-run writes a trace. Approval is a separate step. Disk and network wait for that step.

The language has grown (shell and async preview at spec 0.5). The JSON agents consume is still 0.4 so existing editor integrations keep working until both versions move together.

```bash
git clone https://github.com/kmfarris/imol
cd imol
npm install && npm run build
npm run imol -- agent check examples/dogfood/catalog.imol
npm run check
```

Command outline: [`docs/DEMO.md`](https://github.com/kmfarris/imol/blob/main/docs/DEMO.md). Source: [github.com/kmfarris/imol](https://github.com/kmfarris/imol).
