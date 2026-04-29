---
name: test-generation-skill
description: Generate focused tests for AI-assisted code changes, covering happy path, edge cases, negative cases, and regression scenarios.
metadata:
  version: "1.0.0"
  parent: "vibe-codebase-dashboard"
---

# Test Generation Skill

## Mission

Generate tests that prove behavior, prevent regression, and expose hidden AI-generated defects.

## Test Types

1. Happy Path
   - expected normal behavior

2. Edge Cases
   - empty, null, max/min, duplicate, malformed input

3. Negative Cases
   - invalid permissions
   - invalid state
   - invalid configuration

4. Failure Cases
   - external dependency failure
   - timeout
   - retry exhaustion
   - DB failure

5. Regression Cases
   - previously fixed bugs
   - affected API contracts
   - changed module boundaries

## Output Rules

- Prefer small, deterministic tests.
- Avoid brittle implementation-detail tests.
- Include test names that describe behavior.
- Include commands to run the tests.

## Output Format

```markdown
# Test Plan

## Recommended Tests
| Priority | Test Name | Type | Purpose |
|---:|---|---|---|

## Test Code
```language
```

## Run Command
```bash
```
```
