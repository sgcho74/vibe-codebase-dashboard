---
name: security-review-skill
description: Review code changes for authentication, authorization, secrets, input validation, injection risks, logging, dependency, and permission issues.
metadata:
  version: "1.0.0"
  parent: "vibe-codebase-dashboard"
---

# Security Review Skill

## Mission

Identify security risks introduced by AI-assisted or human-written changes.

## Review Checklist

1. Authentication
   - protected endpoints require authentication
   - session/token handling is safe

2. Authorization
   - role and permission checks are enforced
   - horizontal privilege escalation is prevented

3. Input Validation
   - untrusted input is validated
   - SQL, command, and path injection are prevented

4. Secrets
   - no hard-coded keys or passwords
   - `.env.example` exists without secrets
   - logs do not expose sensitive data

5. Dependencies
   - new dependencies are justified
   - known vulnerabilities are checked

6. Auditability
   - security-sensitive actions are logged safely
   - review evidence is captured

## Output Format

```markdown
# Security Review Result

## Verdict
- Status: Pass / Partial / Fail
- Risk Level: Low / Medium / High

## Findings
| Severity | Area | Finding | Recommendation |
|---|---|---|---|

## Required Fixes
- 
```
