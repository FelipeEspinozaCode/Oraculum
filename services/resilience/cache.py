"""
SimpleCache
===========

Cache en memoria para resultados simbólicos.
Evita llamadas repetidas a engines costosos (ej: remotos).
"""

import time
from typing import Any, Dict, Tuple
from services.observability.metrics_registry import MetricsRegistry


class SimpleCache:
    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self._store: Dict[str, Tuple[float, Any]] = {}
        self.metrics = MetricsRegistry.instance()

    def _is_valid(self, timestamp: float) -> bool:
        return (time.time() - timestamp) < self.ttl

    def get(self, key: str):
        entry = self._store.get(key)

        if not entry:
            self.metrics.record_cache_miss()  # 📊 MISS (no existe)
            return None

        timestamp, value = entry

        if not self._is_valid(timestamp):
            del self._store[key]
            self.metrics.record_cache_miss()  # 📊 MISS (expirado)
            return None

        self.metrics.record_cache_hit()  # 📊 HIT
        return value

    def set(self, key: str, value: Any):
        self._store[key] = (time.time(), value)
