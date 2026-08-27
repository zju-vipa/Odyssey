#!/usr/bin/env python3
"""Run the E0 atomic regressions and preserve machine-readable evidence."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib import error, request


ODYSSEY_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ODYSSEY_ROOT.parent
BRIDGE_ROOT = ODYSSEY_ROOT / "odyssey" / "env" / "mineflayer"
DEFAULT_RESULTS_ROOT = ODYSSEY_ROOT / "odyssey" / "env" / "results" / "e0"
TASKS = {
    "mine_wood": ODYSSEY_ROOT / "scripts" / "smoke_test_mine_wood.py",
    "crafting_table": ODYSSEY_ROOT
    / "scripts"
    / "smoke_test_crafting_table.py",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def http_json(method: str, url: str, payload: dict | None, timeout: int):
    data = None if payload is None else json.dumps(payload).encode()
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method=method,
    )
    try:
        with request.urlopen(req, timeout=timeout) as response:
            return response.status, json.load(response)
    except error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = {"raw": body}
        return exc.code, parsed


def command_snapshot(command: list[str], cwd: Path) -> dict:
    completed = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def parse_first_json(text: str):
    start = text.find("{")
    if start < 0:
        return None
    try:
        value, _ = json.JSONDecoder().raw_decode(text[start:])
        return value
    except json.JSONDecodeError:
        return None


def task_passed(task: str, returncode: int, result: dict | None) -> bool:
    if returncode != 0 or not isinstance(result, dict):
        return False
    if result.get("onError"):
        return False
    if task == "mine_wood":
        return result.get("log_delta", 0) >= 1
    return result.get("crafting_table_delta", 0) >= 1


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bridge", default="http://127.0.0.1:3000")
    parser.add_argument("--mc-host", default="127.0.0.1")
    parser.add_argument("--mc-port", type=int, default=25565)
    parser.add_argument("--username", default="bot")
    parser.add_argument("--wait-ticks", type=int, default=20)
    parser.add_argument("--runs", type=int, default=10)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument(
        "--task",
        action="append",
        choices=sorted(TASKS),
        help="Task to run; repeat for multiple tasks. Defaults to both.",
    )
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    tasks = args.task or list(TASKS)
    run_id = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S%z")
    output_dir = args.output_dir or DEFAULT_RESULTS_ROOT / run_id
    output_dir.mkdir(parents=True, exist_ok=False)

    base_url = args.bridge.rstrip("/")
    health_status, health = http_json("GET", f"{base_url}/health", None, 10)
    version_status, version = http_json("GET", f"{base_url}/version", None, 10)
    if health_status != 200 or version_status != 200:
        write_json(
            output_dir / "startup_failure.json",
            {
                "health_status": health_status,
                "health": health,
                "version_status": version_status,
                "version": version,
            },
        )
        print(f"FAIL: bridge health/version check; evidence={output_dir}")
        return 2

    snapshot = {
        "run_id": run_id,
        "started_at": utc_now(),
        "bridge_url": base_url,
        "minecraft": {
            "host": args.mc_host,
            "port": args.mc_port,
            "username": args.username,
        },
        "runs_per_task": args.runs,
        "tasks": tasks,
        "health": health,
        "version": version,
        "git": command_snapshot(
            ["git", "status", "--short", "--branch"], REPO_ROOT
        ),
        "dependency_tree": command_snapshot(
            ["npm", "ls", "--depth=0", "--json"], BRIDGE_ROOT
        ),
    }
    write_json(output_dir / "environment.json", snapshot)

    records = []
    for task in tasks:
        for run_number in range(1, args.runs + 1):
            reset_payload = {
                "host": args.mc_host,
                "port": args.mc_port,
                "username": args.username,
                "waitTicks": args.wait_ticks,
                "reset": "hard",
            }
            reset_started = time.perf_counter()
            reset_status, reset_response = http_json(
                "POST",
                f"{base_url}/start",
                reset_payload,
                args.timeout,
            )
            reset_latency_ms = round(
                (time.perf_counter() - reset_started) * 1000, 3
            )

            action_started = time.perf_counter()
            if reset_status == 200:
                completed = subprocess.run(
                    [
                        sys.executable,
                        str(TASKS[task]),
                        "--bridge",
                        base_url,
                        "--timeout",
                        str(args.timeout),
                    ],
                    cwd=REPO_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                returncode = completed.returncode
                stdout = completed.stdout
                stderr = completed.stderr
                result = parse_first_json(stdout)
            else:
                returncode = None
                stdout = ""
                stderr = "reset failed"
                result = None
            action_latency_ms = round(
                (time.perf_counter() - action_started) * 1000, 3
            )
            health_after_status, health_after = http_json(
                "GET", f"{base_url}/health", None, 10
            )
            passed = reset_status == 200 and task_passed(
                task, returncode, result
            )
            record = {
                "task": task,
                "run": run_number,
                "started_at": utc_now(),
                "passed": passed,
                "reset": {
                    "status": reset_status,
                    "latency_ms": reset_latency_ms,
                    "response": reset_response,
                },
                "action": {
                    "returncode": returncode,
                    "latency_ms": action_latency_ms,
                    "result": result,
                    "stdout": stdout,
                    "stderr": stderr,
                },
                "health_after": {
                    "status": health_after_status,
                    "response": health_after,
                },
            }
            records.append(record)
            write_json(
                output_dir / f"{task}_{run_number:02d}.json", record
            )
            print(
                f"{task} {run_number}/{args.runs}: "
                f"{'PASS' if passed else 'FAIL'} "
                f"reset={reset_latency_ms}ms action={action_latency_ms}ms"
            )

    minecraft_log = (
        ODYSSEY_ROOT / "runtime" / "minecraft" / "data" / "logs" / "latest.log"
    )
    if minecraft_log.exists():
        shutil.copy2(minecraft_log, output_dir / "minecraft_latest.log")

    summary = {
        "run_id": run_id,
        "finished_at": utc_now(),
        "output_dir": str(output_dir),
        "total": len(records),
        "passed": sum(record["passed"] for record in records),
        "failed": sum(not record["passed"] for record in records),
        "by_task": {
            task: {
                "total": sum(record["task"] == task for record in records),
                "passed": sum(
                    record["task"] == task and record["passed"]
                    for record in records
                ),
                "action_latency_ms": [
                    record["action"]["latency_ms"]
                    for record in records
                    if record["task"] == task
                ],
            }
            for task in tasks
        },
    }
    write_json(output_dir / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
