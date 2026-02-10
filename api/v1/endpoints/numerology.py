from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.db.database import get_db
from api.auth.security import get_current_user
from services.oracle_service import OracleService
from pydantic import BaseModel
from oraculum import InterpretationDepth, OracleDomain

router = APIRouter()

class NumerologyRequest(BaseModel):
    full_name: str
    birth_date: str
    calculation_type: str = "life_path"
    depth: int = 3

@router.post("/analysis")
async def get_numerology_analysis(
    request: NumerologyRequest,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        service = OracleService(db)
        query = f"Analiza la numerología de {request.full_name} nacido el {request.birth_date}. Tipo de cálculo: {request.calculation_type}"

        # CORRECCIÓN: Se añade 'await' y se asegura el flujo del token
        result = await service.consult(
            domain=OracleDomain.NUMEROLOGY,
            query=query,
            depth=InterpretationDepth(request.depth),
            user_id=current_user
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en Numerología: {str(e)}")
