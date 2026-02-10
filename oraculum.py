from enum import Enum

SYSTEM_NAME = "Oraculum"
SYSTEM_VERSION = "1.0.0"

class OracleDomain(str, Enum):
    TAROT = "tarot"
    ASTROLOGY = "astrology"
    NUMEROLOGY = "numerology"
    RUNES = "runes"

class InterpretationDepth(Enum):
    BASIC = 1
    INTERMEDIATE = 2
    DEEP = 3

class UnsupportedOracleDomainError(Exception):
    """Excepción para dominios no soportados."""
    def __init__(self, domain: str):
        self.domain = domain
        super().__init__(f"El dominio '{domain}' no está soportado.")