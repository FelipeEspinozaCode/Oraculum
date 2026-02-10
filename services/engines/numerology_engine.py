from services.engines.base import BaseEngine
from services.engines.registry import register_engine
from services.results.semantic import SemanticResult
from oraculum import OracleDomain, InterpretationDepth
import re

@register_engine(OracleDomain.NUMEROLOGY)
class NumerologyEngine(BaseEngine):
    GEMATRIA_MAP = {
        'a':1,'j':1,'s':1,'b':2,'k':2,'t':2,'c':3,'l':3,'u':3,
        'd':4,'m':4,'v':4,'e':5,'n':5,'w':5,'f':6,'o':6,'x':6,
        'g':7,'p':7,'y':7,'h':8,'q':8,'z':8,'i':9,'r':9
    }

    def _calculate_number(self, text: str) -> int:
        clean_text = re.sub(r'[^a-z]', '', text.lower())
        total = sum(self.GEMATRIA_MAP.get(char, 0) for char in clean_text)
        return self._reduce(total)

    def _reduce(self, n: int) -> int:
        while n > 9 and n not in [11, 22, 33]:
            n = sum(int(digit) for digit in str(n))
        return n

    def interpret(self, query: str, depth: InterpretationDepth = InterpretationDepth.BASIC) -> SemanticResult:
        # Extraer números potenciales de la query
        numbers = re.findall(r'\d+', query)
        calculated = self._calculate_number(query)
        
        symbols = [str(calculated)] + numbers
        return SemanticResult(
            domain=OracleDomain.NUMEROLOGY,
            query=query,
            depth=depth,
            symbols=list(set(symbols)),
            themes=["Destino", "Vibracion"],
            interpretation=f"Analisis numerologico para: {query}",
            confidence=1.0
        )
