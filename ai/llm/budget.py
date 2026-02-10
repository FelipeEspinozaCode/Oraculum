class BudgetManager:
    """Gestiona el límite de gastos de los LLMs."""
    
    def __init__(self, daily_limit: float = 5.0):
        self.daily_limit = daily_limit
        self.current_spend = 0.0

    def can_afford(self, estimated_cost: float) -> bool:
        return (self.current_spend + estimated_cost) <= self.daily_limit

    def record_cost(self, cost: float):
        self.current_spend += cost
        print(f"[Budget] Gasto actualizado: ${self.current_spend:.4f}")