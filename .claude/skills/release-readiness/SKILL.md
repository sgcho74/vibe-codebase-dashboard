---
name: release-readiness-skill
description: Check whether AI-assisted changes are ready for release, including deployment, rollback, monitoring, owner approval, and operational evidence.
metadata:
  version: "1.0.0"
  parent: "vibe-codebase-dashboard"
---

# Release Readiness Skill

## Mission

Confirm that a change can be deployed safely and recovered if it fails.

## Checklist

1. Deployment
   - deployment steps documented
   - environment variables documented
   - migration steps documented

2. Rollback
   - rollback command or procedure exists
   - data rollback considered
   - owner identified

3. Monitoring
   - logs are sufficient
   - metrics or health checks exist
   - failure symptoms are known

4. Approval
   - code owner approved
   - reviewer approved
   - release owner assigned

5. Evidence
   - tests passed
   - CI passed
   - manual checks recorded

## Output Format

```markdown
# Release Readiness Result

## Verdict
Release / Hold / Release with Conditions

## Checklist
| Area | Status | Evidence | Required Action |
|---|---|---|---|

## Rollback Plan
- 
```
