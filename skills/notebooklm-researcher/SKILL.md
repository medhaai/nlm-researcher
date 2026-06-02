---
name: notebooklm-researcher
description: "High-fidelity source-grounded research workflow using NotebookLM, local artifacts, and concise synthesis."
version: 1.0.0
author: NLM Researcher contributors
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [research, notebooklm, synthesis, source-grounded, deep-context]
---

# NLM Researcher

Use this skill when a research task needs more evidence, more source context, or more durable artifacts than a single chat response can safely handle.

The core pattern is:

1. Create or reuse one NotebookLM notebook for one research question or project.
2. Keep a local research workspace with raw source lists, raw query outputs, and final concise outputs.
3. Add only high-signal sources.
4. Run a query/refine/verify loop.
5. Return a short answer to the user and leave deep artifacts in files/NotebookLM.

## Privacy and publication guardrails

- Do not hard-code personal directories, private project names, internal task IDs, credentials, cookies, or organization-specific workflows.
- Use environment variables and placeholders such as `$RESEARCH_ROOT`, `$PROJECT_SLUG`, and `$NOTEBOOK_ID`.
- Do not claim a NotebookLM action succeeded unless a NotebookLM MCP tool or verified `nlm` CLI command confirms it.
- Keep private sources private. Do not paste full proprietary source content into public reports.
- Before publishing a derivative of this skill, run the repository leak audit script if available.

## Recommended workspace

Set a root directory for research artifacts:

```bash
export RESEARCH_ROOT="$HOME/research"
export PROJECT_SLUG="example-project"
mkdir -p "$RESEARCH_ROOT/$PROJECT_SLUG"/{sources,analysis,outputs,daily}
```

Recommended files:

- `notebook_meta.json`: notebook title, ID, source count, creation/update timestamps.
- `sources/sources.csv`: curated source registry.
- `analysis/`: raw NotebookLM query outputs and source-ingestion logs.
- `outputs/`: concise final memos or research packets.
- `daily/`: recurring/living research digests, if applicable.

See `references/research-workspace.md`.

## Source strategy

Prefer high-signal sources:

- official docs, pricing pages, release notes, policy pages;
- primary interviews, talks, podcasts, YouTube videos, or transcripts;
- credible reports with hard numbers;
- regulatory/legal updates;
- job postings or technical docs that reveal roadmap/capability signals.

Avoid adding low-value duplicates, SEO summaries, and generic commentary unless they introduce a specific new fact.

## Query/refine/verify loop

1. Broad map: identify the landscape, major claims, and unknowns.
2. Targeted drill-down: query contradictions, numbers, risks, and assumptions.
3. Verification: ask for specific source-grounded quotes/citations.
4. Synthesis: write a short decision-oriented answer with caveats and next steps.

See `references/query-patterns.md`.

## Tool usage

Use NotebookLM MCP tools when available. If not available, use verified `nlm` CLI commands.

### Verified `nlm` CLI command shapes

```bash
# Create notebook
uvx --from notebooklm-mcp-cli nlm create notebook "RESEARCH-$PROJECT_SLUG"

# List notebooks
uvx --from notebooklm-mcp-cli nlm list notebooks --json

# Add a local file
uvx --from notebooklm-mcp-cli nlm source add "$NOTEBOOK_ID" --file "$SOURCE_FILE" --wait --wait-timeout 180

# Add a URL
uvx --from notebooklm-mcp-cli nlm source add "$NOTEBOOK_ID" --url "$SOURCE_URL" --wait --wait-timeout 240

# Add a YouTube source
uvx --from notebooklm-mcp-cli nlm source add "$NOTEBOOK_ID" --youtube "$YOUTUBE_URL" --wait --wait-timeout 600

# List sources
uvx --from notebooklm-mcp-cli nlm source list "$NOTEBOOK_ID"

# Query notebook
uvx --from notebooklm-mcp-cli nlm query notebook "$NOTEBOOK_ID" "$QUESTION" --json --timeout 300
```

Known pitfall: `nlm add source ...` is not the verified command form. Use `nlm source add NOTEBOOK_ID --file/--url/--youtube ...`.

## Output discipline

For the user-facing response, prefer:

- 3-7 bullet executive summary;
- key evidence/citations or source names;
- top risks/blockers;
- artifact paths and NotebookLM notebook ID/title;
- recommended next action.

Do not paste long raw NotebookLM answers into chat unless explicitly requested.

## Living research

For recurring research, maintain a source registry and short dated digests. Do not blindly add every discovered URL to NotebookLM; graduate only high-signal changes.

See `references/living-research.md`.
