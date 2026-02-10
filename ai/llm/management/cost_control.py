from infrastructure.config import settings
from ai.llm.budget import BudgetManager

class CostController:
    def __init__(self):
        self.budget_manager = BudgetManager()
        self.daily_limit = settings.MAX_DAILY_BUDGET
        # DeepSeek Chat costo promedio (ajustado para ser conservador)
        self.cost_per_token = 0.0002 / 1000 

    def check_request(self, estimated_tokens: int = 500) -> bool:
        estimated_cost = estimated_tokens * self.cost_per_token
        return self.budget_manager.can_afford(estimated_cost, self.daily_limit)

    def update_usage(self, actual_tokens: int):
        actual_cost = actual_tokens * self.cost_per_token
        self.budget_manager.record_cost(actual_cost)
