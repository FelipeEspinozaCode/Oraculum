from fastapi.encoders import jsonable_encoder
from infrastructure.db.models.reading_model import ReadingModel
from infrastructure.logging import get_logger

logger = get_logger("DBReadingRepository")

class DBReadingRepository:
    def __init__(self, db_session):
        self.db = db_session

    def save_reading(self, user_id, domain, query, content, metadata=None):
        try:
            safe_metadata = jsonable_encoder(metadata) if metadata else {}
            new_reading = ReadingModel(
                user_id=user_id,
                domain=domain,
                query=query,
                content=content,
                additional_info=safe_metadata
            )
            self.db.add(new_reading)
            self.db.commit()
            self.db.refresh(new_reading)
            return new_reading
        except Exception as e:
            if self.db: self.db.rollback()
            logger.error(f"Error al guardar lectura: {e}")
            raise e

    def get_user_history(self, user_id: str = None, limit: int = 20):
        try:
            query = self.db.query(ReadingModel)
            if user_id:
                query = query.filter(ReadingModel.user_id == user_id)
            return query.order_by(ReadingModel.id.desc()).limit(limit).all()
        except Exception as e:
            logger.error(f"Error al leer historial del usuario {user_id}: {e}")
            return []
