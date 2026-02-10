import json
import os
from datetime import datetime
from infrastructure.logging import get_logger

logger = get_logger("BudgetManager")

class BudgetManager:
    def __init__(self, storage_path: str = "data/budget_usage.json"):
        self.storage_path = storage_path
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            self._save_data({"date": str(datetime.now().date()), "total_spent": 0.0})

    def _load_data(self) -> dict:
        try:
            if not os.path.exists(self.storage_path): 
                return {"date": str(datetime.now().date()), "total_spent": 0.0}
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data.get("date") != str(datetime.now().date()):
                    return {"date": str(datetime.now().date()), "total_spent": 0.0}
                return data
        except Exception:
            return {"date": str(datetime.now().date()), "total_spent": 0.0}

    def _save_data(self, data: dict):
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def can_afford(self, estimated_cost: float, daily_limit: float) -> bool:
        data = self._load_data()
        return (data["total_spent"] + estimated_cost) <= daily_limit

    def record_cost(self, cost: float):
        data = self._load_data()
        data["total_spent"] += cost
        self._save_data(data)
        logger.info(f"💰 Presupuesto actualizado: \ gastados hoy.")
