---
name: blast-radius-analysis-skill
description: Analyze the impact scope of a proposed code change, including affected modules, APIs, database objects, tests, users, and rollback risk.
metadata:
  version: "1.0.0"
  parent: "vibe-codebase-dashboard"
---

# Blast Radius Analysis Skill

## Mission

Identify what can break if the change is wrong.

## Analysis Checklist

1. Changed Surface
   - files changed
   - modules changed
   - public APIs changed
   - configuration changed
   - database schema or migration changed

2. Downstream Impact
   - callers
   - dependent services
   - UI screens
   - scheduled jobs
   - reports
   - integrations

3. Operational Impact
   - deployment risk
   - rollback path
   - feature flag availability
   - data recovery need
   - monitoring and alerting need

4. Test Scope
   - unit tests needed
   - integration tests needed
   - contract tests needed
   - manual checks needed

## Output Format

```markdown
# Blast Radius Analysis

## Summary
- Risk Level: Low / Medium / High
- Rollback Complexity: Low / Medium / High

## Affected Areas
| Area | Impact | Evidence | Required Check |
|---|---|---|---|

## Required Validation
- 

## Rollback Notes
- 
```
