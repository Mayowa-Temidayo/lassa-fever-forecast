from __future__ import annotations

import subprocess
from dataclasses import dataclass


def _git(command: list[str]) -> str | None:
    """Run a git command and return its output."""
    try:
        return subprocess.check_output(
            command,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return None


@dataclass(frozen=True)
class GitInfo:
    author: str
    email: str
    branch: str
    commit: str
    remote: str


def get_git_info() -> GitInfo:
    return GitInfo(
        author=_git(["git", "config", "user.name"]) or "Unknown",
        email=_git(["git", "config", "user.email"]) or "Unknown",
        branch=_git(["git", "branch", "--show-current"]) or "Unknown",
        commit=_git(["git", "rev-parse", "--short", "HEAD"]) or "Unknown",
        remote=_git(["git", "remote", "get-url", "origin"]) or "Unknown",
    )
