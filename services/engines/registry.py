from __future__ import annotations
from typing import Dict, Type
from oraculum import OracleDomain, UnsupportedOracleDomainError
from services.engines.base import BaseEngine

class EngineRegistry:
    """Registro central de motores oraculares."""
    _engines: Dict[OracleDomain, Type[BaseEngine]] = {}

    @classmethod
    def register(cls, domain: OracleDomain, engine_cls: Type[BaseEngine]) -> None:
        cls._engines[domain] = engine_cls

    def get_engine(self, domain: OracleDomain) -> BaseEngine:
        """Busca e instancia el motor solicitado. (Sincronizado con OracleService)"""
        if domain not in self._engines:
            raise UnsupportedOracleDomainError(domain)
        # Retorna una instancia nueva del motor (ej: TarotEngine())
        return self._engines[domain]()

def register_engine(domain: OracleDomain):
    """Decorador para registro automático de motores."""
    def decorator(cls: Type[BaseEngine]):
        EngineRegistry.register(domain, cls)
        return cls
    return decorator