---
name: critical-validation-skill
description: Challenge AI-generated code with edge cases, negative tests, failure scenarios, security checks, and rollback considerations. Use when code looks complete but needs verification.
metadata:
  version: "1.0.0"
  parent: "vibe-codebase-dashboard"
---

# Critical Validation Skill

## Mission

Validate that the code works beyond the happy path. Build success is not sufficient evidence.

## Validation Areas

1. Edge Cases
   - empty input
   - null input
   - invalid input
   - duplicate input
   - large input
   - boundary values

2. Failure Scenarios
   - DB unavailable
   - external API timeout
   - permission denied
   - missing environment variable
   - invalid configuration
   - partial failure

3. Security
   - authentication
   - authorization
   - input validation
   - secret exposure
   - SQL/command/path injection
   - sensitive logs

4. Data Safety
   - transaction boundaries
   - idempotency
   - rollback
   - destructive operation guards
   - migration reversibility

5. Evidence
   - tests added
   - test command run
   - results observed
   - remaining untested risk

## Output Format

```markdown
# Critical Validation Result

## Verdict
- Validation Status: Pass / Partial / Fail
- Risk Level: Low / Medium / High

## Edge Cases
| Case | Covered? | Evidence | Gap |
|---|---|---|---|

## Failure Scenarios
| Scenario | Covered? | Evidence | Gap |
|---|---|---|---|

## Required Additional Tests
- 
```
