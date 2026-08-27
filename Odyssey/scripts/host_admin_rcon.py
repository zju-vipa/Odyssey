#!/usr/bin/env python3
"""Host-only RCON harness for modernized Odyssey world preparation."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path


ODYSSEY_ROOT = Path(__file__).resolve().parents[1]
IDENTIFIER = re.compile(r"^[A-Za-z0-9_.:-]+$")


def identifier(value: str) -> str:
    if not IDENTIFIER.fullmatch(value):
        raise argparse.ArgumentTypeError(
            "expected a Minecraft identifier without whitespace or commands"
        )
    return value


def run_rcon(command: str, attempts: int = 10, retry_delay: float = 1.0) -> None:
    docker_command = [
        "docker",
        "compose",
        "exec",
        "-T",
        "mc",
        "rcon-cli",
        command,
    ]
    for attempt in range(1, attempts + 1):
        completed = subprocess.run(
            docker_command,
            cwd=ODYSSEY_ROOT,
            text=True,
            capture_output=True,
        )
        if completed.returncode == 0:
            if completed.stdout:
                print(completed.stdout, end="")
            if completed.stderr:
                print(completed.stderr, end="", file=sys.stderr)
            return

        failure_output = f"{completed.stdout}\n{completed.stderr}"
        rcon_startup_race = "connect: connection refused" in failure_output
        if not rcon_startup_race or attempt == attempts:
            if completed.stdout:
                print(completed.stdout, end="", file=sys.stderr)
            if completed.stderr:
                print(completed.stderr, end="", file=sys.stderr)
            raise subprocess.CalledProcessError(
                completed.returncode,
                docker_command,
                output=completed.stdout,
                stderr=completed.stderr,
            )

        print(
            f"RCON not ready; retrying in {retry_delay:g}s "
            f"({attempt}/{attempts})",
            file=sys.stderr,
        )
        time.sleep(retry_delay)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare the Minecraft server through container-local RCON. "
            "This program is for the researcher/server host, not Odyssey agents."
        )
    )
    subparsers = parser.add_subparsers(dest="action", required=True)

    prepare = subparsers.add_parser("prepare-player")
    prepare.add_argument("--player", type=identifier, default="bot")
    prepare.add_argument(
        "--gamemode",
        choices=["survival", "creative", "adventure", "spectator"],
        default="survival",
    )

    summon = subparsers.add_parser("summon-near-player")
    summon.add_argument("--player", type=identifier, default="bot")
    summon.add_argument("--entity", type=identifier, required=True)
    summon.add_argument("--count", type=int, default=1)

    command = subparsers.add_parser("command")
    command.add_argument(
        "server_command",
        help="literal server-console command supplied by the server host",
    )

    args = parser.parse_args()
    if args.action == "prepare-player":
        commands = [
            "gamerule keepInventory true",
            "gamerule doDaylightCycle false",
            f"gamemode {args.gamemode} {args.player}",
            f"clear {args.player}",
            f"kill {args.player}",
            f"deop {args.player}",
        ]
    elif args.action == "summon-near-player":
        if not 1 <= args.count <= 64:
            parser.error("--count must be between 1 and 64")
        commands = [
            f"execute at {args.player} run summon {args.entity} ~2 ~ ~"
            for _ in range(args.count)
        ]
    else:
        commands = [args.server_command]

    for server_command in commands:
        print(f"RCON> {server_command}", flush=True)
        run_rcon(server_command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
