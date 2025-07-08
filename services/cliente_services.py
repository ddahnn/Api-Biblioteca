from sqlalchemy.orm import Session
from fastapi import HTTPException
from modules.Cliente import Cliente
from schemas.cliente_schema import ClienteCreate, ClienteUpdate

def criar_Cliente(db:Session, cliente:ClienteCreate):
    novo_cli = Cliente(**cliente.dict())
    db.add(novo_cli)
    db.commit()
    db.refresh(novo_cli)
    return novo_cli

def listar_Cliente(db:Session):
    return db.query(Cliente).all()

def buscar_Cliente(db:Session, matricula:int):
    return db.query(Cliente).filter(Cliente.matricula == matricula ).first()

def alterar_cadastro(db:Session, matricula:int, dados:ClienteUpdate):
    cliente = db.query(Cliente).filter(Cliente.matricula == matricula).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente, não encontrado")
    dados_dict = dados.dict(exclude_unset=True)
    for campo, valor in dados_dict.items():
        setattr(cliente, campo, valor)
    db.commit()
    db.refresh(cliente)
    return cliente

def deletar_cliente(db:Session, matricula:int):
    cliente = db.query(Cliente).filter(Cliente.matricula == matricula).first()
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente