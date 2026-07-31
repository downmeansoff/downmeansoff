from __future__ import annotations

from collections.abc import Mapping, Sequence

from schemas import SearchHit


def recall_at_k(
    ranked_results: Mapping[str, Sequence[SearchHit]],
    relevant_chunk_ids: Mapping[str, set[str]],
    *,
    k: int,
) -> float:
    if k <= 0:
        raise ValueError("k must be positive")

    scores: list[float] = []
    for query_id, relevant in relevant_chunk_ids.items():
        if not relevant:
            continue
        retrieved = {
            hit.chunk.chunk_id for hit in ranked_results.get(query_id, ())[:k]
        }
        scores.append(1.0 if retrieved & relevant else 0.0)

    return sum(scores) / len(scores) if scores else 0.0


def mean_reciprocal_rank(
    ranked_results: Mapping[str, Sequence[SearchHit]],
    relevant_chunk_ids: Mapping[str, set[str]],
) -> float:
    reciprocal_ranks: list[float] = []
    for query_id, relevant in relevant_chunk_ids.items():
        if not relevant:
            continue
        reciprocal_rank = 0.0
        for rank, hit in enumerate(ranked_results.get(query_id, ()), 1):
            if hit.chunk.chunk_id in relevant:
                reciprocal_rank = 1.0 / rank
                break
        reciprocal_ranks.append(reciprocal_rank)

    return (
        sum(reciprocal_ranks) / len(reciprocal_ranks)
        if reciprocal_ranks
        else 0.0
    )


def failure_buckets(
    ranked_results: Mapping[str, Sequence[SearchHit]],
    relevant_chunk_ids: Mapping[str, set[str]],
    *,
    k: int,
) -> dict[str, list[str]]:
    """Return a compact error taxonomy for regression review."""

    buckets: dict[str, list[str]] = {
        "no_results": [],
        "relevant_below_k": [],
        "relevant_missing": [],
    }

    for query_id, relevant in relevant_chunk_ids.items():
        hits = list(ranked_results.get(query_id, ()))
        if not hits:
            buckets["no_results"].append(query_id)
            continue

        relevant_ranks = [
            rank
            for rank, hit in enumerate(hits, 1)
            if hit.chunk.chunk_id in relevant
        ]
        if not relevant_ranks:
            buckets["relevant_missing"].append(query_id)
        elif min(relevant_ranks) > k:
            buckets["relevant_below_k"].append(query_id)

    return buckets
