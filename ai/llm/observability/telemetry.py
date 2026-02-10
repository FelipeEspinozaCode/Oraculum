from ai.llm.observability.events import LLMEventLogger
from ai.llm.observability.metrics import MetricsCollector

class AITelemetry:
    """
    Fachada central de observabilidad IA.
    Conecta los eventos en log (JSONL) con las métricas en memoria.
    """

    def __init__(self) -> None:
        self.logger = LLMEventLogger()
        self.metrics = MetricsCollector.instance()

    def log_router_choice(self, provider: str, user_id: str | None) -> None:
        self.metrics.inc_provider(provider)
        self.logger.log("router_choice", {
            "provider": provider,
            "user_id": user_id,
        })

    def log_cache_hit(self) -> None:
        self.metrics.inc_cache_hit()
        self.logger.log("cache_hit", {})

    def log_cache_miss(self) -> None:
        self.metrics.inc_cache_miss()
        self.logger.log("cache_miss", {})

    def log_fallback(self, primary: str, secondary: str) -> None:
        self.metrics.inc_fallback()
        self.logger.log("fallback_used", {
            "primary": primary,
            "secondary": secondary,
        })

    def log_llm_call(self, provider: str, tokens: int, user_id: str | None) -> None:
        self.metrics.record_tokens(tokens)
        self.logger.log("llm_call", {
            "provider": provider,
            "tokens": tokens,
            "user_id": user_id,
        })