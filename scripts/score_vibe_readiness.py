import json
from pathlib import Path

ROOT = Path.cwd()
SCAN_FILE = ROOT / "reports" / "repo-scan.json"

DIMENSIONS = [
    ("Context Readiness", "context", 10),
    ("Skill Readiness", "skills", 10),
    ("Agent Role Readiness", "agents", 10),
    ("Tool / MCP Readiness", "tools_mcp", 10),
    ("Human Ownership Readiness", "ownership", 10),
    ("Test & Quality Readiness", "tests", 10),
    ("Build / Deploy Readiness", "build_deploy", 5),
    ("Security & Governance Readiness", "security", 5),
]


def status_from_score(score):
    if score >= 85:
        return "A", "AI coding-ready and VibeOps-ready"
    if score >= 70:
        return "B", "Usable with minor gaps"
    if score >= 55:
        return "C", "Needs standardization before serious use"
    if score >= 40:
        return "D", "Risky for autonomous AI coding"
    return "E", "Not ready"


def base_score(evidence_count):
    if evidence_count == 0:
        return 0
    if evidence_count == 1:
        return 1
    if evidence_count <= 3:
        return 2
    if evidence_count <= 6:
        return 3
    return 4


def weighted(level, weight):
    return round((level / 4) * weight, 1)


def score_vibeops(scan):
    confidence_evidence = scan.get("tests", []) + scan.get("quality", []) + scan.get("cicd", [])
    explainability_evidence = [
        f for f in scan.get("context", [])
        if "architecture" in f.lower() or "adr" in f.lower() or "readme" in f.lower()
    ]
    blast_radius_evidence = [
        f for f in scan.get("context", [])
        if "architecture" in f.lower() or "dependency" in f.lower() or "rollback" in f.lower()
    ] + scan.get("build_deploy", [])
    review_evidence = scan.get("ownership", []) + scan.get("cicd", [])

    factors = {
        "Confidence": confidence_evidence,
        "Explainability": explainability_evidence,
        "Blast Radius": blast_radius_evidence,
        "Evidence of Review": review_evidence,
    }

    result = {}
    total_level = 0

    for name, evidence in factors.items():
        level = base_score(len(evidence))
        total_level += level
        result[name] = {
            "level": level,
            "score": round((level / 4) * 10, 1),
            "evidence": evidence,
        }

    vibeops_weighted = round((total_level / 16) * 15, 1)
    return result, vibeops_weighted


def score_critical_validation(scan):
    evidence = scan.get("tests", []) + scan.get("quality", []) + scan.get("cicd", []) + scan.get("security", [])
    level = base_score(len(evidence))

    if scan.get("tests") and not scan.get("cicd"):
        level = min(level, 2)

    weighted_score = weighted(level, 15)

    return {
        "level": level,
        "weighted_score": weighted_score,
        "evidence": evidence,
    }


def main():
    if not SCAN_FILE.exists():
        raise SystemExit("reports/repo-scan.json not found. Run scripts/scan_repo.py first.")

    scan = json.loads(SCAN_FILE.read_text(encoding="utf-8"))

    dimensions = []
    total = 0

    for name, key, weight in DIMENSIONS:
        evidence = scan.get(key, [])
        level = base_score(len(evidence))
        wscore = weighted(level, weight)
        total += wscore

        dimensions.append({
            "name": name,
            "weight": weight,
            "level": level,
            "weighted_score": wscore,
            "evidence": evidence,
            "status": "missing" if level == 0 else "partial" if level < 3 else "good",
        })

    vibeops, vibeops_score = score_vibeops(scan)
    total += vibeops_score

    dimensions.append({
        "name": "VibeOps Readiness",
        "weight": 15,
        "level": round((vibeops_score / 15) * 4, 1),
        "weighted_score": vibeops_score,
        "evidence": vibeops,
        "status": "partial" if vibeops_score < 10 else "good",
    })

    critical = score_critical_validation(scan)
    total += critical["weighted_score"]

    dimensions.append({
        "name": "Critical Validation Readiness",
        "weight": 15,
        "level": critical["level"],
        "weighted_score": critical["weighted_score"],
        "evidence": critical["evidence"],
        "status": "partial" if critical["level"] < 3 else "good",
    })

    grade, status = status_from_score(total)

    red_flags = []
    if not scan.get("ownership"):
        red_flags.append("No CODEOWNERS / ownership evidence found")
    if not scan.get("cicd"):
        red_flags.append("No CI/CD quality gate found")
    if not scan.get("tests"):
        red_flags.append("No test suite found")
    if not scan.get("security"):
        red_flags.append("No security governance evidence found")
    if not scan.get("tools_mcp"):
        red_flags.append("No MCP / controlled AI tool configuration found")
    if not scan.get("context"):
        red_flags.append("No project context documentation found")
    if not scan.get("skills"):
        red_flags.append("No reusable AI skills found")
    if not scan.get("agents"):
        red_flags.append("No agent role separation found")

    top_gaps = red_flags[:5]

    quick_wins = [
        "Create CLAUDE.md",
        "Create AGENTS.md",
        "Create CODEOWNERS",
        "Create .claude/skills/code-review/SKILL.md",
        "Create .claude/skills/critical-validation/SKILL.md",
        "Create .mcp.json with approved tools and permission boundaries",
        "Add CI workflow for test, lint, typecheck, and secret scan",
        "Create docs/architecture.md",
        "Create docs/rollback.md",
    ]

    result = {
        "overall": {
            "score": round(total, 1),
            "grade": grade,
            "status": status,
            "primary_risk": top_gaps[0] if top_gaps else "No major risk detected",
            "recommended_first_action": quick_wins[0],
        },
        "dimensions": dimensions,
        "vibeops": vibeops,
        "red_flags": red_flags,
        "top_gaps": top_gaps,
        "quick_wins": quick_wins[:5],
        "recommended_files": quick_wins,
    }

    output = ROOT / "reports" / "vibe-dashboard.json"
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
