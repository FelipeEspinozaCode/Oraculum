import logging
from ai.llm.client import BaseLLMClient
from services.resilience.circuit_breaker import CircuitBreaker

logger = logging.getLogger(__name__)

class FallbackManager:
    def __init__(self, primary: BaseLLMClient, secondary: BaseLLMClient = None):
        self.primary = primary
        self.secondary = secondary
        self.breaker = CircuitBreaker(failure_threshold=3, recovery_time=60)

    def generate(self, prompt: str, metadata: dict = None) -> str:
        if self.breaker.can_execute():
            try:
                res = self.primary.generate(prompt, metadata)
                self.breaker.record_success()
                return res
            except Exception as e:
                self.breaker.record_failure()
                logger.warning(f"Primario fallo: {e}")
        
        if self.secondary:
            return self.secondary.generate(prompt, metadata)
        
        raise Exception("Proveedores agotados")
