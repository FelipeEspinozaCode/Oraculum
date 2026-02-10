
import requests
from services.remote.base_remote_engine import BaseRemoteEngine
from services.results.semantic import SemanticResult
from services.resilience.cache import SimpleCache
from services.resilience.circuit_breaker import CircuitBreaker
from oraculum import OracleDomain, InterpretationDepth


class HTTPRemoteEngine(BaseRemoteEngine):

    _cache = SimpleCache(ttl_seconds=300)
    _circuit_breaker = CircuitBreaker()

    def __init__(self, domain: OracleDomain, endpoint_url: str, timeout: int = 5):
        self.domain = domain
        self.endpoint_url = endpoint_url
        self.timeout = timeout

    def _cache_key(self, depth: InterpretationDepth) -> str:
        return f"{self.domain.value}:{depth.value}"

    def interpret(self, depth: InterpretationDepth) -> SemanticResult:

        key = self._cache_key(depth)

        # 1️⃣ Cache
        cached = self._cache.get(key)
        if cached:
            return cached

        # 2️⃣ Circuit breaker
        if not self._circuit_breaker.can_execute():
            raise RuntimeError("Servicio remoto temporalmente deshabilitado por fallos")

        try:
            payload = {"domain": self.domain.value, "depth": depth.value}
            response = requests.post(self.endpoint_url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            result = SemanticResult(
                domain=self.domain,
                depth=depth,
                symbols=data.get("symbols", []),
                themes=data.get("themes", []),
                metadata=data.get("metadata", {"source": "remote"}),
            )

            self._cache.set(key, result)
            self._circuit_breaker.record_success()
            return result

        except Exception:
            self._circuit_breaker.record_failure()
            raise
