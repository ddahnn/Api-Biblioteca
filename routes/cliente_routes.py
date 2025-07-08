from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from typing import List
from config.database import get_db
from schemas.cliente_schema import ClienteCreate, ClienteUpdate, ClienteResponse
from services import cliente_services

router = APIRouter(prefix="/cliente", tags=["Cliente"])

@router.get("/")
def cliente_home():
    return {"Mensagem": "API Cliente Funcionando"}

@router.post("/criar")
def criar_Cliente(cliente:ClienteCreate, db:Session = Depends(get_db)):
    return cliente_services.criar_Cliente(db, cliente)

@router.get("/listar", response_model=List[ClienteResponse])
def exibir_cliente(db:Session = Depends(get_db)):
    return cliente_services.listar_Cliente(db)

@router.get("/buscar/{matricula}", response_model=ClienteResponse)
def buscar_Cliente(matricula:int , db:Session = Depends(get_db)):
    cliente = cliente_services.buscar_Cliente(db, matricula)
    if not cliente:
        raise HTTPException(status_code = 404, detail="Cliente não encontrado")
    return cliente

@router.put("/editar/{matricula}", response_model =ClienteResponse )
def editar_cliente(matricula:int, dados:ClienteUpdate, db:Session = Depends(get_db)):
    cliente = cliente_services.alterar_cadastro(db, matricula, dados)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


@router.delete("/deletar/{matricula}")
def excluir_cliente(matricula:int, db:Session = Depends(get_db)):
    cliente = cliente_services.deletar_cliente(db, matricula)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"Mensagem":f"O cliente foi excluido com sucesso"}