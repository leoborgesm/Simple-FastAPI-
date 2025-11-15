from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="API simples estruturada")

#Incluindo as rotas 
app.include_router(router)