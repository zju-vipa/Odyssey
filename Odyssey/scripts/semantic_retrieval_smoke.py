#!/usr/bin/env python3
"""Index Odyssey skill descriptions and run known-query top-k retrieval."""

from __future__ import annotations

import argparse
import gc
import importlib.util
import json
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = (
    REPO_ROOT / "research" / "manifest" / "odyssey_semantic_encoder.json"
)
DEFAULT_SKILLS = (
    REPO_ROOT / "Odyssey" / "skill_library" / "skill" / "skills.json"
)
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


def load_embedding_module():
    source_path = REPO_ROOT / "Odyssey" / "odyssey" / "retrieval_embedding.py"
    spec = importlib.util.spec_from_file_location(
        "odyssey_retrieval_embedding_smoke", source_path
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--skills", type=Path, default=DEFAULT_SKILLS)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument(
        "--wrapper-profile",
        choices=["legacy-community", "modern-partner"],
    )
    args = parser.parse_args()
    if args.k <= 0:
        parser.error("--k must be positive")

    manifest = read_json(args.manifest.resolve())
    skills = read_json(args.skills.resolve())
    model_dir = REPO_ROOT / manifest["checkpoint"]["local_path"]
    embedding_module = load_embedding_module()
    embeddings = embedding_module.build_retrieval_embeddings(
        str(model_dir),
        device=args.device,
        local_files_only=True,
        wrapper_profile=args.wrapper_profile,
    )

    names = sorted(skills)
    descriptions = [skills[name]["description"] for name in names]
    metadatas = [{"name": name} for name in names]

    with tempfile.TemporaryDirectory(prefix="odyssey-retrieval-") as temp_dir:
        vector_store = embedding_module.build_retrieval_vector_store(
            collection_name="odyssey_semantic_retrieval_smoke",
            embedding_function=embeddings,
            persist_directory=temp_dir,
            collection_metadata={"hnsw:space": "l2"},
            wrapper_profile=args.wrapper_profile,
        )
        vector_store.add_texts(
            texts=descriptions,
            ids=names,
            metadatas=metadatas,
        )
        index_count = vector_store._collection.count()
        query_results = []
        for fixture in KNOWN_QUERIES:
            candidates = retrieve(vector_store, fixture["query"], args.k)
            expected_rank = next(
                (
                    candidate["rank"]
                    for candidate in candidates
                    if candidate["skill"] == fixture["expected_skill"]
                ),
                None,
            )
            query_results.append(
                {
                    **fixture,
                    "expected_rank": expected_rank,
                    "passed": expected_rank is not None,
                    "candidates": candidates,
                }
            )
        embedding_module.persist_retrieval_vector_store(
            vector_store, wrapper_profile=args.wrapper_profile
        )
        del vector_store
        gc.collect()

    passed = index_count == len(skills) == 183 and all(
        result["passed"] for result in query_results
    )
    output = {
        "profile": "odyssey-semantic-retrieval-top5-smoke",
        "encoder_revision": manifest["checkpoint"]["revision"],
        "corpus": str(args.skills.resolve().relative_to(REPO_ROOT)),
        "corpus_count": len(skills),
        "index_count": index_count,
        "distance_metric": "l2",
        "wrapper_profile": embedding_module.resolve_wrapper_profile(
            args.wrapper_profile
        ),
        "k": args.k,
        "device": args.device,
        "known_query_recall_at_k": sum(
            result["passed"] for result in query_results
        )
        / len(query_results),
        "queries": query_results,
        "passed": passed,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    print(
        f"{'PASS' if passed else 'FAIL'}: "
        "Odyssey semantic skill retrieval smoke"
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
