from ai.prompts.base import PromptBuilder
from typing import Any

class TarotPromptBuilder(PromptBuilder):
    def build_from_semantic(self, semantic_data: Any) -> str:
        cartas = self._format_list(getattr(semantic_data, 'symbols', []))
        temas = self._format_list(getattr(semantic_data, 'themes', []))
        depth = self._get_depth_text(semantic_data)
        query = getattr(semantic_data, 'query', 'Consulta general')

        return (
            f"Actúa como un Maestro del Tarot místico. Nivel: {depth}.\n"
            f"Cartas en la tirada: {cartas}.\n"
            f"Arquetipos y Temas: {temas}.\n"
            f"Consulta del usuario: '{query}'\n\n"
            f"TAREA: Interpreta la relación entre estos Arcanos y el momento vital del usuario. "
            f"Mantén un tono místico, sabio y orientador."
        )