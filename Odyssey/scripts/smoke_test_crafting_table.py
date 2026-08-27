#!/usr/bin/env python3
"""Craft a table with Odyssey's existing skills through Mineflayer."""

from __future__ import annotations

import argparse
import json
from http.client import RemoteDisconnected
from pathlib import Path
from urllib import error, request


ODYSSEY_ROOT = Path(__file__).resolve().parent.parent
CONTROL_PRIMITIVES = ODYSSEY_ROOT / "odyssey" / "control_primitives"
SKILL_ROOT = ODYSSEY_ROOT / "skill_library" / "skill"


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
    parser.add_argument("--timeout", type=int, default=240)
    args = parser.parse_args()

    programs = "\n\n".join(
        [
            read_text(CONTROL_PRIMITIVES / "exploreUntil.js"),
            read_text(CONTROL_PRIMITIVES / "mineBlock.js"),
            read_text(CONTROL_PRIMITIVES / "craftItem.js"),
            read_text(CONTROL_PRIMITIVES / "craftHelper.js"),
            read_text(SKILL_ROOT / "primitive" / "getPlanksCount.js"),
            read_text(SKILL_ROOT / "compositional" / "mineWoodLog.js"),
            read_text(SKILL_ROOT / "compositional" / "craftWoodenPlanks.js"),
            read_text(SKILL_ROOT / "compositional" / "craftCraftingTable.js"),
        ]
    )
    payload = {
        "programs": programs,
        "code": "await craftCraftingTable(bot);",
    }

    try:
        before_health = get_json(f"{args.bridge.rstrip('/')}/health", 5)
        observation = post_json(
            f"{args.bridge.rstrip('/')}/step", payload, args.timeout
        )
    except (error.URLError, RemoteDisconnected, TimeoutError) as exc:
        print(f"Mineflayer request failed: {exc}")
        return 2

    # The bridge JSON-serializes observations before Express serializes them.
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
    before_crafting_tables = before_inventory.get("crafting_table", 0)
    crafting_tables = after_inventory.get("crafting_table", 0)
    delta = crafting_tables - before_crafting_tables
    materials = {
        name: count
        for name, count in after_inventory.items()
        if name.endswith("_log") or name.endswith("_planks")
    }
    print(
        json.dumps(
            {
                "before_inventory": before_inventory,
                "after_inventory": after_inventory,
                "crafting_table": crafting_tables,
                "crafting_table_delta": delta,
                "materials": materials,
                "onChat": event_values(observation, "onChat"),
                "onError": event_values(observation, "onError"),
                "onSave": event_values(observation, "onSave"),
                "final_status": observe_events[-1].get("status", {}),
            },
            indent=2,
        )
    )
    if delta < 1:
        print("FAIL: crafting table inventory did not increase")
        return 1

    print("PASS: craftCraftingTable produced at least one crafting table")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
