from fastapi import APIRouter
from app.models import SomaRequest

router = APIRouter()

@router.get("/")
def root():
    return {"Mensagem": "Ola ! API Esta funcionando como estrutura profissional."}

@router.post("/soma")
def somar(payload: SomaRequest):
    resultado = payload.a + payload.b 
    return {"resultado": resultado}

