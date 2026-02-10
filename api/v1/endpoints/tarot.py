from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.db.database import get_db
from api.auth.security import get_current_user
from services.oracle_service import OracleService
from pydantic import BaseModel
from oraculum import InterpretationDepth, OracleDomain

router = APIRouter()

class TarotRequest(BaseModel):
    query: str
    depth: int = 1

@router.post("/analysis")
async def get_tarot_reading(
    request: TarotRequest,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        service = OracleService(db)
        
        # Validar profundidad
        try:
            depth_enum = InterpretationDepth(request.depth)
        except ValueError:
            depth_enum = InterpretationDepth.BASIC

        # CORRECCIÓN: Se añade 'await' para que la lógica se ejecute completamente
        result = await service.consult(
            domain=OracleDomain.TAROT,
            query=request.query,
            depth=depth_enum,
            user_id=current_user
        )
        return result
        
    except Exception as e:
        # Log para depuración interna
        print(f"DEBUG ERROR TAROT: {e}")
        raise HTTPException(status_code=500, detail=str(e))
