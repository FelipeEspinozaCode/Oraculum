from sqlalchemy import Column, Integer, String, Text
from infrastructure.db.database import Base

class TarotModel(Base):
    """Modelo para la sabiduria del Tarot (22 Arcanos Mayores)"""
    __tablename__ = "tarot_knowledge"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False) # Ej: "El Mago"
    arcane_type = Column(String, default="Mayor")
    meaning = Column(Text, nullable=False)
    keywords = Column(String) # Palabras clave separadas por comas

class AstrologyModel(Base):
    """Modelo para la sabiduria de los Astros y Signos"""
    __tablename__ = "astrology_knowledge"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False) # Ej: "Acuario" o "Pluton"
    category = Column(String) # Signo, Planeta, Casa
    element = Column(String) # Fuego, Tierra, Aire, Agua
    description = Column(Text, nullable=False)

class NumerologyModel(Base):
    """Modelo para la sabiduria de los Numeros"""
    __tablename__ = "numerology_knowledge"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True, nullable=False) # 1 al 9, 11, 22, 33
    vibration = Column(String) # Nombre de la vibracion
    meaning = Column(Text, nullable=False)
