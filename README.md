# Vibe Codebase Dashboard Skill

`vibe-codebase-dashboard`는 코드베이스가 **Responsible Vibe Coding**과 **VibeOps** 구조에 적합한지 진단하는 Agent Skill입니다.

핵심 목적은 단순히 “AI가 코드를 빠르게 작성할 수 있는가”를 보는 것이 아니라, **AI가 만든 코드를 사람이 책임지고 검증·설명·운영할 수 있는 구조인지** 확인하는 것입니다.

---

## 핵심 메시지

> AI-generated code is untrusted until verified.  
> Surface completeness is not correctness.  
> Human owner responsibility cannot be outsourced.

바이브 코딩은 개발 속도를 높일 수 있지만, 운영 가능한 코드로 만들기 위해서는 다음 요소가 필요합니다.

- 명확한 프로젝트 컨텍스트
- 역할이 분리된 AI Agent 운영 구조
- 반복 작업을 표준화한 Skill
- 테스트와 품질 게이트
- 사람이 검토한 증거
- 변경 영향 범위 분석
- 보안·권한·릴리즈 통제
- 운영 전 VibeOps 준비도 점검

---

## 주요 기능

이 스킬은 코드베이스를 Read-only로 탐색한 뒤, 아래 항목을 기준으로 대시보드를 생성합니다.

| 평가영역 | 설명 |
|---|---|
| Context Readiness | AI가 프로젝트 목적, 구조, 제약조건을 이해할 수 있는가 |
| Skill Readiness | 반복 작업이 재사용 가능한 Skill로 표준화되어 있는가 |
| Agent Role Readiness | Architect, Coder, Reviewer, Tester 역할이 분리되어 있는가 |
| VibeOps Readiness | Confidence, Explainability, Blast Radius, Evidence 기준을 충족하는가 |
| Critical Validation Readiness | 엣지케이스, 실패 시나리오, 보안 검증이 가능한가 |
| Human Ownership Readiness | 코드 Owner, Reviewer, Approver, 운영 책임자가 명확한가 |
| Tool / MCP Readiness | AI 도구와 외부 시스템 접근이 통제되어 있는가 |
| Test & Quality Readiness | 테스트, 린트, 타입체크, 커버리지 검증이 있는가 |
| Build / Deploy Readiness | 실행, 빌드, 배포, 롤백 경로가 재현 가능한가 |
| Security & Governance Readiness | 비밀정보, 권한, 감사, 보안 기준이 있는가 |

---

## VibeOps 4대 기준

이 스킬은 VibeOps 관점에서 아래 4개 요소를 별도로 평가합니다.

| 기준 | 핵심 질문 |
|---|---|
| Confidence | AI가 만든 코드가 정상 동작한다는 근거가 있는가 |
| Explainability | 왜 이렇게 구현했는지 사람이 설명할 수 있는가 |
| Blast Radius | 변경 실패 시 어떤 범위까지 영향이 있는가 |
| Evidence of Review | 사람이 검토하고 승인한 증거가 있는가 |

---

## 디렉터리 구조

```text
vibe-codebase-dashboard/
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── .github/
│   └── workflows/
│       └── smoke-test.yml
├── .claude/
│   └── skills/
│       ├── code-review/
│       │   └── SKILL.md
│       ├── critical-validation/
│       │   └── SKILL.md
│       ├── blast-radius-analysis/
│       │   └── SKILL.md
│       ├── test-generation/
│       │   └── SKILL.md
│       ├── security-review/
│       │   └── SKILL.md
│       ├── architecture-decision/
│       │   └── SKILL.md
│       ├── vibeops-readiness/
│       │   └── SKILL.md
│       └── release-readiness/
│           └── SKILL.md
├── scripts/
│   ├── scan_repo.py
│   ├── score_vibe_readiness.py
│   ├── render_dashboard.py
│   ├── analyze_blast_radius.py
│   └── detect_review_evidence.py
├── references/
│   ├── vibe-rubric.md
│   ├── vibeops-rubric.md
│   ├── critical-validation-checklist.md
│   ├── human-ownership-checklist.md
│   ├── evidence-patterns.md
│   └── dashboard-schema.md
├── assets/
│   └── dashboard-template.html
└── reports/
    └── .gitkeep

---

## 권장운영방식

```text
[코드베이스 탐색]
        ↓
[Context / Skill / Agent / MCP / Test / CI 파일 탐지]
        ↓
[VibeOps 4대 기준 평가]
 Confidence / Explainability / Blast Radius / Evidence
        ↓
[Critical Validation 평가]
 Edge Case / Failure / Security / Rollback
        ↓
[Human Ownership 평가]
 Owner / Reviewer / Approver / Release Owner
        ↓
[100점 기준 점수화]
        ↓
[1분 대시보드 생성]
        ↓
[Top 5 Gap / Red Flag / Quick Win 도출]
