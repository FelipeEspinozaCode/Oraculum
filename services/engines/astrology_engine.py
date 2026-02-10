import random
from oraculum import OracleDomain, InterpretationDepth
from services.engines.base import BaseEngine
from services.engines.registry import register_engine
from services.results.semantic import SemanticResult

@register_engine(OracleDomain.ASTROLOGY)
class AstrologyEngine(BaseEngine):
    """
    Motor especializado en configuraciones planetarias y zodiacales.
    """
    PLANETS = ["Sol", "Luna", "Mercurio", "Venus", "Marte", "Jupiter", "Saturno"]
    SIGNS = ["Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]

    def interpret(self, query: str, depth: InterpretationDepth = InterpretationDepth.BASIC) -> SemanticResult:
        actual_depth = depth.value if hasattr(depth, 'value') else int(depth)
        num_points = {1: 2, 2: 4, 3: 6}.get(actual_depth, 2)

        selected_planets = random.sample(self.PLANETS, k=min(num_points, len(self.PLANETS)))
        aspectos = [f"{p} en {random.choice(self.SIGNS)}" for p in selected_planets]

        return SemanticResult(
            domain=OracleDomain.ASTROLOGY,
            query=query,
            depth=depth,
            symbols=aspectos,
            themes=["Dinamicas Celestes", "Energia Estelar"],
            interpretation=f"Configuracion astral detectada: {', '.join(aspectos)}",
            confidence=1.0,
            metadata={"zodiac": "Tropical", "house_system": "Placidus"}
        )
