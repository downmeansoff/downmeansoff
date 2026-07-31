from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DocumentChunk(BaseModel):
    """A stable chunk contract used by retrieval, reranking, and evaluation."""

    chunk_id: str
    document_id: str
    text: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class SearchHit(BaseModel):
    """Normalized retrieval result independent of the underlying retriever."""

    chunk: DocumentChunk
    score: float
    rank: int
    source: str


class HybridSearchResult(BaseModel):
    query: str
    hits: list[SearchHit]
    diagnostics: dict[str, Any] = Field(default_factory=dict)
