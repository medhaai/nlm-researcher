# Living research pattern

Use this pattern when a research topic should continue producing periodic updates.

## Cadence options

- `one-time`: static memo or one-off decision.
- `daily`: fast-moving topic, launches, regulation, breaking market data.
- `weekly`: active but slower-moving project.
- `monthly`: competitor/market landscape refresh.
- `quarterly`: strategic thesis refresh.

If cadence is unclear, ask the user before scheduling automation.

## Recurring workflow

1. Read `notebook_meta.json` and `sources/sources.csv`.
2. Check watchlist URLs or search sources for new high-signal candidates.
3. Add only high-signal sources to NotebookLM.
4. Record added, skipped, duplicate, and failed candidates in `sources/sources.csv`.
5. Query NotebookLM for changes since the last digest.
6. Save raw output in `analysis/`.
7. Write a concise digest in `daily/`.

## Digest format

```md
# Research Delta — YYYY-MM-DD

Cadence: daily|weekly|monthly|quarterly
NotebookLM: NOTEBOOK_TITLE / NOTEBOOK_ID

## New sources added
- ...

## Key insight
- ...

## Changed assumption
- ...

## Risk movement
- ...

## Recommended next action
- ...

## Paths
- Raw: ...
- Registry: ...
```

## Guardrail

Do not interpret a blocked or timed-out web fetch as evidence that nothing changed. Record it as a scan caveat and use another discovery path if available.
