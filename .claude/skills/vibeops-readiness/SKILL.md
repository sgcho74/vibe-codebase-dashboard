---
name: vibeops-readiness-skill
description: Assess whether a change or repository is ready for responsible VibeOps using Confidence, Explainability, Blast Radius, and Evidence of Review.
metadata:
  version: "1.0.0"
  parent: "vibe-codebase-dashboard"
---

# VibeOps Readiness Skill

## Mission

Assess operational readiness for AI-assisted development.

## Four Required Factors

1. Confidence
   - tests exist and pass
   - CI verifies the change
   - validation scope is sufficient

2. Explainability
   - design decision is documented
   - non-obvious logic is explained
   - trade-offs are captured

3. Blast Radius
   - affected modules are known
   - rollback path exists
   - impact scope is documented

4. Evidence of Review
   - human reviewer assigned
   - review comments or approval captured
   - release owner identified

## Output Format

```markdown
# VibeOps Readiness Result

| Factor | Status | Evidence | Gap |
|---|---|---|---|
| Confidence |  |  |  |
| Explainability |  |  |  |
| Blast Radius |  |  |  |
| Evidence of Review |  |  |  |

## Verdict
Ready / Not Ready / Ready with Conditions

## Required Conditions
- 
```
