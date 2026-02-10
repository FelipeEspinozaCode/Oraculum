import pytest
from services.engines.numerology_engine import NumerologyEngine
from oraculum import InterpretationDepth

def test_gematria_calculation():
    engine = NumerologyEngine()
    res = engine.interpret("Juan", InterpretationDepth.BASIC)
    assert "1" in res.symbols

def test_master_number_retention():
    engine = NumerologyEngine()
    res = engine.interpret("ki", InterpretationDepth.BASIC)
    assert "11" in res.symbols
