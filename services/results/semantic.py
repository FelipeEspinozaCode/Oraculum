from __future__ import annotations
from datetime import datetime, timezone
from typing import Any, Dict, List
from pydantic import BaseModel, Field, field_validator, ConfigDict
from oraculum import OracleDomain, InterpretationDepth

class SemanticResult(BaseModel):
    model_config = ConfigDict(use_enum_values=False)

    domain: OracleDomain = Field(..., description="Dominio oracular estricto")
    query: str = Field(..., description="Consulta original")
    depth: InterpretationDepth = Field(default=InterpretationDepth.BASIC)
    symbols: List[str] = Field(default_factory=list)
    themes: List[str] = Field(default_factory=list)
    interpretation: str = Field(default="Interpretación técnica base")
    confidence: float = Field(default=1.0)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('depth', mode='before')
    @classmethod
    def transform_depth(cls, v: Any) -> InterpretationDepth:
        if isinstance(v, InterpretationDepth): return v
        mapping = {1: InterpretationDepth.BASIC, 2: InterpretationDepth.INTERMEDIATE, 3: InterpretationDepth.DEEP}
        if isinstance(v, int): return mapping.get(v, InterpretationDepth.BASIC)
        return InterpretationDepth.BASIC
