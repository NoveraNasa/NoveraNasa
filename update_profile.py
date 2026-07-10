from __future__ import annotations

import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USERNAME = os.getenv("GITHUB_USERNAME", "NoveraNasa")
TOKEN = os.getenv("GITHUB_TOKEN", "")
ROOT = Path(__file__).resolve().parent


def request_json(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "NoveraNasa-profile-readme",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def collect_stats() -> dict[str, str]:
    user = request_json(f"https://api.github.com/users/{USERNAME}")
    repos = request_json(
        f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner&sort=updated"
    )
    stars = sum(int(repo.get("stargazers_count", 0)) for repo in repos if not repo.get("fork"))
    return {
        "REPOS": str(user.get("public_repos", len(repos))),
        "FOLLOWERS": str(user.get("followers", 0)),
        "STARS": str(stars),
        "UPDATED": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }


def render(template_name: str, output_name: str, stats: dict[str, str]) -> None:
    content = (ROOT / template_name).read_text(encoding="utf-8")
    for key, value in stats.items():
        content = content.replace("{{" + key + "}}", value)
    (ROOT / output_name).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    stats = collect_stats()
    render("dark_mode.template.svg", "dark_mode.svg", stats)
    render("light_mode.template.svg", "light_mode.svg", stats)
    print(f"Updated profile for {USERNAME}: {stats}")
