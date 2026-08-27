"""Shared semantic-encoder and vector-store contracts for retrieval paths."""

import os
from typing import Any


# Keep the public-code behavior explicit so dependency upgrades cannot silently
# change the vector scale or batching used by skill and planner retrieval.
ENCODER_ENCODE_KWARGS = {
    "batch_size": 32,
    "normalize_embeddings": False,
    "precision": "float32",
}

SKILL_RETRIEVAL_PROFILES = {
    "top5": 5,
    "top10": 10,
}
DEFAULT_SKILL_RETRIEVAL_PROFILE = "top5"
RETRIEVAL_DISTANCE_METRIC = "l2"
RETRIEVAL_WRAPPER_PROFILES = {
    "legacy-community",
    "modern-partner",
}
DEFAULT_RETRIEVAL_WRAPPER_PROFILE = os.environ.get(
    "ODYSSEY_RETRIEVAL_WRAPPER_PROFILE", "modern-partner"
)


def resolve_wrapper_profile(wrapper_profile: str | None = None) -> str:
    profile = wrapper_profile or DEFAULT_RETRIEVAL_WRAPPER_PROFILE
    if profile not in RETRIEVAL_WRAPPER_PROFILES:
        raise ValueError(
            f"unsupported retrieval wrapper profile: {profile}; "
            f"expected one of {sorted(RETRIEVAL_WRAPPER_PROFILES)}"
        )
    return profile


def build_retrieval_embeddings(
    model_name: str,
    *,
    device: str | None = None,
    local_files_only: bool = False,
    wrapper_profile: str | None = None,
) -> Any:
    if not model_name:
        raise ValueError("semantic encoder model path or model ID is required")
    profile = resolve_wrapper_profile(wrapper_profile)
    model_kwargs = {}
    if device is not None:
        model_kwargs["device"] = device
    if local_files_only:
        model_kwargs["local_files_only"] = True
    common_kwargs = {
        "model_kwargs": model_kwargs,
        "encode_kwargs": dict(ENCODER_ENCODE_KWARGS),
        "show_progress": False,
    }
    if profile == "modern-partner":
        from langchain_huggingface import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings(model=model_name, **common_kwargs)

    from langchain_community.embeddings.huggingface import (
        HuggingFaceEmbeddings,
    )

    return HuggingFaceEmbeddings(model_name=model_name, **common_kwargs)


def build_retrieval_vector_store(
    *,
    collection_name: str,
    embedding_function: Any,
    persist_directory: str,
    collection_metadata: dict | None = None,
    wrapper_profile: str | None = None,
) -> Any:
    profile = resolve_wrapper_profile(wrapper_profile)
    if profile == "modern-partner":
        from chromadb.config import Settings
        from langchain_chroma import Chroma

        return Chroma(
            collection_name=collection_name,
            embedding_function=embedding_function,
            persist_directory=persist_directory,
            client_settings=Settings(anonymized_telemetry=False),
            collection_metadata=collection_metadata,
        )

    from langchain_community.vectorstores import Chroma

    return Chroma(
        collection_name=collection_name,
        embedding_function=embedding_function,
        persist_directory=persist_directory,
        collection_metadata=collection_metadata,
    )


def persist_retrieval_vector_store(
    vector_store: Any, *, wrapper_profile: str | None = None
) -> None:
    profile = resolve_wrapper_profile(wrapper_profile)
    if profile == "legacy-community":
        vector_store.persist()
