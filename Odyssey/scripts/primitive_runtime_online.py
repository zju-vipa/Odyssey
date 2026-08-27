#!/usr/bin/env python3
"""Run state-based Minecraft fixtures for selected Odyssey primitives."""

from __future__ import annotations

import argparse
import json
import math
from http.client import RemoteDisconnected
from pathlib import Path
from urllib import error, request


ODYSSEY_ROOT = Path(__file__).resolve().parents[1]
CONTROL_ROOT = ODYSSEY_ROOT / "odyssey" / "control_primitives"
PRIMITIVE_ROOT = ODYSSEY_ROOT / "skill_library" / "skill" / "primitive"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def get_json(url: str, timeout: int):
    with request.urlopen(url, timeout=timeout) as response:
        return json.load(response)


def post_json(url: str, payload: dict, timeout: int):
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=timeout) as response:
        return json.load(response)


def parse_observation(value):
    if isinstance(value, str):
        return json.loads(value)
    return value


def event_values(observation: list, event_name: str) -> list:
    return [
        event.get(event_name, event) if isinstance(event, dict) else event
        for event_type, event in observation
        if event_type == event_name
    ]


def final_observe(observation: list) -> dict | None:
    events = [
        event
        for event_type, event in observation
        if event_type == "observe" and isinstance(event, dict)
    ]
    return events[-1] if events else None


def position_distance(position: dict | None, target: dict) -> float:
    if not isinstance(position, dict):
        return math.inf
    values = [position.get(axis) for axis in ("x", "y", "z")]
    if not all(isinstance(value, (int, float)) for value in values):
        return math.inf
    return math.dist(values, [target[axis] for axis in ("x", "y", "z")])


def block_position_distance(position: dict | None, target: dict) -> float:
    """Measure distance with the block-grid semantics used by GoalNear."""
    if not isinstance(position, dict):
        return math.inf
    position_values = [position.get(axis) for axis in ("x", "y", "z")]
    target_values = [target.get(axis) for axis in ("x", "y", "z")]
    if not all(
        isinstance(value, (int, float))
        for value in position_values + target_values
    ):
        return math.inf
    return math.dist(
        [math.floor(value) for value in position_values],
        [math.floor(value) for value in target_values],
    )


def add_target_arguments(subparser) -> None:
    subparser.add_argument("--x", type=float)
    subparser.add_argument("--y", type=float)
    subparser.add_argument("--z", type=float)
    subparser.add_argument("--dx", type=float)
    subparser.add_argument("--dy", type=float)
    subparser.add_argument("--dz", type=float)


def resolve_target(args, start_position: dict | None) -> dict:
    absolute = [args.x, args.y, args.z]
    relative = [args.dx, args.dy, args.dz]
    if all(value is not None for value in absolute) and all(
        value is None for value in relative
    ):
        return dict(zip(("x", "y", "z"), absolute, strict=True))
    if all(value is None for value in absolute) and any(
        value is not None for value in relative
    ):
        if not isinstance(start_position, dict):
            raise ValueError("bridge health did not return a bot position")
        return {
            axis: start_position[axis] + (delta if delta is not None else 0)
            for axis, delta in zip(
                ("x", "y", "z"), relative, strict=True
            )
        }
    raise ValueError(
        "provide either all of --x/--y/--z or at least one of --dx/--dy/--dz"
    )


def build_fixture(args, target: dict) -> tuple[str, str]:
    if args.primitive == "goto":
        programs = read_text(PRIMITIVE_ROOT / "goto.js")
        code = (
            f"await goto(bot, {target['x']}, {target['y']}, {target['z']}, "
            f"{args.primitive_timeout_ms});"
        )
        return programs, code

    programs = "\n\n".join(
        [
            read_text(CONTROL_ROOT / "exploreUntil.js"),
            read_text(PRIMITIVE_ROOT / "goto.js"),
            read_text(PRIMITIVE_ROOT / "getAnimal.js"),
        ]
    )
    animal_type = json.dumps(args.type)
    code = (
        f"await getAnimal(bot, {animal_type}, "
        f"{target['x']}, {target['y']}, {target['z']});"
    )
    return programs, code


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bridge", default="http://127.0.0.1:3000")
    parser.add_argument("--timeout", type=int, default=180)
    subparsers = parser.add_subparsers(dest="primitive", required=True)

    goto_parser = subparsers.add_parser("goto")
    add_target_arguments(goto_parser)
    goto_parser.add_argument("--primitive-timeout-ms", type=int, default=30000)

    animal_parser = subparsers.add_parser("get-animal")
    animal_parser.add_argument(
        "--type", choices=["sheep", "cow", "chicken", "pig"], required=True
    )
    add_target_arguments(animal_parser)

    args = parser.parse_args()
    base_url = args.bridge.rstrip("/")

    try:
        health_before = get_json(f"{base_url}/health", 5)
        if not health_before.get("bot", {}).get("connected"):
            print("FAIL: bridge has no connected bot; call /start first")
            return 2
        try:
            target = resolve_target(
                args, health_before.get("bot", {}).get("position")
            )
        except (KeyError, TypeError, ValueError) as exc:
            parser.error(str(exc))
        programs, code = build_fixture(args, target)
        observation = parse_observation(
            post_json(
                f"{base_url}/step",
                {"programs": programs, "code": code},
                args.timeout,
            )
        )
    except (error.URLError, RemoteDisconnected, TimeoutError) as exc:
        print(f"FAIL: Mineflayer request failed: {exc}")
        return 2

    final = final_observe(observation)
    if not final:
        print(json.dumps(observation, indent=2))
        print("FAIL: bridge returned no final observe event")
        return 1

    on_error = event_values(observation, "onError")
    on_chat = event_values(observation, "onChat")
    status = final.get("status", {})
    final_position = status.get("position")
    bot_distance = position_distance(final_position, target)
    bot_block_distance = block_position_distance(final_position, target)
    result = {
        "primitive": args.primitive,
        "target": target,
        "start_position": health_before.get("bot", {}).get("position"),
        "final_position": final_position,
        "bot_distance_to_target": bot_distance,
        "bot_block_distance_to_target": bot_block_distance,
        "onChat": on_chat,
        "onError": on_error,
    }

    if args.primitive == "goto":
        passed = not on_error and bot_block_distance <= 2
    else:
        animal_distance = status.get("entities", {}).get(args.type)
        result["animal_type"] = args.type
        result["animal_distance_to_bot"] = animal_distance
        passed = (
            not on_error
            and bot_block_distance <= 2
            and isinstance(animal_distance, (int, float))
            and animal_distance <= 4
        )

    result["passed"] = passed
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(
        f"{'PASS' if passed else 'FAIL'}: "
        f"{args.primitive} state-based online fixture"
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
