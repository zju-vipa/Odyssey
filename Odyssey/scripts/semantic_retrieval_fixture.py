#!/usr/bin/env python3
"""Verify Odyssey top-5/top-10 retrieval across Chroma persistence reload."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
import tempfile
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = (
    REPO_ROOT / "research" / "manifest" / "odyssey_semantic_encoder.json"
)
DEFAULT_SKILLS = (
    REPO_ROOT / "Odyssey" / "skill_library" / "skill" / "skills.json"
)
COLLECTION_NAME = "odyssey_semantic_retrieval_fixture"
KNOWN_QUERIES = [
    {
        "query": "Craft a wooden pickaxe.",
        "expected_skill": "craftWoodenPickaxe",
    },
    {
        "query": "Mine diamond ore using an iron pickaxe.",
        "expected_skill": "mineDiamond",
    },
    {
        "query": "Breed two cows using wheat.",
        "expected_skill": "breedCow",
    },
    {
        "query": "밀을 사용해서 소 두 마리를 번식시킨다.",
        "expected_skill": "breedCow",
    },
]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def package_versions(names: list[str]) -> dict[str, str | None]:
    observed = {}
    for name in names:
        try:
            observed[name] = version(name)
        except PackageNotFoundError:
            observed[name] = None
    return observed


def load_embedding_module():
    source_path = REPO_ROOT / "Odyssey" / "odyssey" / "retrieval_embedding.py"
    spec = importlib.util.spec_from_file_location(
        "odyssey_retrieval_embedding_fixture", source_path
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load retrieval_embedding.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def retrieve(vector_store, query: str, k: int) -> list[dict]:
    results = vector_store.similarity_search_with_score(query, k=k)
    return [
        {
            "rank": rank,
            "skill": document.metadata["name"],
            "score": float(score),
        }
        for rank, (document, score) in enumerate(results, start=1)
    ]


def query_profiles(vector_store, profile_sizes: dict[str, int]) -> dict:
    profiles = {}
    for profile_name, k in profile_sizes.items():
        queries = []
        for fixture in KNOWN_QUERIES:
            candidates = retrieve(vector_store, fixture["query"], k)
            expected_rank = next(
                (
                    candidate["rank"]
                    for candidate in candidates
                    if candidate["skill"] == fixture["expected_skill"]
                ),
                None,
            )
            queries.append(
                {
                    **fixture,
                    "expected_rank": expected_rank,
                    "passed": expected_rank is not None,
                    "candidates": candidates,
                }
            )
        profiles[profile_name] = {
            "k": k,
            "known_query_recall_at_k": sum(
                item["passed"] for item in queries
            )
            / len(queries),
            "queries": queries,
        }
    return profiles


def worker(args) -> int:
    manifest = read_json(args.manifest.resolve())
    skills = read_json(args.skills.resolve())
    embedding_module = load_embedding_module()
    profile_sizes = dict(embedding_module.SKILL_RETRIEVAL_PROFILES)
    model_dir = REPO_ROOT / manifest["checkpoint"]["local_path"]
    embeddings = embedding_module.build_retrieval_embeddings(
        str(model_dir),
        device=args.device,
        local_files_only=True,
        wrapper_profile=args.wrapper_profile,
    )
    vector_store = embedding_module.build_retrieval_vector_store(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(args.persist_directory),
        collection_metadata={
            "hnsw:space": embedding_module.RETRIEVAL_DISTANCE_METRIC
        },
        wrapper_profile=args.wrapper_profile,
    )

    if args.worker == "build":
        names = sorted(skills)
        vector_store.add_texts(
            texts=[skills[name]["description"] for name in names],
            ids=names,
            metadatas=[{"name": name} for name in names],
        )
        embedding_module.persist_retrieval_vector_store(
            vector_store, wrapper_profile=args.wrapper_profile
        )

    count = vector_store._collection.count()
    client_settings = (
        vector_store._client.get_settings()
        if hasattr(vector_store._client, "get_settings")
        else None
    )
    result = {
        "phase": args.worker,
        "wrapper_profile": embedding_module.resolve_wrapper_profile(
            args.wrapper_profile
        ),
        "index_count": count,
        "telemetry_disabled": getattr(
            client_settings, "anonymized_telemetry", None
        )
        is False,
        "profiles": query_profiles(vector_store, profile_sizes),
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0 if count == len(skills) == 183 else 1


def run_worker(args, phase: str, persist_directory: Path) -> tuple[dict, list[str]]:
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--worker",
        phase,
        "--manifest",
        str(args.manifest.resolve()),
        "--skills",
        str(args.skills.resolve()),
        "--persist-directory",
        str(persist_directory),
        "--device",
        args.device,
        "--wrapper-profile",
        args.wrapper_profile,
    ]
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )
    warnings = [
        line.strip()
        for line in completed.stderr.splitlines()
        if "Warning" in line or "telemetry" in line.lower()
    ]
    return json.loads(completed.stdout), warnings


def compare_profiles(build: dict, reload: dict, tolerance: float) -> dict:
    comparisons = {}
    for profile_name, build_profile in build["profiles"].items():
        reload_profile = reload["profiles"][profile_name]
        query_checks = []
        for build_query, reload_query in zip(
            build_profile["queries"], reload_profile["queries"], strict=True
        ):
            build_names = [
                item["skill"] for item in build_query["candidates"]
            ]
            reload_names = [
                item["skill"] for item in reload_query["candidates"]
            ]
            score_deltas = [
                abs(before["score"] - after["score"])
                for before, after in zip(
                    build_query["candidates"],
                    reload_query["candidates"],
                    strict=True,
                )
            ]
            max_score_delta = max(score_deltas, default=0.0)
            query_checks.append(
                {
                    "query": build_query["query"],
                    "candidate_order_equal": build_names == reload_names,
                    "max_score_delta": max_score_delta,
                    "scores_equal_within_tolerance": max_score_delta
                    <= tolerance,
                }
            )
        comparisons[profile_name] = {
            "k": build_profile["k"],
            "queries": query_checks,
            "passed": all(
                item["candidate_order_equal"]
                and item["scores_equal_within_tolerance"]
                for item in query_checks
            ),
        }
    return comparisons


def compare_baseline_evidence(
    build: dict, baseline: dict, tolerance: float
) -> dict:
    baseline_queries = {
        item["query"]: item for item in baseline["fresh_index_results"]
    }
    query_checks = []
    for modern_query in build["profiles"]["top10"]["queries"]:
        legacy_candidates = baseline_queries[modern_query["query"]][
            "top10_candidates"
        ]
        modern_candidates = modern_query["candidates"]
        legacy_names = [item["skill"] for item in legacy_candidates]
        modern_names = [item["skill"] for item in modern_candidates]
        score_deltas = [
            abs(legacy["score"] - modern["score"])
            for legacy, modern in zip(
                legacy_candidates, modern_candidates, strict=True
            )
        ]
        maximum_score_delta = max(score_deltas, default=0.0)
        query_checks.append(
            {
                "query": modern_query["query"],
                "candidate_order_equal": legacy_names == modern_names,
                "maximum_score_delta": maximum_score_delta,
                "scores_equal_within_tolerance": maximum_score_delta
                <= tolerance,
            }
        )
    return {
        "score_tolerance": tolerance,
        "score_comparison_role": "diagnostic_only_across_wrapper_versions",
        "queries": query_checks,
        "candidate_order_equal_for_all": all(
            item["candidate_order_equal"] for item in query_checks
        ),
        "maximum_score_delta": max(
            (item["maximum_score_delta"] for item in query_checks),
            default=0.0,
        ),
        "scores_equal_within_tolerance_for_all": all(
            item["scores_equal_within_tolerance"] for item in query_checks
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--skills", type=Path, default=DEFAULT_SKILLS)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--score-tolerance", type=float, default=0.000001)
    parser.add_argument("--baseline-evidence", type=Path)
    parser.add_argument(
        "--baseline-score-tolerance", type=float, default=0.000001
    )
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument(
        "--wrapper-profile",
        choices=["legacy-community", "modern-partner"],
        default="modern-partner",
    )
    parser.add_argument("--worker", choices=["build", "reload"])
    parser.add_argument("--persist-directory", type=Path)
    args = parser.parse_args()

    if args.worker:
        if args.persist_directory is None:
            parser.error("--persist-directory is required for worker mode")
        return worker(args)

    manifest = read_json(args.manifest.resolve())
    embedding_module = load_embedding_module()
    profile_sizes = dict(embedding_module.SKILL_RETRIEVAL_PROFILES)
    default_profile = embedding_module.DEFAULT_SKILL_RETRIEVAL_PROFILE

    with tempfile.TemporaryDirectory(
        prefix="odyssey-retrieval-fixture-"
    ) as temp_dir:
        persist_directory = Path(temp_dir) / "index"
        build, build_warnings = run_worker(
            args, "build", persist_directory
        )
        reload, reload_warnings = run_worker(
            args, "reload", persist_directory
        )

    comparisons = compare_profiles(
        build, reload, args.score_tolerance
    )
    baseline_comparison = None
    if args.baseline_evidence is not None:
        baseline_comparison = compare_baseline_evidence(
            build,
            read_json(args.baseline_evidence.resolve()),
            args.baseline_score_tolerance,
        )
    prefix_checks = []
    for phase in (build, reload):
        for top5_query, top10_query in zip(
            phase["profiles"]["top5"]["queries"],
            phase["profiles"]["top10"]["queries"],
            strict=True,
        ):
            prefix_checks.append(
                {
                    "phase": phase["phase"],
                    "query": top5_query["query"],
                    "top5_is_top10_prefix": [
                        item["skill"] for item in top5_query["candidates"]
                    ]
                    == [
                        item["skill"]
                        for item in top10_query["candidates"][:5]
                    ],
                }
            )

    profile_contract = {
        "default_profile": default_profile,
        "profile_sizes": profile_sizes,
        "default_is_top5": default_profile == "top5"
        and profile_sizes.get("top5") == 5,
        "top10_is_separate": profile_sizes.get("top10") == 10,
    }
    passed = (
        build["index_count"] == reload["index_count"] == 183
        and profile_contract["default_is_top5"]
        and profile_contract["top10_is_separate"]
        and all(item["passed"] for item in comparisons.values())
        and all(item["top5_is_top10_prefix"] for item in prefix_checks)
        and all(
            profile["known_query_recall_at_k"] == 1.0
            for phase in (build, reload)
            for profile in phase["profiles"].values()
        )
        and (
            args.wrapper_profile != "modern-partner"
            or (
                build["telemetry_disabled"]
                and reload["telemetry_disabled"]
                and not any(
                    "telemetry" in warning.lower()
                    for warning in build_warnings + reload_warnings
                )
            )
        )
        and (
            baseline_comparison is None
            or baseline_comparison["candidate_order_equal_for_all"]
        )
    )
    output = {
        "profile": "odyssey-semantic-retrieval-persist-reload",
        "encoder_revision": manifest["checkpoint"]["revision"],
        "corpus": str(args.skills.resolve().relative_to(REPO_ROOT)),
        "corpus_count": 183,
        "distance_metric": embedding_module.RETRIEVAL_DISTANCE_METRIC,
        "canonical_device": args.device,
        "wrapper_profile": args.wrapper_profile,
        "package_versions": package_versions(
            [
                "langchain-core",
                "langchain-community",
                "langchain-huggingface",
                "langchain-chroma",
                "chromadb",
                "sentence-transformers",
                "transformers",
                "torch",
                "posthog",
            ]
        ),
        "score_tolerance": args.score_tolerance,
        "profile_contract": profile_contract,
        "build": build,
        "reload": reload,
        "reload_comparisons": comparisons,
        "legacy_wrapper_baseline_comparison": baseline_comparison,
        "profile_prefix_checks": prefix_checks,
        "warnings": sorted(set(build_warnings + reload_warnings)),
        "telemetry_warning_free": not any(
            "telemetry" in warning.lower()
            for warning in build_warnings + reload_warnings
        ),
        "passed": passed,
    }
    printable_output = output
    if args.summary_only:
        printable_output = {
            "profile": output["profile"],
            "encoder_revision": output["encoder_revision"],
            "wrapper_profile": output["wrapper_profile"],
            "package_versions": output["package_versions"],
            "corpus_count": output["corpus_count"],
            "distance_metric": output["distance_metric"],
            "profile_contract": output["profile_contract"],
            "build_recall": {
                name: profile["known_query_recall_at_k"]
                for name, profile in build["profiles"].items()
            },
            "reload_recall": {
                name: profile["known_query_recall_at_k"]
                for name, profile in reload["profiles"].items()
            },
            "reload_comparisons": output["reload_comparisons"],
            "legacy_wrapper_baseline_comparison": output[
                "legacy_wrapper_baseline_comparison"
            ],
            "warnings": output["warnings"],
            "telemetry_warning_free": output["telemetry_warning_free"],
            "telemetry_disabled": {
                "build": build["telemetry_disabled"],
                "reload": reload["telemetry_disabled"],
            },
            "passed": output["passed"],
        }
    print(json.dumps(printable_output, ensure_ascii=False, indent=2))
    print(
        f"{'PASS' if passed else 'FAIL'}: "
        "Odyssey semantic retrieval profiles and reload fixture"
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
