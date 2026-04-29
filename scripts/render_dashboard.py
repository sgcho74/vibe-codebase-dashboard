import json
from pathlib import Path

ROOT = Path.cwd()
REPORT_DIR = ROOT / "reports"
DATA_FILE = REPORT_DIR / "vibe-dashboard.json"


def render_markdown(data):
    overall = data["overall"]

    md = []
    md.append("# Vibe Coding Readiness Dashboard")
    md.append("")
    md.append("## Overall")
    md.append("")
    md.append("| 항목 | 결과 |")
    md.append("|---|---:|")
    md.append(f"| Vibe Readiness Score | {overall['score']} / 100 |")
    md.append(f"| Grade | {overall['grade']} |")
    md.append(f"| Status | {overall['status']} |")
    md.append(f"| Primary Risk | {overall['primary_risk']} |")
    md.append(f"| Recommended First Action | {overall['recommended_first_action']} |")
    md.append("")

    md.append("## 1분 요약")
    md.append("")
    md.append("| 질문 | 판단 |")
    md.append("|---|---|")
    md.append("| AI가 코드베이스를 이해할 수 있는가 | Context 점수 기준 판단 필요 |")
    md.append("| AI가 안전하게 수정할 수 있는가 | Test / Quality / VibeOps 기준 판단 필요 |")
    md.append("| 사람이 책임지고 검증하는 구조인가 | Ownership / Review Evidence 기준 판단 필요 |")
    md.append("| 운영 배포 가능한 수준인가 | Build / Deploy / Security 기준 판단 필요 |")
    md.append("| 가장 큰 리스크 | " + overall["primary_risk"] + " |")
    md.append("")

    md.append("## VibeOps 4대 준비도")
    md.append("")
    md.append("| 기준 | 점수 | 근거 파일 수 |")
    md.append("|---|---:|---:|")
    for name, item in data["vibeops"].items():
        md.append(f"| {name} | {item['score']} / 10 | {len(item['evidence'])} |")
    md.append("")

    md.append("## Dimension Score")
    md.append("")
    md.append("| 영역 | 가중치 | 점수 | 상태 |")
    md.append("|---|---:|---:|---|")
    for d in data["dimensions"]:
        md.append(f"| {d['name']} | {d['weight']} | {d['weighted_score']} | {d['status']} |")
    md.append("")

    md.append("## Top 5 Gaps")
    md.append("")
    md.append("| 우선순위 | Gap |")
    md.append("|---:|---|")
    for i, gap in enumerate(data["top_gaps"], start=1):
        md.append(f"| {i} | {gap} |")
    md.append("")

    md.append("## Top 5 Red Flags")
    md.append("")
    md.append("| 우선순위 | Red Flag |")
    md.append("|---:|---|")
    for i, flag in enumerate(data["red_flags"][:5], start=1):
        md.append(f"| {i} | {flag} |")
    md.append("")

    md.append("## Top 5 Quick Wins")
    md.append("")
    md.append("| 우선순위 | Action |")
    md.append("|---:|---|")
    for i, action in enumerate(data["quick_wins"], start=1):
        md.append(f"| {i} | {action} |")
    md.append("")

    md.append("## Recommended Files")
    md.append("")
    for file in data["recommended_files"]:
        md.append(f"- {file}")
    md.append("")

    return "\n".join(md)


def render_html(markdown_text):
    escaped = markdown_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f"""
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title>Vibe Coding Readiness Dashboard</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 32px;
      background: #f7f7f7;
      color: #222;
    }}
    .container {{
      max-width: 1200px;
      margin: auto;
      background: white;
      padding: 32px;
      border-radius: 16px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }}
    pre {{
      white-space: pre-wrap;
      font-size: 14px;
      line-height: 1.5;
    }}
  </style>
</head>
<body>
  <div class="container">
    <pre>{escaped}</pre>
  </div>
</body>
</html>
"""


def main():
    if not DATA_FILE.exists():
        raise SystemExit("reports/vibe-dashboard.json not found. Run scripts/score_vibe_readiness.py first.")

    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    md = render_markdown(data)
    html = render_html(md)

    REPORT_DIR.mkdir(exist_ok=True)
    (REPORT_DIR / "vibe-dashboard.md").write_text(md, encoding="utf-8")
    (REPORT_DIR / "vibe-dashboard.html").write_text(html, encoding="utf-8")

    print(md)


if __name__ == "__main__":
    main()
