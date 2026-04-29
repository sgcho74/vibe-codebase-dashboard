---
name: code-review-skill
description: Review AI-generated or human-written code for correctness, maintainability, readability, architecture fit, and regression risk. Use before merging AI-assisted code.
metadata:
  version: "1.0.0"
  parent: "vibe-codebase-dashboard"
---

# Code Review Skill

## Mission

Review code changes critically before they are accepted. Do not assume AI-generated code is correct because it looks complete.

## Review Checklist

1. Purpose Fit
   - Does the code solve the stated requirement?
   - Are assumptions documented?
   - Is behavior clear from the code and tests?

2. Maintainability
   - Is the code simple enough to maintain?
   - Are names meaningful?
   - Is duplicated logic avoided?
   - Are module boundaries respected?

3. Architecture Fit
   - Does the change follow existing patterns?
   - Does it introduce hidden coupling?
   - Does it bypass established service, repository, API, or security layers?

4. Reliability
   - Are errors handled intentionally?
   - Are retries, timeouts, and fallback behavior appropriate?
   - Are logs useful without exposing sensitive data?

5. Review Evidence
   - Record files reviewed.
   - Record risks found.
   - Record required fixes.
   - Record approval or rejection recommendation.

## Output Format

```markdown
# Code Review Result

## Summary
- Verdict: Approve / Request Changes / Needs Discussion
- Risk Level: Low / Medium / High

## Findings
| Priority | File | Finding | Recommendation |
|---:|---|---|---|

## Required Fixes
- 

## Review Evidence
- Reviewed files:
- Tests checked:
- Remaining risk:
```
