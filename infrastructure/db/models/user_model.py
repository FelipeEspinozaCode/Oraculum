import uuid
from sqlalchemy import Column, String
from infrastructure.db.database import Base # Importamos la Base real de tu database.py

class UserModel(Base):
    __tablename__ = "users"

    # Usamos default para que SQL genere el ID solo si no lo pasas
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)