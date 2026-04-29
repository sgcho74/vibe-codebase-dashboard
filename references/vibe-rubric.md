# Vibe Coding Readiness Rubric

## 1. Context Readiness - 10 points

Checks whether AI can understand the project without repeated manual explanation.

Evidence:
- README.md
- CLAUDE.md
- docs/architecture.md
- docs/runbook.md
- environment setup guide
- coding conventions
- domain glossary

Score:
- 0: No meaningful context
- 1: Basic README only
- 2: README and setup guide exist
- 3: Architecture and runbook exist
- 4: AI-specific context and constraints are documented

Risks if weak:
- AI misunderstands project intent
- inconsistent implementation
- repeated prompting overhead
- hidden architectural violations

Recommended actions:
- create CLAUDE.md
- create architecture.md
- create runbook.md
- create domain glossary

## 2. Skill Readiness - 10 points

Checks whether repeated AI coding tasks are standardized as reusable skills.

Evidence:
- .claude/skills/**/SKILL.md
- reusable prompts
- code review skill
- test generation skill
- refactoring skill
- security review skill
- release checklist skill

Score:
- 0: No skills
- 1: Ad-hoc prompts only
- 2: Some reusable prompts exist
- 3: Formal skills exist for common tasks
- 4: Skills are versioned, documented, and actively used

Risks if weak:
- AI output quality varies by user
- no standard process
- repeated manual instruction
- review criteria drift

Recommended actions:
- create code-review skill
- create test-generation skill
- create critical-validation skill
- create blast-radius-analysis skill

## 3. Agent Role Readiness - 10 points

Checks whether planning, coding, review, testing, and architecture responsibilities are separated.

Evidence:
- AGENTS.md
- .claude/agents/**
- Cursor rules
- role-based prompts
- reviewer/tester/architect role definitions

Score:
- 0: No role separation
- 1: informal role names only
- 2: basic agent roles defined
- 3: roles have responsibilities and boundaries
- 4: roles are linked to workflows and review gates

Risks if weak:
- AI acts as planner, coder, reviewer, and tester at once
- weak critical thinking
- automation bias
- design defects pass into production

Recommended actions:
- create AGENTS.md
- define Architect, Coder, Reviewer, Tester, Security Reviewer
- define when each role must be used

## 4. VibeOps Readiness - 15 points

Checks whether AI-generated code can be trusted through evidence, not assumption.

Sub-factors:
- Confidence
- Explainability
- Blast Radius
- Evidence of Review

Evidence:
- test results
- coverage reports
- ADRs
- PR descriptions
- review checklist
- dependency maps
- impact analysis
- approval logs

Score:
- 0: No VibeOps evidence
- 1: Some tests or review comments exist
- 2: partial VibeOps evidence exists
- 3: VibeOps criteria are part of PR/release process
- 4: VibeOps is automated and auditable

Risks if weak:
- superficially correct AI code
- hidden production risk
- no audit trail
- no explanation for design choices

Recommended actions:
- add VibeOps checklist
- add review evidence template
- add blast radius analysis
- require ADRs for risky changes

## 5. Critical Validation Readiness - 15 points

Checks whether the repository can challenge AI-generated code critically.

Evidence:
- edge case tests
- negative tests
- failure scenario tests
- security tests
- contract tests
- integration tests
- performance tests
- rollback tests
- adversarial review checklist

Score:
- 0: No meaningful validation
- 1: happy-path tests only
- 2: basic test suite exists
- 3: edge/failure/security cases exist
- 4: validation is systematic, automated, and required before merge

Risks if weak:
- build success mistaken for correctness
- hidden bugs
- security vulnerabilities
- production incident from untested edge cases

Recommended actions:
- add critical-validation skill
- require edge case tests
- require failure scenario tests
- add security review checklist

## 6. Human Ownership Readiness - 10 points

Checks whether humans remain responsible for AI-assisted development.

Evidence:
- CODEOWNERS
- reviewers
- approval rules
- production owner
- incident owner
- release owner
- RACI matrix
- PR approval policy

Score:
- 0: No owner
- 1: owner known informally
- 2: owner documented
- 3: owners and reviewers required in workflow
- 4: ownership is enforced and auditable

Risks if weak:
- responsibility gap
- unmanaged AI changes
- unclear production accountability
- weak governance

Recommended actions:
- create CODEOWNERS
- create ownership matrix
- define approval flow
- define release owner

## 7. Tool / MCP Readiness - 10 points

Checks whether AI tool usage is integrated and controlled.

Evidence:
- .mcp.json
- approved tool list
- GitHub tool configuration
- DB tool boundary
- documentation tool boundary
- access permission notes
- environment separation

Score:
- 0: No tool integration
- 1: tools used manually
- 2: tool config exists
- 3: tool permissions and boundaries documented
- 4: tool usage is governed, logged, and environment-aware

Risks if weak:
- uncontrolled tool usage
- excessive permissions
- accidental data exposure
- AI changes outside intended scope

Recommended actions:
- create .mcp.json
- document approved tools
- define read/write boundaries
- separate dev/test/prod access

## 8. Test & Quality Readiness - 10 points

Checks whether AI changes are automatically validated.

Evidence:
- tests/**
- lint config
- typecheck
- coverage
- CI workflow
- test scripts
- static analysis

Score:
- 0: No tests or quality gate
- 1: minimal tests
- 2: tests and lint exist
- 3: CI enforces tests and lint
- 4: quality gates include coverage, type, security, and review evidence

Risks if weak:
- no feedback loop
- AI code quality drift
- regression risk
- hard-to-maintain code

Recommended actions:
- add CI
- add lint/typecheck
- add coverage threshold
- add regression tests

## 9. Build / Deploy Readiness - 5 points

Checks whether the project can be built, run, and deployed reproducibly.

Evidence:
- Dockerfile
- docker-compose.yml
- build scripts
- deployment guide
- release script
- environment setup
- rollback guide

Score:
- 0: No build/deploy evidence
- 1: manual run only
- 2: basic build script exists
- 3: Docker or CI build exists
- 4: reproducible build/deploy/rollback exists

Risks if weak:
- demo-only implementation
- difficult handover
- unstable deployment
- production transition risk

Recommended actions:
- add Dockerfile
- add deployment.md
- add rollback.md

## 10. Security & Governance Readiness - 5 points

Checks whether AI-assisted coding is safe from security and governance perspective.

Evidence:
- SECURITY.md
- .env.example
- secret scanning
- dependency scanning
- permission model
- audit log policy
- secure coding guide

Score:
- 0: No security guidance
- 1: minimal env handling
- 2: security notes exist
- 3: security checks in CI
- 4: governance is enforced and auditable

Risks if weak:
- secret leakage
- excessive permissions
- unsafe AI-generated code
- compliance gap

Recommended actions:
- create SECURITY.md
- add .env.example
- enable secret scan
- add security-review skill
