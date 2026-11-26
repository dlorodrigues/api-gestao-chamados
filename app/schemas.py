from pydantic import BaseModel, Field
from typing import Optional

class ChamadoBase(BaseModel):
    titulo: str = Field(..., min_length=3, description="Título resumido do chamado")
    descricao: str = Field(..., min_length=10, description="Detalhes do problema ou solicitação")
    categoria: str = Field(..., description="Ex: Suporte, Vendas, TI Corporativa")
    prioridade: str = Field(default="Média", description="Baixa, Média ou Alta")

class ChamadoCreate(ChamadoBase):
    pass

class ChamadoResponse(ChamadoBase):
    id: int
    status: str = Field(default="Aberto")

    class Config:
        from_attributes = True