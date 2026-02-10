from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import uuid

from api.auth.models import UserRegister, TokenResponse
from api.auth.security import hash_password, verify_password, create_access_token
from infrastructure.db.models.user_model import UserModel
from infrastructure.db.database import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    # 1. Limpieza de datos
    username = user.username.strip().lower()
    
    # 2. Verificación de existencia
    db_user = db.query(UserModel).filter(UserModel.username == username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # 3. Creación explícita
    hashed = hash_password(user.password)
    new_user = UserModel(
        id=str(uuid.uuid4()),
        username=username,
        hashed_password=hashed
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "Usuario registrado correctamente"}
    except Exception as e:
        db.rollback()
        print(f"DEBUG DB Error: {e}")
        raise HTTPException(status_code=500, detail="Error al guardar en base de datos")

@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = form_data.username.strip().lower()
    db_user = db.query(UserModel).filter(UserModel.username == username).first()

    # DEBUG: Si falla, queremos saber por qué en la consola del servidor
    if not db_user:
        print(f"LOGIN FAIL: Usuario {username} no encontrado")
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    if not verify_password(form_data.password, db_user.hashed_password):
        print(f"LOGIN FAIL: Password incorrecto para {username}")
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = create_access_token({"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
