from ai.prompts.base import PromptBuilder
from typing import Any

class NumerologyPromptBuilder(PromptBuilder):
    def build_from_semantic(self, semantic_data: Any) -> str:
        numeros = self._format_list(getattr(semantic_data, 'symbols', []))
        vibraciones = self._format_list(getattr(semantic_data, 'themes', []))
        depth = self._get_depth_text(semantic_data)

        return (
            f"Eres un Experto en Numerología Pitagórica. Nivel: {depth}.\n"
            f"Números calculados: {numeros}.\n"
            f"Vibraciones: {vibraciones}.\n\n"
            f"TAREA: Muestra el análisis matemático y explica el propósito de vida "
            f"y los desafíos asociados a esta frecuencia numérica."
        )