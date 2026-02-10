from __future__ import annotations
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from oraculum import OracleDomain, InterpretationDepth
from services.results.semantic import SemanticResult

class OracleInterpretation(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    domain: OracleDomain
    depth: InterpretationDepth
    semantic: SemanticResult = Field(..., description="Data técnica generada por el motor")
    narrative: str = Field(..., description="Interpretación narrativa de la IA")
    owner_id: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
