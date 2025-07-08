from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from config.database import get_db
from schemas.autor_schema import AutorCreate, AutorUpdate, AutorResponse
from services import autor_services

router = APIRouter(prefix="/autores", tags=["Autores"])

@router.get("/")
def autores_inicio():
    return {"Mensagem":"Apri  '/autores/' funcionando"}

@router.post("/criar/", response_model=AutorResponse)
def criar_autor(autor: AutorCreate, db: Session = Depends(get_db)):
    return autor_services.criar_autor(db, autor)

@router.get("/listar", response_model=list[AutorResponse])
def listar_autores(db: Session = Depends(get_db)):
    return autor_services.listar_autores(db)

@router.get("/buscar/{autor_id}", response_model=AutorResponse)
def buscar_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = autor_services.buscar_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return autor

@router.put("/editar/{autor_id}", response_model=AutorResponse)
def atualizar_autor(autor_id: int, dados: AutorUpdate, db: Session = Depends(get_db)):
    autor = autor_services.atualizar_autor(db, autor_id, dados)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return autor

@router.delete("/deletar/{autor_id}")
def deletar_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = autor_services.deletar_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return {"msg": "Autor deletado com sucesso"}
