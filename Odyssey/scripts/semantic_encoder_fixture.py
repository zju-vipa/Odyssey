#!/usr/bin/env python3
"""Verify the static and runtime contract of Odyssey's semantic encoder."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = (
    REPO_ROOT / "research" / "manifest" / "odyssey_semantic_encoder.json"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_versions(names: list[str]) -> dict[str, str | None]:
    observed = {}
    for name in names:
        try:
            observed[name] = version(name)
        except PackageNotFoundError:
            observed[name] = None
    return observed


def source_encode_kwargs() -> dict:
    source_path = REPO_ROOT / "Odyssey" / "odyssey" / "retrieval_embedding.py"
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == "ENCODER_ENCODE_KWARGS"
                for target in node.targets
            )
        ):
            return ast.literal_eval(node.value)
    raise ValueError("ENCODER_ENCODE_KWARGS was not found")


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


def static_checks(
    manifest: dict, wrapper_profile: str | None = None
) -> dict:
    checkpoint = manifest["checkpoint"]
    model_dir = REPO_ROOT / checkpoint["local_path"]
    failures = []
    artifacts = []
    for expected in checkpoint["artifacts"]:
        path = model_dir / expected["path"]
        actual_size = path.stat().st_size if path.is_file() else None
        actual_sha256 = sha256_file(path) if path.is_file() else None
        passed = (
            actual_size == expected["size"]
            and actual_sha256 == expected["sha256"]
        )
        artifacts.append(
            {
                "path": expected["path"],
                "size": actual_size,
                "sha256": actual_sha256,
                "passed": passed,
            }
        )
        if not passed:
            failures.append(f"artifact mismatch: {expected['path']}")

    sentence_config = read_json(model_dir / "sentence_bert_config.json")
    pooling_config = read_json(model_dir / "1_Pooling" / "config.json")
    model_config = read_json(model_dir / "config.json")
    transformation = manifest["transformation"]
    config_contract = {
        "output_dimension": model_config.get("hidden_size")
        == transformation["output_dimension"],
        "max_sequence_length": sentence_config.get("max_seq_length")
        == transformation["max_sequence_length"],
        "case_folding": sentence_config.get("do_lower_case")
        == transformation["case_folding"],
        "mean_pooling": (
            pooling_config.get("pooling_mode_mean_tokens") is True
            and pooling_config.get("pooling_mode_cls_token") is False
            and pooling_config.get("pooling_mode_max_tokens") is False
        ),
    }
    failures.extend(
        f"config mismatch: {name}"
        for name, passed in config_contract.items()
        if not passed
    )

    metadata_path = REPO_ROOT / checkpoint["revision_evidence"]
    metadata_revision = (
        metadata_path.read_text(encoding="utf-8").splitlines()[0]
        if metadata_path.is_file()
        else None
    )
    revision_passed = metadata_revision == checkpoint["revision"]
    if not revision_passed:
        failures.append("checkpoint revision metadata mismatch")

    profile = wrapper_profile or manifest["retrieval_wrapper_profiles"][
        "default"
    ]
    if profile == "modern-partner":
        expected_packages = manifest["retrieval_wrapper_profiles"][profile][
            "packages"
        ]
    else:
        expected_packages = manifest["retrieval_wrapper_profiles"][
            "legacy-community"
        ]["packages"]
    observed_packages = package_versions(list(expected_packages))
    package_matches = {
        name: observed_packages[name] == expected
        for name, expected in expected_packages.items()
    }

    encode_kwargs = source_encode_kwargs()

    source_contract = {
        "batch_size": encode_kwargs.get("batch_size")
        == transformation["batch_size"],
        "normalization": encode_kwargs.get("normalize_embeddings")
        == transformation["normalization"],
        "precision": encode_kwargs.get("precision")
        == transformation["precision"],
    }
    failures.extend(
        f"source encoder setting mismatch: {name}"
        for name, passed in source_contract.items()
        if not passed
    )

    return {
        "passed": not failures,
        "wrapper_profile": profile,
        "failures": failures,
        "checkpoint_revision": metadata_revision,
        "revision_passed": revision_passed,
        "config_contract": config_contract,
        "source_contract": source_contract,
        "artifacts": artifacts,
        "package_versions": observed_packages,
        "package_versions_match_observed_profile": package_matches,
    }


def runtime_checks(
    manifest: dict, device: str, wrapper_profile: str | None
) -> dict:
    import numpy as np

    embedding_module = load_embedding_module()
    model_dir = REPO_ROOT / manifest["checkpoint"]["local_path"]
    embeddings = embedding_module.build_retrieval_embeddings(
        str(model_dir),
        device=device,
        local_files_only=True,
        wrapper_profile=wrapper_profile,
    )
    inputs = manifest["runtime_fixture"]["fixed_inputs"]
    first = np.asarray(embeddings.embed_documents(inputs), dtype=np.float32)
    second = np.asarray(embeddings.embed_documents(inputs), dtype=np.float32)
    newline = np.asarray(
        embeddings.embed_query("move\nto the target"), dtype=np.float32
    )
    space = np.asarray(
        embeddings.embed_query("move to the target"), dtype=np.float32
    )

    expected_shape = tuple(manifest["runtime_fixture"]["acceptance"]["shape"])
    tolerance = manifest["runtime_fixture"]["acceptance"][
        "repeat_max_absolute_error"
    ]
    max_repeat_error = float(np.max(np.abs(first - second)))
    newline_space_error = float(np.max(np.abs(newline - space)))
    checks = {
        "shape": first.shape == expected_shape,
        "finite": bool(np.isfinite(first).all()),
        "repeatable": max_repeat_error <= tolerance,
        "newline_space_equivalence": newline_space_error <= tolerance,
    }
    norms = [float(value) for value in np.linalg.norm(first, axis=1)]
    checks["normalization_setting"] = (
        embeddings.encode_kwargs.get("normalize_embeddings") is False
    )
    canonical = np.asarray(first, dtype="<f4")
    return {
        "passed": all(checks.values()),
        "device": device,
        "wrapper_profile": embedding_module.resolve_wrapper_profile(
            wrapper_profile
        ),
        "shape": list(first.shape),
        "dtype": str(first.dtype),
        "checks": checks,
        "max_repeat_absolute_error": max_repeat_error,
        "newline_space_max_absolute_error": newline_space_error,
        "embedding_norms": norms,
        "embedding_sha256": hashlib.sha256(canonical.tobytes()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--run-model", action="store_true")
    parser.add_argument("--device", default="cpu")
    parser.add_argument(
        "--wrapper-profile",
        choices=["legacy-community", "modern-partner"],
    )
    args = parser.parse_args()

    manifest = read_json(args.manifest.resolve())
    result = {
        "static": static_checks(manifest, args.wrapper_profile)
    }
    if args.run_model and result["static"]["passed"]:
        result["runtime"] = runtime_checks(
            manifest, args.device, args.wrapper_profile
        )
    result["passed"] = result["static"]["passed"] and (
        not args.run_model or result.get("runtime", {}).get("passed", False)
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(
        f"{'PASS' if result['passed'] else 'FAIL'}: "
        "semantic encoder contract fixture"
    )
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
