from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from schemas import DocumentChunk, HybridSearchResult, SearchHit

EmbeddingFn = Callable[[Sequence[str]], np.ndarray]
RerankerFn = Callable[[str, Sequence[SearchHit]], Sequence[SearchHit]]


@dataclass(slots=True)
class HybridConfig:
    lexical_weight: float = 0.5
    dense_weight: float = 0.5
    rrf_k: int = 60
    candidate_pool: int = 20

    def __post_init__(self) -> None:
        if self.lexical_weight < 0 or self.dense_weight < 0:
            raise ValueError("retrieval weights must be non-negative")
        if self.lexical_weight + self.dense_weight == 0:
            raise ValueError("at least one retrieval weight must be positive")
        if self.rrf_k <= 0 or self.candidate_pool <= 0:
            raise ValueError("rrf_k and candidate_pool must be positive")


class HybridRetriever:
    """Hybrid lexical+dense retrieval with reciprocal-rank fusion.

    The dense model is injected through ``embedding_fn`` so the same component can
    work with local sentence-transformers, a self-hosted embedding endpoint, or a
    provider API. An optional reranker is injected to keep the orchestration layer
    independent from a specific cross-encoder.
    """

    def __init__(
        self,
        chunks: Sequence[DocumentChunk],
        embedding_fn: EmbeddingFn,
        *,
        config: HybridConfig | None = None,
        reranker: RerankerFn | None = None,
    ) -> None:
        if not chunks:
            raise ValueError("at least one chunk is required")

        self._chunks = list(chunks)
        self._embedding_fn = embedding_fn
        self._config = config or HybridConfig()
        self._reranker = reranker

        texts = [chunk.text for chunk in self._chunks]
        self._tfidf = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
        self._lexical_matrix = self._tfidf.fit_transform(texts)

        dense = np.asarray(self._embedding_fn(texts), dtype=np.float32)
        if dense.ndim != 2 or dense.shape[0] != len(self._chunks):
            raise ValueError("embedding_fn must return [n_texts, embedding_dim]")
        self._dense_matrix = self._normalize(dense)

    def search(self, query: str, *, top_k: int = 5) -> HybridSearchResult:
        clean_query = query.strip()
        if not clean_query:
            raise ValueError("query must not be empty")
        if top_k <= 0:
            raise ValueError("top_k must be positive")

        lexical_scores = cosine_similarity(
            self._tfidf.transform([clean_query]), self._lexical_matrix
        )[0]

        query_embedding = np.asarray(
            self._embedding_fn([clean_query]), dtype=np.float32
        )
        if query_embedding.ndim != 2 or query_embedding.shape[0] != 1:
            raise ValueError("embedding_fn must return one embedding for one query")
        dense_scores = self._normalize(query_embedding) @ self._dense_matrix.T
        dense_scores = dense_scores[0]

        pool = min(self._config.candidate_pool, len(self._chunks))
        lexical_order = np.argsort(-lexical_scores)[:pool]
        dense_order = np.argsort(-dense_scores)[:pool]

        lexical_ranks = {int(idx): rank for rank, idx in enumerate(lexical_order, 1)}
        dense_ranks = {int(idx): rank for rank, idx in enumerate(dense_order, 1)}

        fused_scores: dict[int, float] = {}
        candidates = set(lexical_ranks) | set(dense_ranks)
        for idx in candidates:
            score = 0.0
            if idx in lexical_ranks:
                score += self._config.lexical_weight / (
                    self._config.rrf_k + lexical_ranks[idx]
                )
            if idx in dense_ranks:
                score += self._config.dense_weight / (
                    self._config.rrf_k + dense_ranks[idx]
                )
            fused_scores[idx] = score

        ranked_ids = sorted(fused_scores, key=fused_scores.get, reverse=True)
        hits = [
            SearchHit(
                chunk=self._chunks[idx],
                score=float(fused_scores[idx]),
                rank=rank,
                source="hybrid_rrf",
            )
            for rank, idx in enumerate(ranked_ids, 1)
        ]

        if self._reranker is not None:
            reranked = list(self._reranker(clean_query, hits[:pool]))
            hits = [
                hit.model_copy(update={"rank": rank, "source": "reranked"})
                for rank, hit in enumerate(reranked, 1)
            ]

        return HybridSearchResult(
            query=clean_query,
            hits=hits[:top_k],
            diagnostics={
                "candidate_pool": pool,
                "lexical_candidates": len(lexical_ranks),
                "dense_candidates": len(dense_ranks),
                "reranker_enabled": self._reranker is not None,
            },
        )

    @staticmethod
    def _normalize(matrix: np.ndarray) -> np.ndarray:
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        return matrix / np.clip(norms, 1e-12, None)
