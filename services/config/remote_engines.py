# services/config/remote_engines.py

from services.engines.registry import EngineRegistry
from services.remote.http_remote_engine import HTTPRemoteEngine
from oraculum import OracleDomain

def load_remote_engines():
    """
    Registra engines simbólicos que viven fuera del sistema.
    """

    tarot_ai = HTTPRemoteEngine(
        domain=OracleDomain.TAROT,
        endpoint_url="http://localhost:9001/tarot",
    )

    EngineRegistry.register(OracleDomain.TAROT, lambda: tarot_ai)
