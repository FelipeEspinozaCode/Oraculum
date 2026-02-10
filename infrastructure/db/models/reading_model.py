from sqlalchemy import Column, Integer, String, DateTime, JSON, Text
from datetime import datetime, UTC
from infrastructure.db.database import Base

class ReadingModel(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True) # Estandarizado a user_id
    domain = Column(String)
    query = Column(Text)
    content = Column(Text)
    additional_info = Column(JSON) 
    timestamp = Column(DateTime, default=lambda: datetime.now(UTC))