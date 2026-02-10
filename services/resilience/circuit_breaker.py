import time
import logging
from threading import Lock

logger = logging.getLogger(__name__)

class CircuitBreaker:
    """
    Implementación de patrón fusibles (Circuit Breaker) thread-safe 
    para proteger llamadas a LLMs externos.
    """
    def __init__(self, failure_threshold: int = 3, recovery_time: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time
        
        # Estado dinámico
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        
        # Bloqueo para asegurar integridad en entornos concurrentes (FastAPI)
        self._lock = Lock()

    def can_execute(self) -> bool:
        """Determina si se permite realizar la llamada al proveedor."""
        with self._lock:
            if self.state == "OPEN":
                # Verificar si el tiempo de recuperación ha expirado
                if (time.time() - self.last_failure_time) > self.recovery_time:
                    logger.info("⚡ CIRCUIT BREAKER: Pasando a estado HALF_OPEN para reintento.")
                    self.state = "HALF_OPEN"
                    return True
                return False
            return True

    def record_success(self):
        """Restaura el circuito tras una llamada exitosa."""
        with self._lock:
            if self.state != "CLOSED":
                logger.info("✅ CIRCUIT BREAKER: Salud restaurada. Estado: CLOSED.")
            self.failure_count = 0
            self.state = "CLOSED"

    def record_failure(self):
        """Registra un fallo y abre el circuito si supera el umbral."""
        with self._lock:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                if self.state != "OPEN":
                    logger.critical(f"🚨 CIRCUIT BREAKER: Umbral de fallos alcanzado ({self.failure_count}). Estado: OPEN.")
                self.state = "OPEN"