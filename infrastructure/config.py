import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Oraculum"
    VERSION: str = "1.0.0"

    # --- SEGURIDAD ---
    SECRET_KEY: str = os.getenv("ORACULUM_SECRET_KEY")
    
    if not SECRET_KEY:
        # Quitamos la tilde para evitar errores de codificación (UTF-8)
        raise RuntimeError("FATAL: No se encontro ORACULUM_SECRET_KEY en el archivo .env")

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080

    # --- LLM PROVIDERS ---
    LLM_PROVIDER: str = os.getenv("ORACULUM_LLM_PROVIDER", "deepseek").lower()
    DEEPSEEK_API_KEY: str | None = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_MODEL: str = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "deepseek-v3.1:671b-cloud")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    ALLOWED_ORIGINS: list = ["*"]

settings = Settings()