import httpx
import json
from ai.llm.client import BaseLLMClient
from infrastructure.logging import get_logger

# Usamos el logger centralizado del sistema
logger = get_logger("DeepSeekClient")

class DeepSeekClient(BaseLLMClient):
    def __init__(self, api_key: str, model: str = "deepseek-chat"):
        self.api_key = api_key
        self.model = model
        self.url = "https://api.deepseek.com/v1/chat/completions"

    async def generate(self, prompt: str, metadata: dict = None) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        
        async with httpx.AsyncClient(timeout=45.0) as client:
            try:
                response = await client.post(self.url, headers=headers, json=payload)
                
                if response.status_code != 200:
                    logger.error(f"Error de API {response.status_code}: {response.text}")
                    return None
                
                response.encoding = "utf-8"
                data = response.json()
                
                if metadata and 'cost_controller' in metadata:
                    tokens = data.get("usage", {}).get("total_tokens", 0)
                    metadata['cost_controller'].update_usage(tokens)

                logger.info("Respuesta de DeepSeek Cloud recibida exitosamente.")
                return data['choices'][0]['message']['content']
            except Exception as e:
                logger.critical(f"Fallo de conexión con DeepSeek: {str(e)}")
                return None
