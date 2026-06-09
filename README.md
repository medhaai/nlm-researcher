# NotebookLM Researcher Skill

A public, privacy-safe Hermes skill for running high-fidelity research with NotebookLM.

The skill helps an agent:

- create a durable local research workspace;
- add curated sources to a NotebookLM notebook;
- keep raw NotebookLM outputs separate from concise user-facing summaries;
- run repeatable query/refine/verify loops;
- optionally maintain living research digests over time.

This repository is a productized public version of an internal workflow. It intentionally excludes private project names, personal paths, internal task IDs, and organization-specific operating procedures.

## What this is

- A Hermes `SKILL.md` plus reusable reference templates.
- A source-grounded research operating pattern, not a NotebookLM replacement.
- A way to keep long-context research auditable and reusable.

## What this is not

- It is not affiliated with Google or NotebookLM.
- It does not include credentials or NotebookLM cookies.
- It does not send private sources anywhere by itself; source ingestion is performed only through the user's configured NotebookLM tools or CLI.

## Install

Copy the `skills/notebooklm-researcher` directory into your Hermes skills directory:

```bash
mkdir -p ~/.hermes/skills/research
cp -R skills/notebooklm-researcher ~/.hermes/skills/research/
```

Then list skills from Hermes and load `notebooklm-researcher` when doing NotebookLM-backed research.

## Requirements

One of these must be available:

1. NotebookLM MCP tools exposed in your Hermes session; or
2. the `nlm` CLI from `notebooklm-mcp-cli`, invoked through `uvx`.

Example CLI checks:

```bash
uvx --from notebooklm-mcp-cli nlm --help
uvx --from notebooklm-mcp-cli nlm list notebooks --json
```

## Privacy model

The public skill uses placeholders only:

- `$RESEARCH_ROOT` instead of a user home path;
- `$NOTEBOOK_ID` instead of real notebook identifiers;
- `$PROJECT_SLUG` instead of internal project names;
- generic task labels instead of private task systems.

Before publishing changes, run:

```bash
python scripts/leak_audit.py .
```

## Quick evaluation prompt

Use this when installing in another Hermes environment:

> Install the `notebooklm-researcher` skill, configure the NotebookLM MCP tool or `nlm` CLI, create a tiny test notebook, add one public source, run one broad query plus one verification query, and then report back with: what installed cleanly, what failed, what needs configuration changes, and any GitHub feedback as an issue or PR comment.

## Repository layout

```text
skills/notebooklm-researcher/SKILL.md
skills/notebooklm-researcher/references/research-workspace.md
skills/notebooklm-researcher/references/living-research.md
skills/notebooklm-researcher/references/query-patterns.md
scripts/leak_audit.py
```

## License

MIT. See `LICENSE`.
