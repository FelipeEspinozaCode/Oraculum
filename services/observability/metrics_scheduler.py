import threading
import time
import logging
from services.observability.metrics_persistence import MetricsPersistenceService

logger = logging.getLogger(__name__)

class MetricsScheduler:
    def __init__(self, interval_seconds: int = 300):
        self.interval = interval_seconds
        self.persistence_service = MetricsPersistenceService()
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._run, daemon=True)

    def start(self):
        if not self.thread.is_alive():
            self.thread.start()
            logger.info(f"⏲️ Scheduler de métricas iniciado (Intervalo: {self.interval}s)")

    def stop(self):
        self.stop_event.set()
        logger.info("⏲️ Scheduler de métricas detenido.")

    def _run(self):
        while not self.stop_event.is_set():
            try:
                # CAMBIO AQUÍ: Usamos el nombre correcto del método
                self.persistence_service.persist_current_metrics()
            except Exception as e:
                logger.error(f"❌ Error en el ciclo del Scheduler: {e}")
            
            # Espera el intervalo o hasta que se detenga el evento
            self.stop_event.wait(self.interval)
