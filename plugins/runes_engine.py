from datetime import datetime, UTC
from typing import TYPE_CHECKING
from services.engines.base import BaseEngine
from services.engines.decorators import register_engine
from oraculum import OracleDomain

if TYPE_CHECKING:
    from app.schemas.oracle import OracleQuery, OracleInterpretation


@register_engine(OracleDomain.UNKNOWN)  # Cambiar cuando exista dominio RUNES
class RunesEngine(BaseEngine):
    def interpret(self, query: "OracleQuery") -> "OracleInterpretation":
        from app.schemas.oracle import OracleInterpretation

        return OracleInterpretation(
            domain=query.domain,
            depth=query.depth,
            content="Interpretación Rúnica (Plugin Externo)",
            metadata={"engine": "runes_plugin"},
            timestamp=datetime.now(UTC),
        )
