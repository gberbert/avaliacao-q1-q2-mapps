#!/usr/bin/env python3
"""create_test_cognitive.py
Cria os testes unitários da nova funcionalidade de parametrização cognitiva.
"""

import os

test_path = "/Users/gcostabe/dev/RAG-LOCAL-REEF/backend/tests/test_cognitive_settings.py"

content = '''"""Testes para o módulo de parametrização cognitiva RAG e Soft-Boost de Lobo."""

import pytest
from pydantic import ValidationError

from app.retrieval.cognitive_settings import (
    CognitiveSettings,
    CognitiveSettingsUpdate,
    CognitiveSettingsManager,
    ALLOWED_SOFT_BOOSTS,
    DEFAULT_LOBE_SOFT_BOOST,
    DEFAULT_MAX_CONTEXT_CHARS,
    DEFAULT_SHOW_SOURCES,
    MASTER_ADMIN_PIN,
)
from app.retrieval.reranker import (
    classify_query_lobe,
    get_chunk_lobe,
    rerank_chunks,
)
from app.retrieval.search import RetrievedChunk, build_context


def test_cognitive_settings_defaults():
    s = CognitiveSettings()
    assert s.rag_lobe_soft_boost == DEFAULT_LOBE_SOFT_BOOST
    assert s.rag_max_context_chars == DEFAULT_MAX_CONTEXT_CHARS
    assert s.rag_show_sources == DEFAULT_SHOW_SOURCES


def test_cognitive_settings_validation_valid():
    # Valores válidos: 0.0, 0.05, 0.10, 0.15
    for b in [0.0, 0.05, 0.10, 0.15]:
        u = CognitiveSettingsUpdate(
            rag_lobe_soft_boost=b,
            rag_max_context_chars=12000,
            rag_show_sources=False,
        )
        assert u.rag_lobe_soft_boost == b

    # Caracteres no limite [9000, 16000]
    u1 = CognitiveSettingsUpdate(rag_lobe_soft_boost=0.05, rag_max_context_chars=9000, rag_show_sources=True)
    assert u1.rag_max_context_chars == 9000
    u2 = CognitiveSettingsUpdate(rag_lobe_soft_boost=0.15, rag_max_context_chars=16000, rag_show_sources=True)
    assert u2.rag_max_context_chars == 16000


def test_cognitive_settings_validation_invalid():
    # Soft boost fora dos permitidos (ex: 0.20 ou 0.03)
    with pytest.raises(ValidationError):
        CognitiveSettingsUpdate(rag_lobe_soft_boost=0.20, rag_max_context_chars=10000, rag_show_sources=True)

    with pytest.raises(ValidationError):
        CognitiveSettingsUpdate(rag_lobe_soft_boost=0.03, rag_max_context_chars=10000, rag_show_sources=True)

    # Caracteres abaixo de 9000
    with pytest.raises(ValidationError):
        CognitiveSettingsUpdate(rag_lobe_soft_boost=0.10, rag_max_context_chars=8999, rag_show_sources=True)

    # Caracteres acima de 16000
    with pytest.raises(ValidationError):
        CognitiveSettingsUpdate(rag_lobe_soft_boost=0.10, rag_max_context_chars=16001, rag_show_sources=True)


def test_classify_query_lobe():
    # Consulta de Sinistro -> Parietal
    assert classify_query_lobe("Qual o prazo para homologação de sinistros e expedientes?") == "parietal"

    # Consulta de Tarifação / Contrato -> Temporal
    assert classify_query_lobe("Como funciona a tarifação de contratos de terceiros e prazos de carência?") == "temporal"

    # Consulta de Auditoria / Compliance -> Occipital
    assert classify_query_lobe("Quais são os relatórios de auditoria e conformidade regulatória?") == "occipital"

    # Consulta de Arquitetura / Diretrizes -> Frontal
    assert classify_query_lobe("Qual a diretriz central de arquitetura do sistema?") == "frontal"

    # Consulta de Cognição / Embeddings -> Cerebellum
    assert classify_query_lobe("Como funciona o motor vetorial de embeddings e aprendizado?") == "cerebellum"


def test_get_chunk_lobe():
    chunk_sinistro = RetrievedChunk(
        source_path="01. Modulo Siniestros/manual.md",
        title="Tramitação de Sinistros e Expedientes",
        breadcrumb=["Siniestros", "Expedientes"],
        text="Definição de regras para liquidação e tramitação de sinistros.",
        score=0.8,
    )
    assert get_chunk_lobe(chunk_sinistro) == "parietal"


def test_rerank_soft_boost_applied():
    chunk_sinistro = RetrievedChunk(
        source_path="01. Modulo Siniestros/manual.md",
        title="Sinistros e Expedientes",
        breadcrumb=["Siniestros"],
        text="Regras de sinistros.",
        score=0.50,
    )
    chunk_outro = RetrievedChunk(
        source_path="03. Arquitetura/visao.md",
        title="Visão Geral",
        breadcrumb=["Arquitetura"],
        text="Arquitetura do sistema.",
        score=0.50,
    )

    # Sem boost (0.0): ambos recebem score natural
    res_no_boost = rerank_chunks(
        query="sinistros",
        candidates=[chunk_sinistro, chunk_outro],
        top_k=2,
        soft_boost=0.0,
        target_lobe="parietal",
    )
    score_sinistro_base = next(c.score for c in res_no_boost if c.source_path == chunk_sinistro.source_path)

    # Com boost (+15% = 0.15)
    # Recria candidates
    c1 = RetrievedChunk(
        source_path="01. Modulo Siniestros/manual.md",
        title="Sinistros e Expedientes",
        breadcrumb=["Siniestros"],
        text="Regras de sinistros.",
        score=0.50,
    )
    c2 = RetrievedChunk(
        source_path="03. Arquitetura/visao.md",
        title="Visão Geral",
        breadcrumb=["Arquitetura"],
        text="Arquitetura do sistema.",
        score=0.50,
    )
    res_boost = rerank_chunks(
        query="sinistros",
        candidates=[c1, c2],
        top_k=2,
        soft_boost=0.15,
        target_lobe="parietal",
    )
    score_sinistro_boosted = next(c.score for c in res_boost if c.source_path == c1.source_path)

    # O chunk do lobo parietal deve receber pontuação maior com o boost
    assert score_sinistro_boosted > score_sinistro_base
    assert score_sinistro_boosted <= 1.0


def test_build_context_max_chars():
    chunks = [
        RetrievedChunk(
            source_path=f"doc_{i}.md",
            title=f"Doc {i}",
            breadcrumb=["Test"],
            text="Conteudo extenso de teste. " * 50,
            score=0.9,
        )
        for i in range(20)
    ]
    # Com teto de 9000
    ctx_9k = build_context(chunks, max_chars=9000)
    assert len(ctx_9k) <= 9500

    # Com teto de 15000
    ctx_15k = build_context(chunks, max_chars=15000)
    assert len(ctx_15k) > len(ctx_9k)
    assert len(ctx_15k) <= 15500


def test_master_admin_pin():
    assert MASTER_ADMIN_PIN == "202633"
'''

with open(test_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"SUCCESS: Wrote {test_path}")
