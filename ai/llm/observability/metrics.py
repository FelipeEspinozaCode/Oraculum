import psutil
from collections import defaultdict
from threading import Lock

class MetricsCollector:
    """
    Registro central de métricas unificado (IA + Sistema).
    Implementado como Singleton.
    """
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(MetricsCollector, cls).__new__(cls)
                cls._instance._initialize()
            return cls._instance

    def _initialize(self):
        if not hasattr(self, 'initialized'):
            self.provider_calls = defaultdict(int)
            self.tokens_used = 0
            self.cache_hits = 0
            self.cache_misses = 0
            self.fallback_activations = 0
            self.error_count = 0
            self.active_requests = 0
            self.initialized = True

    @classmethod
    def instance(cls):
        return cls()

    def increment_request(self):
        with self._lock:
            self.active_requests += 1

    def decrement_request(self):
        with self._lock:
            self.active_requests = max(0, self.active_requests - 1)

    def get_snapshot(self):
        """Devuelve un diccionario con el estado actual del sistema e IA."""
        with self._lock:
            return {
                "cpu_usage": psutil.cpu_percent(),
                "ram_usage": psutil.virtual_memory().percent,
                "active_requests": self.active_requests,
                "error_count": self.error_count,
                "tokens_used": self.tokens_used,
                "cache_efficiency": (self.cache_hits / (self.cache_hits + self.cache_misses + 1e-9)) * 100
            }
