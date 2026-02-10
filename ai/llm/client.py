from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseLLMClient(ABC):
    @abstractmethod
    async def generate(self, prompt: str, metadata: Dict[str, Any] | None = None) -> str:
        pass

class MockLLMClient(BaseLLMClient):
    async def generate(self, prompt: str, metadata: Dict[str, Any] | None = None) -> str:
        return "🔮 Respuesta Mock: El destino está en tus manos."
