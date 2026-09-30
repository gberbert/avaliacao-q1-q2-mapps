#!/usr/bin/env python3
"""apply_cognitive_feature.py
Aplica a funcionalidade de Parametrização Cognitiva RAG Customizável no Painel Admin
no repositório /Users/gcostabe/dev/RAG-LOCAL-REEF.
"""

import os
import sys
import re

REPO_DIR = "/Users/gcostabe/dev/RAG-LOCAL-REEF"

def write_cognitive_settings():
    file_path = os.path.join(REPO_DIR, "backend/app/retrieval/cognitive_settings.py")
    content = '''"""Módulo de Parametrização Cognitiva RAG em Tempo de Execução.

Permite a customização dinâmica dos parâmetros do motor cognitivo RAG diretamente
pelo Painel Administrativo (/admin), com persistência na tabela app_settings,
cache em memória reativo de baixa latência e validação estrita por PIN Mestre (202633).
"""

from __future__ import annotations

import asyncio
import logging
import time
import uuid
from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field, field_validator
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.models import AppSetting

logger = logging.getLogger(__name__)

# Chaves persistidas na tabela app_settings
KEY_RAG_LOBE_SOFT_BOOST = "rag_lobe_soft_boost"
KEY_RAG_MAX_CONTEXT_CHARS = "rag_max_context_chars"
KEY_RAG_SHOW_SOURCES = "rag_show_sources"

# Valores padrão de fábrica (Cold-boot seguro)
DEFAULT_LOBE_SOFT_BOOST = 0.0
DEFAULT_MAX_CONTEXT_CHARS = 9000
DEFAULT_SHOW_SOURCES = True

# Conjunto de valores aceitos para o soft-boost
ALLOWED_SOFT_BOOSTS = {0.0, 0.05, 0.10, 0.15}
MIN_CONTEXT_CHARS = 9000
MAX_CONTEXT_CHARS = 16000

# PIN Mestre Corporativo para autenticação de operações cognitivas
MASTER_ADMIN_PIN = "202633"


class CognitiveSettings(BaseModel):
    """Estado completo das configurações cognitivas do RAG."""

    rag_lobe_soft_boost: float = Field(
        default=DEFAULT_LOBE_SOFT_BOOST,
        description="Soft-Boost percentual de score para documentos do lobo prioritário (0.0, 0.05, 0.10, 0.15)",
    )
    rag_max_context_chars: int = Field(
        default=DEFAULT_MAX_CONTEXT_CHARS,
        ge=MIN_CONTEXT_CHARS,
        le=MAX_CONTEXT_CHARS,
        description="Teto de caracteres para injeção de contexto no prompt (9.000 a 16.000)",
    )
    rag_show_sources: bool = Field(
        default=DEFAULT_SHOW_SOURCES,
        description="Exibição de tags/chips de documentos consultados abaixo das respostas do Chat",
    )
    updated_at: datetime | None = None
    updated_by: str | None = None


class CognitiveSettingsUpdate(BaseModel):
    """Payload de atualização validado via Pydantic."""

    rag_lobe_soft_boost: float = Field(
        ...,
        description="Valores aceitos: 0.0 (Desligado), 0.05 (+5%), 0.10 (+10%), 0.15 (+15%)",
    )
    rag_max_context_chars: int = Field(
        ...,
        ge=MIN_CONTEXT_CHARS,
        le=MAX_CONTEXT_CHARS,
        description="Teto de caracteres entre 9000 e 16000 com passos de 1000",
    )
    rag_show_sources: bool = Field(
        ...,
        description="True para exibir badges de documentos consultados, False para ocultar",
    )

    @field_validator("rag_lobe_soft_boost")
    @classmethod
    def validate_boost(cls, v: float) -> float:
        rounded = round(float(v), 2)
        if rounded not in ALLOWED_SOFT_BOOSTS:
            raise ValueError(
                f"Valor de soft-boost inválido ({v}). Valores aceitos: 0.0 (0%), 0.05 (+5%), 0.10 (+10%), 0.15 (+15%)."
            )
        return rounded

    @field_validator("rag_max_context_chars")
    @classmethod
    def validate_chars(cls, v: int) -> int:
        val = int(v)
        if val < MIN_CONTEXT_CHARS or val > MAX_CONTEXT_CHARS:
            raise ValueError(
                f"Teto de caracteres fora do intervalo permitido [{MIN_CONTEXT_CHARS}, {MAX_CONTEXT_CHARS}]: {val}."
            )
        return val


class CognitivePublicFlags(BaseModel):
    """Flags cognitivas públicas para consumo da interface de Chat (sem expor dados sensíveis)."""

    show_sources: bool
    lobe_soft_boost: float
    max_context_chars: int


class CognitiveSettingsManager:
    """Gerenciador Singleton com cache em memória (TTL 60s) e invalidação reativa imediata.

    Garante latência zero em requisições de chat e degradação graciosa para valores de fábrica
    caso o banco de dados esteja temporariamente indisponível.
    """

    _instance: CognitiveSettingsManager | None = None

    def __new__(cls) -> CognitiveSettingsManager:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._cache = None
            cls._instance._cache_timestamp = 0.0
            cls._instance._ttl_seconds = 60.0
            cls._instance._lock = asyncio.Lock()
        return cls._instance

    def invalidate(self) -> None:
        """Invalida o cache em memória imediatamente."""
        self._cache = None
        self._cache_timestamp = 0.0
        logger.info("[CognitiveSettingsManager] Cache de configurações cognitivas invalidado.")

    async def get_settings(self, db: AsyncSession | None = None) -> CognitiveSettings:
        """Recupera as configurações ativas com cache em memória e degradação graciosa."""
        now = time.time()
        if self._cache is not None and (now - self._cache_timestamp) < self._ttl_seconds:
            return self._cache

        async with self._lock:
            if self._cache is not None and (now - self._cache_timestamp) < self._ttl_seconds:
                return self._cache

            if db is not None:
                settings_obj = await self._load_from_db(db)
            else:
                try:
                    from app.auth.database import async_session_factory
                    async with async_session_factory() as session:
                        settings_obj = await self._load_from_db(session)
                except Exception as exc:
                    logger.warning(
                        f"[CognitiveSettingsManager] Não foi possível carregar do banco, aplicando defaults: {exc}"
                    )
                    settings_obj = CognitiveSettings(
                        rag_lobe_soft_boost=DEFAULT_LOBE_SOFT_BOOST,
                        rag_max_context_chars=DEFAULT_MAX_CONTEXT_CHARS,
                        rag_show_sources=DEFAULT_SHOW_SOURCES,
                    )

            self._cache = settings_obj
            self._cache_timestamp = time.time()
            return settings_obj

    async def _load_from_db(self, db: AsyncSession) -> CognitiveSettings:
        """Consulta as chaves na tabela app_settings e formata com fallbacks seguros."""
        try:
            keys = [KEY_RAG_LOBE_SOFT_BOOST, KEY_RAG_MAX_CONTEXT_CHARS, KEY_RAG_SHOW_SOURCES]
            rows = (await db.scalars(select(AppSetting).where(AppSetting.key.in_(keys)))).all()
            settings_dict: dict[str, AppSetting] = {r.key: r for r in rows}

            # 1. Soft-Boost
            boost = DEFAULT_LOBE_SOFT_BOOST
            if KEY_RAG_LOBE_SOFT_BOOST in settings_dict:
                try:
                    val = float(settings_dict[KEY_RAG_LOBE_SOFT_BOOST].value)
                    if round(val, 2) in ALLOWED_SOFT_BOOSTS:
                        boost = round(val, 2)
                except Exception:
                    pass

            # 2. Max Chars
            max_chars = DEFAULT_MAX_CONTEXT_CHARS
            if KEY_RAG_MAX_CONTEXT_CHARS in settings_dict:
                try:
                    val = int(settings_dict[KEY_RAG_MAX_CONTEXT_CHARS].value)
                    if MIN_CONTEXT_CHARS <= val <= MAX_CONTEXT_CHARS:
                        max_chars = val
                except Exception:
                    pass

            # 3. Show Sources
            show_sources = DEFAULT_SHOW_SOURCES
            if KEY_RAG_SHOW_SOURCES in settings_dict:
                raw_val = settings_dict[KEY_RAG_SHOW_SOURCES].value.strip().lower()
                show_sources = raw_val in ("true", "1", "yes", "t")

            # Metadados de auditoria mais recentes
            latest_time = None
            updater = None
            for r in rows:
                if r.updated_at and (latest_time is None or r.updated_at > latest_time):
                    latest_time = r.updated_at
                    updater = str(r.updated_by) if r.updated_by else None

            return CognitiveSettings(
                rag_lobe_soft_boost=boost,
                rag_max_context_chars=max_chars,
                rag_show_sources=show_sources,
                updated_at=latest_time,
                updated_by=updater,
            )
        except Exception as exc:
            logger.error(f"[CognitiveSettingsManager] Erro ao ler app_settings: {exc}")
            return CognitiveSettings(
                rag_lobe_soft_boost=DEFAULT_LOBE_SOFT_BOOST,
                rag_max_context_chars=DEFAULT_MAX_CONTEXT_CHARS,
                rag_show_sources=DEFAULT_SHOW_SOURCES,
            )

    async def update_settings(
        self,
        db: AsyncSession,
        payload: CognitiveSettingsUpdate,
        admin_user_id: uuid.UUID | None = None,
    ) -> CognitiveSettings:
        """Persiste os novos parâmetros na tabela app_settings e recarrega o cache imediatamente."""
        mapping = {
            KEY_RAG_LOBE_SOFT_BOOST: str(payload.rag_lobe_soft_boost),
            KEY_RAG_MAX_CONTEXT_CHARS: str(payload.rag_max_context_chars),
            KEY_RAG_SHOW_SOURCES: "true" if payload.rag_show_sources else "false",
        }

        now_utc = datetime.now(timezone.utc)
        for key, val in mapping.items():
            row = await db.scalar(select(AppSetting).where(AppSetting.key == key))
            if row:
                row.value = val
                row.updated_by = admin_user_id
                row.updated_at = now_utc
            else:
                db.add(AppSetting(key=key, value=val, updated_by=admin_user_id, updated_at=now_utc))

        await db.commit()

        # Invalidação imediata e atualização do cache em memória
        self.invalidate()
        new_settings = CognitiveSettings(
            rag_lobe_soft_boost=payload.rag_lobe_soft_boost,
            rag_max_context_chars=payload.rag_max_context_chars,
            rag_show_sources=payload.rag_show_sources,
            updated_at=now_utc,
            updated_by=str(admin_user_id) if admin_user_id else None,
        )
        self._cache = new_settings
        self._cache_timestamp = time.time()
        logger.info(
            f"[CognitiveSettingsManager] Parâmetros RAG atualizados com sucesso: "
            f"soft_boost={payload.rag_lobe_soft_boost}, max_chars={payload.rag_max_context_chars}, "
            f"show_sources={payload.rag_show_sources} por admin={admin_user_id}"
        )
        return new_settings


cognitive_settings_manager = CognitiveSettingsManager()
'''
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"SUCCESS: Wrote {file_path}")

def update_reranker():
    file_path = os.path.join(REPO_DIR, "backend/app/retrieval/reranker.py")
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    lobe_logic = '''
LOBE_KEYWORDS: dict[str, list[str]] = {
    "frontal": [
        "arquitetura", "arquitectura", "central", "politica", "política", "diretriz", "diretrizes",
        "norma", "normas", "susep", "governanca", "governança", "circular", "resolucao", "resolução",
        "conduta", "mercado", "liderança", "decisao", "decisão", "estrutura", "visão geral", "visao geral"
    ],
    "parietal": [
        "sinistro", "sinistros", "modulo", "módulo", "banco", "comum", "expediente", "expedientes",
        "emissao", "emissão", "calculo", "cálculo", "validapaso", "operacao", "operação", "operacional",
        "tramitacao", "tramitação", "liquidacao", "liquidação", "apolice emitir", "suplemento"
    ],
    "occipital": [
        "auditoria", "compliance", "seguranca", "segurança", "relatorio", "relatório", "visual",
        "regulatorio", "regulatório", "cnsp", "ouvidoria", "lgpd", "conformidade", "risco", "riscos",
        "fiscalizacao", "fiscalização", "opin", "open insurance"
    ],
    "temporal": [
        "contrato", "contratos", "apolice", "apólice", "tarifa", "tarifas", "tarifacao", "tarifação",
        "tributario", "tributário", "fiscal", "cliente", "clientes", "parceiro", "parceiros",
        "codigo civil", "código civil", "glossario", "glossário", "terceiro", "terceiros", "premio", "prêmio",
        "carencia", "carência", "vigencia", "vigência"
    ],
    "cerebellum": [
        "ia", "cognicao", "cognição", "vector", "vetor", "cache", "embedding", "embeddings",
        "llm", "aprendizado", "learning", "retificacao", "retificação", "sinapse", "sinapses",
        "neuroplasticidade", "qdrant", "self-learned"
    ],
}


def classify_query_lobe(query: str) -> str | None:
    """Identifica o lobo neuroanatômico prioritário da consulta corporativa."""
    if not query:
        return None
    lower = query.lower()
    scores: dict[str, int] = {}
    for lobe, kw_list in LOBE_KEYWORDS.items():
        score = sum(1 for kw in kw_list if kw in lower)
        if score > 0:
            scores[lobe] = score
    if not scores:
        return None
    best_lobe, best_count = max(scores.items(), key=lambda x: x[1])
    return best_lobe if best_count >= 1 else None


def get_chunk_lobe(chunk: RetrievedChunk) -> str:
    """Classifica o chunk em um dos lobos com base no título, caminho, breadcrumb e conteúdo."""
    text_sample = getattr(chunk, "text", "")[:350]
    combined = f"{chunk.source_path} {chunk.title} {' '.join(chunk.breadcrumb or [])} {text_sample}".lower()
    scores: dict[str, int] = {}
    for lobe, kw_list in LOBE_KEYWORDS.items():
        score = sum(1 for kw in kw_list if kw in combined)
        if score > 0:
            scores[lobe] = score
    if scores:
        return max(scores.items(), key=lambda x: x[1])[0]
    return "frontal"
'''

    # Ensure LOBE_KEYWORDS and helpers are present before rerank_chunks
    if "def classify_query_lobe" not in code:
        idx = code.find("def rerank_chunks(")
        if idx != -1:
            code = code[:idx] + lobe_logic + "\n\n" + code[idx:]

    # Update rerank_chunks signature
    old_sig = """def rerank_chunks(
    query: str,
    candidates: list[RetrievedChunk],
    top_k: int = 10,
    dense_weight: float = 0.50,
    lexical_weight: float = 0.35,
    structural_weight: float = 0.15,
    entity_sources: set[str] | None = None,
    topological_scores: dict[str, float] | None = None,
) -> list[RetrievedChunk]:"""

    new_sig = """def rerank_chunks(
    query: str,
    candidates: list[RetrievedChunk],
    top_k: int = 10,
    dense_weight: float = 0.50,
    lexical_weight: float = 0.35,
    structural_weight: float = 0.15,
    entity_sources: set[str] | None = None,
    topological_scores: dict[str, float] | None = None,
    soft_boost: float = 0.0,
    target_lobe: str | None = None,
) -> list[RetrievedChunk]:"""

    if old_sig in code:
        code = code.replace(old_sig, new_sig)

    # Insert soft-boost logic before chunk.score = round(final_score, 4)
    target_score_assign = "chunk.score = round(final_score, 4)"
    soft_boost_block = """        # 7. Soft-Boost do Lobo (Lobe Routing Ponderado)
        if soft_boost > 0.0 and target_lobe:
            chunk_lobe = get_chunk_lobe(chunk)
            if chunk_lobe == target_lobe:
                # Aplica bonificação percentual proporcional sem filtro rígido censurador
                final_score = min(1.0, final_score * (1.0 + soft_boost))

        chunk.score = round(final_score, 4)"""

    if target_score_assign in code and "Soft-Boost do Lobo" not in code:
        code = code.replace(target_score_assign, soft_boost_block)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"SUCCESS: Updated {file_path}")

def update_search():
    file_path = os.path.join(REPO_DIR, "backend/app/retrieval/search.py")
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Update search signature
    old_search_sig = """def search(
    query: str,
    top_k: int = 10,
    enable_rerank: bool = True,
    entity_sources: set[str] | None = None,
    topological_scores: dict[str, float] | None = None,
) -> list[RetrievedChunk]:"""

    new_search_sig = """def search(
    query: str,
    top_k: int = 10,
    enable_rerank: bool = True,
    entity_sources: set[str] | None = None,
    topological_scores: dict[str, float] | None = None,
    soft_boost: float = 0.0,
    target_lobe: str | None = None,
) -> list[RetrievedChunk]:"""

    if old_search_sig in code:
        code = code.replace(old_search_sig, new_search_sig)

    # Update rerank_chunks call inside search()
    old_rerank_call = """        reranked = rerank_chunks(
            query,
            all_candidates,
            top_k=top_k,
            entity_sources=entity_sources,
            topological_scores=topological_scores,
        )"""

    new_rerank_call = """        reranked = rerank_chunks(
            query,
            all_candidates,
            top_k=top_k,
            entity_sources=entity_sources,
            topological_scores=topological_scores,
            soft_boost=soft_boost,
            target_lobe=target_lobe,
        )"""

    if old_rerank_call in code:
        code = code.replace(old_rerank_call, new_rerank_call)

    # Ensure build_context guarantees max_chars dynamically
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"SUCCESS: Updated {file_path}")

def update_chat():
    file_path = os.path.join(REPO_DIR, "backend/app/api/chat.py")
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Import cognitive_settings_manager and classify_query_lobe if not present
    if "from app.retrieval.cognitive_settings import cognitive_settings_manager" not in code:
        import_marker = "from app.retrieval.search import ("
        new_imports = "from app.retrieval.cognitive_settings import cognitive_settings_manager\nfrom app.retrieval.reranker import classify_query_lobe\n" + import_marker
        code = code.replace(import_marker, new_imports)

    # In event_stream(), retrieve cog_settings and pass soft_boost and target_lobe
    old_retrieval_chunk = """        query_entities, entity_sources = await get_query_entities_context(db, request.message)
        try:
            await topological_engine.get_or_sync(db)
        except Exception as exc:
            logger.warning(f"[chat] Não foi possível sincronizar motor topológico: {exc}")

        try:
            chunks = search(request.message, top_k=request.top_k, entity_sources=entity_sources)
        except Exception as exc:
            logger.error(f"[chat] Falha no serviço de busca/embeddings: {exc}")
            chunks = []"""

    new_retrieval_chunk = """        # Carrega parâmetros cognitivos dinâmicos do Painel Admin (latência zero via cache)
        cog_settings = await cognitive_settings_manager.get_settings(db)
        target_lobe = classify_query_lobe(request.message) if cog_settings.rag_lobe_soft_boost > 0 else None

        query_entities, entity_sources = await get_query_entities_context(db, request.message)
        try:
            await topological_engine.get_or_sync(db)
        except Exception as exc:
            logger.warning(f"[chat] Não foi possível sincronizar motor topológico: {exc}")

        try:
            chunks = search(
                request.message,
                top_k=request.top_k,
                entity_sources=entity_sources,
                soft_boost=cog_settings.rag_lobe_soft_boost,
                target_lobe=target_lobe,
            )
        except Exception as exc:
            logger.error(f"[chat] Falha no serviço de busca/embeddings: {exc}")
            chunks = []"""

    if old_retrieval_chunk in code:
        code = code.replace(old_retrieval_chunk, new_retrieval_chunk)

    # In build_context call, pass max_chars=cog_settings.rag_max_context_chars
    old_build_ctx = """            context = build_context(
                relevant_chunks,
                edges=hop1_edges,
                conflicts=conflicts,
                doc_summaries=doc_summaries,
                hop2_edges=hop2_edges,
                hop2_docs=hop2_docs,
                query_entities=query_entities,
            )"""

    new_build_ctx = """            context = build_context(
                relevant_chunks,
                edges=hop1_edges,
                conflicts=conflicts,
                doc_summaries=doc_summaries,
                hop2_edges=hop2_edges,
                hop2_docs=hop2_docs,
                query_entities=query_entities,
                max_chars=cog_settings.rag_max_context_chars,
            )"""

    if old_build_ctx in code:
        code = code.replace(old_build_ctx, new_build_ctx)

    # In sources formatting: enforce final_sources = [] if rag_show_sources == False
    old_sources_block = """        # Se houver anexos ou se a resposta contiver recusa
        if (not has_relevant_docs and not has_attachments) or is_refusal_or_not_found(user_facing_content):
            final_sources = []
        else:
            final_sources = candidate_sources"""

    new_sources_block = """        # Se houver anexos ou se a resposta contiver recusa, ou se o admin desativou show_sources
        if (not has_relevant_docs and not has_attachments) or is_refusal_or_not_found(user_facing_content):
            final_sources = []
        elif not cog_settings.rag_show_sources:
            # Diretriz Parametrizada: Chat executivo limpo sem badges de fontes
            final_sources = []
        else:
            final_sources = candidate_sources"""

    if old_sources_block in code:
        code = code.replace(old_sources_block, new_sources_block)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"SUCCESS: Updated {file_path}")

def update_admin():
    file_path = os.path.join(REPO_DIR, "backend/app/api/admin.py")
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Import cognitive items
    cog_imports = """
from app.retrieval.cognitive_settings import (
    CognitivePublicFlags,
    CognitiveSettings,
    CognitiveSettingsUpdate,
    MASTER_ADMIN_PIN,
    cognitive_settings_manager,
)
"""
    if "from app.retrieval.cognitive_settings import" not in code:
        code = cog_imports + "\n" + code

    # Add PIN verification dependency and cognitive endpoints
    endpoints_code = '''
async def verify_admin_pin_token(
    x_admin_pin_token: str | None = Header(None, alias="X-Admin-PIN-Token"),
) -> str:
    """Valida o PIN Mestre corporativo (202633) para alterações sensíveis no motor cognitivo."""
    if not x_admin_pin_token or x_admin_pin_token.strip() != MASTER_ADMIN_PIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"PIN Mestre corporativo inválido ou não fornecido. Requer PIN {MASTER_ADMIN_PIN}.",
        )
    return x_admin_pin_token.strip()


@router.get("/settings/cognitive", response_model=CognitiveSettings)
async def get_cognitive_settings(
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
    _pin: str = Depends(verify_admin_pin_token),
):
    """Retorna os parâmetros dinâmicos do motor cognitivo RAG (Requer Admin + PIN Mestre)."""
    return await cognitive_settings_manager.get_settings(db)


@router.put("/settings/cognitive", response_model=CognitiveSettings)
async def update_cognitive_settings(
    payload: CognitiveSettingsUpdate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
    _pin: str = Depends(verify_admin_pin_token),
):
    """Atualiza em tempo de execução os parâmetros cognitivos RAG com invalidação de cache (Requer Admin + PIN Mestre)."""
    return await cognitive_settings_manager.update_settings(db, payload, admin_user_id=admin.id)


@router.get("/settings/cognitive/flags", response_model=CognitivePublicFlags)
async def get_cognitive_flags(
    db: AsyncSession = Depends(get_db),
):
    """Endpoint público para consulta rápida das flags cognitivas (ex.: show_sources) para a UI do Chat."""
    settings = await cognitive_settings_manager.get_settings(db)
    return CognitivePublicFlags(
        show_sources=settings.rag_show_sources,
        lobe_soft_boost=settings.rag_lobe_soft_boost,
        max_context_chars=settings.rag_max_context_chars,
    )

# Router público e complementar montado para suportar chamadas com ou sem /api
public_settings_router = APIRouter(tags=["cognitive-settings"])

@public_settings_router.get("/settings/cognitive/flags", response_model=CognitivePublicFlags)
@public_settings_router.get("/api/settings/cognitive/flags", response_model=CognitivePublicFlags)
async def get_public_cognitive_flags(
    db: AsyncSession = Depends(get_db),
):
    settings = await cognitive_settings_manager.get_settings(db)
    return CognitivePublicFlags(
        show_sources=settings.rag_show_sources,
        lobe_soft_boost=settings.rag_lobe_soft_boost,
        max_context_chars=settings.rag_max_context_chars,
    )

@public_settings_router.get("/api/admin/settings/cognitive", response_model=CognitiveSettings)
async def get_cognitive_settings_alias(
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
    _pin: str = Depends(verify_admin_pin_token),
):
    return await cognitive_settings_manager.get_settings(db)

@public_settings_router.put("/api/admin/settings/cognitive", response_model=CognitiveSettings)
async def update_cognitive_settings_alias(
    payload: CognitiveSettingsUpdate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
    _pin: str = Depends(verify_admin_pin_token),
):
    return await cognitive_settings_manager.update_settings(db, payload, admin_user_id=admin.id)
'''

    if "def verify_admin_pin_token" not in code:
        code += "\n\n" + endpoints_code

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"SUCCESS: Updated {file_path}")

def update_main():
    file_path = os.path.join(REPO_DIR, "backend/app/main.py")
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    if "public_settings_router" not in code:
        target = "app.include_router(admin.router)"
        replacement = "app.include_router(admin.router)\napp.include_router(admin.public_settings_router)"
        code = code.replace(target, replacement)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"SUCCESS: Updated {file_path}")

def update_frontend_api():
    file_path = os.path.join(REPO_DIR, "frontend/lib/api.ts")
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    types = """
export interface CognitiveSettings {
  rag_lobe_soft_boost: number;
  rag_max_context_chars: number;
  rag_show_sources: boolean;
  updated_at?: string | null;
  updated_by?: string | null;
}

export interface CognitivePublicFlags {
  show_sources: boolean;
  lobe_soft_boost: number;
  max_context_chars: number;
}
"""
    if "export interface CognitiveSettings" not in code:
        code = types + "\n" + code

    methods = """
  getCognitiveSettings: (pin: string) =>
    request<CognitiveSettings>("/admin/settings/cognitive", {
      headers: { "X-Admin-PIN-Token": pin },
    }),
  updateCognitiveSettings: (data: CognitiveSettings, pin: string) =>
    request<CognitiveSettings>("/admin/settings/cognitive", {
      method: "PUT",
      body: JSON.stringify(data),
      headers: { "X-Admin-PIN-Token": pin },
    }),
  getCognitiveFlags: () =>
    request<CognitivePublicFlags>("/settings/cognitive/flags"),
"""
    if "getCognitiveSettings:" not in code:
        marker = "export const adminApi = {"
        code = code.replace(marker, marker + methods)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"SUCCESS: Updated {file_path}")

def write_cognitive_settings_panel():
    file_path = os.path.join(REPO_DIR, "frontend/components/CognitiveSettingsPanel.tsx")
    content = '''"use client";

import { useEffect, useState } from "react";
import {
  Sliders,
  Zap,
  Shield,
  FileText,
  CheckCircle2,
  Lock,
  Unlock,
  Key,
  AlertCircle,
  RefreshCw,
  Sparkles,
  Info,
  Layers,
  ArrowRight,
} from "lucide-react";
import { adminApi, CognitiveSettings, ApiError } from "@/lib/api";

const MASTER_PIN_DEFAULT = "202633";

export default function CognitiveSettingsPanel() {
  const [pin, setPin] = useState<string>("");
  const [pinInput, setPinInput] = useState<string>("");
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [authError, setAuthError] = useState<string | null>(null);

  const [loading, setLoading] = useState<boolean>(false);
  const [saving, setSaving] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [successToast, setSuccessToast] = useState<string | null>(null);

  const [settings, setSettings] = useState<CognitiveSettings>({
    rag_lobe_soft_boost: 0.0,
    rag_max_context_chars: 9000,
    rag_show_sources: true,
  });

  const loadSettings = async (tokenPin: string) => {
    setLoading(true);
    setError(null);
    try {
      const data = await adminApi.getCognitiveSettings(tokenPin);
      setSettings(data);
      setIsAuthenticated(true);
      setPin(tokenPin);
      setAuthError(null);
    } catch (err: any) {
      if (err instanceof ApiError && err.status === 403) {
        setAuthError("PIN Mestre incorreto. Operação restrita ao PIN 202633.");
        setIsAuthenticated(false);
      } else {
        setError(err.message || "Falha ao carregar configurações cognitivas.");
      }
    } finally {
      setLoading(false);
    }
  };

  const handlePinSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!pinInput.trim()) {
      setAuthError("Informe o PIN Mestre corporativo.");
      return;
    }
    loadSettings(pinInput.trim());
  };

  const handleSave = async () => {
    if (!isAuthenticated || !pin) {
      setAuthError("Autenticação com PIN Mestre necessária.");
      return;
    }
    setSaving(true);
    setError(null);
    setSuccessToast(null);

    try {
      const updated = await adminApi.updateCognitiveSettings(settings, pin);
      setSettings(updated);
      setSuccessToast("Parâmetros do Motor Cognitivo RAG salvos e aplicados em runtime com sucesso!");
      setTimeout(() => setSuccessToast(null), 5000);
    } catch (err: any) {
      setError(err instanceof ApiError ? err.message : "Erro ao salvar parâmetros cognitivos.");
    } finally {
      setSaving(false);
    }
  };

  // Helper de texto de status do teto de caracteres
  const getContextDepthBadge = (chars: number) => {
    if (chars <= 9000) {
      return {
        label: "Padrão Ágil (Cold-Boot Rápido)",
        color: "text-amber-400 bg-amber-500/10 border-amber-500/30",
        desc: "Otimizado para baixa latência e respostas concisas em máquinas com hardware modesto.",
      };
    }
    if (chars <= 14000) {
      return {
        label: "Balanceado (Recomendado)",
        color: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
        desc: "Ideal para cruzar múltiplas normas e regras operacionais sem truncamento.",
      };
    }
    return {
      label: "Máxima Profundidade Analítica",
      color: "text-purple-400 bg-purple-500/10 border-purple-500/30",
      desc: "Sintetiza resoluções extensas, catálogos e múltiplos artigos regulatórios exaustivos.",
    };
  };

  const depthInfo = getContextDepthBadge(settings.rag_max_context_chars);

  return (
    <div className="space-y-6">
      {/* Toast de Sucesso */}
      {successToast && (
        <div className="flex items-center gap-3 p-4 rounded-xl bg-emerald-950/80 border border-emerald-500/40 text-emerald-200 shadow-xl shadow-emerald-950/50 animate-in fade-in slide-in-from-top-2 duration-300">
          <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
          <p className="text-sm font-medium">{successToast}</p>
        </div>
      )}

      {/* Alerta de Erro */}
      {error && (
        <div className="flex items-center gap-3 p-4 rounded-xl bg-rose-950/80 border border-rose-500/40 text-rose-200 shadow-xl shadow-rose-950/50">
          <AlertCircle className="w-5 h-5 text-rose-400 shrink-0" />
          <p className="text-sm">{error}</p>
        </div>
      )}

      {/* Card Principal de Parametrização */}
      <div className="rounded-2xl border border-slate-800 bg-gradient-to-b from-slate-900/90 to-slate-950/90 p-6 sm:p-8 backdrop-blur-xl shadow-2xl relative overflow-hidden">
        {/* Glow de fundo */}
        <div className="absolute top-0 right-0 -mr-20 -mt-20 w-80 h-80 rounded-full bg-blue-600/10 blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 rounded-full bg-indigo-600/10 blur-3xl pointer-events-none" />

        {/* Header do Card */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800/80 pb-6 mb-6">
          <div className="flex items-start gap-4">
            <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-lg shadow-indigo-950/50 shrink-0">
              <Sliders className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2.5">
                <h2 className="text-xl font-bold text-white tracking-tight">
                  Ajustes do Motor Cognitivo e RAG
                </h2>
                <span className="px-2 py-0.5 text-[10px] font-semibold tracking-wider uppercase rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30">
                  Runtime Live
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-1 max-w-xl">
                Parametrização dinâmica em tempo de execução — Modifique roteamento de lobos, teto de caracteres e visibilidade de fontes sem reiniciar o backend.
              </p>
            </div>
          </div>

          {/* Status de Autenticação por PIN */}
          {isAuthenticated ? (
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs">
              <Unlock className="w-4 h-4 text-emerald-400" />
              <span>PIN Mestre 202633 Validado</span>
            </div>
          ) : (
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs">
              <Lock className="w-4 h-4 text-amber-400" />
              <span>Requer PIN Mestre (202633)</span>
            </div>
          )}
        </div>

        {/* Se não autenticado: Modal / Gate de PIN Mestre */}
        {!isAuthenticated ? (
          <div className="py-8 px-4 max-w-md mx-auto text-center space-y-5">
            <div className="w-14 h-14 mx-auto rounded-2xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
              <Key className="w-7 h-7" />
            </div>
            <div className="space-y-1.5">
              <h3 className="text-base font-semibold text-white">
                Autenticação de Segurança Corporativa
              </h3>
              <p className="text-xs text-slate-400">
                A mutação dos parâmetros cognitivos afeta diretamente a inferência de IA. Insira o PIN Mestre corporativo para desbloquear os controles.
              </p>
            </div>

            {authError && (
              <div className="p-3 rounded-lg bg-rose-950/80 border border-rose-500/30 text-rose-300 text-xs">
                {authError}
              </div>
            )}

            <form onSubmit={handlePinSubmit} className="space-y-3">
              <div className="relative">
                <input
                  type="password"
                  value={pinInput}
                  onChange={(e) => setPinInput(e.target.value)}
                  placeholder="Digite o PIN Mestre (ex: 202633)"
                  className="w-full px-4 py-2.5 rounded-xl bg-slate-950 border border-slate-700 text-center font-mono tracking-widest text-sm text-white focus:outline-none focus:border-indigo-500 transition shadow-inner"
                  autoFocus
                />
              </div>
              <div className="flex gap-2">
                <button
                  type="button"
                  onClick={() => {
                    setPinInput(MASTER_PIN_DEFAULT);
                    loadSettings(MASTER_PIN_DEFAULT);
                  }}
                  className="w-1/2 py-2.5 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium border border-slate-700 transition"
                >
                  Usar PIN 202633
                </button>
                <button
                  type="submit"
                  disabled={loading}
                  className="w-1/2 py-2.5 px-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white text-xs font-semibold shadow-lg shadow-indigo-950/50 flex items-center justify-center gap-1.5 transition"
                >
                  {loading ? <RefreshCw className="w-3.5 h-3.5 animate-spin" /> : <Unlock className="w-3.5 h-3.5" />}
                  <span>Desbloquear</span>
                </button>
              </div>
            </form>
          </div>
        ) : (
          /* Formulário de Configuração Desbloqueado */
          <div className="space-y-8">
            {/* Parâmetro A: Soft-Boost do Lobo */}
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className="text-sm font-semibold text-slate-200">
                    Parâmetro A: Soft-Boost do Lobo (Lobe Routing Ponderado)
                  </span>
                  <span className="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">
                    {Math.round(settings.rag_lobe_soft_boost * 100)}%
                  </span>
                </div>
              </div>
              <p className="text-xs text-slate-400 leading-relaxed">
                Em vez de aplicar um filtro rígido (Hard Routing) que bloqueia domínios cruzados, o Soft-Boost bonifica percentualmente o score de similaridade dos documentos pertencentes ao lobo identificado na pergunta (ex: Sinistros, Regulatório, Tarifação).
              </p>

              {/* Botões Segmentados */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 pt-1">
                {[
                  { val: 0.0, label: "Desligado (0%)", sub: "Busca vetorial pura", color: "border-slate-700 hover:border-slate-500" },
                  { val: 0.05, label: "+5% Sutil", sub: "Leve afinidade temática", color: "border-blue-500/40 hover:border-blue-400" },
                  { val: 0.10, label: "+10% Equilibrado", sub: "Recomendado produção", color: "border-indigo-500/40 hover:border-indigo-400" },
                  { val: 0.15, label: "+15% Intenso", sub: "Alta prioridade no lobo", color: "border-purple-500/40 hover:border-purple-400" },
                ].map((item) => {
                  const isSelected = settings.rag_lobe_soft_boost === item.val;
                  return (
                    <button
                      key={item.val}
                      type="button"
                      onClick={() => setSettings({ ...settings, rag_lobe_soft_boost: item.val })}
                      className={`p-3 rounded-xl border text-left transition-all ${
                        isSelected
                          ? "bg-gradient-to-br from-indigo-900/60 to-purple-900/60 border-indigo-400 text-white shadow-lg shadow-indigo-950/40 ring-1 ring-indigo-400/50 scale-[1.02]"
                          : "bg-slate-950/60 border-slate-800 text-slate-400 hover:text-slate-200 hover:bg-slate-900/60"
                      }`}
                    >
                      <div className="font-semibold text-xs text-white">{item.label}</div>
                      <div className="text-[11px] text-slate-400 mt-0.5">{item.sub}</div>
                    </button>
                  );
                })}
              </div>

              {/* Diretriz Explicativa */}
              <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-800/80 flex items-start gap-2.5 text-xs text-slate-400">
                <Info className="w-4 h-4 text-indigo-400 shrink-0 mt-0.5" />
                <span>
                  {settings.rag_lobe_soft_boost === 0.0 ? (
                    "0% (Desligado): Todos os documentos do acervo competem igualmente por similaridade semântica no Qdrant."
                  ) : (
                    `+${Math.round(settings.rag_lobe_soft_boost * 100)}% Ativo: Chunks do domínio classificado recebem bônus proporcional no reranker [score = min(1.0, score * ${(1.0 + settings.rag_lobe_soft_boost).toFixed(2)})], priorizando-os no topo do contexto sem censurar os demais.`
                  )}
                </span>
              </div>
            </div>

            {/* Parâmetro B: Teto de Caracteres do Contexto RAG */}
            <div className="space-y-3 border-t border-slate-800/80 pt-6">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <span className="text-sm font-semibold text-slate-200">
                  Parâmetro B: Teto de Caracteres do Contexto RAG (Max Context Chars)
                </span>
                <div className={`px-2.5 py-1 rounded-lg text-xs font-semibold border ${depthInfo.color}`}>
                  {settings.rag_max_context_chars.toLocaleString("pt-BR")} caracteres — {depthInfo.label}
                </div>
              </div>
              <p className="text-xs text-slate-400 leading-relaxed">
                Define o orçamento máximo injetado no prompt via <code className="text-indigo-300">build_context(...)</code>. O topo do contexto prioriza sempre sinapses de aprendizado e alertas de conflito.
              </p>

              {/* Slider Interativo */}
              <div className="space-y-2 pt-2">
                <input
                  type="range"
                  min="9000"
                  max="16000"
                  step="1000"
                  value={settings.rag_max_context_chars}
                  onChange={(e) =>
                    setSettings({ ...settings, rag_max_context_chars: parseInt(e.target.value, 10) })
                  }
                  className="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-indigo-500"
                />
                <div className="flex justify-between text-[10px] text-slate-500 font-mono">
                  <span>9.000 chars (Ágil)</span>
                  <span>12.000 chars</span>
                  <span>14.000 chars (Recomendado)</span>
                  <span>16.000 chars (Exaustivo)</span>
                </div>
              </div>

              {/* Descrição do modo selecionado */}
              <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-800/80 flex items-start gap-2.5 text-xs text-slate-400">
                <Zap className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                <span>{depthInfo.desc}</span>
              </div>
            </div>

            {/* Parâmetro C: Exibição de Fontes Consultadas */}
            <div className="space-y-3 border-t border-slate-800/80 pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <span className="text-sm font-semibold text-slate-200 block">
                    Parâmetro C: Exibição de Fontes Consultadas (Show Sources Toggle)
                  </span>
                  <p className="text-xs text-slate-400 mt-0.5">
                    Exibir badges e links com os nomes dos documentos consultados abaixo das respostas no Chat.
                  </p>
                </div>

                {/* Switch Visual Moderno */}
                <button
                  type="button"
                  onClick={() => setSettings({ ...settings, rag_show_sources: !settings.rag_show_sources })}
                  className={`w-14 h-8 flex items-center rounded-full p-1 transition-colors duration-300 focus:outline-none shrink-0 ${
                    settings.rag_show_sources ? "bg-indigo-600 justify-end" : "bg-slate-800 justify-start"
                  }`}
                >
                  <div className="w-6 h-6 rounded-full bg-white shadow-md transform transition-transform" />
                </button>
              </div>

              <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-800/80 flex items-start gap-2.5 text-xs text-slate-400">
                <FileText className="w-4 h-4 text-blue-400 shrink-0 mt-0.5" />
                <span>
                  {settings.rag_show_sources ? (
                    <strong className="text-slate-200">
                      Ligado (Transparência Completa): Usuários visualizam os badges com os documentos que fundamentaram cada resposta no Chat.
                    </strong>
                  ) : (
                    <strong className="text-slate-300">
                      Desligado (Modo Executivo Limpo): Interface ultra limpa focada puramente na resposta sintetizada pela IA, sem badges de fontes.
                    </strong>
                  )}
                </span>
              </div>
            </div>

            {/* Botão de Ação Salvar */}
            <div className="border-t border-slate-800/80 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div className="text-xs text-slate-500">
                {settings.updated_at && (
                  <span>Última atualização: {new Date(settings.updated_at).toLocaleString("pt-BR")}</span>
                )}
              </div>

              <button
                type="button"
                onClick={handleSave}
                disabled={saving}
                className="w-full sm:w-auto px-6 py-3 rounded-xl bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:from-indigo-500 hover:to-pink-500 disabled:opacity-50 text-white font-semibold text-sm shadow-xl shadow-indigo-950/50 flex items-center justify-center gap-2 transition-all hover:scale-[1.02] active:scale-[0.98]"
              >
                {saving ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin text-white" />
                    <span>Aplicando Parâmetros no Runtime...</span>
                  </>
                ) : (
                  <>
                    <Sparkles className="w-4 h-4 text-white" />
                    <span>Salvar Parâmetros Cognitivos</span>
                  </>
                )}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
'''
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"SUCCESS: Wrote {file_path}")

def update_admin_page():
    file_path = os.path.join(REPO_DIR, "frontend/app/admin/page.tsx")
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Import CognitiveSettingsPanel
    if "import CognitiveSettingsPanel from" not in code:
        marker = 'import AdminRbacPanel from "@/components/AdminRbacPanel";'
        new_import = marker + '\nimport CognitiveSettingsPanel from "@/components/CognitiveSettingsPanel";'
        code = code.replace(marker, new_import)

    # Update adminTab type to include 'cognitive'
    old_tab_state = 'const [adminTab, setAdminTab] = useState<"knowledge" | "quality" | "sources" | "snapshots" | "tokens" | "users" | "rbac">("knowledge");'
    new_tab_state = 'const [adminTab, setAdminTab] = useState<"knowledge" | "quality" | "sources" | "snapshots" | "tokens" | "users" | "rbac" | "cognitive">("cognitive");'
    if old_tab_state in code:
        code = code.replace(old_tab_state, new_tab_state)

    # Add tab button for Cognitive Settings
    tab_btn = '''          <button
            onClick={() => setAdminTab("cognitive")}
            className={`pb-3 px-4 text-sm font-medium border-b-2 transition flex items-center gap-2 whitespace-nowrap ${
              adminTab === "cognitive"
                ? "border-indigo-500 text-indigo-400 bg-indigo-500/10 rounded-t-lg font-semibold"
                : "border-transparent text-slate-400 hover:text-slate-200"
            }`}
          >
            <span>🎛️ Parâmetros Cognitivos RAG</span>
          </button>
'''
    if 'setAdminTab("cognitive")' not in code:
        search_tab = '<button\n            onClick={() => setAdminTab("knowledge")}'
        code = code.replace(search_tab, tab_btn + search_tab)

    # Add Panel rendering
    if '{adminTab === "cognitive" && <CognitiveSettingsPanel />}' not in code:
        panel_marker = '{adminTab === "knowledge" && <KnowledgePanel />}'
        code = code.replace(panel_marker, '{adminTab === "cognitive" && <CognitiveSettingsPanel />}\n\n        ' + panel_marker)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"SUCCESS: Updated {file_path}")

def update_knowledge_panel():
    file_path = os.path.join(REPO_DIR, "frontend/components/KnowledgePanel.tsx")
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    if "import CognitiveSettingsPanel from" not in code:
        code = 'import CognitiveSettingsPanel from "@/components/CognitiveSettingsPanel";\n' + code

    # Embed CognitiveSettingsPanel at top of KnowledgePanel for immediate accessibility
    if "<CognitiveSettingsPanel />" not in code:
        marker = '<div className="space-y-6">'
        code = code.replace(marker, marker + '\n      <CognitiveSettingsPanel />', 1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"SUCCESS: Updated {file_path}")

if __name__ == "__main__":
    print("Iniciando aplicação dos parâmetros cognitivos RAG...")
    write_cognitive_settings()
    update_reranker()
    update_search()
    update_chat()
    update_admin()
    update_main()
    update_frontend_api()
    write_cognitive_settings_panel()
    update_admin_page()
    update_knowledge_panel()
    print("Todos os arquivos foram criados e atualizados com sucesso!")
