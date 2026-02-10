import pytest
from services.oracle_service import OracleService
from infrastructure.db.database import SessionLocal
from oraculum import OracleDomain, InterpretationDepth

@pytest.mark.asyncio
async def test_oracle_service_returns_interpretation():
    db = SessionLocal()
    service = OracleService(db)
    # El servicio SÍ es asíncrono porque llama a la IA
    result = await service.consult(
        domain=OracleDomain.TAROT,
        query="¿Qué energía rige mi día?",
        depth=InterpretationDepth.BASIC,
        user_id="test_admin"
    )
    assert result is not None
    db.close() # Síncrono
