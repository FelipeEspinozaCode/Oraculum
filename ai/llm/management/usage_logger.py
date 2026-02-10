"""
Usage Logger — Oraculum
=======================

Registra uso de proveedores LLM para auditoría y métricas.
"""

from datetime import datetime, UTC
from infrastructure.logging import get_logger

logger = get_logger("llm_usage")


class UsageLogger:
    """
    Registra eventos de uso de IA.
    """

    def log(self, provider: str, tokens: int, user_id: str | None = None) -> None:
        logger.info(
            "LLM_USAGE",
            extra={
                "provider": provider,
                "tokens": tokens,
                "user_id": user_id,
                "timestamp": datetime.now(UTC).isoformat(),
            },
        )
