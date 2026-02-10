import random
from oraculum import OracleDomain, InterpretationDepth
from services.engines.base import BaseEngine
from services.engines.registry import register_engine
from services.results.semantic import SemanticResult

@register_engine(OracleDomain.TAROT)
class TarotEngine(BaseEngine):
    ARCANA = [
        "El Mago", "La Sacerdotisa", "La Emperatriz", "El Emperador",
        "El Hierofante", "Los Enamorados", "El Carro", "La Justicia",
        "El Ermitaño", "La Rueda de la Fortuna", "La Fuerza", "El Colgado",
        "La Muerte", "La Templanza", "El Diablo", "La Torre", "La Estrella",
        "La Luna", "El Sol", "El Juicio", "El Mundo", "El Loco"
    ]

    def interpret(self, query: str = None, depth: InterpretationDepth = InterpretationDepth.BASIC) -> SemanticResult:
        # Selección de cantidad según el objeto Enum directamente
        count_map = {
            InterpretationDepth.BASIC: 1,
            InterpretationDepth.INTERMEDIATE: 2,
            InterpretationDepth.DEEP: 3
        }
        count = count_map.get(depth, 1)
        
        drawn = random.sample(self.ARCANA, k=count)

        return SemanticResult(
            domain=OracleDomain.TAROT,
            query=query or "Tirada general",
            depth=depth,
            symbols=drawn,
            themes=["Destino", "Sincronicidad"],
            interpretation=f"Símbolos: {', '.join(drawn)}"
        )