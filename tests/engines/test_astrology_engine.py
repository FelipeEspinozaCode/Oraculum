import pytest
from oraculum import OracleDomain, InterpretationDepth
from services.engines.astrology_engine import AstrologyEngine
from services.results.semantic import SemanticResult

def test_astrology_engine_returns_semantic_result():
    engine = AstrologyEngine()
    # Los motores son síncronos, NO llevan await
    result = engine.interpret("query", InterpretationDepth.BASIC)
    assert isinstance(result, SemanticResult)
    assert result.domain == OracleDomain.ASTROLOGY
