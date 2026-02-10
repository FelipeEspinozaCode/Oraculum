import hashlib
import json
from typing import Optional
from ai.llm.observability.telemetry import AITelemetry


class SemanticCache:
    """
    Caché en memoria para interpretaciones híbridas.
    """

    def __init__(self) -> None:
        self._store: dict[str, str] = {}
        self.telemetry = AITelemetry()

    def _build_key(self, domain: str, depth: str, symbols: list[str], themes: list[str]) -> str:
        payload = {
            "domain": domain,
            "depth": depth,
            "symbols": sorted(symbols),
            "themes": sorted(themes),
        }

        raw = json.dumps(payload, ensure_ascii=False)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def get(self, domain: str, depth: str, symbols: list[str], themes: list[str]) -> Optional[str]:
        key = self._build_key(domain, depth, symbols, themes)
        value = self._store.get(key)

        if value:
            self.telemetry.log_cache_hit()
        else:
            self.telemetry.log_cache_miss()

        return value

    def set(self, domain: str, depth: str, symbols: list[str], themes: list[str], value: str) -> None:
        key = self._build_key(domain, depth, symbols, themes)
        self._store[key] = value
