from fastapi import FastAPI
from app.indicators.ivp import calculate_ivp

app = FastAPI(
    title="Atlas Humano API",
    description="Auditoria de Realidade Social — Curitiba",
    version="0.1"
)

@app.get("/")
def root():
    return {"projeto": "Atlas Humano", "autor": "Paulo H. L. Godinho"}
