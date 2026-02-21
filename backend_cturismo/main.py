
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Co Turismo Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/clientes", response_model=List[schemas.ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db)

@app.post("/clientes", response_model=schemas.ClienteOut)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db, cliente)

@app.put("/clientes/{cliente_id}", response_model=schemas.ClienteOut)
def atualizar_cliente(cliente_id: int, data: schemas.ClienteUpdate, db: Session = Depends(get_db)):
    result = crud.update_cliente(db, cliente_id, data)
    if not result:
        raise HTTPException(404, "Cliente não encontrado")
    return result

@app.delete("/clientes/{cliente_id}")
def remover_cliente(cliente_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_cliente(db, cliente_id)
    if not ok:
        raise HTTPException(404, "Cliente não encontrado")
    return {"status": "removido"}
