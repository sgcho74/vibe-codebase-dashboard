# Human Ownership Checklist

Responsible vibe coding requires clear human accountability.

## Required Ownership Questions

1. Who owns this code?
2. Who can approve changes?
3. Who reviews AI-generated code?
4. Who operates this in production?
5. Who responds when it fails?
6. Who approves risky changes?
7. Who owns rollback?
8. Who signs off release?

## Required Files

- CODEOWNERS
- AGENTS.md
- CONTRIBUTING.md
- SECURITY.md
- docs/runbook.md
- docs/rollback.md
- docs/release-checklist.md

## Recommended Role Model

| Role | Responsibility |
|---|---|
| Owner | Final accountability |
| Architect | Design and impact judgment |
| Coder | Implementation |
| Reviewer | Code quality and maintainability |
| Tester | Test adequacy and edge cases |
| Security Reviewer | Security and permission review |
| Release Owner | Deployment and rollback |
| Incident Owner | Production issue response |

## Red Flags

- No owner
- Direct push to main
- No reviewer
- No approval flow
- No release owner
- No rollback owner
- AI code accepted without human review
