from fastapi import APIRouter
from firebase_admin import firestore
from app.firebase_config import initialize_firebase

router = APIRouter()

initialize_firebase()
db = firestore.client()

@router.post("/usuarios")
def cadastrar_usuario(usuario: dict):
    db.collection("usuarios").add(usuario)
    return {"mensagem": "Usuário cadastrado com sucesso"}