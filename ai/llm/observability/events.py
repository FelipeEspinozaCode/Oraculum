import json
from datetime import datetime, UTC
from pathlib import Path


class LLMEventLogger:
    """
    Logger estructurado para eventos relacionados con LLM.
    Guarda eventos en formato JSONL (un JSON por línea).
    """

    def __init__(self, log_file: str = "ai_usage.log") -> None:
        self.log_path = Path(log_file)

    def log(self, event_type: str, payload: dict) -> None:
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "event": event_type,
            **payload,
        }

        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
