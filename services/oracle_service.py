from datetime import datetime, UTC
import logging
from services.engines.registry import EngineRegistry
from services.persistence.db_reading_repository import DBReadingRepository
from services.results.oracle_interpretation import OracleInterpretation
from ai.interpreters.symbolic import SymbolicInterpreter
from ai.llm.factory import get_llm_client
from ai.llm.management.cost_control import CostController
from oraculum import OracleDomain, InterpretationDepth

logger = logging.getLogger(__name__)

class OracleService:
    def __init__(self, db_session=None):
        self.registry = EngineRegistry()
        self.interpreter = SymbolicInterpreter()
        self.repository = DBReadingRepository(db_session) if db_session else None
        self.cost_controller = CostController()
        self.primary_ai = get_llm_client("deepseek")
        self.secondary_ai = get_llm_client("ollama")

    async def consult(self, domain: OracleDomain, query: str, depth: InterpretationDepth, user_id: str = None) -> OracleInterpretation:
        if isinstance(domain, str):
            domain = OracleDomain(domain.lower())

        # 1. Obtener símbolos del motor (Tarot, Astrología, etc.)
        engine = self.registry.get_engine(domain)
        semantic_data = engine.interpret(query=query, depth=depth)
        
        # 2. Interpretar símbolos (Traducción a lenguaje humano/base)
        base_knowledge = self.interpreter.interpret(semantic_data, user_id=user_id)

        # 3. Orquestación de Narrativa IA
        context_str = "\n".join([f"- {item['symbol']}: {item['meaning']}" for item in base_knowledge])
        prompt = f"Actua como un Oraculo experto en {domain.value}. Interpreta: {query}. Contexto simbolico: {context_str}"
        narrative_text = ""

        # Nivel 1: DeepSeek
        if self.primary_ai:
            if self.cost_controller.check_request(estimated_tokens=500):
                try:
                    narrative_text = await self.primary_ai.generate(prompt, metadata={'cost_controller': self.cost_controller})
                except Exception as e:
                    logger.warning(f"Fallo Nivel 1: {e}")

        # Nivel 2: Ollama (Fallback)
        if not narrative_text and self.secondary_ai:
            try:
                narrative_text = await self.secondary_ai.generate(prompt)
            except Exception as e:
                logger.warning(f"Fallo Nivel 2: {e}")

        # Nivel 3: SQL Fallback
        if not narrative_text:
            header = "--- Interpretación de Respaldo (Sabiduría Local) ---\n"
            body = "\n".join([f"[{item['symbol']}]: {item['meaning']}" for item in base_knowledge])
            narrative_text = header + body

        # 4. Construcción del Objeto de Resultado Formal
        result = OracleInterpretation(
            domain=domain,
            depth=depth,
            semantic=semantic_data,
            narrative=narrative_text,
            owner_id=user_id
        )

        # 5. Persistencia
        if self.repository:
            try:
                self.repository.save_reading(
                    user_id=user_id, 
                    domain=domain.value, 
                    query=query,
                    content=narrative_text, 
                    metadata=semantic_data.model_dump()
                )
            except Exception as e:
                logger.error(f"Error persistiendo lectura: {e}")

        return result
