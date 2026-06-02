# Research workspace pattern

Use a local workspace to make NotebookLM-backed research reproducible and auditable.

## Suggested layout

```text
$RESEARCH_ROOT/$PROJECT_SLUG/
  notebook_meta.json
  sources/
    sources.csv
    source-notes.md
  analysis/
    YYYY-MM-DD_query-name.json
    source-add-log.md
  outputs/
    research-packet.md
  daily/
    YYYY-MM-DD_digest.md
```

## `notebook_meta.json`

```json
{
  "notebook_title": "RESEARCH-example-project",
  "notebook_id": "NOTEBOOK_ID_PLACEHOLDER",
  "project_slug": "example-project",
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD",
  "source_count": 0
}
```

## `sources/sources.csv`

Recommended columns:

```csv
source_key,title,url,type,tags,date_added,last_checked,status,notebook_source_id,why_it_matters,last_insight
```

Status values:

- `candidate`: discovered but not yet added;
- `added`: successfully added to NotebookLM;
- `skipped`: low-signal or not relevant;
- `duplicate`: already covered;
- `failed`: attempted but failed;
- `stale`: no longer useful.
```
