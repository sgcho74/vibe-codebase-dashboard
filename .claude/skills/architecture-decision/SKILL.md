---
name: architecture-decision-skill
description: Capture design decisions, alternatives, trade-offs, and consequences for non-trivial AI-assisted changes.
metadata:
  version: "1.0.0"
  parent: "vibe-codebase-dashboard"
---

# Architecture Decision Skill

## Mission

Make implementation choices explainable and auditable.

## When To Use

Use this skill when a change affects:
- architecture
- data model
- integration
- security boundary
- deployment pattern
- technology choice
- public API
- performance-critical path

## ADR Template

```markdown
# ADR: <Title>

## Status
Proposed / Accepted / Superseded

## Context
What problem are we solving?

## Decision
What did we decide?

## Alternatives Considered
| Alternative | Pros | Cons | Reason Not Selected |
|---|---|---|---|

## Consequences
- Positive:
- Negative:
- Risk:

## Validation Evidence
- Tests:
- Review:
- Rollback:
```
