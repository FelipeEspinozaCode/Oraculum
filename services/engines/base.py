from __future__ import annotations

from abc import ABC, abstractmethod

from services.results.semantic import SemanticResult


class BaseEngine(ABC):
    """
    Interfaz base de motores oraculares.
    """

    domain: str

    @abstractmethod
    def interpret(self, query: str) -> SemanticResult:
        raise NotImplementedError
