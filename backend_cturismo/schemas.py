
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClienteBase(BaseModel):
    nome: str
    email: str
    origem: Optional[str] = "site"
    status: Optional[str] = "ativo"
    selecionado_viagem: Optional[bool] = False

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nome: Optional[str]
    email: Optional[str]
    origem: Optional[str]
    status: Optional[str]
    selecionado_viagem: Optional[bool]

class ClienteOut(ClienteBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True
