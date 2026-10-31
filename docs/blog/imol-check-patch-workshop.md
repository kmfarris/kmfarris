# IMOL: structure on the critical path

Agent loops often treat source files as text buffers: the model proposes a diff, the host applies it, and errors surface later—sometimes on disk already changed. IMOL inverts the order. Parse first. Diagnose with stable declaration IDs. Patch in memory and re-check. Dry-run plan invokes before anything touches the filesystem.

## Three commands, one discipline

**Check.** `imol agent check` returns JSON: `ok`, `has_holes`, diagnostics anchored to `@id` when possible. Agents can branch on machine-readable failure instead of guessing from stderr.

**Patch.** Operations target declarations by UUID—replace, insert after, delete—not fragile line numbers. Fmt output is the IR; patches commute with canonical formatting.

**Workshop plan.** Plan blocks describe tool invokes under a capability envelope (`allow_net`, `allow_write`, `allow_shell`, MCP binds). Dry-run emits a trace; approval is explicit. Side effects wait on policy, not on model enthusiasm.

## Why two spec versions appear

Language surface features advance (shell, async preview at 0.5). Agent stdout JSON remains at **0.4** until a deliberate schema migration—integrations in Cursor and MCP depend on stable oracle shapes.

## Try it

```bash
git clone https://github.com/kmfarris/imol
cd imol
npm install && npm run build
npm run imol -- agent check examples/dogfood/catalog.imol
npm run check
```

Terminal cast outline: [`docs/DEMO.md`](https://github.com/kmfarris/imol/blob/main/docs/DEMO.md).

## Where it fits

Teams building agent platforms need the same primitives databases got decades ago: constraints before mutation, traces before commit. IMOL is a small language plus CLI plus MCP oracles encoding that contract for LLM-authored programs—not a replacement for your runtime, but a layer agents can call without improvising JSON tool schemas per repo.
