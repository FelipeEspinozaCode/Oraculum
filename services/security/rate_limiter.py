import logging
from datetime import datetime, timezone
from threading import Lock
from typing import Dict
from services.security.rate_limit_models import UserRateLimit

logger = logging.getLogger(__name__)

class RateLimiter:
    """
    Limitador Singleton con auto-limpieza. 
    Evita Memory Leaks eliminando IPs inactivas de la memoria RAM.
    """
    _instance = None
    _instance_lock = Lock()

    def __init__(self, max_requests: int = 10, window_seconds: int = 60) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.users: Dict[str, UserRateLimit] = {}
        self._users_lock = Lock()
        self.last_cleanup = datetime.now(timezone.utc)

    @classmethod
    def instance(cls) -> "RateLimiter":
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = cls(max_requests=10, window_seconds=60)
        return cls._instance

    def _cleanup(self):
        """Elimina usuarios que no han tenido actividad en la última ventana."""
        now = datetime.now(timezone.utc)
        # Ejecutar limpieza cada 10 minutos (600 segundos)
        if (now - self.last_cleanup).total_seconds() > 600:
            keys_to_del = []
            for ip, lim in self.users.items():
                # Si el tiempo desde su última petición supera la ventana, es candidato a borrado
                inactivity = (now - lim.last_request).total_seconds()
                if inactivity > self.window_seconds:
                    keys_to_del.append(ip)
            
            for ip in keys_to_del:
                del self.users[ip]
            
            self.last_cleanup = now
            logger.info(f"🧹 Limpieza de RateLimiter: {len(keys_to_del)} usuarios eliminados de RAM.")

    def check(self, user_id: str) -> bool:
        """Verifica si el usuario puede realizar la petición."""
        with self._users_lock:
            self._cleanup() # Mantenimiento automático
            
            if user_id not in self.users:
                self.users[user_id] = UserRateLimit(self.max_requests, self.window_seconds)
            
            return self.users[user_id].allow_request()