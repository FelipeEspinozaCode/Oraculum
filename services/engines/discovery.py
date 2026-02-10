"""
Engine Discovery
================
Se encarga de descubrir y registrar automáticamente:

• Engines core del sistema
• Plugins externos
• Engines remotos configurados

Este módulo se ejecuta UNA SOLA VEZ al iniciar la aplicación.
"""

from services.config.engine_loader import load_engines as load_core_engines
from services.config.plugin_loader import load_external_plugins as load_plugins
from services.config.remote_engines import load_remote_engines


def discover_engines() -> None:
    """
    Ejecuta todos los mecanismos de carga de engines.

    Este método debe llamarse al iniciar el sistema para garantizar
    que todos los engines estén registrados en el EngineRegistry.
    """
    load_core_engines()
    load_plugins()
    load_remote_engines()
