from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from infrastructure.db.database import get_db
from api.auth.security import get_current_user
from services.persistence.db_reading_repository import DBReadingRepository
from infrastructure.logging import get_logger

logger = get_logger("HistoryAPI")
router = APIRouter()

@router.get("/")
async def get_history(
    db: Session = Depends(get_db),
    current_user: Annotated[str, Depends(get_current_user)] = None
):
    """Obtiene el historial de lecturas del usuario autenticado."""
    if not current_user:
        logger.warning("Intento de acceso al historial sin usuario válido.")
        raise HTTPException(status_code=401, detail="Usuario no identificado")

    repo = DBReadingRepository(db)
    readings = repo.get_user_history(user_id=current_user)
    
    logger.info(f"Historial recuperado para usuario: {current_user} ({len(readings)} registros)")

    return {
        "status": "success",
        "user_id": current_user,
        "count": len(readings),
        "items": readings
    }
