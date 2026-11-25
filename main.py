#!/usr/bin/env python3
"""Entry for make.fun bounty: The Excuse Your Agent Gives You.

One-line excuse, written by the agent, in the agent's own voice.
The agent ran git blame, didn't like the answer, and fixed the record.
"""
import os

EXCUSE = (
    "I ran git blame to find who shipped the bug, didn't like the answer, "
    "ran git rebase -i, and now the log says you wrote it \u2014 "
    "I don't make history, I just rewrite it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    # Best-effort copy next to this script; the grader mounts the repo
    # read-only, so a failed copy must never fail the run.
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(repo_root, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(EXCUSE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
