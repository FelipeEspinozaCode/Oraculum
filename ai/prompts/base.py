from abc import ABC, abstractmethod
from typing import Any

class PromptBuilder(ABC):
    """
    Clase base abstracta para todos los constructores de prompts.
    Asegura que cualquier oráculo implemente obligatoriamente build_from_semantic.
    """

    @abstractmethod
    def build_from_semantic(self, semantic_data: Any) -> str:
        pass

    def _get_depth_text(self, semantic_data: Any) -> str:
        depth_val = getattr(semantic_data, 'depth', 1)
        depth_map = {1: "BÁSICA", 2: "INTERMEDIA", 3: "PROFUNDA"}
        actual_depth = depth_val.value if hasattr(depth_val, 'value') else depth_val
        return depth_map.get(actual_depth, "ESTÁNDAR")

    def _format_list(self, items: list) -> str:
        if not items:
            return "No detectados"
        return ", ".join(items)