from typing import Optional, List, Union
from ai.llm.providers.deepseek_client import DeepSeekClient
from ai.llm.providers.ollama_client import OllamaClient
from ai.interpreters.symbolic import SymbolicInterpreter

class ProviderRouter:
    def __init__(self) -> None:
        # Inicializamos los 3 niveles de redundancia
        self.cloud = DeepSeekClient()
        self.local = OllamaClient(model="deepseek-v3.1:671b-cloud")
        self.static = SymbolicInterpreter()

    def get_unified_response(self, domain: str, prompt: str, identifiers: List[Union[str, int]]) -> tuple:
        """
        Intenta obtener respuesta de:
        1. DeepSeek Cloud
        2. Ollama Local
        3. Motor Estático (SQL)
        """
        # NIVEL 1: DeepSeek Cloud
        try:
            res = self.cloud.generate(prompt)
            if res: return res, "DEEPSEEK_CLOUD"
        except Exception as e:
            print(f"DEBUG: Cloud no disponible")

        # NIVEL 2: Ollama Local
        try:
            res = self.local.generate(prompt)
            if res: return res, "OLLAMA_LOCAL"
        except Exception as e:
            print(f"DEBUG: Local no disponible")

        # NIVEL 3: Motor Estático (SQL)
        # Si fallan las IAs, el bibliotecario entra en acción
        try:
            meanings = [self.static.get_prediction(domain, i) for i in identifiers]
            header = "--- Sabiduría Ancestral (Offline) ---\n"
            return header + "\n".join(meanings), "STATIC_DB"
        except Exception as e:
            return f"Error crítico en todos los motores: {str(e)}", "ERROR"
