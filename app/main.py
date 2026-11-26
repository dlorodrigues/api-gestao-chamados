from fastapi import FastAPI, HTTPException, status
from typing import List
from pydantic import BaseModel, Field

# Importando os schemas que criamos na Etapa 4
from app.schemas import ChamadoCreate, ChamadoResponse

app = FastAPI(
    title="API de Gestão de Chamados",
    description="API RESTful para gerenciamento e triagem de atendimentos ao cliente.",
    version="1.0.0"
)

# Banco de dados simulado em memória
banco_chamados = []
contador_id = 1

class ChamadoUpdateStatus(BaseModel):
    status: str = Field(..., description="Novo status do chamado: Aberto, Em Andamento ou Resolvido")

@app.get("/", tags=["Status"])
def verificar_status():
    return {
        "status": "online",
        "mensagem": "API de Gestão de Chamados operando normalmente."
    }

@app.post("/chamados", response_model=ChamadoResponse, status_code=status.HTTP_201_CREATED, tags=["Chamados"])
def criar_chamado(chamado: ChamadoCreate):
    global contador_id
    novo_chamado = {
        "id": contador_id,
        "titulo": chamado.titulo,
        "descricao": chamado.descricao,
        "categoria": chamado.categoria,
        "prioridade": chamado.prioridade,
        "status": "Aberto"
    }
    banco_chamados.append(novo_chamado)
    contador_id += 1
    return novo_chamado

@app.get("/chamados", response_model=List[ChamadoResponse], tags=["Chamados"])
def listar_chamados():
    return banco_chamados

@app.get("/chamados/{chamado_id}", response_model=ChamadoResponse, tags=["Chamados"])
def buscar_chamado_por_id(chamado_id: int):
    for chamado in banco_chamados:
        if chamado["id"] == chamado_id:
            return chamado
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Chamado com ID {chamado_id} não foi encontrado."
    )

@app.patch("/chamados/{chamado_id}/status", response_model=ChamadoResponse, tags=["Chamados"])
def atualizar_status_chamado(chamado_id: int, dados: ChamadoUpdateStatus):
    for chamado in banco_chamados:
        if chamado["id"] == chamado_id:
            chamado["status"] = dados.status
            return chamado
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Chamado com ID {chamado_id} não foi encontrado para atualização."
    )