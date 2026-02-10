# services/remote/base_remote_engine.py

"""
BaseRemoteEngine
================
Clase base para engines que viven fuera del sistema (microservicios IA).
No conoce FastAPI ni OracleService.
Solo trabaja con SemanticResult.
"""

from services.results.semantic import SemanticResult
from oraculum import OracleDomain, InterpretationDepth


class BaseRemoteEngine:
    """
    Interfaz base para cualquier engine remoto.
    """

    domain: OracleDomain

    def interpret(self, depth: InterpretationDepth) -> SemanticResult:
        """
        Debe ser implementado por engines remotos concretos.
        """
        raise NotImplementedError("Remote engine must implement interpret()")
