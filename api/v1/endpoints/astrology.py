from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.db.database import get_db
from api.auth.security import get_current_user
from services.oracle_service import OracleService
from pydantic import BaseModel, Field
from oraculum import InterpretationDepth, OracleDomain

router = APIRouter()

class AstrologyRequest(BaseModel):
    birth_date: str
    sign: str
    focus: str = "general"
    depth: int = 1

@router.post("/analysis")
async def get_astrology_reading(
    request: AstrologyRequest,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        service = OracleService(db)
        query = f"Signo: {request.sign}, Fecha: {request.birth_date}, Foco: {request.focus}"
        
        # CORRECCIÓN: Se añade 'await' para la llamada asíncrona
        result = await service.consult(
            domain=OracleDomain.ASTROLOGY,
            query=query,
            depth=InterpretationDepth(request.depth),
            user_id=current_user
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en Astrología: {str(e)}")
