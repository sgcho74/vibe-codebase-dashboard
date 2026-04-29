from pathlib import Path
import json
import fnmatch

ROOT = Path.cwd()

PATTERNS = {
    "context": [
        "README.md",
        "CLAUDE.md",
        "docs/architecture.md",
        "docs/runbook.md",
        "docs/**/*.md",
    ],
    "skills": [
        ".claude/skills/**/SKILL.md",
        "skills/**/SKILL.md",
    ],
    "agents": [
        "AGENTS.md",
        ".claude/agents/**",
        "agents.yml",
        "agents.yaml",
    ],
    "tools_mcp": [
        ".mcp.json",
        "mcp.json",
        "tools.json",
        "tool-config.yaml",
    ],
    "ownership": [
        "CODEOWNERS",
        ".github/CODEOWNERS",
        "OWNERS",
        "CONTRIBUTING.md",
        "SECURITY.md",
    ],
    "tests": [
        "tests/**",
        "__tests__/**",
        "test/**",
        "spec/**",
        "*.test.*",
        "*.spec.*",
    ],
    "quality": [
        ".eslintrc*",
        "eslint.config.*",
        "pyproject.toml",
        "mypy.ini",
        "pyrightconfig.json",
        "ruff.toml",
        "sonar-project.properties",
    ],
    "cicd": [
        ".github/workflows/**",
        ".gitlab-ci.yml",
        "Jenkinsfile",
        "azure-pipelines.yml",
    ],
    "build_deploy": [
        "Dockerfile",
        "docker-compose.yml",
        "Makefile",
        "package.json",
        "pom.xml",
        "build.gradle",
        "pyproject.toml",
        "requirements.txt",
        "docs/deployment.md",
        "docs/rollback.md",
    ],
    "security": [
        ".env.example",
        "SECURITY.md",
        ".gitleaks.toml",
        "semgrep.yml",
        "dependabot.yml",
        ".github/dependabot.yml",
    ],
}

EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
    "target",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "reports",
}


def all_repo_files():
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        files.append(path)
    return files


def match_files(patterns):
    files = []
    for file in all_repo_files():
        rel = str(file.relative_to(ROOT)).replace("\\", "/")
        for pattern in patterns:
            if fnmatch.fnmatch(rel, pattern):
                files.append(rel)
                break
    return sorted(set(files))


def main():
    result = {}
    for category, patterns in PATTERNS.items():
        result[category] = match_files(patterns)

    report_dir = ROOT / "reports"
    report_dir.mkdir(exist_ok=True)

    output = report_dir / "repo-scan.json"
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
