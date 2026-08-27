#!/usr/bin/env python3
"""Run Odyssey's existing mineWoodLog skill through the Mineflayer bridge."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib import error, request


ODYSSEY_ROOT = Path(__file__).resolve().parent.parent
CONTROL_PRIMITIVES = ODYSSEY_ROOT / "odyssey" / "control_primitives"
MINE_WOOD_LOG = (
    ODYSSEY_ROOT
    / "skill_library"
    / "skill"
    / "compositional"
    / "mineWoodLog.js"
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def post_json(url: str, payload: dict, timeout: int) -> dict:
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=timeout) as response:
        return json.load(response)


def get_json(url: str, timeout: int) -> dict:
    with request.urlopen(url, timeout=timeout) as response:
        return json.load(response)


def event_values(observation: list, event_name: str) -> list:
    return [
        event.get(event_name, event) if isinstance(event, dict) else event
        for event_type, event in observation
        if event_type == event_name
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bridge", default="http://127.0.0.1:3000")
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args()

    programs = "\n\n".join(
        [
            read_text(CONTROL_PRIMITIVES / "exploreUntil.js"),
            read_text(CONTROL_PRIMITIVES / "mineBlock.js"),
            read_text(MINE_WOOD_LOG),
        ]
    )
    payload = {
        "programs": programs,
        "code": "await mineWoodLog(bot);",
    }

    try:
        before_health = get_json(f"{args.bridge.rstrip('/')}/health", 5)
        observation = post_json(
            f"{args.bridge.rstrip('/')}/step", payload, args.timeout
        )
    except error.URLError as exc:
        print(f"Mineflayer request failed: {exc}")
        return 2

    # The original bridge JSON-serializes the observation before passing it to
    # Express' res.json(), so the HTTP response contains a JSON string.
    if isinstance(observation, str):
        observation = json.loads(observation)

    observe_events = [
        event for event_type, event in observation if event_type == "observe"
    ]
    if not observe_events:
        print(json.dumps(observation, indent=2))
        print("FAIL: the bridge returned no final observe event")
        return 1

    before_inventory = before_health.get("bot", {}).get("inventory", {})
    after_inventory = observe_events[-1].get("inventory", {})
    before_logs = sum(
        count
        for name, count in before_inventory.items()
        if name.endswith("_log")
    )
    after_logs = sum(
        count
        for name, count in after_inventory.items()
        if name.endswith("_log")
    )
    delta = after_logs - before_logs
    logs = {
        name: count
        for name, count in after_inventory.items()
        if name.endswith("_log") and count > 0
    }
    result = {
        "before_inventory": before_inventory,
        "after_inventory": after_inventory,
        "log_delta": delta,
        "logs": logs,
        "onChat": event_values(observation, "onChat"),
        "onError": event_values(observation, "onError"),
        "onSave": event_values(observation, "onSave"),
        "final_status": observe_events[-1].get("status", {}),
    }
    print(json.dumps(result, indent=2))
    if delta < 1:
        print("FAIL: wood log inventory did not increase")
        return 1

    print("PASS: mineWoodLog collected at least one wood log")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
