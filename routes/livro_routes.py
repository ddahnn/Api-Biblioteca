from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from typing import List
from config.database import get_db
from schemas.livro_schema import LivroCreate, LivroUpdate, LivroResponse
from services import livro_services

router = APIRouter(prefix='/livros', tags=["Livros"])

@router.get("/")
def livro_home():
    return {"Mensagem": "livro home"}

@router.post("/criar/")
def criar_Livro(livro: LivroCreate, db: Session = Depends(get_db)):
    return livro_services.criar_Livro(db, livro)

@router.get("/listar", response_model=List[LivroResponse])
def exibir_Livros(db: Session = Depends(get_db)):
    return livro_services.listar_Livro(db)

@router.get("/buscar/{isbn}", response_model=LivroResponse)
def buscar_Livro(isbn: int, db: Session = Depends(get_db)):
    livro = livro_services.buscar_Livro(db, isbn)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return livro

@router.put("/editar/{isbn}", response_model=LivroResponse)
def atualizar_Livro(isbn: int, dados: LivroUpdate, db: Session = Depends(get_db)):
    livro = livro_services.atualizar_Livro(db, isbn, dados)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return livro

@router.delete("/deletar/{isbn}")
def excluir_livro(isbn: int, db: Session = Depends(get_db)):
    livro = livro_services.deletar_livro(db, isbn)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return {"Mensagem": "Livro excluído com sucesso."}
