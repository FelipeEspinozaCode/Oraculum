from infrastructure.config import settings
from ai.llm.client import BaseLLMClient

def get_llm_client(provider: str = None) -> BaseLLMClient:
    provider = (provider or settings.LLM_PROVIDER).lower()
    
    if provider == "ollama":
        from ai.llm.providers.ollama_client import OllamaClient
        return OllamaClient(model=settings.OLLAMA_MODEL, base_url=settings.OLLAMA_BASE_URL)
    
    if provider == "deepseek" and settings.DEEPSEEK_API_KEY:
        from ai.llm.providers.deepseek_client import DeepSeekClient
        return DeepSeekClient(api_key=settings.DEEPSEEK_API_KEY)
    
    # En lugar de MockLLMClient, devolvemos None para forzar el fallback
    return None
