import pytest
from oraculum import OracleDomain, InterpretationDepth
from services.engines.numerology_engine import NumerologyEngine
from services.results.semantic import SemanticResult

def test_numerology_engine_returns_semantic_result():
    engine = NumerologyEngine()
    # Los motores son síncronos, NO llevan await
    result = engine.interpret("query", InterpretationDepth.BASIC)
    assert isinstance(result, SemanticResult)
    assert result.domain == OracleDomain.NUMEROLOGY
