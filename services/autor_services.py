from sqlalchemy.orm import Session # type: ignore
from modules.Autor import Autor
from schemas.autor_schema import AutorCreate, AutorUpdate

def criar_autor(db: Session, autor: AutorCreate):
    novo_autor = Autor(**autor.dict())
    db.add(novo_autor)
    db.commit()
    db.refresh(novo_autor)
    return novo_autor

def listar_autores(db: Session):
    return db.query(Autor).all()

def buscar_autor(db: Session, autor_id: int):
    return db.query(Autor).filter(Autor.id == autor_id).first()

def atualizar_autor(db: Session, autor_id: int, dados: AutorUpdate):
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if autor:
        for campo, valor in dados.dict().items():
            setattr(autor, campo, valor)
        db.commit()
        db.refresh(autor)
    return autor

def deletar_autor(db: Session, autor_id: int):
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if autor:
        db.delete(autor)
        db.commit()
    return autor
