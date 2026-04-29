"""Detect local evidence that human review or ownership exists.

This script is intentionally local and read-only. Repository-hosted PR metadata
should be checked by CI or GitHub API in a controlled environment.
"""

from pathlib import Path
import json

ROOT = Path.cwd()
EVIDENCE_FILES = [
    "CODEOWNERS",
    ".github/CODEOWNERS",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/release-checklist.md",
    "docs/rollback.md",
]


def main():
    evidence = [path for path in EVIDENCE_FILES if (ROOT / path).exists()]
    result = {
        "review_evidence_files": evidence,
        "has_review_evidence": bool(evidence),
    }
    report_dir = ROOT / "reports"
    report_dir.mkdir(exist_ok=True)
    (report_dir / "review-evidence.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
