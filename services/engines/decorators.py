from typing import Type
from oraculum import OracleDomain
from services.engines.base import BaseEngine
from services.engines.registry import EngineRegistry


def register_engine(domain: OracleDomain):
    def decorator(engine_cls: Type[BaseEngine]):
        EngineRegistry.register(domain, engine_cls)
        return engine_cls
    return decorator
