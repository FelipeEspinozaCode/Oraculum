import pytest
from services.engines.base import BaseEngine
from services.engines.registry import EngineRegistry
from oraculum import OracleDomain, UnsupportedOracleDomainError

def test_registry_resolves_correct_engine():
    # Definimos un motor de prueba
    class DummyEngine(BaseEngine):
        def interpret(self, query, depth): return "dummy"
    
    # El registro es estático para 'register' pero de instancia para 'get_engine'
    registry = EngineRegistry()
    registry.register(OracleDomain.RUNES, DummyEngine)
    
    engine = registry.get_engine(OracleDomain.RUNES)
    assert isinstance(engine, DummyEngine)

def test_registry_raises_error_for_unregistered_domain():
    registry = EngineRegistry()
    # Limpiamos o buscamos algo que no esté registrado
    # Usamos un string que no esté en el Enum para forzar el error de validación o búsqueda
    with pytest.raises(UnsupportedOracleDomainError):
        registry.get_engine("invalid_domain")
