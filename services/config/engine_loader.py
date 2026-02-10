"""
Engine Loader
==================
Descubre automáticamente todos los engines dentro de services.engines
para que se registren vía decoradores. 

Esta versión incluye manejo de errores para evitar que un plugin corrupto
detenga la carga del sistema completo.
"""

import pkgutil
import importlib
import logging
import services.engines

# Configuración de log básica para ver la carga en consola
logger = logging.getLogger(__name__)

def load_engines() -> None:
    """
    Importa dinámicamente todos los módulos dentro de services.engines
    para activar los decoradores @register_engine.
    """
    package = services.engines
    loaded_count = 0
    
    logger.info("Iniciando descubrimiento dinámico de motores en %s...", package.__name__)

    for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
        # Evitamos cargar subpaquetes si los hubiera, solo archivos .py
        if is_pkg:
            continue
            
        full_module_name = f"{package.__name__}.{module_name}"
        
        try:
            importlib.import_module(full_module_name)
            logger.info("✓ Motor cargado exitosamente: %s", module_name)
            loaded_count += 1
        except Exception as e:
            logger.error("❌ Error cargando motor %s: %s", module_name, str(e))

    logger.info("Proceso de carga finalizado. Motores activos: %d", loaded_count)