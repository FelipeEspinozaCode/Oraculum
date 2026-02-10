import logging
from datetime import datetime, timezone
from infrastructure.db.database import SessionLocal
from infrastructure.db.models.metrics_model import MetricsModel
from ai.llm.observability.metrics import MetricsCollector

logger = logging.getLogger(__name__)

class MetricsPersistenceService:
    """
    Gestiona la persistencia de métricas desde el Singleton de memoria
    hacia la base de datos SQL.
    """

    def __init__(self):
        self.collector = MetricsCollector.instance()

    def persist_current_metrics(self):
        """Captura el estado actual de MetricsCollector y lo guarda en DB."""
        db = SessionLocal()
        try:
            snapshot = self.collector.get_snapshot()
            
            db_metrics = MetricsModel(
                cpu_usage=snapshot.get("cpu_usage", 0.0),
                ram_usage=snapshot.get("ram_usage", 0.0),
                active_requests=snapshot.get("active_requests", 0),
                error_count=snapshot.get("error_count", 0)
                # El timestamp se genera solo en el modelo
            )
            
            db.add(db_metrics)
            db.commit()
            logger.info("Métricas persistidas correctamente en la base de datos.")
        except Exception as e:
            db.rollback()
            logger.error(f"Error al persistir métricas: {e}")
        finally:
            db.close()
