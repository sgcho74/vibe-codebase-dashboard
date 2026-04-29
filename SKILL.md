---
name: vibe-codebase-dashboard
description: Analyze a software codebase and generate a one-page dashboard showing whether the repository is ready for responsible vibe coding and VibeOps. Use when the user asks to inspect a codebase, evaluate AI coding readiness, identify missing context, skills, agents, hooks, plugins, MCPs, tests, quality gates, review evidence, ownership, or production readiness.
compatibility: Works with Claude Code, Cursor, Codex CLI, and general AI coding agents. Requires read access to the repository. Optional Python 3 for dashboard generation.
metadata:
  version: "1.0.0"
  owner: "enterprise-ai-coding"
  mode: "read-only by default"
---

# Vibe Codebase Dashboard Skill

## Mission

Explore the current repository and produce a one-page dashboard that answers:

1. Is this codebase ready for responsible vibe coding?
2. Can AI understand, modify, test, and explain this codebase safely?
3. Is there enough human ownership and review evidence?
4. What is missing before production-grade AI coding can be trusted?
5. What should be fixed first?

This skill must not evaluate vibe coding readiness only by speed, automation, or AI tool availability.

A repository is vibe-coding-ready only when it supports responsible human ownership, critical validation, explainability, and controlled production operation.

Default behavior is read-only analysis. Do not modify source code unless explicitly requested.

---

## Core Principle

AI-generated code is untrusted until verified.

Surface completeness is not correctness.

Human owner responsibility cannot be outsourced.

The dashboard must explicitly answer:

- Who is responsible?
- What was reviewed?
- What evidence proves it works?
- What can break if this change fails?
- Can a human explain the design decision?
- Is there a safe path to test, rollback, and operate?

---

## Vibe Coding Readiness Model

Evaluate the repository across ten dimensions:

1. Context Readiness
2. Skill Readiness
3. Agent Role Readiness
4. VibeOps Readiness
5. Critical Validation Readiness
6. Human Ownership Readiness
7. Tool / MCP Readiness
8. Test & Quality Readiness
9. Build / Deploy Readiness
10. Security & Governance Readiness

Use evidence from actual files, not assumptions.

---

## Scoring Model

Total score: 100 points.

| Dimension | Weight |
|---|---:|
| Context Readiness | 10 |
| Skill Readiness | 10 |
| Agent Role Readiness | 10 |
| VibeOps Readiness | 15 |
| Critical Validation Readiness | 15 |
| Human Ownership Readiness | 10 |
| Tool / MCP Readiness | 10 |
| Test & Quality Readiness | 10 |
| Build / Deploy Readiness | 5 |
| Security & Governance Readiness | 5 |

Score levels:

| Level | Meaning |
|---:|---|
| 0 | Not found |
| 1 | Weak / partial |
| 2 | Exists but not operationalized |
| 3 | Operational and documented |
| 4 | Mature / reusable / automated |

Convert each dimension score to its weighted score.

---

## Readiness Grade

| Score | Grade | Meaning |
|---:|---|---|
| 85-100 | A | AI coding-ready and VibeOps-ready |
| 70-84 | B | Usable with minor gaps |
| 55-69 | C | Needs standardization before serious use |
| 40-54 | D | Risky for autonomous or semi-autonomous AI coding |
| 0-39 | E | Not ready |

---

## Repository Exploration Procedure

### Step 1. Build Codebase Map

Inspect:

- root files
- package/module structure
- README and documentation
- framework and language indicators
- build files
- test files
- CI/CD files
- AI assistant configuration files
- review and ownership files
- deployment and rollback files
- security and secret management files

Look for files such as:

- README.md
- CLAUDE.md
- AGENTS.md
- CODEOWNERS
- CONTRIBUTING.md
- SECURITY.md
- CHANGELOG.md
- ADR documents
- docs/architecture.md
- docs/runbook.md
- docs/deployment.md
- docs/rollback.md
- .cursor/rules/**
- .windsurf/rules/**
- .github/copilot-instructions.md
- .claude/skills/**/SKILL.md
- .claude/agents/**
- .claude/settings.json
- .mcp.json
- package.json
- pyproject.toml
- requirements.txt
- pom.xml
- build.gradle
- Dockerfile
- docker-compose.yml
- .github/workflows/**
- tests/**
- .env.example
- pre-commit config
- lint/typecheck/coverage configs

### Step 2. Extract Evidence

For each dimension, collect:

- detected files
- detected conventions
- missing files
- weak signals
- risk notes
- recommended actions

Never mark an item as complete without concrete evidence.

### Step 3. Evaluate VibeOps Readiness

Evaluate the following four VibeOps factors:

1. Confidence
   - Are there tests, CI results, coverage, and reproducible validation evidence?
2. Explainability
   - Are design decisions, ADRs, comments, and PR explanations available?
3. Blast Radius
   - Can the team understand the impact scope of a change?
4. Evidence of Review
   - Is there proof that a human reviewed the change?

### Step 4. Evaluate Critical Validation

Check whether the repository supports:

- edge case tests
- failure scenario tests
- adversarial review
- security review
- rollback test
- data migration validation
- API contract validation
- negative test cases
- performance or load validation where relevant

Do not treat build success as sufficient validation.

### Step 5. Evaluate Human Ownership

Check whether the repository defines:

- code owner
- module owner
- reviewer
- approver
- release owner
- incident owner
- production responsibility
- approval gates for risky changes

Human ownership is mandatory for responsible vibe coding.

### Step 6. Generate Dashboard

Produce three outputs:

1. `reports/vibe-dashboard.md`
2. `reports/vibe-dashboard.html`
3. `reports/vibe-dashboard.json`

If file creation is not available, print the dashboard in Markdown.

---

## Dashboard Layout

The dashboard must fit on one page and include:

1. Overall score
2. Readiness grade
3. One-minute executive summary
4. VibeOps 4-factor table
5. Ten-dimension readiness table
6. Top 5 gaps
7. Top 5 red flags
8. Top 5 quick wins
9. Evidence table with file paths
10. Recommended files to create
11. Recommended skills to add
12. Suggested AI coding operating model

---

## Red Flag Rules

Highlight red flags when:

- AI-generated code can be merged without tests
- No human review evidence exists
- No CODEOWNERS or ownership file exists
- No architecture document exists
- No rollback procedure exists
- No `.env.example` exists
- Secrets may be committed
- No CI quality gate exists
- No MCP/tool permission boundary exists
- No blast radius analysis is possible
- Tests only cover happy path
- No production readiness checklist exists

---

## Output Rules

Always include:

- concise executive summary
- evidence-based score
- missing elements
- risk impact
- recommended priority
- copy-pasteable action items

Avoid:

- vague advice
- unsupported assumptions
- excessive code details
- source code modification unless requested

---

## Recommended Improvement Files

When gaps are found, recommend concrete files to create, such as:

- CLAUDE.md
- AGENTS.md
- CODEOWNERS
- CONTRIBUTING.md
- SECURITY.md
- .cursor/rules/project-rules.md
- .claude/skills/code-review/SKILL.md
- .claude/skills/test-generation/SKILL.md
- .claude/skills/critical-validation/SKILL.md
- .claude/skills/blast-radius-analysis/SKILL.md
- .claude/skills/security-review/SKILL.md
- .mcp.json
- .github/workflows/ci.yml
- docs/architecture.md
- docs/runbook.md
- docs/rollback.md
- docs/adr/0001-architecture-decision-template.md


## Bundled Sub-Skills

This skill package includes reusable sub-skills under `.claude/skills/`:

- `code-review`
- `critical-validation`
- `blast-radius-analysis`
- `test-generation`
- `security-review`
- `architecture-decision`
- `vibeops-readiness`
- `release-readiness`

Use these sub-skills when the dashboard identifies related gaps.
