from pydantic import BaseModel, Field, ConfigDict
from typing import Dict, Optional, List
from datetime import datetime, timezone

class InterpretationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    domain: str = Field(..., example="tarot", description="El dominio del oráculo consultado")
    engine: str = Field(..., example="SymbolicInterpreter", description="Motor que procesó la lectura")
    content: str = Field(..., description="La narrativa generada por la IA")
    depth: str = Field(..., example="DEEP", description="Nivel de profundidad de la interpretación")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Optional[Dict] = Field(default_factory=dict, description="Datos adicionales de la consulta")

class HistoryFilters(BaseModel):
    domain: Optional[str] = Field(None, example="astrology")
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    keyword: Optional[str] = Field(None, description="Palabra clave para buscar en las consultas")
    skip: int = Field(0, ge=0)
    limit: int = Field(20, le=100)

class GenericResponse(BaseModel):
    status: str = Field(..., example="success")
    message: str = Field(..., example="Operación completada")
