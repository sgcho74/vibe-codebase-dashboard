# VibeOps Rubric

VibeOps evaluates whether AI-generated or AI-assisted code can move toward production responsibly.

The four required factors are:

1. Confidence
2. Explainability
3. Blast Radius
4. Evidence of Review

---

## 1. Confidence

Question:
Can we trust that the code works under expected and unexpected conditions?

Evidence:
- unit tests
- integration tests
- regression tests
- coverage reports
- CI success
- manual verification logs
- performance checks

Weak signals:
- tests only cover happy path
- no coverage report
- no CI
- no test command documented

High risk cases:
- payment
- authentication
- authorization
- database migration
- customer-facing API
- production workflow
- batch processing
- security-sensitive logic

Recommended action:
Require automated tests and critical validation before merge.

---

## 2. Explainability

Question:
Can a human explain why the implementation is designed this way?

Evidence:
- ADR
- PR description
- design notes
- comments explaining complex logic
- diagrams
- trade-off documentation

Weak signals:
- AI-generated code without explanation
- complex logic without comments
- no architecture document
- no decision history

Recommended action:
Require ADR or design note for non-trivial changes.

---

## 3. Blast Radius

Question:
What can break if this change is wrong?

Evidence:
- dependency map
- API impact analysis
- DB migration impact analysis
- affected modules list
- rollback plan
- feature flag
- test scope mapping

Weak signals:
- no module boundary
- no dependency documentation
- no rollback procedure
- direct DB changes without migration notes

Recommended action:
Require blast radius analysis for risky changes.

---

## 4. Evidence of Review

Question:
Is there proof that a human reviewed and accepted the change?

Evidence:
- PR approval
- reviewer comments
- checklist
- test report
- security review
- release approval
- audit trail

Weak signals:
- direct push to main
- no CODEOWNERS
- no review policy
- AI-generated changes merged without human approval

Recommended action:
Require reviewer and owner approval before merge.
