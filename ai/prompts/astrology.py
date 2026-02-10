from ai.prompts.base import PromptBuilder
from typing import Any

class AstrologyPromptBuilder(PromptBuilder):
    def build_from_semantic(self, semantic_data: Any) -> str:
        astros = self._format_list(getattr(semantic_data, 'symbols', []))
        aspectos = self._format_list(getattr(semantic_data, 'themes', []))
        depth = self._get_depth_text(semantic_data)

        return (
            f"Eres un Astrólogo Experto en evolución del alma. Nivel: {depth}.\n"
            f"Configuración detectada: {astros}.\n"
            f"Aspectos clave: {aspectos}.\n\n"
            f"TAREA: Describe cómo influyen estas energías en el clima astrológico actual. "
            f"Habla de tránsitos y consejos prácticos basados en el zodíaco."
        )