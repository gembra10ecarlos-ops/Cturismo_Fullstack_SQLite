
from sqlalchemy.orm import Session
from . import models, schemas

def get_clientes(db: Session):
    return db.query(models.Cliente).all()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def update_cliente(db: Session, cliente_id: int, data: schemas.ClienteUpdate):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not db_cliente:
        return None

    for k, v in data.dict(exclude_unset=True).items():
        setattr(db_cliente, k, v)

    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not db_cliente:
        return False

    db.delete(db_cliente)
    db.commit()
    return True
