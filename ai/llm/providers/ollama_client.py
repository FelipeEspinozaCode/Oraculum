import httpx
import logging
from ai.llm.client import BaseLLMClient

logger = logging.getLogger(__name__)

class OllamaClient(BaseLLMClient):
    def __init__(self, model: str, base_url: str = "http://localhost:11434"):
        self.model = model
        self.url = f"{base_url}/api/generate"

    async def generate(self, prompt: str, metadata: dict = None) -> str:
        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                res = await client.post(self.url, json={"model": self.model, "prompt": prompt, "stream": False})
                res.raise_for_status()
                print('\033[92m--- [🏠 OLLAMA LOCAL RESPONSE RECEIVED] ---\033[0m')
                return res.json().get("response", "").strip()
            except Exception as e:
                logger.warning(f"⚠️ Ollama no disponible: {str(e)}. ¿Está Ollama ejecutándose?")
                return None
