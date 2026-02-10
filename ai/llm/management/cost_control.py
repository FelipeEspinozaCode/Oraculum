from ai.llm.budget import BudgetManager

class CostController:
    def __init__(self):
        self.budget_manager = BudgetManager()

    def check_request(self, estimated_tokens: int):
        # Lógica simple de validación
        return self.budget_manager.can_afford(0.01) # Costo ficticio por ahora

    def update_usage(self, actual_cost: float):
        self.budget_manager.record_cost(actual_cost)