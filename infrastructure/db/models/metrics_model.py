from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime, timezone
from infrastructure.db.database import Base

class MetricsModel(Base):
    """
    Snapshot histórico de métricas del sistema IA.
    """
    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    cpu_usage = Column(Float)
    ram_usage = Column(Float)
    active_requests = Column(Integer)
    error_count = Column(Integer)