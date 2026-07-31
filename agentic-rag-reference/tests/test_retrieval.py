from __future__ import annotations

import hashlib

import numpy as np

from evaluation import mean_reciprocal_rank, recall_at_k
from retrieval import HybridRetriever
from schemas import DocumentChunk


def fake_embeddings(texts: list[str]) -> np.ndarray:
    """Deterministic local embeddings for a dependency-light test."""

    rows: list[np.ndarray] = []
    for text in texts:
        digest = hashlib.sha256(text.lower().encode("utf-8")).digest()
        vector = np.frombuffer(digest[:16], dtype=np.uint8).astype(np.float32)
        rows.append(vector)
    return np.vstack(rows)


def test_hybrid_search_and_metrics() -> None:
    chunks = [
        DocumentChunk(
            chunk_id="c1",
            document_id="d1",
            text="Supplier lead time and delivery delay policy",
        ),
        DocumentChunk(
            chunk_id="c2",
            document_id="d1",
            text="Inventory safety stock calculation and reorder point",
        ),
        DocumentChunk(
            chunk_id="c3",
            document_id="d2",
            text="Contract payment terms and invoice approval",
        ),
    ]

    retriever = HybridRetriever(chunks, fake_embeddings)
    result = retriever.search("inventory reorder safety stock", top_k=3)

    assert len(result.hits) == 3
    assert {hit.chunk.chunk_id for hit in result.hits} == {"c1", "c2", "c3"}
    assert [hit.rank for hit in result.hits] == [1, 2, 3]

    ranked = {"q1": result.hits}
    relevant = {"q1": {"c2"}}

    assert recall_at_k(ranked, relevant, k=3) == 1.0
    assert 0.0 < mean_reciprocal_rank(ranked, relevant) <= 1.0
