from __future__ import annotations

import subprocess
from datetime import datetime


def _run_git_command(command: list[str]) -> str:
    """Execute a Git command and return its output."""

    try:
        return subprocess.check_output(
            command,
            text=True,
        ).strip()
    except Exception:
        return "Unknown"


AUTHOR = _run_git_command(["git", "config", "user.name"])

EMAIL = _run_git_command(["git", "config", "user.email"])

BRANCH = _run_git_command(["git", "branch", "--show-current"])

COMMIT = _run_git_command(["git", "rev-parse", "--short", "HEAD"])

REMOTE = _run_git_command(["git", "remote", "get-url", "origin"])

DATE = datetime.now().strftime("%Y-%m-%d")

TIME = datetime.now().strftime("%H:%M:%S")
