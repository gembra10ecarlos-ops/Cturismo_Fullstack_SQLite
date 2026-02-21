
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from .database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, index=True)
    origem = Column(String, default="site")
    status = Column(String, default="ativo")
    selecionado_viagem = Column(Boolean, default=False)
    criado_em = Column(DateTime, default=datetime.utcnow)
