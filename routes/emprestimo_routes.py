from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.emprestimo_schema import (
    EmprestimoCreate,
    EmprestimoDevolucao,
    EmprestimoResponse
)
from services import emprestimo_services
from typing import List

router = APIRouter(prefix="/emprestimos", tags=["Empréstimos"])

@router.post("/retirar", response_model=EmprestimoResponse)
def retirar_livro(dados: EmprestimoCreate, db: Session = Depends(get_db)):
    try:
        return emprestimo_services.criar_emprestimo(db, dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")

@router.put("/devolver/{emprestimo_id}")
def devolver_livro(emprestimo_id: int, dados: EmprestimoDevolucao, db: Session = Depends(get_db)):
    try:
        return emprestimo_services.devolver_livro(db, emprestimo_id, dados)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/cliente/{cliente_id}", response_model=List[EmprestimoResponse])
def listar_emprestimos_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return emprestimo_services.listar_emprestimos_por_cliente(db, cliente_id)

@router.get("/ativos", response_model=List[EmprestimoResponse])
def listar_emprestimos_ativos(db: Session = Depends(get_db)):
    return emprestimo_services.listar_todos_emprestimos_ativos(db)
