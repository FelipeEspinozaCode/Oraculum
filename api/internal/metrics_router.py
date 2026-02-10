from fastapi import APIRouter, Depends, HTTPException, status
from services.observability.snapshots import build_metrics_snapshot
from app.dependencies.auth import get_current_user_optional

router = APIRouter(prefix="/internal", tags=["Internal Monitoring"])


@router.get("/metrics")
def get_metrics(user=Depends(get_current_user_optional)):
    """
    Endpoint interno de monitoreo del sistema IA.

    Protegido opcionalmente por autenticación.
    Puede ser reforzado luego con roles (admin/devops).
    """

    # Si en el futuro quieres hacerlo SOLO admin:
    # if not user or user.role != "admin":
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")

    snapshot = build_metrics_snapshot()

    return {
        "status": "ok",
        "service": "oraculum-ai-core",
        "metrics": snapshot
    }
