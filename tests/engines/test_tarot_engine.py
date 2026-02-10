import pytest
from oraculum import OracleDomain, InterpretationDepth
from services.engines.tarot_engine import TarotEngine
from services.results.semantic import SemanticResult

def test_tarot_engine_returns_semantic_result():
    engine = TarotEngine()
    # Los motores son síncronos, NO llevan await
    result = engine.interpret("query", InterpretationDepth.BASIC)
    assert isinstance(result, SemanticResult)
    assert result.domain == OracleDomain.TAROT
