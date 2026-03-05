
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="C Turismo Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="backend_cturismo/static"), name="static")

@app.get("/docs", include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="C Turismo API Docs",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_favicon_url="/static/logo.svg",
        swagger_css_url="/static/swagger-theme.css",
        swagger_ui_parameters={"defaultModelsExpandDepth": 0}
    )

@app.get("/", include_in_schema=False)
def root():
    return {"service": "C Turismo API", "status": "ok"}

@app.get("/health", include_in_schema=False)
def health():
    return {"status": "ok"}

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
