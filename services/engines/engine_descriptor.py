from dataclasses import dataclass
from typing import Type
from services.engines.base import BaseEngine
from oraculum import OracleDomain


@dataclass
class EngineDescriptor:
    """
    Describe un motor oracular registrado en el sistema.
    """
    domain: OracleDomain
    engine_class: Type[BaseEngine]
    source: str  # "core", "plugin", "remote"
