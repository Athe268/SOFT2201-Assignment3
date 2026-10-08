"""Print separate statement and branch percentages from coverage JSON."""

import json
import sys
from pathlib import Path


def percentage(covered: int, total: int) -> str:
    """Format one percentage using one decimal place."""
    if total == 0:
        return "n/a"
    return f"{covered * 100 / total:.1f}%"


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "coverage.json")
    report = json.loads(path.read_text(encoding="utf-8"))
    for filename, details in sorted(report["files"].items()):
        summary = details["summary"]
        statements = percentage(
            summary["covered_lines"], summary["num_statements"]
        )
        branches = percentage(
            summary["covered_branches"], summary["num_branches"]
        )
        print(f"{filename}: statements {statements}, branches {branches}")


if __name__ == "__main__":
    main()
