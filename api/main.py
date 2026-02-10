import sys
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

# Configuración de Rutas
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

from infrastructure.config import settings
from infrastructure.db.database import engine, Base
from infrastructure.db.models.user_model import UserModel
from infrastructure.db.models.reading_model import ReadingModel
from infrastructure.db.models.metrics_model import MetricsModel
from infrastructure.logging import get_logger

from oraculum import SYSTEM_NAME, SYSTEM_VERSION
from services.security.rate_limiter import RateLimiter
from services.observability.metrics_scheduler import MetricsScheduler

logger = get_logger("MainApp")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Iniciando {SYSTEM_NAME} v{SYSTEM_VERSION}...")
    scheduler = MetricsScheduler(interval_seconds=300)
    scheduler.start()
    yield
    scheduler.stop()
    logger.info("Apagando sistema...")

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.limiter = RateLimiter.instance()

    async def dispatch(self, request: Request, call_next):
        if request.url.path == "/": return await call_next(request)
        if not self.limiter.check(request.client.host):
            raise HTTPException(status_code=429, detail="Límite de peticiones excedido.")
        return await call_next(request)

app = FastAPI(title=SYSTEM_NAME, version=SYSTEM_VERSION, lifespan=lifespan)

# --- CONFIGURACIÓN DE CORS (Seguridad de producción) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RateLimitMiddleware)

# Registro de Rutas
from api.auth.routes import router as auth_router
from api.v1.endpoints.tarot import router as tarot_router
from api.v1.endpoints.astrology import router as astrology_router
from api.v1.endpoints.numerology import router as numerology_router
from api.history.routes import router as history_router

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/api/auth", tags=["Seguridad"])
app.include_router(tarot_router, prefix="/api/v1/tarot", tags=["Tarot"])
app.include_router(astrology_router, prefix="/api/v1/astrology", tags=["Astrología"])
app.include_router(numerology_router, prefix="/api/v1/numerology", tags=["Numerología"])
app.include_router(history_router, prefix="/api/v1/history", tags=["Historial"])

@app.get("/")
async def root():
    return {"status": "online", "version": SYSTEM_VERSION}
