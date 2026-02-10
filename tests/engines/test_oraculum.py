from oraculum import OracleDomain, InterpretationDepth

def test_oracle_domain_enum():
    assert OracleDomain.TAROT.value == "tarot"

def test_interpretation_depth_enum():
    assert InterpretationDepth.BASIC.name == "BASIC"
