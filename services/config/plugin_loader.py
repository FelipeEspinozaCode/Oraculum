"""
Plugin Loader
=============

Carga engines externos ubicados en la carpeta /plugins
sin que el core tenga que conocerlos.
"""

import pkgutil
import importlib
import sys
from pathlib import Path


def load_external_plugins() -> None:
    """
    Descubre e importa todos los módulos dentro de la carpeta plugins.
    Esto activa los decoradores @register_engine de cada plugin.
    """
    plugins_path = Path(__file__).resolve().parents[2] / "plugins"

    if not plugins_path.exists():
        return

    sys.path.append(str(plugins_path.parent))

    for _, module_name, _ in pkgutil.iter_modules([str(plugins_path)]):
        importlib.import_module(f"plugins.{module_name}")
