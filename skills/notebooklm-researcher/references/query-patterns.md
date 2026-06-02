# Query patterns

## Broad map

Ask NotebookLM:

```text
Map the source set. What are the core claims, strongest evidence, unresolved unknowns, and contradictions? Separate directly sourced facts from interpretation.
```

## Hard numbers

```text
Extract all hard numbers relevant to this decision. For each number, provide source, date, exact quote if available, and confidence. Flag weak or inferred numbers separately.
```

## Risk register

```text
Create a risk register from the sources. Include regulatory, market, technical, operational, security, dependency, and execution risks. For each risk, cite supporting evidence and suggest a mitigation or next validation step.
```

## Contradiction finder

```text
Find claims that conflict across sources. For each contradiction, explain which source is stronger and what additional evidence would resolve it.
```

## Final synthesis

```text
Write a decision-oriented synthesis for a time-constrained operator. Include: answer, evidence, caveats, strongest counterargument, and recommended next action.
```
