import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Localizamos la raíz del proyecto de forma más segura
# .parent (db) -> .parent (infrastructure) -> .parent (root)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = os.path.join(BASE_DIR, "oraculum.db")

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Nueva forma estándar de SQLAlchemy 2.0 para definir la Base
class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()