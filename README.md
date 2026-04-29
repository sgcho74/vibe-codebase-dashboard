# Vibe Codebase Dashboard Skill

`vibe-codebase-dashboard`는 코드베이스가 바이브 코딩과 VibeOps 구조에 적합한지 진단하는 Agent Skill입니다.

핵심 관점은 단순한 AI 코딩 속도가 아니라 **AI가 만든 코드를 사람이 책임지고 검증·설명·운영할 수 있는 구조인지** 확인하는 것입니다.

## What it checks

- Context readiness
- Skill readiness
- Agent role readiness
- VibeOps readiness
  - Confidence
  - Explainability
  - Blast Radius
  - Evidence of Review
- Critical validation readiness
- Human ownership readiness
- Tool / MCP readiness
- Test & quality readiness
- Build / deploy readiness
- Security & governance readiness

## Repository structure

```text
vibe-codebase-dashboard/
├── SKILL.md
├── scripts/
├── references/
├── assets/
└── reports/
```

## Usage

Copy this directory into your AI coding agent skill path, or keep it as a standalone repository and reference it from Cursor, Claude Code, or Codex CLI.

### Run locally

```bash
python scripts/scan_repo.py
python scripts/score_vibe_readiness.py
python scripts/render_dashboard.py
```

Outputs:

```text
reports/repo-scan.json
reports/vibe-dashboard.json
reports/vibe-dashboard.md
reports/vibe-dashboard.html
```

## Suggested prompt

```text
Use the vibe-codebase-dashboard skill.

Analyze this repository in read-only mode and generate a one-page dashboard that evaluates whether this codebase is ready for responsible vibe coding and VibeOps.

Do not judge readiness only by whether the code builds or tests pass.

Evaluate the repository across context, skills, agents, VibeOps, critical validation, human ownership, tools/MCP, tests, build/deploy, and security/governance.

Output the overall score, grade, one-minute summary, VibeOps 4-factor table, top gaps, red flags, quick wins, evidence table, and recommended files to create.
```

## License

MIT
